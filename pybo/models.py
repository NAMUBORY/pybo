from django.db import models


# Create your models here.
# 질문 모델 추가(테이블)
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()  # 괄호 없어서 오류남/ 괄호 유의
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# 답변 모델 추가(테이블)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


