from django.shortcuts import render

# Create your views here.


def lobby(request):
    return render(request=request, template_name='clients/lobby.html')