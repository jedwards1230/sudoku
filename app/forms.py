from django import forms

class PuzzleForm(forms.Form):
    cell_0 = forms.CharField(label='0')
    cell_1 = forms.CharField(label='1')
    cell_2 = forms.CharField(label='2')
    cell_3 = forms.CharField(label='3')
    cell_4 = forms.CharField(label='4')
    cell_5 = forms.CharField(label='5')
    cell_6 = forms.CharField(label='6')
    cell_7 = forms.CharField(label='7')
    cell_8 = forms.CharField(label='8')