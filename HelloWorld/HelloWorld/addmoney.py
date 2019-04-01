# -*- coding: utf-8 -*-
from django.shortcuts import render
from common.AddMoney import AddMoney
from common.config import Money

def add_money(request):
    ctx = {}
    if request.POST:
        uid = request.POST['uid']
        platform_id = request.POST['platform_id']
        cookie = Money.cookie.value
        num = request.POST['num']
        ctx['rlt'] = AddMoney(cookie, uid, platform_id).add_more_money(num)
    return render(request, "addmoney.html", ctx)


