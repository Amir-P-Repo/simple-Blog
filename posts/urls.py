from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'),name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/post/<slug:slug>/edit/', views.UserPostUpdateView.as_view(), name='user_post_edit'),
    path('dashboard/post/<slug:slug>/delete/', views.UserPostDeleteView.as_view(), name='user_post_delete'),


]