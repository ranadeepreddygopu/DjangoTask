from django.shortcuts import render,redirect
from Task.forms import TaskForm
from Task.models import Task

# Create your views here.
def Home(request):
    return render(request,'Home.html')
def Add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Add/')
            except:
               pass
    else:
        form = TaskForm()
    return render(request,'Taskadd.html',{'form':form})
def search(request):
    if request.method == 'POST':
        if 'Name' in request.POST and request.POST['Name']:
            q = request.POST['Name']
            Tasks = Task.objects.filter(Name=q)
            return render(request, 'search_results.html',
                {'Tasks': Tasks, 'query': q})
    else:
        return render(request,'Search.html')
def GetImages(request):
    return render(request,'GetImages.html')
