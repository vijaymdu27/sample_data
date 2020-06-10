from django.shortcuts import render,HttpResponse
from data.models import Country
import csv

def index(request):
    with open('sample.txt') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
                p = Country(country=row['Country'], city=row['City'])
                p.save()
    return HttpResponse("created")
def delete(request):
    delete = Country.objects.all()
    delete.delete()
    return HttpResponse("deleted")