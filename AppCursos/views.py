from django.shortcuts import render

# Create your views here.
def cascada(request):
    return render(request,'Cursos/cascada.html')

def hipertexto(request):
    return render(request,'Cursos/webhtml.html')