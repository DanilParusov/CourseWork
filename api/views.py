from flask import Blueprint, jsonify
from api.utils import load_posts_from_json, get_post_by_id
import logging

api_blueprint = Blueprint('api_blueprint', __name__)
logging.basicConfig(filename='logs/api.log', level=logging.INFO)

@api_blueprint.route('/api/posts')
def all_posts():
    posts = load_posts_from_json()
    return jsonify(posts)

@api_blueprint.route('/api/posts/<post_id>')
def post_json(post_id):
    post = get_post_by_id(post_id)
    return jsonify(post)
