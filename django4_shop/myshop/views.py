from django.shortcuts import render

# Create your views here.

def mainFunc(request): # 메인
    return render(request, 'main.html') # main.html 생성

def page1Func(request): # 1페이지
    return render(request, 'page1.html') # page1.html 생성

def page2Func(request): # 2페이지
    return render(request, 'page2.html') # page2.html 생성

def cartFunc(request): # 장바구니
    name = request.POST["name"]
    price = request.POST["price"]
    print(name, price)
    product = {'name':name, 'price':price}
    
    productList = [] # 세션에 들어갈... 장바구니
    if "shop" in request.session: # 첫번째 상품은 없을것 ->
        productList = request.session['shop']
        productList.append(product)
        request.session['shop'] = productList # 세션 30분간 기억
    else:
        productList.append(product)
        request.session['shop'] = productList
        
    print(productList)
    context = {} # html에 보낼 용도
    context['products'] = request.session['shop'] # context라는 dict타입에 들어감
    return render(request, 'cart.html', context)

def buyFunc(request): # 결제하기
    if "shop" in request.session:
        productList = request.session['shop'] # 세션에 있는거 모두 꺼냄 
        print(productList)
        
        total = 0 
        for pro in productList: # 총 금액 구하기
            total += int(pro['price'])
        print(total)
        request.session.clear() # session 안에 모든 키 삭제
        
    return render(request, 'buy.html', {'total':total})









