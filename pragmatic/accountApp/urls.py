from django.urls import path

from accountApp.views import hello_world, AccountCreateView

app_name = "accountApp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create'),
]