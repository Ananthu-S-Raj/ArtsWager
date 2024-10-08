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

def first(request):
    # first_prize = betting_table.objects.filter(prize="first")
    # second_prize = betting_table.objects.filter(prize="second")
    # return render(request, 'index.html', {'first': first_prize, 'second': second_prize})
    return index(request)

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
        balance=request.POST.get('phone')
        password=request.POST.get('balance')
        
        UP=user_register(name=name,email=email,phone_number=phone,password=password,balance=balance)
        UP.save()

        subject = f"Welcome to ArtsWager 😀🤝"
        msg = "Dear " + name + ",\n\nYou have successfully created your account on ArtsWager❗ We're thrilled to have you join our community of betting enthusiasts.👏"
        sends_mail(email, msg,subject)
        messages.success(request,"Account created Successfully.You can Login now.")

    # return render(request,'index.html')
    return index(request)



def creator_reg(request):
    return render(request,'creator_registration.html')

def creator_registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Create event creator object
        UP = event_creators(name=name, email=email, phone_number=phone, password=password)
        UP.save()
        
        # Send email
        msg = "Thank you for registering as an event creator!"
        sends_mail(email, msg)

        # Redirect or return response
        return HttpResponse("Registration successful. Email sent.")
    
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
        # return render(request,'index.html')
        return index(request)

    elif event_creators.objects.filter(email=email,password=password).exists():
        creator=event_creators.objects.get(email=email,password=password)
        request.session['creator_id']=creator.id
        return render(request,'index.html')
    
    elif participant_register.objects.filter(email=email,password=password,status="accepted").exists():
        participiant=participant_register.objects.get(email=email,password=password)
        request.session['participiant_id']=participiant.id
        request.session['participiant_gender']=participiant.gender
        return render(request,'index.html')
    # status="accepted"
        
    else:
        messages.error(request,"Invalid login credentials or user does not exist.!")

        return render(request,'login.html')
    
def create_event(request):
        return render(request,'create_events.html')

def confirm_event(request):
    if request.method=="POST":
        item=request.POST.get('item')
        venue=request.POST.get('venue')
        date=request.POST.get('date')
        time=request.POST.get('time')
        gender=request.POST.get('gender')
        UP=events(item=item,venue=venue,date=date,time=time,gender=gender)
        UP.save()
        return render(request,'create_events.html')

def view_events(request):
    data=events.objects.all()
    return render(request,'view_events.html',{'result':data})

def apply(request):
    data=events.objects.all()
    return render(request,'apply_event.html',{'result':data})

def participants(request):
    data=participant_register.objects.all()
    return render(request,'view_participants.html',{'result':data})



def reqaccept(request,id):
    s=participant_register.objects.get(id=id)
    s.status='accepted'
    s.save()
    return redirect(participants)   
    
def reqreject(request,id):
    s=participant_register.objects.get(id=id)
    s.status='rejected'
    s.save()
    return redirect(participants)


def declare_result(request):
    data=participant_register.objects.filter(status="accepted")
    return render(request,'declare_result.html',{'result':data})

def feedback(request):
    return render(request,'feedback.html')
def send_feedback(request):
    if request.method=="POST":
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        UP=feedbacks(subject=subject,message=message,u_id=request.session['uid'],u_name=request.session['u_name'])
        UP.save()
        # return render(request,'index.html')
        messages.success(request,"Feedback send successfully")

        return index(request)
    

def view_feedbacks(request):
    data=feedbacks.objects.all() 
    return render(request,'view_feedback.html',{'result':data})

def parti_profile(request):
    data=participant_register.objects.get(id=request.session['participiant_id'])
    return render(request,'participiant_profile.html',{'result':data})

def view_participants(request):
    data=participant_register.objects.all()
    return render(request,'view_participants.html',{'result':data})
def user_profile(request):
    data=user_register.objects.get(id=request.session['uid'])
    return render(request,'user_profile.html',{'result':data})

def new_participant(request):
    return render(request,'participant_reg.html')

def participant_registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        category=request.POST.get('category')
        status=request.POST.get('status')
        password=request.POST.get('password')
        UP=participant_register(name=name,email=email,phone_number=phone,age=age,gender=gender,category=category,password=password,status="pending")
        UP.save()
        # return render(request,'index.html')
        return index(request)
    
def my_events(request):
    data = events.objects.filter(gender=request.session['participiant_gender'])
    status_data = registered_events.objects.filter(p_id=request.session['participiant_id'], status="submitted")
    registered_items = status_data.values_list('item', flat=True)
    filtered_data = [item for item in data if item.item not in registered_items]
    return render(request, 'filtered_events.html', {'result': filtered_data, 'reg_info': status_data})

def participation_request(request):
    if request.method=="POST":
        chest_number=request.POST.get('chest_number')
        name=request.POST.get('name')
        item=request.POST.get('item')
        venue=request.POST.get('venue')
        time=request.POST.get('time')
        UP=registered_events(chest_number=chest_number,name=name,item=item,venue=venue,time=time,result="Not Declared",p_id=request.session['participiant_id'],status="submitted")
        UP.save()
        return redirect(my_events)


def sends_mail(mail, msg,subject):
    crl = pycurl.Curl()
    crl.setopt(crl.URL, 'https://alc-training.in/gateway.php')
    data = {'email': mail, 'msg': msg,'subject':subject}
    pf = urlencode(data)

    # Sets request method to POST,
    # Content-Type header to application/x-www-form-urlencoded
    # and data to send in request body.
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
    # return render(request,'index.html')
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
    # Your logic here
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

    # return render(request,'index.html')
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

    # return render(request,'index.html')
    return redirect(user_profile)