from django.urls import path

from ..views.render import *

urlpatterns = [
    path("", RenderView.as_view(), name="render_render"),
    path("queue/", QueueView.as_view(), name="render_queue"),
    path("change/", ChangeQueueView.as_view(), name="render_change")
]
