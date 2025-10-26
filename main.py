import requests
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
response = requests.get("https://api.npoint.io/c4e9524c14e578859d8a")
all_posts = [x for x in response.json()]
author = "Angela Yu"
current_year = datetime.today().year


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts, author=author, year=current_year)

@app.route('/about')
def about():
    return render_template("about.html", year=current_year)

@app.route('/contact')
def contact():
    return render_template("contact.html", year=current_year)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    for post in all_posts:
        if post["id"] == blog_id:
            requested_post = post
    return render_template("post.html", post=requested_post, year=current_year)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form["username"]
    mail = request.form["email"]
    phone = request.form["phone"]
    text = request.form["message"]
    print(f'{name}\n{mail}\n{phone}\n{text}')
    return f"<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)