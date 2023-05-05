#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import os

from faker import Faker

fake = Faker()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "good.settings")

import django

django.setup()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from goods.models import GoodType, Good
import csv
import requests

with open('data.csv', newline="") as w:
    reader = csv.reader(w)
    no = 0
    for row in list(reader)[1:]:
        no += 1
        title = row[0].strip().replace('\u202c', '').replace('\n', '').replace('\r', '').replace('\t', '')
        price = row[1]
        img = row[2]
        good_type = row[3]
        file_name = "good_image/{}.jpg".format(str(no))
        with open('upload/' + file_name, 'wb') as w:
            w.write(requests.get(img).content)
        good_type_record = GoodType.objects.filter(name=good_type).first()
        if not good_type_record:
            good_type_record = GoodType()
            good_type_record.name = good_type
            good_type_record.save()
        record = Good()
        record.title = title
        record.price = float(price)
        record.good_type = good_type_record
        record.inventory = fake.random_int(min=0, max=999)
        record.image = file_name
        record.save()
