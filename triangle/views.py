from django.shortcuts import render


def calculate_triangle(request):
    result = ""
    base = ""
    height = ""
    error = None

    if request.method == "POST":
        if 'calculate' in request.POST:
            try:
                base = float(request.POST.get("base"))
                height = float(request.POST.get("height"))
                if base <= 0 or height <= 0:
                    raise ValueError("Енгізілген сан оң болуы керек")
                result = 0.5 * base * height
            except ValueError as e:
                error = str(e)
        elif 'clear' in request.POST:
            base = ""
            height = ""
            result = ""

    return render(request, "triangle/triangle.html",
                  {"base": base, "height": height, "result": result, "error": error})
