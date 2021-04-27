from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateView

app_name = 'festival'

urlpatterns = [
    path('',  views.Topview.as_view(), name='home'),
    path('festival/',views.IndexView.as_view() , name = 'index'),
    path('festival/create/', views.CreateView.as_view(), name ='create'),
    path('festival/<str:url_code>/<int:pk>/update/', views.UpdateView.as_view(), name ='update'),
    path('festival/<str:url_code>/', views.CategoryView.as_view(), name='category'),
    path('festival/<str:url_code>/<int:pk>', views.area, name = 'detail'),
    path('about/', views.AboutView.as_view(), name = 'about' ),
    path('policy/', views.PolicyView.as_view(), name = 'policy' ),
    path('sitemap/', views.SitemapView.as_view(), name = 'sitemap' ),
    path('requirements/', views.RequirementsView.as_view(), name = 'requirements' ),
    path('contact/', views.contact, name='contact'),
    path('contact/complete/', views.complete, name='complete')

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
