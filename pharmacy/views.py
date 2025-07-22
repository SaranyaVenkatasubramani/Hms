from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PharmacyItemForm
from .models import PharmacyItem
from .models import Prescription

def pharmacy_view(request):
    if request.method == 'POST':
        form = PharmacyItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacy')
    else:
        form = PharmacyItemForm()

    inventory = PharmacyItem.objects.all().order_by('-added_on')
    prescriptions = Prescription.objects.all().order_by('-date_created')  # 🔹 Add this

    return render(request, 'pharmacy.html', {
        'form': form,
        'inventory': inventory,
        'prescriptions': prescriptions  # 🔹 Pass it to the template
    })




@login_required
def pharmacy_dashboard(request):
    inventory = Inventory.objects.all()
    prescriptions = Prescription.objects.select_related('patient', 'doctor').order_by('-date_created')

    form = InventoryForm()

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacy_dashboard')

    return render(request, 'pharmacy/pharmacy.html', {
        'inventory': inventory,
        'prescriptions': prescriptions,
        'form': form
    })