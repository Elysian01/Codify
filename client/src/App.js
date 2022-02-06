import React, { Component } from "react";
import { Controlled as CodeMirror } from "react-codemirror2";
import Pusher from "pusher-js";
import pushid from "pushid";
import axios from "axios";

import "./App.css";
import "codemirror/lib/codemirror.css";
import "codemirror/theme/material.css";

import "codemirror/mode/python/python";

const Code = (props) => (
    <div>
    {
      props.val.map(line => (
        <div className="code">{line}</div>
      ))
    }
    
    </div>
)

class App extends Component {
  constructor() {
    super();
    const x = '{';
    const y = '}';
    const endl = "\\n";
    this.state = {
      id: "",
      python: "",
      output : ""
      // output : [`dictionary1 = ${x} "name" : "Joy", "age": 25 ${y} dictionary2 = ${x} "name": "Joy", "city": "New York" ${y}  merged_dict = ${x} + **dictionary1, **dictionary2 + ${y} print("Merged dictionary:", merged_dict) })`, `dictionary1 = ${x} + "name" : "Joy", "age": 25 + ${y} dictionary2 = ${x} + "name": "Joy", "city": "New York" + ${y}  merged_dict = ${x} + **dictionary1, **dictionary2 + ${y} print("Merged dictionary:", merged_dict) })`, `dictionary1 = ${x} + "name" : "Joy", "age": 25 + ${y} dictionary2 = ${x} + "name": "Joy", "city": "New York" + ${y}  merged_dict = ${x} + **dictionary1, **dictionary2 + ${y} print("Merged dictionary:", merged_dict) })`],
    };
    
    this.pusher = new Pusher("e8a9556db3bd933d3fb1", {
      cluster: "ap2",
      forceTLS: true
    });

    this.channel = this.pusher.subscribe("my‑event");
  }

  componentDidUpdate() {
    this.runCode();
  }

  componentDidMount() {
    this.setState({
      id: pushid()
    });
    
    // this.setState({ output : });

    this.channel.bind("my-event", data => {
      const { id } = this.state;
      if (data.id === id) return;

      this.setState({
        python : data.python
      });
    });
  }

  syncUpdates = () => {
    const data = { ...this.state };

    // axios
    //   .post("http://localhost:5000/update-editor", data)
    //   .catch(console.error);
  };

  runCode = () => {
    const { python } = this.state;
  };

  onSubmit = (e) => {
    e.preventDefault();
    console.log(this.state.python);

    // case 1 : there is only one comment in the code
    // case 2 : there are multiple comments in the code
    // case 3 : there are no comments in the code

    // if the code is blank
    if(!(this.state.python)){
      alert("Please write code before submitting!!!");
    }else{
      // if code is present, but there is not comment in the code
      if(!this.state.python.includes("#")){
        alert("There is no comment in the code");
      }
       // if code is present, and there is only one comment in the code
      else if(this.state.python.split('#').length - 1 === 1){
        const comment = this.state.python.split('#')[1].split('\n')[0];
        // post request
        axios.post("http://127.0.0.1:9000/codify", { text : comment })
        .then(res => {
          console.log(res.data);
          if(res.data.code){
            this.setState({ output: res.data.code });
            // this.setState({ output : [['from sklearn.impute import SimpleImputer', '# define the imputer', "imputer = SimpleImputer(missing_values=nan, strategy='median')", '# transform the dataset', 'transformed_values = imputer.fit_transform(values)', '# count the number of NaN values in each column', "print('Missing: %d' % isnan(transformed_values).sum())", 'from sklearn.impute import SimpleImputer', '# define the imputer', "imputer = SimpleImputer(missing_values=nan, strategy='median')", '# transform the dataset', 'transformed_values = imputer.fit_transform(values)', '# count the number of NaN values in each column', "print('Missing: %d' % isnan(transformed_values).sum())"], ['df.fillna(df.median())', "print('Missing: %d' % isnan(df).sum())"]] });
            
          }
          
        })
        .catch(err => {
          console.log(err.message);
        });

      }else if(this.state.python.split('#').length - 1 >= 1){
        console.log('multiple comments');

        const comment = this.state.python.split('#')[this.state.python.split('#').length - 1].split('\n')[0];
        console.log(comment);
        // post request
        axios.post("http://127.0.0.1:9000/codify", { text : comment })
        .then(res => {
          console.log(res.data);
          if(res.data.code){
            this.setState({ output: res.data.code });
          }
          
        })
        .catch(err => {
          console.log(err.message);
        });
      }
    }
  }

  
  addCode = (e) => {
    console.log(e.currentTarget.id);
    let filtered = "";
    for(let i = 0; i < this.state.output[e.currentTarget.id].length; i++) {
      filtered += this.state.output[e.currentTarget.id][i] + '\n';
    }
    console.log(filtered);
    this.setState({ python : this.state.python + '\n' + filtered });
  }

  render() {
    const { python } = this.state;
    const codeMirrorOptions = {
      theme: "material",
      lineNumbers: true,
      scrollbarStyle: null,
      lineWrapping: true
    };
    
    return (
      <div className="App">
        <div className="header">
          <h2 className="text-center">
              <i className="fas fa-code"></i>
              Codify
          </h2>
          <h5 class="tagline">
              <span>Instantly</span> Convert your <span>Thoughts</span> into <span>Code</span>
          </h5>
          <div class="nav text-center">
            <h5><a href="/Home" className="primary-color text">Home</a></h5>
            <b  className="active">.</b>
            <h5><a href="/">Editor</a></h5>
          </div>
        </div>
        <div className="playground">
          <form onSubmit={this.onSubmit}>
            <div className="code-editor python-code">
              <div className="editor-header">Code</div>
              <CodeMirror
                value={python}
                options={{
                  mode: "python",
                  ...codeMirrorOptions
                }}
                onBeforeChange={(editor, data, python) => {
                  this.setState({ python }, () => this.syncUpdates());
                }}
              />
              <div className="submit-div">
                <p><button type="submit" className="w3-button submit-btn w3-purple" >Submit</button></p>
              </div>
            </div>
          </form>
        </div>
        <section className="result">
          {this.state.output && <div><h4> Suggestions</h4></div>}
          <div className="output" >
            { 
              <div className="scroll">
              
                {
                  
                    this.state.output
                    && 
                    this.state.output.map((op, index) => {                    
                      return (
                        <div>
                          <Code val={op} key={index} />
                          <button id = {index} className="w3-button add-btn w3-purple" onClick={this.addCode} key={index} >Accept Code</button>
                          <br />
                          <br />

                        </div>
                      )
                    })
                  } 
                
                
               {/* { return this.state.output && <button className="w3-button add-btn w3-purple" onClick={this.addCode} key={index} >Accept Code</button> } */}

                {/* {this.state.output &̥& this.state.output[0][0]} */}
                {/* <div className="code" >      
                  from sklearn.impute import SimpleImputer <br/>
                  # define the imputer <br/>
                  imputer = SimpleImputer(missing_values=nan, s trategy='mean') <br/>
                  # transform the dataset <br/>
                  transformed_values = imputer.fit_transform(values) <br/>
                  # count the number of NaN values in each column <br/>
                  print('Missing: %d' % isnan(transformed_values).sum()) <br/>

                  <button className="w3-button add-btn w3-purple" onClick={this.addCode} >Accept Code</button>
                </div> */}
              

                {/* <div className="code" >      
                  df.fillna(df.mean()) <br />
                  print('Missing: %d' % isnan(df).sum()) <br/>
                    <button className="w3-button add-btn w3-purple" onClick={this.addCode} >Accept Code</button>
                </div> */}
              </div>
            }
            
          </div>
        </section>
      </div>
    );
  }
}

export default App;
