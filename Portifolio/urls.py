from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('resumo/', include('resume.urls')),
    path('projetos/', include('projects.urls')),
    path('contatos/', include('contact.urls')),

]
