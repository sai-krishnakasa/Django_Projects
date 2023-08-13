from datetime import datetime
import email
from fileinput import filename
import http
from re import A
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Bookings, MyUser,History,Buses,driver_details
from django.contrib import  messages,auth
from email_validator import validate_email
from .EmailAuthBackend import EmailAuthBackend
import os
from django.contrib.auth.hashers import check_password,make_password
from django.db.models import Q
from BusTicektApppt.settings import BASE_DIR
from django.core.mail import send_mail
from BusTicektApppt.filters import BookingFilter
from datetime import datetime,timedelta
import pytz


UTC=pytz.utc
time_now=datetime.now(UTC)
def add_driver(request):
        if request.method=='POST':
                name=request.POST['name']
                driver_id=request.POST['driver_id']
                mobile=request.POST['mobile']
                if driver_details.objects.filter(driver_id=driver_id).exists():
                        messages.error(request,'driver_id Already Attached with another User')
                        return redirect('add_driver')
                if driver_details.objects.filter(mobile=mobile).exists():
                        messages.error(request,'driver_id Already Attached with another User')
                        return redirect('add_driver')
                if len(mobile)!=10 or mobile[0] not in ['6','7','8','9']:
                        messages.error(request,'Invalid Mobile Number')
                        return redirect('add_driver')
                driver_details.objects.create(name=name,driver_id=driver_id,mobile=mobile)
                messages.success(request,'Driver Created Successfully')
                return redirect('profile')
        return render(request,'add_driver.html')


def create_history(sender,message):
        obj=History.objects.create(user=sender,item=message)
        obj.save()
# Create your views here.


def buses_delete(request,id):
        bus=Buses.objects.get(pk=id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def driver_delete(request,id):
        driver=driver_details.objects.get(pk=id).delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_bus(request):
        date=datetime.now().strftime("%Y-%m-%dT%H:%M")
        print('date'+date)
        # date=date+'T00:00'
        drivers=driver_details.objects.all()
        if request.method=='POST':
                driver_name=request.POST['driver']
                origin=request.POST['origin']
                destination=request.POST['destination']
                bus_no=request.POST['bus_no']
                bus_type=request.POST['bus_type']
                seat_type=request.POST['seat_type']
                seats_available=request.POST['seats']
                start_date=request.POST['start_time']
                print(start_date)
                if start_date < str(date):
                        messages.error(request,f" Can't Add Bus,Starting time is Beyond Current time ")
                        return render(request,'add_bus.html',{'drivers':drivers,'origin':origin,'destination':destination,'bus_no':bus_no,'bus_type':bus_type,'start_date':start_date})
                end_date=request.POST['end_time']
                if start_date>end_date:
                        messages.error(request,f'Ending time Should Always be greater Than Starting time')
                        return render(request,'add_bus.html',{'drivers':drivers,'origin':origin,'destination':destination,'bus_no':bus_no,'bus_type':bus_type,'start_date':start_date,'end_date':end_date})

                fare=request.POST['fare']
                driver_deta=driver_details.objects.filter(name=driver_name).first()
                driver_buses=driver_deta.buses.all()
                can_add=True
                buss=''
                for bus in driver_buses:
                        if datetime.now(UTC)> bus.start_time and datetime.now(UTC) < bus.end_time:
                                can_add=False
                                buss=bus
                        if(can_add==False):
                                break
                if (can_add==True):
                        bus=Buses.objects.create(driver_details=driver_deta, origin=origin,destination=destination,bus_no=bus_no,bus_type=bus_type,seat_type=seat_type,start_time=start_date,end_time=end_date,not_booked_seats=seats_available,fare=fare)
                        messages.error(request,f'Bus {bus.bus_no} Created Successfully')
                        bus.save()
                else:
                        messages.error(request,f'The Driver is Busy with bus {buss.bus_no.upper()} {buss}  at this time ')
                        return render(request,'add_bus.html',{'drivers':drivers,'origin':origin,'destination':destination,'bus_no':bus_no,'bus_type':bus_type,'start_date':start_date,'end_date':end_date,'fare':fare})
                return redirect('book')
        origins=Buses.objects.values('origin').distinct()
        dests=Buses.objects.values('destination').distinct()
        bus_types=Buses.objects.values('bus_type').distinct()
        origins=[i['origin'] for i in origins ]
        # drivers=[i['name'] for i in drivers ]
        # print(drivers)
        bus_types=[i['bus_type'] for i in bus_types ]
        dests=[i['destination'] for i in dests ]
        return render(request,'add_bus.html',{'origins':origins,'dests':dests,'bus_types':bus_types,'drivers':drivers,'date':date})


def buses_detail(request,id):
        bus=Buses.objects.get(pk=id)
        return render(request,'cnfm_payment.html',{'bus':bus,'hide_submit':'okay'})


def driver_detail(request,id):
        driver=driver_details.objects.get(driver_id=id)
        driver_buses=driver.buses.all()
        return render(request,'driver_details.html',{'driver':driver,'driver_buses':driver_buses})
        

def admin_desk(request):
        if 'email'  not in request.session:
                return redirect('login')
        else:
                email=request.session['email']
                user=MyUser.objects.filter(email=email).first()
                if user.is_admin==False or user.is_admin==0 :
                        messages.error(request,'You are Not Authorized to Access Admin desk ')
                        return redirect('profile')
        buses=Buses.objects.all()
        drivers=driver_details.objects.all()
        return render(request,'admin_desk.html',{'buses':buses,'drivers':drivers})


def register(request):
        if 'email' in request.session:
                messages.error(request,'Already Logged in please Logout to Register')
                return redirect('home')
        if request.method=='POST':
                first_name=request.POST['first_name']
                last_name=request.POST['last_name']
                user_name=request.POST['user_name']
                gender=request.POST['gender']
                email=request.POST['email']
                phone=request.POST['phone']
                password1=request.POST['password1']
                password2=request.POST['password2']
                try:
                        validate_email(email)
                except Exception as ex:
                        messages.error(request,'Error:'+str(ex))
                        return redirect('register')
                if MyUser.objects.filter(email=email).exists():
                        messages.error(request,' Error Email Already Registered')
                        return render(request,'register.html',{'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'password1':password1,'phone':phone})
                if password1!=password2:
                        messages.error(request,' Error Both Passwords Should Be Same')
                        return render(request,'register.html',{'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'password1':password1,'phone':phone})
                if MyUser.objects.filter(phone=phone).exists():
                        messages.error(request,'Error Mobile Number Already Registered')
                        return render(request,'register.html',{'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'password1':password1,'phone':phone})
                if phone[0] not in ['6','7','8','9'] or len(phone)!=10:
                        messages.error(request,'Error Mobile Number Inavalid')
                        return render(request,'register.html',{'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'password1':password1,'phone':phone})
                if password1!=password2:
                        messages.error(request,'Error Both passwords Should be same')
                        return render(request,'register.html',{'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'password1':password1,'phone':phone})
                if len(password1)<6:
                        messages.error(request,'Password Should be a Minimum of 6 characters')
                        return render(request,'register.html',{'first_name':first_name,'last_name':last_name,'user_name':user_name,'email':email,'password1':password1,'phone':phone})
                user=MyUser.objects.create_user(user_name=user_name,first_name=first_name,last_name=last_name,email=email,gender=gender,phone=phone,password=password1)
                message=f" an Account created on {datetime.today().strftime('%b %d %Y %H:%M:%S')} with Username:{user_name}"
                create_history(user,message)
                user.save()
                messages.success(request,f'Account with {email} hase been created Successfully')
                return redirect('login')
        print('register')
        return render(request,'register.html')


def update_wallet(request):
        if request.method=='POST':
                amount=request.POST['amount']
                if(int(amount)<0):
                        messages.error( request,f"Amount should not be Negative use Withdraw instead ")
                        return redirect('profile')
                trans_type=request.POST['type']
                password=request.POST['password']
                user=MyUser.objects.filter(email=request.session['email']).first()
                print(check_password(password,user.password))
                if check_password(password,user.password):
                        if trans_type.lower()=='deposit':
                                bal=user.balance
                                user.balance=int(bal)+int(amount)
                                user.save() 
                                message=f"An Amount of {amount} has been {trans_type}ed into the wallet on {datetime.today().strftime('%b %d %Y %H:%M:%S')} "
                                create_history(user,message)
                                messages.success(request,f'{amount} has been depoisited into the wallet')
                                return redirect('profile')
                        else:
                                bal=user.balance
                                if int(bal)-int(amount)>=0:
                                        user.balance=int(bal)-int(amount)
                                else:
                                        messages.error(request,"Sorry We Can't lend you")
                                        return redirect('profile')
                                message=f"An Amount of {amount} has been {trans_type } ed from the wallet on {datetime.today().strftime('%b %d %Y %H:%M:%S')} "
                                create_history(user,message)
                                user.save()
                                messages.success(request,f'{amount} has been withdrawed from the wallet')
                        return redirect('profile')
                else:
                        messages.error(request,'INVALID PASSWORD')
                        return redirect('profile')
        else:
                return redirect('profile')


def booking_details(request):
        email=request.session['email']
        user=MyUser.objects.filter(email=email).first()
        # bookings=Bookings.objects.all()
        if user.is_admin:
                bookings=Bookings.objects.all().order_by('-booking_Bus_details__start_time')
                book_filter=BookingFilter(request.GET,queryset=bookings)
        else:
                bookings=Bookings.objects.filter(booking_cust_details_id=user.pk).order_by('-booking_Bus_details__start_time')
                book_filter=BookingFilter(request.GET,queryset=bookings)
        return render(request,'all_bookings.html',{'bookings':bookings,'time_now':time_now,'filter':book_filter,'user':user})


def delete_ticket(request,id):
                book=Bookings.objects.get(id=id)
                count=book.no_of_passengers
                fare=book.booking_Bus_details.fare
                init_fare=fare
                user=MyUser.objects.get(id=book.booking_cust_details.id)
                bus=Buses.objects.get(id=book.booking_Bus_details.id)
                print(bus)
                bus.not_booked_seats+=count
                bus.save()
                time_remain=bus.start_time-datetime.now(UTC)
                # seconds=time_remain.seconds
                # print(time_remain)
                # if time_remain.days>0:contact_us

                #         seconds+=time_remain.days*60*60
                # print(seconds)
                # print(time_remain)
                # print(time_remain.seconds)
                # print(time_remain.days)
                # print(time_remain.seconds*(time_remain.days*60*60))
                total_secs=time_remain.seconds
                if time_remain.days>0:
                        total_secs+=time_remain.days*24*60*60
                if total_secs>86400:
                        fare=math.floor(fare*0.7)
                        messages.success(request,f'success 70% of {init_fare*count} Which Is  {fare*count} Has Been Credited Back to Your Wallet')
                elif total_secs>86400/2:
                        fare=math.floor(fare*0.5)
                        messages.success(request,f' 50% of {init_fare*count} Which Is  {fare*count} Has Been Credited Back to Your Wallet')
                else:
                        fare=math.floor(fare*0.4)
                        messages.success(request,f'success 40% of {init_fare*count} Which Is  {fare*count} Has Been Credited Back to Your Wallet')
                # message=f'A Refund of {fare*count} has been Refunded Back'
                # create_history(user,message)
                user.balance+=fare*count
                email=user.email
                user.save()
                message=f'Successfully Cancelled the Ticket of id {book.id},A refund of {fare*count} has been processed  '
                book.delete()
                create_history(user,message)
                email_from=settings.EMAIL_HOST_USER
                receiver=(email,)
                send_mail('Cancelled Ticket ',message,email_from,receiver)
                print('Mail sent')
                return redirect('profile')
                

def history(request):
        email=request.session['email']
        print(request.user)
        print('helo')
        user=MyUser.objects.filter(email=email).first()
        items=History.objects.filter(user=user).values('item')
        items=items[::-1]
        items=items[:30]
        l=[]
        for i in items:
                l.append(i['item'])
        return render(request,'history.html',{'items':l})


def wallet_bal(request):
        user=MyUser.objects.filter(email=request.session['email']).first()
        return HttpResponse(user.balance)


def profile(request):
        if 'email' not  in request.session:
                messages.error(request,' Login to Access the Page')
                return redirect('login')
        email=request.session['email']
        print(email)
        user =MyUser.objects.filter(email=email).first()
        print(user.username)
        return render(request,'user_profile.html',{'customer':user})
        

def edit_profile(request):
        if 'email' in request.session:
                email=request.session['email']
                user =MyUser.objects.filter(email=email).first()
                if request.method=='POST':
                        username=request.POST['username']
                        if username!='':
                                user.username=username
                        Firstname=request.POST['firstname']
                        if Firstname!='':
                                user.firstname=Firstname
                        lastname=request.POST['lastname']
                        if lastname !='':
                                user.lastname=lastname
                        phone=str(request.POST['phone'])
                        user_exist=MyUser.objects.filter(Q(phone=phone)&~Q(email=user.email)).first()
                        if  user_exist:
                                messages.error(request,' Mobile Number Registered with Another Account')
                                return redirect('edit_profile')
                        if len(phone)!=10:
                                messages.error(request,'Invalid Mobile Number')
                                return redirect('edit_profile')
                        if phone!='':
                                user.phone=phone
                        if 'file' in request.FILES :
                                message='Profile_pic'
                                try:
                                        os.remove(f'{BASE_DIR}/{user.profile_pic.url}')
                                        
                                except:
                                        pass
                                # print(request.FILES['file'])
                                # print(request.FILES['file'].filename)
                                if (str(request.FILES['file']).split('.')[-1]).lower() not in ['jpg','png','jfif']:
                                        messages.error(request,'Only jpg,png,jfif Formats are Accepted For Profile Pic')
                                        return redirect('profile')

                                user.profile_pic=request.FILES['file']
                        message=f"Profile updated on {datetime.today().strftime('%b %d %Y %H:%M:%S')}"
                        messages.success(request,f"Profile Successfully Updated")
                        create_history(user,message)
                        user.save()
                        return redirect('profile')
                return render(request,'edit_profile.html',{'user':user})
        messages.error(request,'Please Login to Continue')
        return redirect('login')


import math, random,time
def generateOTP() :
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP


def reset_password(request):
        if request.method=='POST':
                pass1=request.POST['password1'] 
                pass2=request.POST['password2']
                print(request.POST['email'])
                if pass1==pass2:
                        user=MyUser.objects.filter(email=request.POST['email']).first()
                        hashed=make_password(pass1)
                        user.password=hashed
                        user.save()
                        message=f"Reseted Password on  {datetime.today().strftime('%b %d %Y %H:%M:%S')}"
                        create_history(user,message)
                        messages.success(request,'Password Reset Successful')
                        return redirect('login')
                else:
                        messages.error(request,'Both the passwords should be Same')
                        return redirect('reset_password')
        return render(request,'reset_password.html')


def verify_otp(request):
        if request.method=='POST':
                otp_org=request.POST['otp_org']
                otp_gen_time=request.POST['otp_gen_time']
                email=request.POST['email']
                if 'otp' in request.POST :
                        print('OTP: '+otp_org)
                        print(request.POST['otp'])
                        if request.POST['otp']==otp_org and (time.time())-float(otp_gen_time)<300:
                                return render(request,'reset_password.html',{'email':email})
                        else:
                                messages.error(request,'Ivalid OTP / OTP expired, Kindly use within 5 Mins')
                                return redirect('verify_otp')
        else:
                return render(request,'reset_password.html',{'email':email})


def contact_us(request):
        if request.method=='POST':
                name=request.POST['name']
                message=f'Hello {name} , we have rerceived Your Mail'
                message+=request.POST['message']
                rec_email=request.POST['email']
                send_mail('Contacting From Bus Booking APP',message,'saikrishnakasa123@gmail.com',(rec_email,))
                return redirect('home')
        else:
                return render(request,'contact_us.html')


def forgot_password(request):
        if request.method=='POST':
                email=request.POST['email']
                if MyUser.objects.filter(email=email).exists():
                        otp=generateOTP()
                        otp_gen_time=time.time() 
                        message='Your password is '+otp+'\n otp is valid for only 5 mins'
                        email_from=settings.EMAIL_HOST_USER
                        receiver=(email,)
                        send_mail('Forgot Password',message,email_from,receiver)
                        print('Mail sent')
                        return render(request,'otp.html',{'otp':otp,'otp_gen_time':otp_gen_time,'email':email})
                else:
                        messages.error(request,'INVALID EMAIL ADDRESS')
                        return redirect('forgot_password')
        return render(request,'forgot_password.html')

def login(request):
        if 'email' in request.session:
                messages.error(request,'Already Logged in please Logout to Login')
                return redirect('home')
        if request.method=='POST':
                email=request.POST['email']
                password=request.POST['password']
                user=MyUser.objects.filter(email=email).first()
                if not user :
                        messages.error(request,f"Don't  have an Account with this {email}")
                        return redirect('login')
                if EmailAuthBackend.authenticate(email=email,password=password):
                        request.session['email']=email
                        request.session['is_loggedin']=True
                        print(request.session['email'])
                        print(request.session['is_loggedin'])
                        auth.login(request,user)
                        return redirect('home')
                else:
                        messages.error(request,'INVALID_DETAILS')
                        return render(request,'login.html',{'email':email})
        return render(request,'login.html')
def session(request):
        # print(request.session['email'])
        if 'is_loggedin' in request.session:
                is_loggedin=request.session['is_loggedin']
                email=request.session['email']
                email=email+' '+str(is_loggedin)
                return HttpResponse(email)
        else:
                return HttpResponse('No One Logged in')

def logout(request): 
        if 'email' in request.session:
                del request.session['is_loggedin']
                del request.session['email']
        auth.logout(request)
        return redirect('home')



