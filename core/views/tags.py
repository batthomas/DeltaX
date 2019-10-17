from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from ..models import Tag


class OverviewView(View):
    template_name = "tags/overview.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"tags": Tag.objects.all()})


class DetailsView(View):
    template_name = "tags/details.html"

    def get(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=self.kwargs.get("tag_id"))
        tasks = tag.tasks.order_by("created")

        page = request.GET.get("page", 1)
        paginator = Paginator(tasks, 10)

        tasks = paginator.get_page(page)
        return render(request, "tags/details.html", {
            "tag": Tag.objects.get(pk=self.kwargs.get("tag_id")),
            "tasks": tasks
        })
