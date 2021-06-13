from django.http import HttpResponse
from django.shortcuts import render
from hello.models import *

def demo(request):
    return render(request, 'demo.html')
def home(request):
    return render(request, 'home.html')
def home1(request, year, month):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))
def home2(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home1时间标签：%s年/%s月" %(year, month))
def yoyo(request):
    context = {}
    context['name'] = '奥斯卡'
    return render(request, 'yoyo.html', context)
def page1(request):
    return render(request, 'page1.html')
def sonpage(request):
    context = {"ads": ["selenium", "appium", "requests"]
               }
    return render(request, 'sonpage.html', context)

def user_name(request):
    return render(request, 'name.html')
def user_mail(request):
    if request.method == 'GET':
        r = request.GET.get('name', None)
        res = ""
        res = User.objects.filter(user_name="%s" %r)
        try:
            res = res[0].mail
        except:
            res = "未查询到数据"
        return render(request, 'name.html', {"email": res})
    else:
        return render(request, 'name.html')


def register(request):
    '''注册页面'''
    res = ""
    if request.method =='POST':
        user_name = request.POST.get('username')
        psw = request.POST.get('psw')
        mail = request.POST.get('mail')
        user_lst = User.objects.filter(user_name=user_name)
        if user_lst:
            '''如果已经注册过'''
            res = "该用户已经呗注册过了：%s" %user_name
            return render(request, 'register.html', {"rename": res})
        else:
            '''r如果没有注册过，那么插入数据库'''
            test1 = User(user_name=user_name, psw=psw, mail=mail)
            test1.save()
            return render(request, 'login.html')
    # return render(request, 'register.html')


def login(request):
    '''登陆页面'''
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        psw = request.POST.get('psw',None)
        user_lst = User.objects.filter(user_name=username,psw=psw).first()
        if user_lst:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('账号密码不正确')
