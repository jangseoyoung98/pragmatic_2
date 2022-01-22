from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from accountApp.models import HelloWorld
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountApp.forms import AccountUpdateForm


def hello_world(request):
    
    # 로그인 되어 있을 경우에만 헬로월드에 접속할 수 있도록 하는 것
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accountApp:login'))


class AccountCreateView(CreateView): # class 베이스 뷰가 간단하고 직관적이다!
    model = User  # 장고 기본 제공 모델
    form_class = UserCreationForm # 장고 기본 제공 폼
    success_url = reverse_lazy('accountApp:hello_world')  # 계정 만들기 성공 했으면, 어느 경로로 연결할 것인가?
    template_name = 'accountApp/create.html'  # 어느 html 파일을 통해서 볼지?

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/update.html'

    # 업데이트의 경우도 로그인 되어 있을 경우에만 가능하도록 + 타 계정에는 접속할 수 없도록!
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountApp:login')
    template_name = 'accountApp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
