from django.urls import path
from . import views
from .views import criar_superusuario


urlpatterns = [
   path('cadastro/', views.cadastro, name='cadastro'),
   path('criar-superusuario/', criar_superusuario),
    path('login/', views.login_view, name='login'),
    path('', views.pag_inicial, name='pag_inicial'), 
    path('adicionar-peca/<str:maquina>/', views.adicionar_peca, name='adicionar_peca'),
    path('adicionar-peca/', views.escolher_maquina, name='escolher_maquina'),
    path('peças/', views.peças, name='peças'),
    path('selecionar-maquina/', views.selecionar_maquina, name='selecionar_maquina'),
    path('excluir-peca/<int:peca_id>/', views.excluir_peca, name='excluir_peca'),

    path('fabrica-2/', views.fabrica2, name='fabrica2'),
    path('fabrica-3/', views.fabrica3, name='fabrica3'),

    path('perfiladora-fabrica2/', views.perfiladora_fabrica2, name='perfiladora_fabrica2'),
    path('cosma_perfiladoras-fabrica2/', views.cosma_perfiladoras_fabrica2, name='cosma_perfiladoras_fabrica2'),
    path('fagorGabinete-perfiladoras-fabrica2/', views.fagorGabinete_perfiladoras_fabrica2, name='fagorGabinete_perfiladoras_fabrica2'),
    path('olmaFH_perfiladoras-fabrica2/', views.olmaFH_perfiladoras_fabrica2, name='olmaFH_perfiladoras_fabrica2'),
    path('sares1_perfiladoras-fabrica2/', views.sares1_perfiladoras_fabrica2, name='sares1_perfiladoras_fabrica2'),
    path('sares2_perfiladoras-fabrica2/', views.sares2_perfiladoras_fabrica2, name='sares2_perfiladoras_fabrica2'),

    path('pintura-fabrica2/', views.pintura_fabrica2, name='pintura_fabrica2'),
    path('pinturapo3_F2/', views.pinturapo3_F2, name='pinturapo3_F2'),
    path('pinturapo4_F2/', views.pinturapo4_F2, name='pinturapo4_F2'),

    path('prensas-fabrica2/', views.prensas_fabrica2, name='prensas_fabrica2'),
    path('omera1_prensas-fabrica2/', views.omera1_prensas_fabrica2, name='omera1_prensas_fabrica2'),
    path('omera2_prensas-fabrica2/', views.omera2_prensas_fabrica2, name='omera2_prensas_fabrica2'),
    path('omera3_prensas-fabrica2/', views.omera3_prensas_fabrica2, name='omera3_prensas_fabrica2'),
    path('omera4_prensas-fabrica2/', views.omera4_prensas_fabrica2, name='omera4_prensas_fabrica2'),

    path('prensa-fabrica3/', views.prensa_fabrica3, name='prensa_fabrica3'),
    path('Aita_prensa-F3/', views.Aita_prensa_F3, name='Aita_prensa_F3'),
    path('fagor_prensa-F3/', views.fagor_prensa_F3, name='fagor_prensa_F3'),

    path('perfiladora-fabrica3/', views.perfiladora_fabrica3, name='perfiladora_fabrica3'),
    path('jundiai_perfiladorasF3/', views.jundiai_perfiladorasF3, name='jundiai_perfiladorasF3'),
    path('sares3_perfiladorasF3/', views.sares3_perfiladorasF3, name='sares3_perfiladorasF3'),
    path('sares4_perfiladorasF3/', views.sares4_perfiladorasF3, name='sares4_perfiladorasF3'),

    path('pintura_fabrica3/', views.pintura_fabrica3, name='pintura_fabrica3'),
    path('pinturaliquidaF3/', views.pinturaliquidaF3, name='pinturaliquidaF3'),

    



    ]
