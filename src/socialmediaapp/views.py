from django.shortcuts import render,get_object_or_404,redirect
from .models import Articale_list
from .forms import ArticlecreateForm,UserLoginForm,UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
import datetime as dt
date1 = dt.datetime.now().date()


def article_list(request):
    articledata=Articale_list.objects.all()
    query1=request.GET.get('query')
    if query1:
        articledata = Articale_list.objects.filter(
        Q(title__icontains = query1) |
        Q(author__username = query1) |
        Q(body__icontains = query1)
        )
    paginator = Paginator(articledata,4)
    page = request.GET.get('page')

    try:
        articledata = paginator.page(page)
    except PageNotAnInteger:
        articledata = paginator.page(1)
    except EmptyPage:
        articledata = paginator.page(paginator.num_pages)

    return render(request,'article.html',{'articledata':articledata})

def article_detaile(request,id,slug):
    articledata=get_object_or_404(Articale_list,id=id,slug=slug)
    is_liked=False
    if articledata.likes.filter(id=request.user.id).exists():
        is_liked=True
    return render(request,'articledetaile.html',{'articledata':articledata,
                                                'is_liked':is_liked,
                                                'total_likes':articledata.total_likes()})
def ArticleLike(request):
    aid=request.POST.get('articledata_id')
    articledata=get_object_or_404(Articale_list, id=aid)

    if articledata.likes.filter(id=request.user.id).exists():
        articledata.likes.remove(request.user)
        is_liked=False
    else:
        articledata.likes.add(request.user)
        is_liked=True
    return HttpResponseRedirect(articledata.get_absolute_url())

def article_create(request):
    if request.method=='POST':
        form = ArticlecreateForm(request.POST)
        if form.is_valid():
            title1 = request.POST.get('title')
            body1 = request.POST.get('body')
            Articale_list(
            title = title1,
            body = body1,
            author = request.user,
            created_date = date1
            ).save()
            messages.success(request, 'New Article Is Crated Successfully')
            return redirect('article_list')
    else:
        form = ArticlecreateForm()
        return render(request,'articlecreate.html',{'form':form})

def registerView(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('loginview')
        else:
            return HttpResponse('Invalid Data')
    else:
        form = UserRegisterForm()
        return render(request,'registerform.html',{'form':form})

def loginView(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username,password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'User Login Successfully')
                    return redirect('article_list')
                else:
                    return HttpResponse('Inactive Person')
            else:
                return HttpResponse('None')
        else:
            return HttpResponse('Incorrect Detail Given')

    else:
        form=UserLoginForm()
        return render(request,'loginform.html',{'form':form})

def logoutview(request):
    logout(request)
    messages.success(request, 'User Logout Successfully')
    return redirect('article_list')










# suresh--->abcd1234
#avanthik--->xyz@1234
#siva ------>siva@9502
#baburao--->rao@9876
#hanvika--->hanvi@9876
#ganesh====>gani@543
