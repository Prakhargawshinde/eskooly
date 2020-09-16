from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView,ListView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Blog_Application.models import Post_blog_form
from django.urls import reverse
from django.contrib.auth.models import User
from Blog_Application import models
from django import forms
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
class Welcome(TemplateView):
    template_name = 'Blog_Application/welcome.html'


@method_decorator(login_required, name='dispatch')
class BlogWelcome(TemplateView):
    template_name = 'Blog_Application/blogwelcome.html'

@method_decorator(login_required, name='dispatch')
class PostBlog(CreateView):
    model = Post_blog_form
    fields = ('Title','Description','Pic')
    def get_success_url(self):
        return reverse('ViewBlog')


class ViewBlog(ListView):
    model = Post_blog_form
    fields = '__all__'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ViewBlog, self).get_context_data(**kwargs)
        list_blog = Post_blog_form.objects.all()
        paginator = Paginator(list_blog, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_blog = paginator.page(page)
        except PageNotAnInteger:
            file_blog = paginator.page(1)
        except EmptyPage:
            file_blog = paginator.page(paginator.num_pages)
        context['list_blog'] = file_blog
        return context

class DetailViewBlog(DetailView):
    model = Post_blog_form

class DeleteBlog(DeleteView):
    model = Post_blog_form
    def get_success_url(self):
        return reverse('BlogWelcome')

class BlogSignup(CreateView):
    model = User
        #fields = "__all__"
    fields = ('username','password','email','first_name','last_name')
    def get_success_url(self):
        return reverse('login')

def checkUser(request):
    usercheck = request.GET.get('username')
    print('usercheck')
    data = {'is_exist':User.objects.filter(username__iexact=usercheck).exists()}
    print(data)
    return JsonResponse(data)
