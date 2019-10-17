from enum import IntEnum

from django import forms


class QueueChangeAction(IntEnum):
    CREATE = 0
    DELETE = 1


class ChangeQueueForm(forms.Form):
    task = forms.IntegerField(widget=forms.HiddenInput())
    action = forms.TypedChoiceField(choices=[(e.value, e.name) for e in QueueChangeAction], coerce=int)