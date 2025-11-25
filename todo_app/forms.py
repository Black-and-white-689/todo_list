from django import forms

from django.forms import DateInput

from todo_app.models import Task, Tag


#  Adding/Editing Tasks
class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Task tags"
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": DateInput(attrs={"type": "date"})
        }


#  Search forms
class TaskSearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by task"}),
    )


class TagSearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by tag"}),
    )
