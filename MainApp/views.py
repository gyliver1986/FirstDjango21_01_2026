from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    return HttpResponse(f'<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>Иванов И.П.</i>' )


def about(request):  
    name = "Иван"
    soname = "Петрович"
    famaly = "Иванов" 
    tel = '8-923-602-01-02'
    email =  'vasya@mail.ru'

    return HttpResponse(f'Имя: {name}<br> Отчество: {soname} <br> Фамилия: {famaly}  ')  


def get_item(request, item_id):
    for item in items:
        if item['id'] == item_id:
            resul = f""" 
            <h2> имя: {item['name']}</h2>
            <p> количество: {item["quantity"]} </p>
            <p> <a href='/items'> назад к списку товара </a> </p> 
            """
            return HttpResponse(resul)
        
    return HttpResponseNotFound(f'страница с id {item_id} не найдена')     
   

def get_items(request):
    result = "<h1>список товара</h1><ol>"
    for item in items:
        result += f"""<li><a href='/item/{item['id']}'> {item['name']} </a> </li> """

    result += '</ol>'    
        
    return HttpResponse(result)    
    
     
    


