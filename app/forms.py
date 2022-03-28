from django import forms

class PuzzleForm(forms.Form):
    cell_0 = forms.CharField(disabled=True)
    cell_1 = forms.CharField()
    cell_2 = forms.CharField()
    cell_3 = forms.CharField()
    cell_4 = forms.CharField()
    cell_5 = forms.CharField()
    cell_6 = forms.CharField()
    cell_7 = forms.CharField()
    cell_8 = forms.CharField()