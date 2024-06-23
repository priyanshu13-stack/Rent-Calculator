from django.db import models

class RentEntry(models.Model):
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    last_electricity_units = models.PositiveIntegerField(default=0)
    current_electricity_units = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - Rent: {self.monthly_rent}, Last Units: {self.last_electricity_units}, Current Units: {self.current_electricity_units}, Cost per Unit: {self.cost_per_unit}"
