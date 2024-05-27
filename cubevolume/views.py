from django.shortcuts import render
from .forms import SquareForm


def calculate_volume(request):
    form = SquareForm()
    volume = None

    if request.method == 'POST':
        if 'calculate' in request.POST:
            form = SquareForm(request.POST)
            if form.is_valid():
                side_length = form.cleaned_data['side_length']
                volume = side_length ** 3
        elif 'clear' in request.POST:
            form = SquareForm()
            volume = None

    return render(request, 'cube/cube.html', {'form': form, 'volume': volume})
