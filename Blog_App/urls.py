"""Blog_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from Blog_Application import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/',views.Welcome.as_view()),
    path('BlogWelcome/',views.BlogWelcome.as_view(),name='BlogWelcome'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    path('PostBlog/',views.PostBlog.as_view()),
    path('ViewBlog/',views.ViewBlog.as_view(),name='ViewBlog'),
    path('Detail/<pk>',views.DetailViewBlog.as_view()),
    path('Delete/<pk>',views.DeleteBlog.as_view()),
    path('BlogSignup/',views.BlogSignup.as_view()),
    path('CheckUser/',views.checkUser),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
