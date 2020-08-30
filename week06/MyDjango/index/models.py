# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
# 鍥句功or鐢靛奖
class Type(models.Model):
    # id = models.AutoField(primary_key=True)  # Django浼氳嚜鍔ㄥ垱寤�骞惰�缃�负涓婚敭
    typename = models.CharField(max_length=20)

# 浣滃搧鍚嶇О鍜屼綔鑰�涓绘紨)
class Name(models.Model):
    # id 鑷�姩鍒涘缓
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)