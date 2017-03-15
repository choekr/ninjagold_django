from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ninjaGold/index.html")

def process(request):
    pass
