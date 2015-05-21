from django import forms


from menu.models import Tea, TEA_KINDS


class TeaSearchForm(forms.Form):
    name = forms.CharField(label="", max_length=255, required=False)

    kind = forms.MultipleChoiceField(
            label="kind", choices=TEA_KINDS, required=False)

    extra_report = forms.BooleanField(
            label="Export additional report", required=False)

    def clean(self):
        clnd = self.cleaned_data

        if not self.is_valid():
            return clnd

        if not clnd["name"] and not clnd["kind"]:
            raise forms.ValidationError("Please input name or kind.")

        return clnd
