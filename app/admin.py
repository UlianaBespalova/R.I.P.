from django.contrib import admin
from app.models import Author, Question, Answer, Tag, LikeDislike, Question_tags

# Register your models here.

class AuthorAdmin (admin.ModelAdmin):
    pass

class QuestionAdmin (admin.ModelAdmin):
    pass

class AnswerAdmin (admin.ModelAdmin):
    pass

class TagAdmin (admin.ModelAdmin):
    pass

class LikeDislikeAdmin (admin.ModelAdmin):
    pass

class Question_tagsAdmin (admin.ModelAdmin):
    pass


admin.site.register (Author, AuthorAdmin)
admin.site.register (Question, QuestionAdmin)
admin.site.register (Answer, AnswerAdmin)
admin.site.register (Tag, TagAdmin)
admin.site.register (LikeDislike, LikeDislikeAdmin)
admin.site.register (Question_tags, Question_tagsAdmin)
