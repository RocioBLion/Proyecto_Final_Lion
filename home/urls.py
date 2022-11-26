from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from home import views

app_name = "home"
urlpatterns = [
    path('accounts/login', views.login_request, name="Login"),
    path("accounts/singup", view=views.register, name="Register"),
    path("", view=views.index, name="index"),
    path("search/", views.search, name="search"),
    #path('avatar/load', views.avatar_load, name='avatar-load'),
    path('accounts/profile', view=views.user_update, name='user-update'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url=reverse_lazy("home:password-change-done")
        ),
        name="password-change"
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/change-password-done.html'
        ),
        name="password-change-done"
    ),
]














