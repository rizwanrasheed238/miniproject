from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('singleproduct/<int:id>/', views.singleproduct, name='singleproduct'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('shop/', views.shop, name='shop'),

]
