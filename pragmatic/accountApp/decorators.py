from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# 겟이든 포스트든 그 pk를 확인해서 유저오브젝트가 실제 리퀘스트를 보낸 유저와 같은지를 판별하고, 아닌 경우 포비든 리턴
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # 요청을 받으면서 프라이머리 키로 값을 받은 pk를 가지고 있는 유저가 유저가 됨
        user = User.objects.get(pk=kwargs['pk'])
        # 유저를 확인함
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated


