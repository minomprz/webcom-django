from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='index'),
    path('about', views.about, name='about'),
    path('wines', views.wines, name='wines'),
    path('wines/create', views.add_wine, name='create'),
    path('wines/edit', views.edit, name='edit'),
    path('delete/<int:id>', views.del_wine, name='delete'),
    path('wines/edit/<int:id>', views.edit, name='edit')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

