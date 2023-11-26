from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import StudentForm
from .models import Student
import json

def get_author(request):
    template = loader.get_template("master.html")
    return HttpResponse(template.render())


def register(request):
    if request.method == "POST":
        form=StudentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form["name"].data
            email = form["email"].data
            resume_file = request.FILES.get('resume')
            Student.objects.create(name=name, email=email, resume=resume_file)
            return HttpResponse("success")
        return HttpResponse(json.dumps(form.errors))
    form = StudentForm()
    context = {"form": form}
    return render(request, "register.html", context)



# def submitaction(request):
#     form = StudentForm(request.POST, request.FILES)
#     if form.is_valid():
#         name = form["name"].data
#         email = form["email"].data
#         resume_file = request.FILES.get('resume')
#         Student.objects.create(name = name, email = email, resume=resume_file)
#         return HttpResponse("success")
#     return HttpResponse(json.dumps(form.errors))










