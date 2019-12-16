from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Question, Author, Answer, Question_tags, Tag, LikeDislike
from random import choice
from faker import Faker
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

f = Faker()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--authors', type=int)
        parser.add_argument('--questions', type=int)
        parser.add_argument('--answers', type=int)
        parser.add_argument('--likes', type=int)
        parser.add_argument('--p', type=int)


    def fill_authors(self, cnt):
        for i in range(cnt):
            u = User(username = f.name())
            u.save()
            Author.objects.create(
                rating=f.random_int(min=-100, max=100),
                user=u
            )

    def fill_pictures(self, cnt):
        list_ = Author.objects.all();
        for l in list_:
            l.avatar = "static/pictures/avatarka1"
            l.save()



    def fill_questions(self, cnt):
        author_ids = list (Author.objects.values_list('id', flat=True))
        tags = list (Tag.objects.values_list('id', flat=True))
        for i in range(cnt):
            text = f.text ()
            Question.objects.create(
            title = text,
            content = f.text(),
            author_id = choice(author_ids),
            rating=f.random_int(min=-100, max=100),
            )
            for j in range(3):
                Question_tags.objects.create(
                tag_id = choice(tags),
                question = Question.objects.get(title=text),
                )


    def fill_answers(self, cnt):
        author_ids = list (Author.objects.values_list('id', flat=True))
        questions_list = list (Question.objects.values_list('id', flat=True))
        for que in questions_list:
            for i in range(f.random_int(min=1, max=5)):
                Answer.objects.create(
                    author_id = choice(author_ids),
                    content = f.text(),
                    correct = choice([True, False]),
                    question_id = que,
                    )


    def fill_likes(self, cnt):
        #LikeDislike.objects.all().delete()
        author_ids = list (Author.objects.values_list('id', flat=True))
        question_ids = list (Question.objects.values_list('id', flat=True))
        answer_ids = list (Answer.objects.values_list('id', flat=True))
        for i in range(cnt):
            LikeDislike.objects.create(
            vote = choice([-1, 1]),
            author_id = choice(author_ids),
            content_type = ContentType.objects.get_for_model(Question),
            object_id = choice(question_ids),
            )



    def handle(self, *args, **options):
        #self.fill_authors(options.get('authors', 0))
        #self.fill_questions(options.get('questions', 0))
        self.fill_likes(options.get('likes', 0))
        #self.fill_answers(options.get('answers', 0))
        #self.fill_pictures(options.get('p', 0))
