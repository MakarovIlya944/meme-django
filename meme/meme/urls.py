from django.contrib import admin
from django.urls import path, include
from default import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path(r'alias/', include('alias.urls')),
]
