from flask import Flask
import wikipediaapi


app = Flask(__name__)

wiki = wikipediaapi.Wikipedia()


@app.route("/my_article/<string:keyword>")
def get_article(keyword):
    if wiki.page(keyword).exists():
        data = wiki.page(keyword).text
        return data
    else:
        return f"'{keyword}' is not on Wikipedia"    


@app.route("/my_article/summary/<string:keyword>")
def get_summary(keyword):
    if wiki.page(keyword).exists():
        title = wiki.page(keyword).title
        summary = wiki.page(keyword).summary
        return f"{title} ::: {summary}"
    else:    
        return f"'{keyword}' is not on Wikipedia"

@app.route("/my_article/url/<string:keyword>")
def get_url(keyword):
    if wiki.page(keyword).exists():
        url = (wiki.page(keyword).canonicalurl)
        return url
    else:    
        return f"'{keyword}' is not on Wikipedia"

@app.route("/my_article/<string:keyword>/<string:word>")
def word_search(keyword,word):
    word = word.lower()
    if wiki.page(keyword).exists():
        data = (wiki.page(keyword).text).lower()
        number = data.count(word)
        if number > 0:    
            return f"'{word}' is found {number} times in '{keyword}' article"
        else:
            return f"'{word}' is not found in '{keyword}' article"
    else:    
        return f"'{keyword}' is not on Wikipedia"

@app.route("/my_article/count/<string:keyword>")
def word_counter(keyword):
    if wiki.page(keyword).exists():
        data = wiki.page(keyword).text
        number = len(data.split())
        return f"{number}"
    else:    
        return f"'{keyword}' is not on Wikipedia"        
 


    
