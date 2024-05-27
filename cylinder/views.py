from django.shortcuts import render


def calculate_cylinder(request):
    result = ""
    radius = ""
    height = ""
    error = None

    if request.method == "POST":
        if 'calculate' in request.POST:
            try:
                radius = float(request.POST.get("radius"))
                height = float(request.POST.get("height"))
                if radius <= 0 or height <= 0:
                    raise ValueError("Енгізілген сан оң болуы керек")
                result = 3.14 * radius ** 2 * height
            except ValueError as e:
                error = str(e)
        elif 'clear' in request.POST:
            radius = ""
            height = ""
            result = ""

    return render(request, "cylinder/cylinder.html",
                  {"radius": radius, "height": height, "result": result, "error": error})
