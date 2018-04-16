from django.db import models

# Create your models here.
class CardiovascularD(models.Model):
    """
    Model representing a types of cardiovascular diseases 
    """
    name = models.CharField(max_length=200, help_text="Enter a cardiovascular disease)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
#class Refernces(models.Model):
# name = models.CharField(max_length=200, help_text="Enter a refernce)")
    # reference will be like ncbi and dna bank of japan, embl, swissprot"
   # def __str__(self):
        """
       # String for representing the Model object (in Admin site etc.)
        """
        #return self.name