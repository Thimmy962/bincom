from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator





def lga(request, uniqueid = False):
    if uniqueid:
        try:

            lga = LGA.objects.get(uniqueid = uniqueid)
    
        except LGA.DoesNotExist:
            return render(request, "lga.html",{
            "message": "LGA DOES EXIST"
            })


        return render(request, "lga.html",{
        "lga": lga,
        "wards": lga.get_wards()
        })

    queryset = LGA.objects.all()

    p = Paginator(queryset, 15)
    page = request.GET.get("page")
    lgas = p.get_page(page)

    return render(request, "index.html",{
        "lgas": lgas
    })





def ward(request, uniqueid=False):
    if uniqueid:
        try:

            ward = Ward.objects.get(uniqueid = uniqueid)
    
        except LGA.DoesNotExist:
            return render(request, "ward.html",{
            "message": "WARD DOES EXIST"
            })


        return render(request, "ward.html",{
        "ward": ward,
        "polling_units": ward.get_polling_units()
        })
    
    queryset = Ward.objects.all()

    p = Paginator(queryset, 20)
    page = request.GET.get("page")
    wards= p.get_page(page)

    return render(request, "ward.html",{
        "wards": wards
    })





# class Polling_Unit_list(ListView):
#     queryset = Polling_Unit.objects.all().exclude(lga_id = 0, ward_id = 0)
#     template_name = "polling_units.html"
#     paginate_by = 15
#     context_object_name = "polling_units"

# polling_unitlist = Polling_Unit_list.as_view()





def polling_unit(request, uniqueid = False):
    if uniqueid:
        try:

            unit = Polling_Unit.objects.get(uniqueid = uniqueid)
        
        except LGA.DoesNotExist:
            return render(request, "polling_units.html",{
            "message": "Polling Unit DOES EXIST"
            })

        return render(request, "polling_units.html",{
        "unit": unit,
        "results": unit.get_announced_results()
        })
    queryset = Polling_Unit.objects.all()

    p = Paginator(queryset, 15)
    page = request.GET.get("page")
    polling_units = p.get_page(page)

    return render(request, "polling_units.html",{
        "polling_units": polling_units
    })    





def new_result(request):
    if request.method == "POST":
        try:
            polling_unit_uniqueid = request.POST.get("polling_unit")
            party = request.POST.get("party")
            score = request.POST.get("party_score")
            another_result = request.POST.get("another_result")

            new = Announced_PU_Result(polling_unit_uniqueid = polling_unit_uniqueid,
                                    party_abbreviation = party, party_score = score)
            
            new.save()

            if another_result == "Yes":
                return HttpResponseRedirect(reverse("bincom:new_result"))
            elif another_result == "No":
                return HttpResponseRedirect(reverse("bincom:index"))
        except:
            LGAS = LGA.objects.all()
            return render(request, "new_results.html",{
            "lgas": LGAS,
            "wards": Ward.objects.filter(lga_id = LGAS.first().lga_id),
            "parties": ["PDP", "DPP", "ACN", "PPA", "CDC", "JP", "ANPP", "LABO", "CPP"],
            "message": "Party Score Out of Range"
        })

    else:
        LGAS = LGA.objects.all()
        return render(request, "new_results.html",{
            "lgas": LGAS,
            "wards": Ward.objects.filter(lga_id = LGAS.first().lga_id),
            "parties": ["PDP", "DPP", "ACN", "PPA", "CDC", "JP", "ANPP", "LABO", "CPP"]
        })
    


# save and go to home page
def new_polling_unit(request):
    if request.method == "POST":
        name = request.POST.get("polling_unit_name")
        unit_id = request.POST.get("polling_unit_id")
        lga_id = request.POST.get("lga_id")
        ward_id = request.POST.get("ward_id")
        add_new = request.POST.get("add_new_result")

        new = Polling_Unit(polling_unit_name = name, 
                           polling_unit_id = unit_id,
                           ward_id = ward_id,
                           lga_id = lga_id)
        new.save()
        if add_new == "Yes":
            return HttpResponseRedirect(reverse("bincom:new_result"))
        elif add_new == "No":
            return HttpResponseRedirect(reverse("bincom:index"))
        
    else:
        LGAS = LGA.objects.all()
        return render(request, "new_polling_unit.html",{
            "lgas": LGAS,
            "wards": Ward.objects.filter(lga_id = LGAS.first().lga_id)
        })


def load_wards(request, lga_id):
    try:
        wards = Ward.objects.filter(lga_id = lga_id).all()
        data = [{"ward_id":ward.ward_id,"ward_name": ward.ward_name} for ward in wards]
        print(data)
        return JsonResponse(data, safe = False)
    except:
        return JsonResponse([], safe=False)
    




def load_polling_units(request, lga_id, ward_id):
    try:
        units = Polling_Unit.objects.filter(lga_id = lga_id, ward_id = ward_id)
        data = [{"unit_id":unit.uniqueid,"unit_name": unit.polling_unit_name} for unit in units]
        print(data)
        return JsonResponse(data, safe = False)
    except:
        return JsonResponse([], safe=False)