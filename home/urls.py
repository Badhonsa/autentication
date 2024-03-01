
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from auucount.views import *
from visit.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('logout/', log_out, name='logout'),
    path('reg/', registration_page, name='reg'),
    path('forget_pass/', forget_pass, name='forget_pass'),
    path('Talk/',Talk, name='Talk'),
    path('verify_acc/',verify_acc, name='verify_acc'),





]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
