from faker import Faker


class FakeData:
    def __init__(self):
        self.faker = Faker()
        self.users_data = []
        self.posts_data = []
        self.user_create_url = "http://127.0.0.1:8000/api/users/"
        self.token_url = "http://127.0.0.1:8000/api/token/"
        self.post_create_url = "http://127.0.0.1:8000/api/posts/"


class FakeUsers(FakeData):

    def create_user(self):
        number_of_users = int(input('Введите количество постов которые хотите создать для пользователей: '))
        for item in range(number_of_users):
            data = {
                'email': self.faker.email(),
                'password': self.faker.password()
            }
            self.users_data.append(data)
        return self.users_data


fake_data = FakeData()
fake_users = FakeUsers()
fake_users.create_user()
print(fake_users.users_data)


class FakePosts(FakeData):

    def create_post(self):
        numbers_of_posts = int(input('Введите количество постов которые хотите создать для пользователей: '))
        for item in self.users_data:
                data = {
                    'user': item.email,
                    'title': self.faker.text()
                }
                self.posts_data.append(data)
        return self.posts_data


fake_posts = FakePosts()
fake_posts.create_post()
print(fake_posts.posts_data)
# number_of_users = 4
# user_data = []
# for i in range(number_of_users):
#     email = faker.email()
#     password = faker.password()
#     data = {
#         "email": email,
#         "password": password,
#         "password_repeat": password
#     }
#
#     user_data.append(data)
#
# number_of_posts = 16
# post_data_list = []
# for b in range(number_of_posts):
#     title = faker.job()
#     print(title)
#     description = faker.text()
#     post_data = {
#         'title': title,
#         'description': description,
#     }
#
#     post_data_list.append(post_data)
#
# user_create_url = "http://127.0.0.1:8000/api/users/"
# token_url = "http://127.0.0.1:8000/api/token/"
# post_create_url = "http://127.0.0.1:8000/api/posts/"
#
#
#
# def get_user_token(user_datas):
#     user_token_data = []
#     for item in user_datas:
#         requests.post(url=user_create_url, data=item)
#         a = requests.post(url=token_url, data=item)
#         token_data = a.json()
#         user_token_data.append(token_data['access'])
#     return user_token_data
#
#
# # print(get_user_token(user_data))
#
#
# def create_user_post(user_token, posts_data):
#     result_data = []
#     for token, post in zip(user_token, posts_data):
#         responce = requests.post(url=post_create_url, data=post, headers={'Authorization': f"Bearer {token}"})
#         result_dict = {'data': responce.text, 'status_code': responce.status_code}
#         result_data.append(result_dict)
#     return result_data
#
# # def create_like()
#
#
# def main():
#     user_tokens = get_user_token(user_data)
#     user_create_posts = create_user_post(user_tokens, post_data_list)
#
#
# main()
