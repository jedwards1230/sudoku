from django import forms

# TODO: apply readonly dynamically in template. editing is currently blocked.
# TODO: look into parameters for form fields
# TODO: Look into creating these dynamically for arbitrary scaling
# up to 5x5 requires 9 more lines. so tedious :/
class PuzzleForm(forms.Form):
    col_0 = forms.IntegerField(label='0')
    col_1 = forms.IntegerField(label='1')
    col_2 = forms.IntegerField(label='2')
    col_3 = forms.IntegerField(label='3')
    col_4 = forms.IntegerField(label='4')
    col_5 = forms.IntegerField(label='5')
    col_6 = forms.IntegerField(label='6')
    col_7 = forms.IntegerField(label='7')
    col_8 = forms.IntegerField(label='8')
    col_9 = forms.IntegerField(label='9')
    col_10 = forms.IntegerField(label='10')
    col_11 = forms.IntegerField(label='11')
    col_12 = forms.IntegerField(label='12')
    col_13 = forms.IntegerField(label='13')
    col_14 = forms.IntegerField(label='14')
    col_15 = forms.IntegerField(label='15')
    col_16 = forms.IntegerField(label='16')