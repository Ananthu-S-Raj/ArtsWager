from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import user_register, event_creators, participant_register
from urllib.parse import urlencode
import pycurl
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
import re

def index(request):
    first_prize = betting_table.objects.filter(prize="first")
    second_prize = betting_table.objects.filter(prize="second")
    return render(request, 'index.html', {'first': first_prize, 'second': second_prize})


def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def reg(request):
    return render(request,'register.html')

def addlogin(request):
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        
        UP=user_register(name=name,email=email,phone_number=phone,password=password)
        UP.save()

        subject = f"Welcome to ArtsWager 😀🤝"
        msg = "Dear " + name + ",\n\nYou have successfully created your account on ArtsWager❗ We're thrilled to have you join our community of betting enthusiasts.👏"
        sends_mail(email, msg,subject)
        messages.success(request,"Account created Successfully.You can Login now.")

    return index(request)



    return render(request, 'index.html')

def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=="admin@gmail.com" and password=="admin":
        request.session['admin_details']=email
        request.session['admin_details']=password
        return render(request,'index.html')
    
    elif user_register.objects.filter(email=email,password=password).exists():
        user=user_register.objects.get(email=email,password=password)
        request.session['uid']=user.id
        request.session['u_email']=user.email
        request.session['u_name']=user.name
        request.session['balance']=user.balance
        return index(request)
    
        
    else:
        messages.error(request,"Invalid login credentials or user does not exist.!")

        return render(request,'login.html')


def feedback(request):
    return render(request,'feedback.html')
def send_feedback(request):
    if request.method=="POST":
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        UP=feedbacks(subject=subject,message=message,u_id=request.session['uid'],u_name=request.session['u_name'])
        UP.save()
        messages.success(request,"Feedback send successfully")

        return index(request)
    

def view_feedbacks(request):
    data=feedbacks.objects.all() 
    return render(request,'view_feedback.html',{'result':data})


def user_profile(request):
    data=user_register.objects.get(id=request.session['uid'])
    return render(request,'user_profile.html',{'result':data})



def sends_mail(mail, msg,subject):
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
    data = {'email': mail, 'msg': msg,'subject':subject}
    pf = urlencode(data)

    crl.setopt(crl.POSTFIELDS, pf)
    crl.perform()
    crl.close()

def bet_now(request):
    return render(request,'betnow.html')

def confirm_bet(request):
    if request.method=="POST":
        user_id=request.session.get('uid')
        u_name=request.session.get('u_name')
        u_email=request.session.get('u_email')
        item=request.POST.get('item')
        district=request.POST.get('district')
        position=request.POST.get('position')
        payment=request.POST.get('payment')
        main_balance=request.POST.get('main_balance')

        money=float(main_balance)-float(payment)
        user=user_register.objects.get(id=user_id)
        user.balance=money
        up=betting_table(user_id=user_id,u_name=u_name,u_email=u_email,item=item,district=district,position=position,prize="Not declared")
        up.save()
        user.save()
    return index(request)

def history(request):
    data = betting_table.objects.filter(user_id=request.session.get('uid'))
    return render(request, 'history.html', {'data': data})

def declare_winners(request):
    data = betting_table.objects.filter(prize="Not declared")
    return render(request, 'declare_winners.html', {'data': data})

def confirm_winner(request):
    if request.method=='POST':
        user_id=request.POST.get('user_id')
        u_name=request.POST.get('u_name')
        u_email=request.POST.get('u_email')
        prize=request.POST.get('prize')
        up=betting_table.objects.get(user_id=user_id)
        up.prize=prize
        up.save()
        subject = f"Congratulations! You've won the {prize} Prize at Arts Wager 🏆"
        msg = (
    f"Dear {u_name},\n\n"
    f"We are excited to announce that you have won the {prize} Prize"
    "in our recent contest at Arts Wager. Your dedication and creativity have shone through!\n\n"
    "We greatly appreciate your participation and the unique perspective you bring to our community. "
    "Your work has stood out among the submissions, and we are pleased to honor your achievement.\n\n"
    "Keep an eye on your inbox for further details on how to claim your prize worth.\n\n"
    "Once again, congratulations on this fantastic achievement!🏆💰💸\n\n"
    "Warm regards,\n"
    "The Arts Wager Team"
)

        sends_mail(u_email, msg,subject)       
    return declare_winners(request)

def bet_list(request):
    data = betting_table.objects.exclude(prize="Not declared")
    return render(request, 'bet_list.html', {'data': data})

def users_list(request):
    data = user_register.objects.all()
    return render(request, 'users_list.html', {'result': data})

def del_user(request):
    if request.method=="POST":
        uid=request.POST.get('user_id')
        user=user_register.objects.get(id=uid)
        user.delete()
        messages.info(request,"User Revoked!")
    return redirect(users_list)


def t_a_result(request):
    return render(request,'t&a_result.html')



def pass_change(request):
    return render(request,'password_change.html')

def acc_update(request):
    return render(request, 'update_account.html')

def update_account(request):
    if request.method=="POST":
        uid=request.POST.get('uid')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        
        user=user_register.objects.get(id=uid)
        user.name=name
        user.email=email
        user.phone=phone
        user.save()

        subject = f"Account Updated🤝"
        msg = "Dear " + name + ",\n\nYou have successfully updated your ArtsWager account❗."
        sends_mail(email, msg,subject)
        messages.success(request,"Account Updated Successfully.")

    return redirect(user_profile)

def change_password(request):
    if request.method=="POST":
        uid=request.POST.get('uid')
        password=request.POST.get('password')
        
        user=user_register.objects.get(id=uid)
        user.password=password
        user.save()
        name = user.name
        email = user.email

        subject = f"Password Updated🤝"
        msg = "Dear " + name + ",\n\nYou have successfully updated your ArtsWager account password❗."
        sends_mail(email, msg,subject)
        messages.success(request,"Password Updated Successfully.")

    return redirect(user_profile)