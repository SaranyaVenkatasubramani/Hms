from django.shortcuts import render, redirect
from .forms import LabTestForm
from .models import LabTest

def add_lab_test(request):
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_lab_test')
    else:
        form = LabTestForm()
    
    recent_tests = LabTest.objects.order_by('-date')[:5]
    return render(request, 'lab.html', {'form': form, 'recent_tests': recent_tests})

