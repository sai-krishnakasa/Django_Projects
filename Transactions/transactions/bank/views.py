from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import User
from django.db.transaction import atomic
from django.utils.decorators import method_decorator


class Transaction(View):
    def get(self, request):
        return render(request, "ui.html")

    @atomic
    def post(self, request):
        print(request.POST)
        payee = request.POST["payee"]
        payor = request.POST["payor"]
        amount = int(request.POST["amount"])

        payee = User.objects.get(name=payee)
        if payee.balance < amount:
            raise Exception("Insufficient Bal..")
        payee.balance -= amount
        payee.save()

        payor = User.objects.get(name=payor)
        payor.balance += amount
        payor.save()

        return HttpResponse("Trnsaction Successful")
