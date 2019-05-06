from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem

def todoview(request):
    all_todo = TodoItem.objects.all()
    return render(request,'index.html',
    {'all_items':all_todo})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    #create a new todo all_items
    #save
    #redirect the browser yo '/todo/'
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
