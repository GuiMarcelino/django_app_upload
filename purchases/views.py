
from types import MethodDescriptorType
from typing import List
from django.http.request import HttpRequest
from purchases.models import Item, Merchant, Purchase, Purchaser
from django.shortcuts import render
from decimal import Decimal

def split_row(row):
    return row.decode("utf8").replace('\n', '').split('\t')

def save_row_to_db(row):
    row = split_row(row)
    purchaser, _ = Purchaser.objects.get_or_create(name=row[0])
    item , _ = Item.objects.get_or_create(description=row[1], price=row[2])
    merchant,_ = Merchant.objects.get_or_create(address=row[4],name=row[5])
    purchase = Purchase.objects.create(
        count=row[3],
        purchaser=purchaser,
        merchant=merchant,
        item=item,
    )
    return purchase


def parse_tab_file(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'purchases\dashboard.html', context={})

    if request.method == "POST":
        
        tab_file = request.FILES.get('tabfile')
        rows = tab_file.readlines()
        purchases_list = [save_row_to_db(row) for row in rows[1:]]

        soma = 0
        for purchase in purchases_list:
            value: Decimal = Decimal(purchase.count) * Decimal(purchase.item.price)
            soma += value

        return render(request, 'purchases\dashboard.html', context={'bruto_total': soma})



