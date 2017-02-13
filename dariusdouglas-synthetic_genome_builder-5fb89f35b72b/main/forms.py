from django import forms

from .models import Genome


# FORM THAT WILL BE USED TO CREATE GENOMES
class GenomeForm(forms.ModelForm):
    class Meta:
        # FIELDS TO DISPLAY IN FORM USED TO CREATE GENOME
        model = Genome
        fields = ['title',
                  'file']
