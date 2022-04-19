from django.shortcuts import render,HttpResponse


def reports(request):
    return render(request, 'home.html')
    # return HttpResponse("Report model is created")