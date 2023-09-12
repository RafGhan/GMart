from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rafi Ghani',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
