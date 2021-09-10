from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.SignUp.as_view(), name="signup") # as_view create a generic view
]
