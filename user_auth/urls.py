from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', RegisterUser, name="sign_up"),
    path('signin/', loginUser, name="sign_in"),
    path('signout/', logoutUser, name="sign_out")
]
