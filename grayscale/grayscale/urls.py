from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from imageconvert.views import HomeView, task_status, task_result

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tasks/status/(?P<task_id>[a-zA-Z0-9-_]+)/$', task_status),
    url(r'^tasks/result/(?P<task_id>[a-zA-Z0-9-_]+)/$', task_result),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
