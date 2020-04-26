import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Question, Option, Answer
from django.views.decorators.csrf import csrf_exempt
question_arr = list(Question.objects.all())
displayed_question = []
dict = {}
correct, wrong, total_question = 0, 0, 0
# Create your views here.
def home_page(request):
    return render(request, 'homepage.html')

def quiz(request):
    if request.method == 'POST':
        global dict, total_question
        name = request.POST['name']
        nickname = request.POST['nickname']
        number = request.POST['number']
        if nickname == '':
            dict['name'] = name
            dict['number'] = number
        else:
            dict['name'] = name
            dict['nickname'] = nickname
            dict['number'] = number
    total_question += 1
    question = random.choice(question_arr)
    while question in displayed_question:
        question = random.choice(question_arr)
    displayed_question.append(question)
    options = question.option_set.all()      #add list here
    answers = question.answer_set.all()
    dict['question'] = question
    dict['options'] = options
    dict['answers'] = answers
    dict['correct'] = correct
    dict['wrong'] = wrong
    if total_question-1 == int(dict['number']):
        return render(request, 'result.html', context=dict)
    else:
        return render(request, 'quizquestion.html', context=dict)

@csrf_exempt
def check_answer(request, user_answer):
    global correct, wrong
    question = dict['question']
    correct_answer = question.answer_set.all()[0]
    if correct_answer.answer == user_answer:
        correct += 1
        return JsonResponse({
            'message':'Bingo!!! You got that right',
        })
    wrong += 1
    return JsonResponse({
        'message':'OOPS! You got that wrong.Correct one is '+correct_answer.answer
    })

def reload(request):
    global displayed_question, dict, correct, wrong, total_question
    displayed_question = []
    dict = {}
    correct, wrong, total_question = 0, 0, 0
    return render(request, 'homepage.html')
