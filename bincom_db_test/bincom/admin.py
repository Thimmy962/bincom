from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Polling_Unit)

@admin.register(Announced_PU_Result)
class Announced_PU_ResultAdmin(admin.ModelAdmin):
    list_display = ["result_id", "polling_unit_uniqueid", "party_abbreviation", "party_score"]
    search_fields = ["party_score", "party_abbreviation", "polling_unit_uniqueid"]
    list_filter = ["party_score", "party_abbreviation"]