from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template.context_processors import csrf
from django.contrib import auth
from django.conf import settings as settings_s
from .forms import MyRegisterForm
from django.contrib.auth.models import User

from .models import *

def pagination(page, object_list):
    p = Paginator(object_list, settings_s.PAGE_CONST)

    try:
        objects_page = p.get_page(page)

    except PageNotAnInteger:
        objects_page = p.get_page(1)

    return objects_page

class MainView(TemplateView):
    template_name = 'questions/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            all_tags = Tag.objects.get_all_tags()
            questions = Question.objects.sort_by_question_date()
            objects_page = pagination(request.GET.get('page'), questions);
            return render(request, self.template_name, {"tags": all_tags, "page_obj": objects_page, "user": auth.get_user(request)})
        else:
            all_tags = Tag.objects.get_all_tags()
            questions = Question.objects.sort_by_question_date()
            objects_page = pagination(request.GET.get('page'), questions);
            return render(request, self.template_name, {"tags": all_tags, "page_obj": objects_page})


def ask(request):
    all_tags = Tag.objects.get_all_tags()
    return render(request, "questions/ask.html", {"tags" : all_tags})  #Ищет путь до файла отностильно папки templates

def question(request, questions_id):
    all_tags = Tag.objects.get_all_tags()
    question = Question.objects.get_by_id(questions_id)
    answers = Answer.objects.get_answer_by_question(questions_id)
    return render(request, "questions/question.html", {'answers':answers,'questions_id':questions_id, 'question':question,
                                                       "tags": all_tags})

def tag(request, tag_name):
    all_tags = Tag.objects.get_all_tags()
    questions_by_tag = Tag.objects.all().filter(title=tag_name)
    #questions_by_tag = Question.objects.filter(entry__tags__title = tag_name)
    return render(request, "questions/tag.html", {'tag_name': tag_name, 'questions':questions_by_tag, "tags": all_tags})

# Добавить выход на страницу ту, с которой авторизовались
def login(request):
    all_tags = Tag.objects.get_all_tags()

    prev = request.GET.get('сontinue')

    args={}
    args.update(csrf(request))
    args['tags']=all_tags
    args['prev']=prev

    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(prev)
        else:
            args['login_error']="Sorry, wrong password or login!"
            return render_to_response("questions/login.html",args)
    else:
        return render_to_response("questions/login.html",args)


def logout(request):
    prev = request.GET.get('сontinue')
    auth.logout(request)
    return redirect(prev)

def register(request):

    # ИСПРАВИТЬ ОШИБКУ В ПЕРЕДАЧЕ ДАННЫХ

    #all_tags = Tag.objects.get_all_tags()
    #return render(request, "questions/register.html",{"tags": all_tags})
    args = {}
    args.update(csrf(request))

    if request.POST:
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("/")
    else:
        form = MyRegisterForm()
        args['form']=form
        return render(request,"questions/register.html",args )


def settings(request):
    all_tags = Tag.objects.get_all_tags()
    return render(request, "questions/settings.html", {"tags": all_tags})

def hot(request):
    all_tags = Tag.objects.get_all_tags()
    questions = Question.objects.sort_by_question_date()
    objects_page = pagination(request.GET.get('page'), questions);
    return render(request, 'questions/hot.html', {"tags": all_tags, "page_obj": objects_page})