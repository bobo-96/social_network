from faker import Faker

from config import posts_amount, MAX_POSTS
from send_request import SendRequest
from urls import user_create_post
from users_create import get_user_token


class GeneratePost:
    def __init__(self, users, amount_posts, max_posts):
        self.users = users
        self.amount_posts = amount_posts
        self.max_posts = max_posts

    def generate_post(self):
        posts = []
        faker = Faker()
        if self.amount_posts > self.max_posts:
            raise ValueError(
                {"Error": f"You can generate max {self.max_posts} posts!"})
        else:
            for user in self.users:
                url = user_create_post
                access_token = user['access']
                for post in range(self.amount_posts):
                    post = {}
                    post["title"] = faker.name
                    post["description"] = faker.text
                    post['url'] = url
                    post['token'] = access_token
                    posts.append(post)
            return posts


create_posts = GeneratePost(get_user_token, posts_amount, MAX_POSTS).generate_post()


class SendPost(SendRequest):
    def __init__(self, posts, method=''):
        super().__init__(method=method)
        self.posts = posts

    def send_post(self):
        send_posts = []
        for post in self.posts:
            data = {'title': post['title'], 'description': post['description']}
            response = self.send_url(url=post['url'], data=data, headers={
                'Authorization': f"Bearer {post['token']}"})
            data['id'] = response['id']
            send_posts.append(data)
        return send_posts


send_posts = SendPost(create_posts, 'POST'.upper()).send_post()
