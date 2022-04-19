from django.db import models

# Create your models here.
class Reports(models.Model):
    scenario_name = models.CharField(max_length=10,blank=True)
    facility_size = models.IntegerField(blank=True)
    no_of_manufacturing_suites = models.IntegerField(blank=True)
    no_of_qc_labs = models.IntegerField(blank=True)
    no_of_process_trains_in_parallel = models.IntegerField(blank=True)
    cleanroom = models.IntegerField(blank=True)
    qc = models.IntegerField(blank=True)
    fixed_capital_investment = models.IntegerField(blank=True)
    no_of_operators = models.IntegerField(blank=True)
    manufacturing_time = models.IntegerField(blank=True)

    def __str__(self):
        return self.scenario_name