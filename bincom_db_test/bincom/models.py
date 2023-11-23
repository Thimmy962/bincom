from django.urls import reverse
from django.db import models

# Create your models here.
class Polling_Unit(models.Model):
    uniqueid = models.IntegerField(primary_key=True, auto_created=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    polling_unit_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.polling_unit_name

    class Meta:
        db_table = 'polling_unit'

    
    def total_votes(self):
        votes = 0
        
        # get all the announced result linked to this polling unit through the uniqid
        results = Announced_PU_Result.objects.filter(polling_unit_uniqueid = self.uniqueid)
        
        # loop throught each result
        for result in results:

            # add the score of each announced result to the votes
            votes += result.party_score
        return votes
    
    
    def get_absolute_url(self):
        return reverse("bincom:detailed_polling_unit_result", args=[self.uniqueid])
    

    # get the announced results for this polling unit
    def get_announced_results(self):
        return Announced_PU_Result.objects.filter(polling_unit_uniqueid = self.uniqueid)





class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True, auto_created=True)
    ward_id  = models.IntegerField()
    ward_name = models.CharField(max_length=50) 
    lga_id = models.IntegerField()

    class Meta:
        db_table = 'ward'

    
    def get_polling_units(self):
        return Polling_Unit.objects.filter(ward_id = self.ward_id, lga_id = self.lga_id)
    

    def get_number_of_votes(self):
        votes = 0
        units = self.get_polling_units()
        for unit in units:
            votes += unit.total_votes()
        return votes 



    def get_number_of_polling_units(self):
        return len(self.get_polling_units())


    def get_absolute_url(self):
        return reverse("bincom:detailed_ward_result", args=[self.uniqueid])





class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True, auto_created=True)
    lga_id = models.IntegerField()
    state_id = models.IntegerField(default=25)
    lga_name = models.CharField(max_length=50)


    def get_absolute_url(self):
        return reverse("bincom:detailed_lga_result", args=[self.uniqueid])
    

    def get_number_of_votes(self):
            votes = 0
        # get all uniqueid for the polling unit under this lga
            polling_units = Polling_Unit.objects.filter(lga_id = self.lga_id)

            # loop through each polling unit and get all the Announced Pu Results whose polling_unit_uniquid
            for polling_unit in polling_units:
                votes += polling_unit.total_votes()
            return votes 


    def get_number_of_wards(self):
        return len(self.get_wards())
    
    def get_wards(self):
        return Ward.objects.filter(lga_id = self.lga_id)


    class Meta:
        db_table = 'lga'





class Announced_PU_Result(models.Model):
    result_id = models.IntegerField(primary_key=True, auto_created=True)
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()


    class Meta:
        db_table = "announced_pu_results"
