from django.shortcuts import render, redirect
from django.http import HttpResponse
from celebrities.models import Celebrity

# Create your views here.
def home(request):
    # return HttpResponse("Hello world!")
    return render (request, "home.html" )

def list_celebrities(request):
    all_celebrities = Celebrity.objects.all()
    return render(request=request, template_name="t_celebrities/list_celebrities.html", context={"celebrities": all_celebrities})    

def detail_celebrity(request, id):
    celebrity = Celebrity.objects.get(id=id)
    return render(request=request, template_name="t_celebrities/detail_celebrity.html", context={"celebrity": celebrity})

def create_celebrity(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        biography = request.POST.get("biography")
        childhood = request.POST.get("childhood")
        image = request.FILES.get("image")
        career = request.POST.get("career")

        Celebrity.objects.create(name=name, biography=biography, childhood=childhood, image=image, career=career)
        return redirect(f"/celebrities/")
    if request.method == 'GET':
        return render(request=request, template_name="t_celebrities/create_celebrity.html")    