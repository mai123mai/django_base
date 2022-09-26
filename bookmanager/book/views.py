from django.shortcuts import render

# Create your views here.
'''
视图函数：
    所谓的视图函数，其实就是ｐｙｔｈｏｎ函数
    视图函数有两个要求：
        １．第一个参数是接收请求  就是 HttpRequest
        

'''
# request
from django.http import HttpRequest
from django.http import HttpResponse

# 首页视图函数
def index(request):
    # return HttpResponse('ok')
    '''
    render : 渲染模板
    request:请求
    template_name：模板名字
    context=None
    '''
    context = {
        'name':'马上双十一了，点我有惊喜！'
    }
    return render(request,'book/index.html',context=context)