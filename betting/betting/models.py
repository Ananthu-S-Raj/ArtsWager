from django.db import models



class user_register(models.Model):
    name=models.CharField(max_length=150)
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    balance=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=120)
    password=models.CharField(max_length=120)

class events(models.Model):
    item=models.CharField(max_length=150)
    venue=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    time=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    
class event_creators(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class result(models.Model):
    name=models.CharField(max_length=120)
    item=models.CharField(max_length=120)
    result=models.CharField(max_length=120)

class feedbacks(models.Model):
    u_id=models.CharField(max_length=255)
    u_name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)

class participant_register(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=120)
    gender=models.CharField(max_length=120)
    age=models.CharField(max_length=150)
    category=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    chest_number = models.CharField(max_length=3, unique=True)

class registered_events(models.Model):
    chest_number=models.CharField(max_length=150)
    p_id=models.CharField(max_length=150)
    name=models.CharField(max_length=120)
    item=models.CharField(max_length=120)
    venue=models.CharField(max_length=120)
    time=models.CharField(max_length=120)
    result=models.CharField(max_length=120)
    status=models.CharField(max_length=120)

class betting_table(models.Model):
    user_id=models.CharField(max_length=150)
    u_name=models.CharField(max_length=150)
    u_email=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    position=models.CharField(max_length=150)
    prize=models.CharField(max_length=150)
    