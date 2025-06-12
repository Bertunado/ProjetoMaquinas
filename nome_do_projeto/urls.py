from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # inclui as URLs do app core
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='index'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pag-inicial/', views.pag_inicial, name='pag_inicial'),
    path('pecas/<str:categoria>/', views.pecas_view, name='pecas_view'),
    path('selecionar-maquina/', views.selecionar_maquina, name='selecionar_maquina'),
    path('adicionar-peca/<str:maquina>/', views.adicionar_peca, name='adicionar_peca'),
    path('excluir-peca/<str:maquina>/<int:peca_id>/', views.excluir_peca, name='excluir_peca'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)