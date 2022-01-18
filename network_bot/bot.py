from likes import AddLike
from posts_create import send_posts
from users_create import get_user_token


add_like = AddLike(send_posts, get_user_token,
                    method='POST'.upper()).add_like()