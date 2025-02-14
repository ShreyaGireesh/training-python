from django.shortcuts import render
from .models import Students
from .forms import AddStudenttForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    students = Students.objects.all()
    context = {"students": students}
    return render(request, "index.html", context)


def get_detail(request, id):
    student = Students.objects.get(id = id)
    context = {"student": student}
    return render(request, "details.html", context)

class StudentCreateView(CreateView):
    model = Students
    form_class = AddStudenttForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('index')

    
    def form_valid(self, form):
        return super().form_valid(form)