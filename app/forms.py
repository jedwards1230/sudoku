from django import forms

# TODO: look into parameters for form fields
# TODO: Look into creating these dynamically for arbitrary scaling
# up to 5x5 requires 9 more lines. so tedious :/
class PuzzleForm(forms.Form):
    col_0 = forms.IntegerField()
    col_1 = forms.IntegerField()
    col_2 = forms.IntegerField()
    col_3 = forms.IntegerField()
    col_4 = forms.IntegerField()
    col_5 = forms.IntegerField()
    col_6 = forms.IntegerField()
    col_7 = forms.IntegerField()
    col_8 = forms.IntegerField()
    col_9 = forms.IntegerField()
    col_10 = forms.IntegerField()
    col_11 = forms.IntegerField()
    col_12 = forms.IntegerField()
    col_13 = forms.IntegerField()
    col_14 = forms.IntegerField()
    col_15 = forms.IntegerField()
    col_16 = forms.IntegerField()