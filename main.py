from flask import Flask, render_template, request, jsonify
from posts_dao import PostsDAO
from api.views import api_blueprint

posts_dao = PostsDAO("data/posts.json", "data/comments.json")

app = Flask(__name__)
app.register_blueprint(api_blueprint)

@app.route("/")
def index_page():
    posts = posts_dao.get_posts_all()
    return render_template("index.html", posts=posts)

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    comments = posts_dao.get_comments_by_post_id(post_id)
    post = posts_dao.get_post_by_pk(post_id)
    number = len(comments)
    return render_template("post.html", comments=comments, post=post, number=number)

@app.route("/user/<user_name>")
def get_posts_by_user(user_name):
    posts = posts_dao.get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts, user_name=user_name)

@app.route('/search')
def search_page():
    word = request.args['s']
    posts = posts_dao.search_for_posts(word)
    number = len(posts)
    return render_template("search.html", posts=posts, number=number)

app.run(debug=True)