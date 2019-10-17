from django import forms
from django_select2.forms import Select2MultipleWidget

from ..models import Tag


class BootstrapSelect2MultipleWidget(Select2MultipleWidget):
    def build_attrs(self, *args, **kwargs):
        attrs = super(BootstrapSelect2MultipleWidget, self).build_attrs(*args, **kwargs)
        attrs.setdefault("data-theme", "bootstrap")
        return attrs

    @property
    def media(self):
        return super(BootstrapSelect2MultipleWidget, self).media + forms.Media(css={
            "width": "100%",
            "screen": (
                "https://cdnjs.cloudflare.com/ajax/libs/select2-bootstrap-theme/0.1.0-beta.10/select2-bootstrap.min.css",)})


class CreateTaskForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)
    approach = forms.CharField(widget=forms.Textarea)
    answer = forms.CharField(widget=forms.Textarea)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=BootstrapSelect2MultipleWidget)