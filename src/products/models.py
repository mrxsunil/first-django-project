from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # have to user max_length
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=10000)
    summary     = models.TextField(blank=False,null=False)
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
       return reverse("products:product_details_view", kwargs={"my_id":self.id })

# blank => how the field is rendered if True, then it is required, has nothing to do with database
# null => has to do with database, if True, django will store empty values as null
