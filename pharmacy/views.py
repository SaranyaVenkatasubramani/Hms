
from django.shortcuts import render, redirect
from .forms import PharmacyItemForm
from .models import PharmacyItem

def pharmacy_view(request):
    if request.method == 'POST':
        form = PharmacyItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacy')
    else:
        form = PharmacyItemForm()

    inventory = PharmacyItem.objects.all().order_by('-added_on')  # Fetch from DB
    return render(request, 'pharmacy.html', {
        'form': form,
        'inventory': inventory
    })