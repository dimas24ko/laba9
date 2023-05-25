from django.http import HttpResponse

def project(request):
    return HttpResponse('laba 9')

def student(request):
    return HttpResponse('Kosharenko Dmytro')