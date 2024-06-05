from django import forms

class MedicineSearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, required=False, label='Search Medicine')
