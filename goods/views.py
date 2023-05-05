import math
from django.shortcuts import render, redirect
from goods.models import Good, GoodType, Order
from user.models import User
from django.http.response import JsonResponse
import datetime
import time
import random


# Create your views here.
def index(request):
    if request.method == 'GET':
        if request.session.get('username'):
            userinfo = {
                "islogin": 1,
                "username": request.session['username']
            }
        else:
            userinfo = {
                "islogin": 0
            }
        search_val = request.GET.get('search_val', '')
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
        limit = 20
        type_record = GoodType.objects.filter().first()
        if search_val:
            goods = Good.objects.filter(good_type=type_record, title__contains=search_val)
            total = goods.count()
            goods = goods.all()[(page - 1) * limit:page * limit]
        else:
            goods = Good.objects.filter(good_type=type_record)
            total = goods.count()
            goods = goods.all()[(page - 1) * limit:page * limit]
        total_pages = math.ceil(total / limit)

        return render(request, 'index.html', {"userinfo": userinfo,
                                              "goods": goods,
                                              "search_val": search_val,
                                              "total_pages": total_pages,
                                              "page": page})
    return render(request, 'index.html')


def purchase(request):
    if request.method == 'GET':
        if not request.session.get('username'):
            return JsonResponse({"status": 10001, "msg": 'please log in first'})
        good_id = request.GET.get('id')
        good_count = int(request.GET.get('good_count', 1))
        good = Good.objects.filter(id=good_id).first()
        if good.inventory < good_count:
            return JsonResponse({"status": 10001, "msg": 'Insufficient inventory'})
        order_id = str(datetime.datetime.fromtimestamp(time.time())).replace("-", "").replace(" ", "").replace(":",
                                                                                                               "").replace(
            ".", "") + str(random.randint(100, 999))
        order = Order()
        order.order_num=order_id
        order.image=good.image
        user = User.objects.filter(user_name=request.session.get('username')).first()
        order.user = user
        order.title = good.title
        order.status = 'ordered'
        order.total_price = good.price * good_count
        order.number = good_count
        order.save()
        return JsonResponse({"status": 10000, "msg": 'Purchase successful'})


def cancellation(request):
    if request.method == 'GET':
        order_id=request.GET.get('id')
        order=Order.objects.filter(id=order_id).first()
        order.status='canceled'
        order.save()
        if request.session.get('username'):
            userinfo = {
                "islogin": 1,
                "username": request.session['username']
            }
        else:
            userinfo = {
                "islogin": 0
            }

        user = User.objects.filter(user_name=request.session.get('username')).first()

        orders = Order.objects.filter(user=user).all()

        return render(request, 'order.html', {"userinfo": userinfo,
                                              "orders": orders})


def order(request):
    if request.method == 'GET':
        if request.session.get('username'):
            userinfo = {
                "islogin": 1,
                "username": request.session['username']
            }
        else:
            userinfo = {
                "islogin": 0
            }
        user = User.objects.filter(user_name=request.session.get('username')).first()

        orders = Order.objects.filter(user=user).all()

        return render(request, 'order.html', {"userinfo": userinfo,
                                              "orders": orders})
