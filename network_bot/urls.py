# USER REGISTRATION {"username": "username", "password": "password"}
user_registration_url = 'http://127.0.0.1:8000/api/users/'  # POST

# USER GET TOKEN {"email": "email", "password": "password"}
user_get_token = 'http://127.0.0.1:8000/api/token/'  # POST

# USER CREATE POST {"title": "12345", "description": "qwertyu"}
user_create_post = 'http://127.0.0.1:8000/api/posts/'  # POST

# POST SET LIKE OR DISLIKE
set_like_or_dislike = "http://0.0.0.0:8000/api/posts/"  # POST

end_like_url = '/set_like/'
end_dislike_url = '/set_dislike/'