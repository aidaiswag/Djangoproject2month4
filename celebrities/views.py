from django.shortcuts import render
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