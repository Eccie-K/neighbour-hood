from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^home/',views.home, name='home'),
    url(r'signup', views.signup, name='signup'),
    url(r'^new_hood/', views.new_hood, name='new_hood'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^update_profile/', views.update_profile, name='update_profile'),
    url(r"^details/(?P<hood_id>[0-9])$", views.details, name="details"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)