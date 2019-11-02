from django.urls import path

from ..views.tasks import *

urlpatterns = [
    path("", OverviewView.as_view(), name="tasks_overview"),
    path("<int:task_id>", DetailsView.as_view(), name="tasks_details"),
    path("create/", CreateView.as_view(), name="tasks_createtask")
]
