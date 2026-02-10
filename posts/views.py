from django.shortcuts import get_object_or_404,redirect,render

from .models import Post

from django.views.generic.edit import CreateView
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView,DeleteView

from django.urls import reverse_lazy

from .forms import PostForm,CommentForm,UserRegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth import login, logout
from django.contrib import messages



class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'  
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='published').order_by('-created_at')
    paginate_by = 5
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  
        return context



    



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug,status='published')
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        else:
            messages.error(request, "Invalid comment.")

        return redirect('post_detail', slug=slug)
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('post_list')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

class DashboardView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        
        return Post.objects.filter(author=self.request.user).order_by('-created_at')

class UserPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('dashboard')    
    
class UserPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user    