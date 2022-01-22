from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from accountApp.models import HelloWorld
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountApp.forms import AccountUpdateForm

from accountApp.decorators import account_ownership_required

# 배열로 만들고, 메서드 데코레이터에 넣으면, 배열 내에 있는 데코레이터를 다 확인함
has_ownership = [account_ownership_required, login_required()]


@login_required
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

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountApp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountApp:login')
    template_name = 'accountApp/delete.html'
