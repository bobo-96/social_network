from faker import Faker

from config import MAX_USERS, users_amount
from send_request import SendRequest
from urls import user_registration_url, user_get_token


class GenerateUser:
    def __init__(self, amount_users, max_users):
        self.amount_users = amount_users
        self.max_users = max_users

    faker = Faker()

    def generate_user(self):
        users = []
        if self.amount_users > self.max_users:
            raise ValueError(
                {"Error": f"You can generate max {self.max_users} users!"})
        else:
            for user in range(self.amount_users):
                user = {}
                user["email"] = self.faker.email()
                user["password"] = self.faker.password()
                users.append(user)
            return users


generate_users = GenerateUser(users_amount, MAX_USERS).generate_user()


class UserRegistrationApi(SendRequest):
    def __init__(self, users, method=None):
        super().__init__(method)
        self.users = users

    def send_request(self):
        send_users = []
        for user in self.users:
            response = self.send_url(data=user, url=user_registration_url)
            user['id'] = response['id']
            send_users.append(user)
        return send_users


user_registration_api = UserRegistrationApi(
    method='POST'.upper(), users=generate_users).send_request()


class GetUserToken(SendRequest):
    def __init__(self, users, method=None):
        super().__init__(method)
        self.users = users

    def get_token(self):
        user_tokens = []
        for user in self.users:
            response = self.send_url(url=user_get_token, data=user)
            response['id'] = user['id']
            user_tokens.append(response)

        return user_tokens


get_user_token = GetUserToken(
    users=user_registration_api, method='POST'.upper()).get_token()
