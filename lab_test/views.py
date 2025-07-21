from django.shortcuts import render, redirect
from .forms import LabTestForm
from .models import LabTest
from patients.models import Patient  # Assuming you have a Patient model

def add_lab_test(request):
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_lab_test')  # or redirect to a success page
    else:
        form = LabTestForm()
        patients= Patient.objects.all()  # Assuming you have a Patient model

    tests = LabTest.objects.order_by('-date')
    return render(request, 'lab.html', {
        'form': form,
        'tests': tests,
        'patients': patients
    })

def lab_report(request):
    tests = LabTest.objects.order_by('-date')
    return render(request, 'lab_report.html', {
        'tests': tests
    })