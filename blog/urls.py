from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



