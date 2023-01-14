from posts_dao import PostsDAO

posts_keys_should_be = {"poster_name", "poster_avatar", "pic", "content",  "views_count", "likes_count", "pk"}
comments_keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


class TestPostsDao:

    def test_get_posts_all(self):
        posts = PostsDAO("../data/posts.json", "../data/comments.json").get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == posts_keys_should_be, "неверный список ключей"

    def test_get_posts_by_user(self):
        posts = PostsDAO("../data/posts.json", "../data/comments.json").get_posts_by_user("leo")
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert posts[0]["poster_name"] == "leo", "возвращаются неверные посты"
        assert set(posts[0].keys()) == posts_keys_should_be, "неверный список ключей"

    def test_get_comments_by_post_id(self):
        comments = PostsDAO("../data/posts.json", "../data/comments.json").get_comments_by_post_id(1)
        assert type(comments) == list, "возвращается не список"
        assert len(comments) > 0, "возвращается пустой список"
        assert set(comments[0].keys()) == comments_keys_should_be, "неверный список ключей"
        assert comments[0]["commenter_name"] == "hanna", "возвращается неверый комментарий"

    def test_get_post_by_pk(self):
        post = PostsDAO("../data/posts.json", "../data/comments.json").get_post_by_pk(1)
        assert type(post) == dict, "возвращается не словарь"
        assert set(post) == posts_keys_should_be, "неверный список ключей"
        assert post["poster_name"] == "leo", "возвращается неверный пост"













