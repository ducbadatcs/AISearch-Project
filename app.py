from flask import url_for, Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    print("searchj")
    query: str =  request.form.get("search")
    print(f"Received query: {query}")
    return render_template("search.html", query=query)
    
if __name__ == "__main__":
    app.run(debug=True)