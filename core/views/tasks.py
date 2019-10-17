from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View

from .auth import AuthenticationRequiredMixin
from ..forms import CreateTaskForm
from ..models import Task


class OverviewView(View):
    template_name = "tasks/overview.html"

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by("created")

        paginator = Paginator(tasks, 5)
        page = request.GET.get("page", 1)

        tasks = paginator.get_page(page)
        return render(request, self.template_name, {"tasks": tasks})


class DetailsView(View):
    template_name = "tasks/details.html"

    def get(self, request, *args, **kwargs):
        context = {"task": Task.objects.get(pk=self.kwargs.get("task_id"))}
        return render(request, self.template_name, context)


class CreateView(AuthenticationRequiredMixin, View):
    template_name = "tasks/create.html"

    def get(self, request, *args, **kwargs):
        form = CreateTaskForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.user = request.user
            task.task = form.cleaned_data["question"]
            task.approach = form.cleaned_data["approach"]
            task.answer = form.cleaned_data["answer"]
            task.save()
            for tag in form.cleaned_data["tags"]:
                task.tags.add(tag)
            task.save()
            return redirect("tasks_details", task.pk)
