from django.contrib import admin
from django.urls import path, include
from meme.views import DefaultPages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DefaultPages.as_view()),
    path('signup/', DefaultPages.as_view(template='default/signup.html', mode='signup')),
    path('signin/', DefaultPages.as_view(template='default/signin.html')),
    path(r'alias/', include('alias.urls')),
    path(r'hookah/', include('hookah.urls')),
]
