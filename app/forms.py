from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Question, Author, Tag, Question_tags, Answer
from django.core.exceptions import ObjectDoesNotExist


class LoginForm(forms.ModelForm):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Author
        fields = []

    def clean_login(self):
            login = self.cleaned_data['login']
            user = User.objects.filter(username=login)
            if not user:
                self.add_error('login', 'User with such login is not found')
            return user



class SettingsForm(forms.ModelForm):

    user_name = forms.CharField(min_length = 2, max_length = 50)
    email= forms.EmailField(max_length = 250)
    nick_name = forms.CharField(min_length = 2, max_length = 100)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    password_repeat = forms.CharField(widget=forms.PasswordInput(), required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = ['avatar']


    def __init__(self, this_user, request_post='', *args, **kwargs):

        if request_post:
            self.user_name = request_post.get('user_name')
        else:
            self.user_name = this_user.username

        if request_post:
            self.email = request_post.get('email')
        else:
            self.email = this_user.email

        if request_post:
            self.nick_name = request_post.get('nick_name')
        else:
            self.nick_name = this_user.first_name

        if request_post:
            self.password = request_post.get('password')

        super().__init__(*args, **kwargs)


    def save(self, this_user, commit=True):
        obj = super().save(commit=False)
        this_user.username = self.user_name
        this_user.email = self.email
        this_user.first_name = self.nick_name
        #set_pswd
        this_user.save()
        obj.user = this_user
        #obj.avatar = request_post.get('avatar'))
        #if commit:
            #pass
            #obj.save()
        return obj




class SignUpForm(forms.ModelForm):

    user_name = forms.CharField(min_length = 2, max_length = 50)
    email= forms.EmailField(max_length = 250)
    nick_name = forms.CharField(min_length = 2, max_length = 100)
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())
    avatar = forms.ImageField(required=False)


    class Meta:
        model = Author
        fields = ['avatar']

    def save(self, request_post, commit=True):
        obj = super().save(commit=False)
        u = User.objects.create_user(
        username = request_post.get('user_name'),
        email = request_post.get('email'),
        first_name = request_post.get('nick_name'),
        password = request_post.get('password'))
        u.save()
        obj.user = u
        #obj.avatar = request_post.get('avatar'))
        if commit:
            obj.save()
        return obj


    def clean_password_repeat(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password_repeat']
        if password1 and password2 and password1 != password2:
            self.add_error('password_repeat', 'Passwords dont match')
        return password2



class AskForm(forms.ModelForm):

    title = forms.CharField(min_length = 2, max_length = 100)
    content = forms.CharField(min_length = 2, max_length = 1000)
    tags = forms.CharField()


    class Meta:
        model = Question
        fields = ['title', 'content']

    def __init__(self, author, *args, **kwargs):
        self.author = author
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.author = self.author
        if commit:
            obj.save()
        return obj


    def save_tags (self, str_tags, new_question):

        tags_list = str_tags.split(', ')
        for tag in tags_list:
            tag = tag.lower()
            try:
                t = Tag.objects.get(tag_title=tag) #если такого тега нет, создаем
            except ObjectDoesNotExist:
                Tag.objects.create(tag_title = tag)
                t = Tag.objects.get(tag_title=tag)

            Question_tags.objects.create(
            tag_id = t.pk,
            question = new_question)




    def clean_title(self):
            data = self.cleaned_data['title']
            same_question = Question.objects.filter(title=data)
            if same_question:
                self.add_error('title', 'Question with the same title already exists. Please, change the title of your question')
            return data

    def clean_tags(self):
            data = self.cleaned_data['tags']
            tags_list=(data.split(', '))
            for tag in tags_list:
                if not tag:
                    self.add_error('tags', 'List the tags separated by commas')
                if len(tag)>20:
                    self.add_error('tags', 'Each tag must not have more than 20 characters')
            return data



class AnswerForm(forms.ModelForm):

    content = forms.CharField(min_length = 2, max_length = 1000)

    class Meta:
        model = Answer
        fields = ['content']

    def __init__(self, qid, author="", *args, **kwargs):
        self.author = author
        self.question = Question.objects.get(pk=qid)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.author = self.author
        obj.question = self.question
        if commit:
            obj.save()
        return obj
