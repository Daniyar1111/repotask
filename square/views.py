from django.shortcuts import render
from .forms import SquareForm


def calculate_area(request):
    form = SquareForm()
    area = None

    if request.method == 'POST':
        if 'calculate' in request.POST:
            form = SquareForm(request.POST)
            if form.is_valid():
                side_length = form.cleaned_data['side_length']
                area = side_length ** 2
        elif 'clear' in request.POST:
            form = SquareForm()
            area = None

    return render(request, 'square/square.html', {'form': form, 'area': area})
