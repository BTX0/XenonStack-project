from django.shortcuts import render
from pandas import value_counts
import mysql.connector as sql
f_name=''
l_name=''
mob=''
email=''
pasd=''

# Create your views here.
def signupaction(request):
    global f_name, l_name,mob,email,pasd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database="xenon")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                f_name=value
            if key=="last_name":
                l_name=value
            if key=="mobile":
                mob=value
            if key=="email":
                email=value
            if key=="password":
                pasd=value
        c="insert into users values ('{}','{}','{}','{}','{}')".format(f_name,l_name,mob,email,pasd)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')
