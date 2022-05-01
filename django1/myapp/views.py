from django.shortcuts import render
from django.http.response import HttpResponse

# 스프링 서블릿

# Create your views here.
def indexFunc(request): # 클라이언트 요청에 반응 [응답]
    # return HttpResponse('요청 처리 결과') # 요청 처리 결과
    
    msg = '장고 만세'
    # ss = "<html><body>장고 프로젝트 구현 %s</html></body>" %msg
    ss = "<html><body>장고 프로젝트 구현 {}</html></body>".format(msg)
    return HttpResponse(ss)

def showFunc(request):
    
    msg = '파이썬 어쩌구 저쩌구'
    return render(request, 'show.html', {'mymsg':msg}) # render - forward 방식, dict로, 밀어버려서 요청명이 생긴것











