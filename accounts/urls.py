from django.urls import path

from .views import SignUpPageView

# Create url patterns below
urlpatterns = [
    path("signup/", SignUpPageView.as_view(), name="signup"),
]
