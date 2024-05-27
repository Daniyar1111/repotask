from django.shortcuts import render


def calculate_resistance(request):
    result = None
    r1 = ""
    r2 = ""
    error = None

    if request.method == "POST":
        if 'calculate' in request.POST:
            try:
                r1 = float(request.POST.get("r1"))
                r2 = float(request.POST.get("r2"))
                if r1 <= 0 or r2 <= 0:
                    raise ValueError("Кедергі оң сан болуы қажет")
                result = (r1 * r2) / (r1 + r2)
            except ValueError as e:
                error = str(e)
        elif 'clear' in request.POST:
            r1 = ""
            r2 = ""
            result = ""

    return render(request, "resistance/resistance.html",
                  {"r1": r1, "r2": r2, "result": result, "error": error})
