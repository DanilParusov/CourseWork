import json

def load_posts_from_json():
    with open('data/posts.json', 'r', encoding='UTF-8') as file:
        return json.load(file)

def get_post_by_id(id):
        index = int(id) - 1
        return load_posts_from_json()[index]