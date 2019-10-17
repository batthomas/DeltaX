from django.urls import path

from ..views.tags import *

urlpatterns = [
    path("", OverviewView.as_view(), name="tags_overview"),
    path("<int:tag_id>", DetailsView.as_view(), name="tags_details")
]
