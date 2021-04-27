from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('',include('festival.urls')),
    path('festival/',  include('festival.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url = '/festival/') ),
    path('accounts/', include('social_django.urls', namespace='social')),
]
