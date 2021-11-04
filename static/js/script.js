function addNewCard(data) {
    query = data[0]["text"]
    intent = data[0]["intent"]
    entities = data[0]["intent"]
    
    const cards = document.querySelector(".cards");
    cards.style.visibility = "visible";
    newCard = `
        <div class="card">
            <div class="query-section">
                <h5>${query}</h5>
                <div class="info">
                    <h5>Intent: <span>${intent}</span></h5>
                    <h5>Entities: <span>${entities}</span></h5>
                </div>
            </div>`
    
    for(let i=0; i<data.length; i++) {
        newCard += `<div class="code-center">
                    <pre>
                        <code class="language-python">
                            ${data[i]['code']}
                        </code>
                    </pre>
                </div>`
    }
        
        
        newCard += `</div>`
    cards.innerHTML += newCard;
    Prism.highlightAll();

}


function getCode() {
    addNewCard(data);
}

function randomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min); 
}

const data = [
    {
        "id": 1,
        "query": "replace null value with their mean values",
        "intent": "null_imputation",
        "entities": "mean",
        "priority": 1,
        "code": `
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