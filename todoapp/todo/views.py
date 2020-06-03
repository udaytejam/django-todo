from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TodoItem

def todo(request):
    items = TodoItem.objects.all().order_by('check')
    total = TodoItem.objects.all().count()
    done = TodoItem.objects.filter(check=True).count()
    todo = total - done
    donepercent = 0 if total==0 else (done * 100)//total
    context = {'items': items, 'total':total, 'done': done, 'todo':todo, 'donepercent':donepercent}
    return render(request, 'todo/todolist.html', context)

def create_item(request):
    new_item = request.POST.get('new_item')
    item = TodoItem()
    item.name = new_item
    item.save()
    # return render(request, 'todo/todolist.html', {})    
    return HttpResponseRedirect(reverse('todo'))

# def delete_item(request, item_name):
#     print(request.POST)
#     item_to_delete = get_object_or_404(TodoItem, name=item_name)
#     print(item_to_delete)
#     item_to_delete.delete()
#     return HttpResponseRedirect(reverse('todo'))    

def update_item(request, item_id):
    item_to_update = get_object_or_404(TodoItem, id=item_id)
    check = item_to_update.check
    item_to_update.check = not check
    item_to_update.save()
    return HttpResponseRedirect(reverse('todo'))


def delete_item(request, item_id):
    print(request.POST)
    item_to_delete = get_object_or_404(TodoItem, id=item_id)
    # print(item_to_modify)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse('todo'))