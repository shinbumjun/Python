from django.shortcuts import render
from django.views.generic.base import TemplateView # 2) import
from django.http.response import HttpResponseRedirect

# Create your views here.

# 1
def mainFunc(request): # 요청을 받아서 처리
    return render(request, "index.html") # 포워드 방식

# 2
class CallView(TemplateView):
    template_name = "callget.html"

"""
# 3 따로따로 처리
def insertFunc(request):
    return render(request, 'insert.html') # urls(gtapp)에서 옴

# 4 따로따로 처리
def insertokFunc(request): 
    # irum = request.GET.get('name') # 이름 받기
    irum = request.GET['name']
    print(irum)
    return render(request, 'list.html', {'irum':irum}) # dict타입으로
"""    

# 한방에 처리 (insert에서 GET, POST으로 들어온것 처리)
def insertFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request, 'insert.html') # forward방식

    elif request.method == 'POST':
        print('POST 요청 처리')
        irum = request.POST.get('name') # 이름 받기
        return render(request, 'list.html', {'irum':irum})
        
    else:
        print('요청 에러')

# 오류가 한번 나옴, csrf(사이트 간 요청 위조)   
# python django csrf token를 만듬 -> 해킹방지{% csrf_token %}
    
    
    
    
    
    
    
    
    
    
    
    
    