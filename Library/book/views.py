from django.shortcuts import render
from book.models import Book
from book.models import Student
from book.forms import bookform
from book.forms import studentform
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def addbook(request):
    if(request.method=='POST'):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbookdetails(request)
    return render(request,'addbook.html')
def addstudents(request):
    if(request.method=='POST'):
        n=request.POST['n']
        a=request.POST['a']
        p=request.POST['p']
        b=Student.objects.create(name=n,age=a,place=p)
        b.save()
        return viewstudents(request)
    return render(request,'addstudents.html')
def viewbookdetails(request):
    k=Book.objects.all()
    return render(request,'viewbookdetails.html',{'b':k})
def viewstudents(request):
    k=Student.objects.all()
    return render(request,'viewstudents.html',{'b':k})
def addbook1(request):
    f=bookform()       #empty form object creation
    if(request.method=='POST'):
        f=bookform(request.POST)
        if f.is_valid():
            f.save()
            return viewbookdetails(request)
    return render(request,'addbook1.html',{'f':f})
def addstudents1(request):
    f=studentform()       #empty form object creation
    if(request.method=='POST'):
        f=studentform(request.POST)
        if f.is_valid():
            f.save()
            return viewstudents(request)
    return render(request,'addstudents1.html',{'f':f})
def fact(request):
    if(request.method=='POST'):
        n=int(request.POST['n'])
        f=1
        for i in range(1,n+1):
            f=f*i
        return render(request,'fact.html',{'fact':f})
    return render(request,'fact.html')
def view(request,p):
    b=Book.objects.get(id=p)
    return render(request,'view.html',{'b':b})
def delete(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return viewbookdetails(request)
def edit(request,p):
    b=Book.objects.get(id=p)
    f=bookform(instance=b)
    if (request.method == 'POST'):
        f = bookform(request.POST,request.FILES,instance=b)
        if f.is_valid():
            f.save()
            return viewbookdetails(request)
    return render(request, 'addbook1.html', {'f': f})
