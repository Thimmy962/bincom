from .models import LGA

def header_items(request):
    return {"lgas": LGA.objects.all()}
