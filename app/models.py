from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models import Sum, F
# Create your models here.




class LikeDislikeManager (models.Manager):

    def questions(self):
        return self.get_queryset().filter(content_type__model='question')

    def answers(self):
        return self.get_queryset().filter(content_type__model='answer')


class LikeDislike (models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = ((LIKE, 'like'), (DISLIKE, 'dislike'))

    vote = models.SmallIntegerField(choices=VOTES, default=LIKE)
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = LikeDislikeManager()


class Author (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = "static/pictures", default='static/pictures/default.jpeg')

    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username




class QuestionManager (models.Manager):
    def get_question(self, qid):
        return self.get(pk=qid)

    def hot(self):
        return self.order_by('-id')

    def new(self):
        return self.order_by('-id')

    def find_tag(self, our_tag):
        return Question.objects.filter(question_tags__tag__tag_title=our_tag)

    def get_answers (self, qid):
        return Answer.objects.filter(question=qid)



class Question (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    rating = GenericRelation(LikeDislike, related_query_name='questions')

    objects = QuestionManager()

    def overall_rating(self):
        return LikeDislike.objects.questions().filter(object_id=self.id).aggregate(Sum('vote')).get('vote__sum') or 0


    def tag_list(self):
        return list(set(Tag.objects.filter(question_tags__question=self.id)))

    def count_answers (self):
        return (Answer.objects.filter(question = self.id)).count()

    def __str__(self):
        return self.title



class Tag (models.Model):
    tag_title = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_title



class Answer (models.Model):
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', null=True, blank=True, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    rating = GenericRelation(LikeDislike, related_query_name='answers')

    def overall_rating(self):
        return LikeDislike.objects.answers().filter(object_id=self.id).aggregate(Sum('vote')).get('vote__sum') or 0






class Question_tags(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
