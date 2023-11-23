from django.urls import path
from .views import *

app_name = "bincom"

urlpatterns = [
    path("", polling_unit, name="index"),
    path("lgas/", lga, name="lga_list"),
    path("lga/<int:uniqueid>/", lga, name="detailed_lga_result"),
    path("wards/", ward, name="ward_list"),
    path("ward/<int:uniqueid>/", ward, name="detailed_ward_result"),
    path("polling_unit/<int:uniqueid>/", polling_unit, name="detailed_polling_unit_result"),
    path("new_polling_unit/", new_polling_unit, name="new_polling_unit"),
    path("new_result/", new_result, name="new_result"),
    path("new_polling_unit/load_wards/<int:lga_id>/", load_wards, name='load_wards'),
    path("new_result/load_wards/<int:lga_id>/", load_wards, name='load_wards'),
    path("new_result/load_polling_units/<int:lga_id>/<int:ward_id>/", load_polling_units, name='load_polling_units'),
]