from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^fixtures',views.team,name='fixtures'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
