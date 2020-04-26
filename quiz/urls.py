from django.urls import path, include
from quiz.views import home_page, quiz, check_answer, reload



urlpatterns = [
    path('', home_page, name = 'index'),
    path('quiz/', quiz, name = 'quiz'),
    path('quiz/check/<str:user_answer>', check_answer, name = 'check'),
    path('quiz/reload', reload, name = 'reload')
]
