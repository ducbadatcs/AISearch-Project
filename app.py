from flask import url_for, Flask, render_template, request, redirect
from multiquery_search import multi_query_search

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("search")
    docs, ai_summary = multi_query_search(query)
    print(f"Received query: {query}")
    
    return render_template("search.html", 
                           query=query, 
                           docs = docs, ai_summary = ai_summary)
    
if __name__ == "__main__":
    app.run(debug=True)