from django.shortcuts import render
from django.http import HttpResponse
from celebrities.models import Celebrity

# Create your views here.
def index(request):
    # return HttpResponse("Hello world!")
    return render (request, "index.html" )

def list_celebrities(request):
    all_celebrities = Celebrity.objects.all()
    return render(request=request, template_name="list_celebrities.html", context={"celebrities": all_celebrities})    