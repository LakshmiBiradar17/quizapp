from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Controller -Business logic
from quizapp.models import Question
from django.shortcuts import  render


def index(request):
    questions_list  = Question.objects.all()
    # output = ""
    # for question in questions:
    #     output = output + question.content
    # return HttpResponse(output)
    return render(request,"quizapp/index.html",{'questions_list': questions_list})


def detail(request, question_id):
    message = ""
    is_correct = False
    if request.method == "POST":
        answer_id = int(request.POST.get("answer"))
        # question_id = request.POST.get("question_id")
        question = Question.objects.get(id=question_id)

        for answer in question.answer_set.all():
            if answer_id == answer_id and answer.correct:
                message = "Correct answer"
                is_correct = True
                break

            if not is_correct:
                message = "wrong answer"

        print(question_id, answer_id)
        print(request.body)
    question = Question.objects.get(id=question_id)
    return render(request, "quizapp/detail.html", {'question': question, 'message': message, 'result': is_correct})
