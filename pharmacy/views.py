

from django.shortcuts import render, redirect
from .forms import InventoryForm
from .models import PharmacyItem, DispensedMedicine
from .forms import InventoryForm, DispenseMedicineForm

def pharmacy_home(request):
    inventory = PharmacyItem.objects.all()
    prescriptions = DispensedMedicine.objects.all()
    inventory_form = InventoryForm()
    dispense_form = DispenseMedicineForm()
    return render(request, 'pharmacy.html', {
        'inventory': inventory,
        'prescriptions': prescriptions,
        'inventory_form': inventory_form,
        'dispense_form': dispense_form
    })

def add_inventory_item(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('pharmacy-home')
def dispense_medicine(request):
    if request.method == 'POST':
        form = DispenseMedicineForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('pharmacy-home')



