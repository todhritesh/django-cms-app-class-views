from django.shortcuts import render , redirect
from .forms import PostForm
from .models import *
from django.views.generic import ListView , FormView , View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse_lazy

class PostCategoryListView(ListView):
    template_name = './crm/post_category_list.html'
    def get_queryset(self):
        filter_text = self.request.GET.get('category')
        posts = {}
        if filter_text is not None:
            posts = Post.objects.filter(category=filter_text)
        else:
            posts = Post.objects.all()
        categories = Category.objects.all()
        return {'posts':posts,'categories':categories}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset()) 
        return context


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "./crm/login.html"
    success_url = reverse_lazy('post_category_listview')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        form = self.get_form()

        user = authenticate(username=username , password=password)

        if user is not None:
            login(request, user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)


class LogoutView(View):
    def get(self , request):
        logout(request)
        return redirect('post_category_listview')




    
    


