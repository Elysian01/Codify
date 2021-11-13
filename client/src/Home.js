import React from "react";
import './Home.css';
import './prism.css';
import axios from 'axios';

const Code = (props) => (
    <div className="code-center">
        <pre>
            <code className="language-python" >{props.val}</code>
        </pre>
    </div>
)


class Home extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            output : ""
        }
    }

    getCode = (e) => {
        e.preventDefault();
        // console.log(e.target.elements.nl_input.value);
        // axios.post("http://127.0.0.1:9000/codify", { text : e.target.elements.nl_input.value })
        // .then(res => {
        //   console.log(res.data);
        //   if(res.data.code){
            this.setState({ output : [['test1', 'test2', 'test3'], ['testtttt1', 'testtt2']] });
        //   }
          
        // })
        // .catch(err => {
        //   console.log(err.message);
        // });
    }
    render(){
        return (
            <div>
                <br />
                <div class="header">
                    <h2 class="text-center">
                        <i class="fas fa-code"></i>
                        Codify
                    </h2>
                    <h5 class="tagline">
                        <span>Instantly</span> Convert your <span>Thoughts</span> into <span>Code</span>
                    </h5>
                    <div class="nav text-center">
                        <h5><a href="" class="active">Home</a></h5>
                        <b class="primary-color text">.</b>
                        <h5><a href="/">Editor</a></h5>
                    </div>
                </div>

                <br />

                <div class="center">
                    <form onSubmit = {this.getCode} class="center" >
                        <input type="text" name="nl_input" id="nl-input" placeholder="Please enter your query in english here..." maxlength="500" autocomplete="off"/>
                        <button id="get-code-btn" class="get-code-btn">Get Code &lt;/&gt;</button>
                    </form>
                </div>

                <br /><br />

                <div class="container cards">

                    <div class="card">
                        <div class="query-section">
                            <h5><b>Code For:</b> replace null value with their mean values</h5>
                            <div class="info">
                                <h5>Intent: <span>null_imputation</span></h5>
                                <h5>Entities: <span>mean</span></h5>
                            </div>
                        </div>
                        {
                            // this.state.output 
                            //     &&
                            //     this.state.output.map((op, index) => {
                            //         let filtered = "";
                            //         for(let i = 0; i < op.length; i++){
                            //             filtered += op[i] + '\n';
                            //         }
                            //         console.log(filtered);
                            //         return (
                            //           <Code val='dfdf' key={index} />  
                            //         )
                            //     })
                            }
                            
                        {
                            this.state.output 
                            &&
                            this.state.output.map((t, i) => (
                                <Code val='sfdsf' />
                            ))
                        }
                        <Code val='fd' />
                        <div class="code-center">
                            <pre>
                                <code class="language-python">
{`df.fillna(df.mean())
print('Missing: %d' % isnan(df).sum())`}
                                
                                </code>
                            </pre>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Home;