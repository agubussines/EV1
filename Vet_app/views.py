from django.shortcuts import render

# Create your views here.
def landing_page(request):
    # Esto le dice a Django que renderice el archivo index.html
    return render(request, 'index.html')