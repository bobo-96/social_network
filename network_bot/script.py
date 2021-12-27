import requests
from faker import Faker

faker = Faker()

number_of_users = 4
user_data = []
for i in range(number_of_users):
    email = faker.email()
    password = faker.password()
    data = {
        "email": email,
        "password": password,
        "password_repeat": password
    }

    user_data.append(data)

number_of_posts = 16
post_data_list = []
for b in range(number_of_posts):
    title = faker.job()
    print(title)
    description = faker.text()
    post_data = {
        'title': title,
        'description': description,
    }

    post_data_list.append(post_data)

user_create_url = "http://127.0.0.1:8000/api/users/"
token_url = "http://127.0.0.1:8000/api/token/"
post_create_url = "http://127.0.0.1:8000/api/posts/"



def get_user_token(user_datas):
    user_token_data = []
    for item in user_datas:
        requests.post(url=user_create_url, data=item)
        a = requests.post(url=token_url, data=item)
        token_data = a.json()
        user_token_data.append(token_data['access'])
    return user_token_data


# print(get_user_token(user_data))


def create_user_post(user_token, posts_data):
    result_data = []
    for token, post in zip(user_token, posts_data):
        responce = requests.post(url=post_create_url, data=post, headers={'Authorization': f"Bearer {token}"})
        result_dict = {'data': responce.text, 'status_code': responce.status_code}
        result_data.append(result_dict)
    return result_data

# def create_like()


def main():
    user_tokens = get_user_token(user_data)
    user_create_posts = create_user_post(user_tokens, post_data_list)
    print(user_create_posts)
    print('----------------------------------------------------------------------------')
    print(post_data_list)


main()
