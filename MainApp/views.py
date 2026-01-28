from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist





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
    
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, 'errors.html', {'errors': [f'Item with id={item_id} not found']})
    else:
         context = {'item': item}

    
    return render(request, "item_page.html", context)
           
    
def get_items(request):
    context = {'items': Item.objects.all()}
       
        
    return render(request, 'items_list.html', context)   
    
     
    


