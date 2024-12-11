from flask import url_for, Flask, render_template, request, redirect
from multiquery_search import multi_query_search

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("search")
    search_data = multi_query_search(query)
    print(f"Received query: {query}")
    
    return render_template("search.html", 
                           query=query, 
                           docs = search_data[0], ai_summary = search_data[1])
    
if __name__ == "__main__":
    app.run(debug=True)