from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AskForm, AnswerForm, LoginForm, SettingsForm
from app.models import Author
from django.contrib.auth.models import User
#from django.core.exceptions import KeyError

# Create your views here.

def paginate (request, object_list):

    current_page = Paginator(object_list, 5)
    page = request.GET.get ('page')

    try:
        our_objects_list = current_page.page(page)
    except PageNotAnInteger:
        our_objects_list = current_page.page(1)
    except EmptyPage:
        our_objects_list = current_page.page(current_page.num_pages)

    return our_objects_list



def index (request):
    return render (request, 'index.html' , {
    'questions_list': paginate(request, Question.objects.new()),
    })


def hot_questions (request):
    return render (request, 'index_hot.html' , {
    'questions_list': paginate(request, Question.objects.hot()),})


def tag_questions (request, tg):
    return render (request, 'index_tag.html' , {'tg':tg,
    'questions_list': paginate(request, Question.objects.find_tag(tg)),})


def question (request, qid):
    if request.POST:
        form = AnswerForm(qid, request.user.author, data=request.POST)
        if form.is_valid():
            answer = form.save()
            return redirect(reverse("one-question", kwargs={'qid': qid}))
    else:
        form = AnswerForm(qid)
    return render(request, 'one-question.html', {
    'question': Question.objects.get_question(qid),
    'answers' : Question.objects.get_answers(qid),
    'form': form })



def login (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('login')
            password = request.POST.get('password')
            user = auth.authenticate(username = username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render (request, 'login.html', {'form': form, 'login':form.data.get('login')})


def logout (request):
    auth.logout(request)
    return redirect(reverse("index"))



def signup (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST),
        files = request.FILES,
        if form.is_valid():
            author = form.save(request.POST)
            return redirect(reverse("login"))
    else:
        form = SignUpForm()
    return render (request, 'signup.html', {
    'form': form,
    'user_name':form.data.get('user_name'),
    'email':form.data.get('email'),
    'nick_name':form.data.get('nick_name')})



@login_required(login_url="login")
def ask(request):
    if request.POST:
        form = AskForm(request.user.author, data=request.POST)
        if form.is_valid():
            question = form.save()
            form.save_tags(request.POST.get('tags'), question)
            return redirect(reverse("one-question", kwargs={'qid': question.pk}))
    else:
        form = AskForm(request.user.author)

    return render(request, 'ask.html', {
    'form': form,
    'title':form.data.get('title'), #ты мне не нравишься
    'content':form.data.get('content'),
    'tags':form.data.get('tags')})





@login_required(login_url="login")
def settings (request):
    saved = ""
    if request.POST:
        form = SettingsForm(request.user, request.POST, data=request.POST)
        #form.save(request.user) #
        if form.is_valid():
            form.save(request.user)
            saved = "Changes saved"

    else:
        form = SettingsForm(request.user)

    return render (request, 'settings.html', {
    'form': form,
    'user_name':form.user_name,
    'email':form.email,
    'nick_name':form.nick_name,
    'saved':saved})



















#@login_required(login_url="login")
#def settings (request):
#    return render (request, 'settings.html', {})
