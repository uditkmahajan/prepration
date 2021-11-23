from os import system
from django import http
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from student.models import Jee

# for home page
def home(request) :
    return render(request,"student/home.html")

# paper download karne k liye exam choose karne k liye
def download_paper(request) :
    return render(request,"student/download/download_paper.html")

#  exam ka year choose karne k liye
def year(request,slug) :
    a=[2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010]
    return render(request,"student/download/year.html",{"year":a})

# paper download karne k liye
def paper(request,slug1,slug2) :
    return render(request,"student/download/paper.html",{"slug2":slug2})

# test choose karne k liye
def test(request) :
    return render(request,"student/test/test.html")

# test k ander k topic if-else choose karne ke liye
def sub_test(request,slug) :
    return render(request,"student/test/sub_test.html",{"test":slug,"sub_test":["if-else","for loop"]})

# exam choose karna syllabus k liye
def syllabus(request) :
    return render(request,"student/syllabus/syllabus.html")

# syllabus show karne k liye
def sub_syllabus(request,slug) :
    if slug=="jee" :
        return render(request,"student/syllabus/jee.html")
    elif slug=="neet" :
        return render(request,"student/syllabus/neet.html")
    elif slug=="gate" :
        return render(request,"student/syllabus/gate.html")
