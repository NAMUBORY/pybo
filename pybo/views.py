from django.shortcuts import render, redirect
# 추가
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Question
from .forms import QuestionForm


# Create your views here.
# HttpResponse 클래스는 페이지 요청에 대신 응답을 할 때 사용하는 장고 클래스이다.
def index(request):
    # pybo 목록 출력
    # return HttpResponse("안녕하세요 pybo App에 오신것을 환영합니다.")
    question_list = Question.objects.order_by('-create_date')  # -는 내림차순
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):  # 페이지 오류시 500이 아닌 404 오류코드 띄움
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
