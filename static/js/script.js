function addNewCard(query, code) {

    const cards = document.querySelector(".cards");
    cards.style.visibility = "visible";
    newCard = `
        <div class="card">
            <div class="query-section">
                <h5>${query}</h5>
            </div>
            <div class="code-center">
                <pre>
                    <code class="language-python">
                        ${code}
                    </code>
                </pre>
            </div>
        </div>
    `
    cards.innerHTML = newCard + cards.innerHTML;
    Prism.highlightAll();

}


function getCode() {
    addNewCard(codes[0]["query"], codes[0]["code"]);
}

function randomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min); 
}

codes = [
    {
        "id": 1,
        "query": "Demo code for flask routing with port set to 3000, from backend",
        "code": `
                from flask import Flask
                app = Flask(__name__)

                # route
                @app.route('/')
                # route function
                def home():
                    # send 'hey!'
                    return 'hey!'

                # listen
                if __name__ == "__main__":
                    app.run(port=3000)
                    # if you need to make it live debuging add 'debug=True'
                    # app.run(port=3000, debug=True)
            `
    }
];