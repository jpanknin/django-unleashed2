from django.conf.urls import url

from .views import homepage, tag_detail

urlpatterns = [
	url(r'^$', homepage),
	url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer/tag_detail.html')
]