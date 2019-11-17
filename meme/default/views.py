from django.shortcuts import render

# Create your views here.
def sindex(request):
    return render(request, "index.html")
