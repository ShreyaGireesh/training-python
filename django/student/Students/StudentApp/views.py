from django.shortcuts import render
from .models import Students

# Create your views here.
def index(request):
    students = Students.objects.all()
    context = {"students": students}
    return render(request, "index.html", context)


def get_detail(request, id):
    student = Students.objects.get(id = id)
    context = {"student": student}
    return render(request, "details.html", context)