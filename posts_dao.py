import json

class PostsDAO:

    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts_from_json(self):
        with open(self.posts_path, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def load_comments_from_json(self):
        with open(self.comments_path, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def get_posts_all(self):
        return self.load_posts_from_json()

    def get_posts_by_user(self, user_name):
        posts = []
        for post in self.get_posts_all():
            if user_name in post["poster_name"].split(" "):
                posts.append(post)
                return posts
            else:
                raise ValueError("No find post")

    def get_comments_by_post_id(self, post_id):
        comments = []
        for comment in self.load_comments_from_json():
            if post_id == comment["post_id"]:
                comments.append(comment)
                return comments
            else:
                raise ValueError("No find comments")

    def search_for_posts(self, query):
        posts = []
        for post in self.get_posts_all():
            if query.lower() in post["content"].lower():
                posts.append(post)
        return posts

    def get_post_by_pk(self, pk):
        index = int(pk) - 1
        return self.get_posts_all()[index]



