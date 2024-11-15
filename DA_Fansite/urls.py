from django.urls import path
from django.contrib import admin
from DA_Fansite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('companion/<int:posicao>/', views.detalhes_companion, name='descricao_lista'),
    path('classe/<str:clase>/', views.detalhes_classe, name='classe')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('companion/<int:posicao>/', views.detalhes_companion, name='descricao_lista'),
    path('classe/<str:clase>/', views.detalhes_classe, name='classe'),
    path('adicionar-dado/', views.adicionar_dado, name='adicionar_dado'),
    path('editar-dado/<int:id>/', views.editar_dado, name='editar_dado'),
    path('remover-dado/<int:id>/', views.remover_dado, name='remover_dado'),
    path('entrar/', views.entrar, name='entrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
]