from django.http import HttpResponse
from django.shortcuts import redirect, render
from requests import request
from accounts.models import Buses,MyUser,Bookings, driver_details
from BusTicektApppt.filters import BusesFilter
from django.contrib import  messages
from django.core.mail import send_mail
from django.conf import settings
from accounts.views import create_history
from datetime import datetime,timedelta
# from django.views.decorators.cache import cache_page
import pytz
UTC=pytz.utc
time_now=datetime.now(UTC)


def home(request):
    if 'email'  not in request.session:
            return redirect('login')
    buses=Buses.objects.all()
    buses_filter=BusesFilter(request.GET,queryset=buses)
    user=MyUser.objects.filter(email=request.session['email']).first()
    return render(request,'index.html',{'buses':buses,'filter':buses_filter,'user':user})

def book(request):
    if 'email'  not in request.session:
            return redirect('login')
    user=MyUser.objects.filter(email=request.session['email']).first()
    # if user.is_admin:
    #     # messages.error(request,'error Admin not Allowed to Book Tickets')
    #     return redirect('profile')
    if request.method=='GET':
        buses=Buses.objects.all().order_by('start_time')
        buses_filter=BusesFilter(request.GET,queryset=buses)
        return render(request,'booking.html',{'buses':buses,'filter':buses_filter,'time_now':time_now,'user':user})
def booking(request,id):
    if 'email'  not in request.session:
            return redirect('login')
    user=request.session['email']
    bus=Buses.objects.get(pk=id)
    
    if request.method=='POST':
        if bus.start_time<datetime.now(UTC):
            messages.error(request,"You Are Not Allowed to Book this bus at this time")
            return redirect('book')
        count=int(request.POST['count'])
        fare= int(request.POST['fare'])
        amount=int(count*fare)
        email=request.session['email']
        user=MyUser.objects.filter(email= request.session['email']).first()
        if int(user.balance)-amount<0:
            messages.error(request,'error Insufficient Balance , Add wallet Balance  to continue Booking')
            return redirect('profile')
        if bus.not_booked_seats-int(count)<0:
            messages.error(request,'Seats Not Avaliable')
            return redirect('book')
        else:
            bus.not_booked_seats=bus.not_booked_seats-count
            user.balance=user.balance-int(amount)
            # driver=Buses.objects.filter(driver_details=user.dri)
            Bookings.objects.create(booking_cust_details=user,booking_Bus_details=bus,no_of_passengers=count)
            booking=Bookings.objects.filter(booking_cust_details=user,booking_Bus_details=bus,no_of_passengers=count).first()
            print(booking.id)
            booking_id=booking.id
            user.save()
            bus.save()
            message=f"A bus From {bus.origin}-{bus.destination} have been booked on {datetime.today().strftime('%b %d %Y %H:%M:%S')} "
            create_history(user,message)
            messages.success(request,'Booked Successfully')
            message=f'''
            Driver Name: {bus.driver_details.name }\n Driver phone Number: {bus.driver_details.mobile} \n Booking id :{booking_id} The Bus Having Bus NO:{bus.bus_no} is reserved for You   on {bus.start_time.date()},A Total of  {count} seat(s) is/are Booked 
            Keep the email confidential ,use the email while Boarding...Happy Journey..\n
            Standard Cancellation Charges apply ,incase of ticket cancellation
            Refund Policy \n
                Note:\n
                    Cancelling Before 24hrs of time of Departure 70% of amount will be refunded \n
                    Cancelling Before 12hrs of Starting 50% will be refunded back \n
                        '''
            email_from=settings.EMAIL_HOST_USER
            receiver=(email,)
            send_mail('BOOKING Successful',message,email_from,receiver)
            messages.success(request,'Booking Successful')
            return redirect('book')
    return render(request,'cnfm_payment.html',{'bus':bus})

def user_details(request):
    if 'email' in request.session:
        email=request.session['email']
        cust=MyUser.objects.first()
        return render(request,'user_details.html',{'customer':cust})
    return HttpResponse('Email not in sesion')
