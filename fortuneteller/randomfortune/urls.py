from django.urls import path,include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views
from django.conf.urls.static import static

urlpatterns=[
path("", views.fortune),

]