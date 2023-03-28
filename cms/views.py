from django.shortcuts import render , redirect
from .forms import PostForm , CategoryForm
from .models import *
from django.views.generic import ListView , FormView , View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

class PostCategoryListView(ListView):
    template_name = './crm/post_category_list.html'
    def get_queryset(self):
        cat_filter = self.request.GET.get('category',None)
        search_text = self.request.GET.get('search',None)
        posts = {}
        if cat_filter is not None:
            posts = Post.objects.filter(category=cat_filter)
        elif search_text is not None:
            posts = Post.objects.filter(Q(title__icontains=search_text)|Q(auther__username__icontains=search_text)|Q(category__cat_name__icontains=search_text))
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


class PostFormView(LoginRequiredMixin,FormView):
    form_class = PostForm
    login_url = reverse_lazy('login_formview')
    success_url = reverse_lazy('post_formview')
    template_name = './crm/create_post.html'

    def form_valid(self, form):
        post = Post()
        data = form.cleaned_data
        post.title = data['title']
        print(data['category'].id,'cat')
        post.category = Category.objects.get(pk=data['category'].id)
        post.content = data['content']
        post.auther = self.request.user

        post.save()

        return super().form_valid(form)





class CategoryFormView(LoginRequiredMixin,FormView):
    form_class = CategoryForm
    login_url = reverse_lazy('login_formview')
    success_url = reverse_lazy('post_formview')
    template_name = './crm/create_category.html'

    def form_valid(self, form):
        cat = Category()
        data = form.cleaned_data
        cat.cat_name = data['cat_name']
        cat.cat_descr = data['cat_descr']

        cat.save()

        return super().form_valid(form)





    
    


