"""betting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('first',views.first),
    path('reg/',views.reg),
    path('reg/register',views.register),
    path('login',views.login),
    path('addlogin',views.addlogin),
    path('logout/',views.logout),
    path('creator_registration',views.creator_registration),
    path('creator_reg',views.creator_reg),
    path('create_event',views.create_event),
    path('confirm_event',views.confirm_event),
    path('view_events',views.view_events),
    path('apply',views.apply),
    path('participants',views.participants),
    path('reqaccept/<int:id>',views.reqaccept),
    path('reqreject/<int:id>',views.reqreject),
    path('feedback',views.feedback),
    path('send_feedback',views.send_feedback),
    path('view_feedbacks',views.view_feedbacks),
    path('parti_profile',views.parti_profile),
    path('view_participants',views.view_participants),
    path('user_profile',views.user_profile),
    path('new_participant',views.new_participant),
    path('participant_registration',views.participant_registration),
    path('my_events',views.my_events),
    path('participation_request',views.participation_request),
    path('bet_now',views.bet_now),
    path('confirm_bet',views.confirm_bet),
    path('history',views.history),
    path('declare_winners',views.declare_winners),
    path('confirm_winner',views.confirm_winner),
    path('bet_list',views.bet_list),
    path('users_list',views.users_list),
    path('del_user',views.del_user),
    path('update_account',views.update_account),

    path('acc_update',views.acc_update),
    path('pass_change',views.pass_change),
    path('change_password',views.change_password),
    path('t_a_result',views.t_a_result),

        #path('declare_result',views.declare_result),
        #path('first/<int:id>',views.first),
        # path('second/<int:id>',views.second),
        #path('third/<int:id>',views.third),
        #path('failed/<int:id>',views.failed),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

