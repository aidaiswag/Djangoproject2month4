"""
URL configuration for celebrity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from celebrities.views import list_celebrities, detail_celebrity, home, create_celebrity
from django.conf import settings
from django.conf.urls import static
from users.views import sign_up, sign_in, sign_out

users = [
    path("users/sign-up/", sign_up),
    path("users/sign-in/", sign_in),
    path("users/sign-out/", sign_out)
]
 
celebrities = [
    path("celebrities/", list_celebrities),
    path("celebrities/<int:id>/", detail_celebrity),
    path("celebrities/create/", create_celebrity)
] 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    *celebrities,
    *users
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
