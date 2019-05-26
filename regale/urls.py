from django.contrib import admin
from django.urls import path,include
from regaleapp import views, static
from regale import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/',views.signup),
    path('login/',views.signin),
    path('logout/',views.logout_view),
    path('dashboard/<int:pk>/',views.dashboard),
    path('search/',views.dashboard),
    path('profile/<int:pk>/',views.profile_view),
    path('profile/<int:pk>/edit/',views.profile_edit),
    path('create_profile/<int:pk>/', views.create_profile),
    path('cusines/',views.cusines_view),
    path('profiles/',views.profiles_list_view),
    path('friendship/', include('friendship.urls')),
    path('profile/<int:pk>/sendrequest/',views.profile_view),
    path('about/',views.error_404),
    path('contact_us/',views.error_404)
]
