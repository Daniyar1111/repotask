from django import forms


class SquareForm(forms.Form):
    side_length = forms.FloatField(label='Шаршы қабырғасының ұзындығы:', min_value=0)
