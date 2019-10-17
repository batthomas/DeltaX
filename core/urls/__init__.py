from django.conf.urls import include, url

from . import tasks, tags, auth, render

urlpatterns = [
    url("tasks/", include(tasks)),
    url("tags/", include(tags)),
    url("render/", include(render)),
    url("", include(auth))
]
