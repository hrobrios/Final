from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import TareaListView, TareaCreateView, TareaUpdateView, TareaDeleteView


urlpatterns = [
    path('', views.inicio, name='home'),
    path('acceso/', views.acceso, name="acceso"),
    path('users/', views.home, name="users"),
    path('register_user/', views.register_user, name='register_user'),
    #path('formulariouser/', views.crear_usuario, name='formulariouser'),
    path("pacientes/", views.pacientes, name="pacientes"),
    path('mostrarpaciente/', views.mostrarpaciente, name='mostrarpaciente'),
    path("ficha1/", views.ficha1, name="ficha1"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='aplicacion/login.html'), name='login'),

    #path('tareas/', views.tareas, name='tareas'),
    path('mostrartarea/', views.mostrartarea, name='mostrartarea'),
    path("creartarea", TareaCreateView.as_view(), name="creartarea"),
    path("tarealista/", TareaListView.as_view(), name="tarealista"),
    path("modifitarea/<pk>/", TareaUpdateView.as_view(), name="modifitarea"),
    path("eliminar/<pk>/", TareaDeleteView.as_view(), name="eliminar"),

]