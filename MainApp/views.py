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
    context = {'name': 'Alexander', 'mail': 'Gulin'}
    return render(request, 'index.html', context)

def about(request):  
    author = {"name": "Иван",
               "soname" : "Петрович",
               "famaly" : "Иванов", 
               "tel" : '8-923-602-01-02',
               "email" :  'vasya@mail.ru'
              }
    context = {"author": author }
    
    return render(request, "about.html", context)

    # return HttpResponse(f'Имя: {name}<br> Отчество: {soname} <br> Фамилия: {famaly}  ')  


def get_item(request, item_id):
    
   

   context = {'items': items}
   

   return render(request, 'item_page.html', context, item_id)
    
        
#    return HttpResponseNotFound(f'страница с id {item_id} не найдена')     
   

def get_items(request):
    context = {'items': items}
       
        
    return render(request, 'items_list.html', context)   
    
     
    


