from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(f'<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>Иванов И.П.</i>' )
                        
                        

