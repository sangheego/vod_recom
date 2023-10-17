from django.contrib import admin
from django.urls import path
from account.views import success, custom_login, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('success/', success, name='success'),
]
