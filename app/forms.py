from django import forms

# TODO: Make this able to scale with board size
class PuzzleForm(forms.Form):
    col_0 = forms.CharField(label='0', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_1 = forms.CharField(label='1', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_2 = forms.CharField(label='2', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_3 = forms.CharField(label='3', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_4 = forms.CharField(label='4', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_5 = forms.CharField(label='5', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_6 = forms.CharField(label='6', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_7 = forms.CharField(label='7', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    col_8 = forms.CharField(label='8', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
'''    cell_9 = forms.CharField(label='9', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_10 = forms.CharField(label='10', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_11 = forms.CharField(label='11', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_12 = forms.CharField(label='12', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_13 = forms.CharField(label='13', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_14 = forms.CharField(label='14', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_15 = forms.CharField(label='15', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_16 = forms.CharField(label='16', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cell_17 = forms.CharField(label='17', widget=forms.TextInput(attrs={'readonly':'readonly'}))'''