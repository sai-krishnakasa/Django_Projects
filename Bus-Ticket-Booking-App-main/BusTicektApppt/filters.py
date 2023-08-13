from cProfile import label
from attr import fields
from django import forms
import django_filters
from accounts.models import Buses,Bookings
from django.utils.translation import gettext_lazy as _
from django import forms
class BusesFilter(django_filters.FilterSet):
    start_time = django_filters.DateFilter(
        field_name="start_time",lookup_expr='gte',
        widget=forms.DateInput(attrs={'type':'date'})
    )
    class Meta:
        model=Buses
        fields=[
            'origin',
            'destination',
            'seat_type',
            'bus_type',
        ]

# class BookingFilter(django_filters.FilterSet):
#     pass
#     date_filter=django_filters.DateFilter(
#         lookup_expr='exact',
#         widget=forms.DateInput(attrs={'type':'date'})
#     )
#     class Meta:
#         model=Bookings
#         fields=[
#             'no_of_passengers',
#             'date_filter'
#         ]
    

class BookingFilter(django_filters.FilterSet):
    # Booking.booking_Bus_details.start_time
    start_date = django_filters.DateFilter(field_name="booking_Bus_details__start_time",lookup_expr='contains',widget=forms.DateInput(attrs={'id':'datepicker','type':'date'}))
    mobile_no = django_filters.CharFilter(label='Mobile', field_name="booking_cust_details__phone",lookup_expr='exact')
    origin = django_filters.CharFilter(label='Origin', field_name="booking_Bus_details__origin",lookup_expr='icontains')
    class Meta:
        model=Bookings
        fields={
           'id':['exact']
        }