from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
import base64
import pickle
from django.http import JsonResponse



def index(request):
    
    tasks = request.session.get('tasks', [])
    #if request.method == "POST":
    #    tasks -= 1
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    tasks = request.session.get('tasks', [])
    if request.method == "POST":
        
        task = request.POST.get("task")
        print(f"after adding task in add without to index{task}")
        tasks.append(task)
        print(f"tasks variable in add value is {tasks}")
       
        
        request.session['tasks'] = tasks
        
        return HttpResponseRedirect(reverse("index"))
    return render(request, "tasks/add.html", {
                  "tasks" : tasks
                  })

def delete(request, task_id):
    tasks = request.session.get('tasks', [])
    if 0 <= task_id < len(tasks):  # Check if the task_id is valid
        tasks.pop(task_id)  # Remove the task with the specified index
        request.session['tasks'] = tasks  # Update the session
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "error"})
        


def show_session_data(request):
    # Fetch session key
    session_key = request.session.session_key
    
    # Using Django's built-in methods to get session data
    s = SessionStore(session_key=session_key)
    session_data = s.load()
    print(session_data)
    return render(request, "tasks/show-session.html", {
        "session_data": session_data
    })