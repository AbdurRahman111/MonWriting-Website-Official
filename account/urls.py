from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup_function, name="signup_function"),
    path('submit_signup', views.submit_signup, name="submit_signup"),
    path('login', views.login_function, name="login_function"),
    path('logout', views.logout_funciotn, name="logout_function"),
    path('update-profile',views.update_profile, name='update_profile'),
]