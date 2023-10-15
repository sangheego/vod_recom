from django.contrib import admin
from django.urls import path
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', account_views.login,name='login'),
    path('logout/', account_views.logout, name='logout'),
]
