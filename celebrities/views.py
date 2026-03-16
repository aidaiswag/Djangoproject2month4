from django.shortcuts import render, redirect
from django.http import HttpResponse
from celebrities.models import Celebrity
from celebrities.forms import CreateCelebrityForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # return HttpResponse("Hello world!")
    return render (request, "home.html" )

def list_celebrities(request):
     if request.method == "GET":
        all_celebrities = Celebrity.objects.all()
        return render(request=request, template_name="t_celebrities/list_celebrities.html", context={"celebrities": all_celebrities})    

def detail_celebrity(request, id):
    if request.method == "GET":
        celebrity = Celebrity.objects.get(id=id)
        return render(request=request, template_name="t_celebrities/detail_celebrity.html", context={"celebrity": celebrity})

@login_required(login_url="/users/sign-in/")
def create_celebrity(request):
    if request.method == 'POST':
        form = CreateCelebrityForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse("Error data")
        name = form.cleaned_data.get("name")
        biography = form.cleaned_data.get("biography")
        childhood = form.cleaned_data.get("childhood")
        image = form.cleaned_data.get("image")
        career = form.cleaned_data.get("career")
        

        Celebrity.objects.create(name=name, biography=biography, childhood=childhood, image=image, career=career)
        return redirect(f"/celebrities/")
    if request.method == 'GET':
        form = CreateCelebrityForm()
        return render(request=request, template_name="t_celebrities/create_celebrity.html", context={"form": form})    
    
