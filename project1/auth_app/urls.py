from django.urls import path

from .views import user_login, user_signup, user_logout, change_password

urlpatterns = [
    path("login/", user_login, name="user_urls"),
    path("signup/", user_signup, name="signup_urls"),
    path("logout/", user_logout, name="logout_urls"),
    path("cpass/", change_password, name="cpass_urls")
]
