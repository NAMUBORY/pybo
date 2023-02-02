from django.contrib import admin
# 추가
from .models import Question
from .models import Answer


# Register your models here.
# [검색] 기능 소스 추가
# 클래스 상속
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
