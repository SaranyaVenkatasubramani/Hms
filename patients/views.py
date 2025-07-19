from django.shortcuts import render
def patient_dashboard(request):
    return render(request,'patient_dashboard.html')
def doctor(request):
    return render(request,'doctor.html')
def book(request):
    return render(request,'book.html')
def patient_login(request):
    return render(request, 'patients/patdashboard.html')


