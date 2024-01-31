from django.urls import path
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',views.home,name='home'),
    path('logIn/',views.logIn,name='logIn'),
    path('signup/',views.signUp,name="signUp"),
    path('logOut/',views.logOut,name='logOut'),
    path('restaurant/<int:id>/',views.restaurant,name='restaurant'),
    path('allMenu/<int:id>/',views.allMenu,name='allMenu'),
    path('menu/',views.Menu,name='Menu')


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)