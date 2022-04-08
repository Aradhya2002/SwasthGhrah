import keyword
from multiprocessing import Value
from multiprocessing.managers import ValueProxy
from typing import ValuesView
from winreg import KEY_QUERY_VALUE
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector as mysql
fn = ''
ln = ''
g = ''
em = ''
pswd = ''

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    global em,pswd
    if request.method=="POST":
        m= mysql.connect(host="localhost", user="root", password="Aradhya@123", database='hms')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pswd=value
        
        c="select * from register where email= '{}' and password = '{}'".format(em,pswd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html')
        else:
            return render(request, 'welcome.html')
    return render(request, 'login.html')

def userpage(request):
    return render(request, 'userpage.html')

def register(request):
    global fn,ln,g,em,pswd
    if request.method=="POST":
        m= mysql.connect(host="localhost", user="root", password="Aradhya@123", database='hms')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                fn=value
            if key=="lastname":
                ln=value
            if key=="gender":
                g=value
            if key=="email":
                em=value
            if key=="password":
                pswd=value
        
        c="insert into register values( '{}', '{}', '{}', '{}', '{}' )".format(fn,ln,g,em,pswd)
        cursor.execute(c)
        m.commit()
    
    return render(request, 'register.html')
    