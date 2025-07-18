
from django.shortcuts import render

def doc_dashboard(request):
    return render(request, 'docdashboard.html')
def appointment(request):
    return render(request,'appointlist.html')
    