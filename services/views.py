from django.shortcuts import render, redirect

# Create your views here.


def cloud_services_view(request):
    return render(request, "services/cloud-services.html")
    
def web_and_app_view(request):
    return render(request, "services/web-and-app-services.html")

def it_consulting_view(request):
    return render(request, "services/it-consulting-services.html")

def security_and_compliance_view(request):
    return render(request, "services/security-and-compliance-serevices.html")

def training_serevices_view(request):
    return render(request, "services/training-serevices.html")

def other_serevices_view(request):
    return render(request, "services/other-serevices.html")
