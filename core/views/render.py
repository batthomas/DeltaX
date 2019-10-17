import base64

from django.shortcuts import render, redirect
from django.views.generic import View

from ..forms import ChangeQueueForm, QueueChangeAction
from ..latex_renderer import LatexDocument
from ..models import Task
from ..views import AuthenticationRequiredMixin


class RenderView(AuthenticationRequiredMixin, View):
    template_name = "render/render.html"
    viewer_template = "render/viewer.html"

    def get(self, request, *args, **kwargs):
        queue = []
        if request.session.get("queue", False):
            for tid in request.session.get("queue"):
                queue.append(Task.objects.get(pk=tid))
        return render(request, self.template_name, {"queue": queue})

    def post(self, request, *args, **kwargs):
        queue = []
        if request.session.get("queue", False):
            for tid in request.session.get("queue"):
                queue.append(Task.objects.get(pk=tid))
        document = LatexDocument(queue)
        latex = document.generate_latex()
        pdf = document.generate_pdf()
        return render(request, self.viewer_template, {
            "latex": latex,
            "pdf": base64.b64encode(pdf).decode()
        })


class QueueView(AuthenticationRequiredMixin, View):
    template_name = "render/queue.html"

    def get(self, request, *args, **kwargs):
        queue = []
        if request.session.get("queue", False):
            for tid in request.session.get("queue"):
                queue.append(Task.objects.get(pk=tid))
        return render(request, self.template_name, {"queue": queue})


class ChangeQueueView(AuthenticationRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        form = ChangeQueueForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            action = form.cleaned_data["action"]
            render_queue = request.session.get("queue")
            if not isinstance(render_queue, list):
                render_queue = []
            if action == QueueChangeAction.CREATE:
                if task not in render_queue:
                    render_queue.append(task)
            elif action == QueueChangeAction.DELETE:
                if task in render_queue:
                    render_queue.remove(task)
            request.session["queue"] = render_queue
            return redirect("tasks_details", task)
        return redirect("tasks_overview")
