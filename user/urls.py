from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/',views.register,name='user-register'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile,name='user-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
