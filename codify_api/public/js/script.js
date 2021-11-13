const url = "http://127.0.0.1:9000/codify"

response = {
            'text': 'insert median values replacing with the null values',
            'intent': 'null_imputation',
            'entities': [('STATISTICS', 'median')],
            'code': [
                ['from sklearn.impute import SimpleImputer', '# define the imputer', "imputer = SimpleImputer(missing_values=nan, strategy='median')", '# transform the dataset', 'transformed_values = imputer.fit_transform(values)', '# count the number of NaN values in each column', "print('Missing: %d' % isnan(transformed_values).sum())"],
                ['df.fillna(df.median())', "print('Missing: %d' % isnan(df).sum())"]
            ]
        }

function addNewCard(data) {
    console.log(data);
    query = data["text"]
    intent = data["intent"]
    if (data["entities"])
        entities = data["entities"][0][0]
    else
        entities = ""
    
    const cards = document.querySelector(".cards");
    cards.style.visibility = "visible";
    newCard = `
        <div class="card">
            <div class="query-section">
                <h5><b>Code For:</b> ${query}</h5>
                <div class="info">
                    <h5>Intent: <span>${intent}</span></h5>
                    <h5>Entities: <span>${entities}</span></h5>
                </div>
            </div>`
    
    if (data['code'].length == 0) {
        newCard += `<div class="code-center">
                    <pre>
                        <code class="language-python">
                            ${data[0][code]}
                        </code>
                    </pre>
                </div>`
    }
    else {
        for (let i = 0; i < data['code'].length; i++) {
            newCard += `<div class="code-center">
                        <pre>
                            <code class="language-python">
                                ${preprocessCode(data['code'][i])}
                            </code>
                        </pre>
                    </div>`
        }
    }
            
        
        newCard += `</div>`
    cards.innerHTML = newCard + cards.innerHTML;
    Prism.highlightAll();

}


function getCode() {
    text = document.querySelector(".input_text").value;
    console.log(text);
    request = { "text": text }
    
    fetch(url, {
    method: "POST",
    body: JSON.stringify(request),
    headers: {"Content-type": "application/json; charset=UTF-8"}
    })
    .then(response => response.json()) 
    .then(data => addNewCard(data))
        .catch(err => console.log(err));
    
    document.querySelector(".input_text").value = ""
    // addNewCard(response);
}

function randomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min); 
}


function preprocessCode(codeList) {
    let formattedCode = ""
    for (let i = 0; i < codeList.length; i++) { 
        formattedCode += codeList[i] + "\n";
    }
    return formattedCode;
    // console.log(formattedCode)
}

sample_code =  [
        ['from sklearn.impute import SimpleImputer', '# define the imputer', "imputer = SimpleImputer(missing_values=nan, strategy='median')", '# transform the dataset', 'transformed_values = imputer.fit_transform(values)', '# count the number of NaN values in each column', "print('Missing: %d' % isnan(transformed_values).sum())"],
]

// preprocessCode(sample_code[0])



const data = [
    {
        "id": 1,
        "query": "replace null value with their mean values",
        "intent": "null_imputation",
        "entities": "mean",
        "priority": 1,
        "code": `
                ## THIS IS SAMPLE CODE SNIPPET, CODE NOT FOUND IN DATABASE

                from sklearn.impute import SimpleImputer
                # define the imputer
                imputer = SimpleImputer(missing_values=nan, strategy='mean')
                # transform the dataset
                transformed_values = imputer.fit_transform(values)
                # count the number of NaN values in each column
                print('Missing: %d' % isnan(transformed_values).sum())
            `
    }, 
    {
        "id": 2,
        "query": "replace null value with their mean values",
        "intent": "null_imputation",
        "entities": "mean",
        "priority": 2,
        "code": `
                df.fillna(df.mean())
                print('Missing: %d' % isnan(df).sum())
            `
    }
];