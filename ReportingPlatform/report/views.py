from turtle import end_fill
from django.shortcuts import render, redirect
from django.http import Http404

from .models import *
from .forms import * 

def report(request):
    return render(request, 'report/show-all.html')

def add(request):
    if request.method == 'POST':
        data = {
            'title'      :  request.POST['title'],
            'category'   :  request.POST['category'],
            'sub_category':  request.POST['subCategory'],
            'subject'    :  request.POST['subject'],
        }
        print(data)
        Report.objects.create(data)
        return redirect('../showAll/')
        
        
    return render(request, 'report/add.html')

def loadSubCats(request):
    categoryID = request.GET.get('categoryID')
    #categoryID = Category.objects.filter(name=catID).first()
    #print(categoryID) 
    sub_categories = subCategory.objects.all().filter(category= categoryID)
    #count = subCategory.objects.filter(category_id= category).count()
    return render(request, 'report/load-sub-cats.html', {'sub_categories' : sub_categories})

def showAll(request):
    data = Report.objects.get()
    allReports = []
    print(data)

    return render(request, 'report/show-all.html')

def deleteAll(request):
    report = Report.objects.get()
    if report :
        report.delete()
    else:
        Http404("Page does not exist")
    return render(request, 'report/delete-all.html')

def delete(request):
    ID = request.GET.get('ID')
    report = Report.objects.get(id=ID)
    if report :
        report.delete()
    else:
        Http404("Page does not exist")
    return render(request, 'report/delete.html')

def message(request):
    message = request.GET.get('message')
    if message == 'Thanks':
        msg = 'Thank you for your report. We will contact you from email. You will be return to home page after '
        return render(request, 'report/message.html', {'message' : msg})
    elif message == 'Delete':
        #
        return render(request, 'report/message.html', {'message' : msg})
    elif message=='DeleteAll':
        return render(request, 'report/message.html', {'message' : msg})
    else:
        msg = Http404("Page does not exist")
        return render(request, 'report/message.html', {'message' : msg})
    