from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("features/", views.features, name="features"),
    path("contacts/", views.contacts, name="contacts"),


    path('register/', views.register, name='register'),
    #path('login/', views.register, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('notes/create', views.note_create, name='note_create'),
    path('notes/view/<int:pk>/', views.note_view, name='note_view'),
    path('notes/remove/<int:pk>/', views.note_delete, name='note_delete'),
]