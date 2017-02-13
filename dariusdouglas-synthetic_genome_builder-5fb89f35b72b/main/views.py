from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Genome
from .forms import GenomeForm
from Gene_Expressions.Gene_Expression import main

# CONTEXT DICTIONARIES CONTAIN DATA SENT TO TEMPLATES


# List all genome objects on template
def list(request):
    all_genomes = Genome.objects.all()

    # ALLOWS SEARCHING FOR A PARTICULAR GENOME IN LIST
    # Q IS SEARCH BOX INPUT
    query = request.GET.get('q')

    # IF QUERY INPUT IN SEARCH BOX, FILTER LIST BASED ON INPUT
    if query:
        all_genomes = all_genomes.filter(title__contains=query)
    context = {
        'genome_list': all_genomes,
    }
    return render(request, "genome_list.html", context)


# GET A PARTICULAR GENOME OBJECT FROM DATABASE
def detail(request, id=None):

    # IF OBJECT DOES NOT EXIST RETURN ERROR MESSAGE
    instance = get_object_or_404(Genome, id=id)
    context = {
        'genome': instance
    }
    return render(request, "genome_detail.html", context)


# USE DATA INPUT FROM FORM TO CREATE GENOME
def create(request):
    # DECLARE GENOME FORM
    form = GenomeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # ADD EVERY POTENTIAL PROTEIN TO SYNTHETIC GENOME
        setattr(instance, 'sequence', main(request.FILES['file'].read().splitlines()))
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {"form": form}
    return render(request, "genome_create.html", context)


# PATH TO CHEATSHEET TEMPLATE
def cheatsheet(request):
    return render(request, 'cheatsheet.html', {})


# PATH TO DNA MODEL TEMPLATE
def DNA_3D(request):
    return render(request, 'DNA_3D.html', {})


# PATH TO INDEX PAGE
def index(request):
    template = "index.html"
    context = {}
    return render(request, template, context)
