from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from accountApp.models import HelloWorld
from django.views.generic import CreateView


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountApp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountApp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView): # class 베이스 뷰가 간단하고 직관적이다!
    model = User  # 장고 기본 제공 모델
    form_class = UserCreationForm # 장고 기본 제공 폼
    success_url = reverse_lazy('accountApp:hello_world')  # 계정 만들기 성공 했으면, 어느 경로로 연결할 것인가?
    template_name = 'accountApp/create.html'  # 어느 html 파일을 통해서 볼지?




