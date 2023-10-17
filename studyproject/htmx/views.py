from django.shortcuts import render,redirect,HttpResponse
from .models import task
from django.http import JsonResponse
from .forms import taskform

def task_list(request):
    tasks = task.objects.all()
    #print(tasks)
    

    if request.method == 'post':
        pass
    
        return render(request,'task.html',{'tasks': tasks})
    return render(request,'task.html',{'tasks': tasks})

'''def toggle_task(request,task_id):        
        form = taskform(request.POST)
        print('post working')
        if form.is_valid():
            tasks = task.objects.get(pk=form.cleaned_data['task_id'])
            print('datafetch')
            tasks.status = not tasks.status
            print('invertstatus')
            tasks.save()
            print('save')
            
            return render(request,'task.html')
        return JsonResponse({'error' : 'error'})'''
    
def clicked(request):
    return HttpResponse('<button>Clicked</button>')