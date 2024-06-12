from django.urls import path
from .import views
from django.contrib.staticfiles.urls import static
from django.conf import settings


urlpatterns = [
   path("login/", views.login_user, name='login'),
   path("signup/", views.register_page, name='register'),
   path('profile/',views.user_profile, name='profile'),
   path('logout/', views.logou_user, name='logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)