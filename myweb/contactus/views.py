from django.shortcuts import render
from pandas import value_counts
import mysql.connector as sql
name=''
email=''
subject=''
message=''


# Create your views here.
def contactusaction(request):
    global name,email,subject,message
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database="xenon")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                name=value
            if key=="email":
                email=value
            if key=="subject":
                subject=value
            if key=="message":
                message=value
            
        c="insert into contactus values ('{}','{}','{}','{}')".format(name,email,subject,message)
        cursor.execute(c)
        m.commit()
    return render(request,'contactus.html')
