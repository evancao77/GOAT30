# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

# 实例基本信息表：
class Tb_Instances(models.Model):
    instance_name = models.CharField(max_length=32, verbose_name='实例名称')
    instance_role = models.IntegerField(verbose_name='角色 1-master 2-relica')
    host_name = models.CharField(max_length=100, verbose_name='主机名称')
    host_ip = models.CharField(max_length=16, verbose_name='IP')
    port = models.IntegerField(verbose_name='端口号')
    db_type = models.IntegerField(verbose_name='数据库类型 1-mysql,2-oracle,3-mongodb,4-redis,5-tibd,6-pg')
    user_name = models.CharField(max_length=64, verbose_name='管理用户名')
    user_pwd = models.CharField(max_length=64, verbose_name='管理用户密码')
    memo = models.CharField(max_length=256, verbose_name='备注，说明业务用途')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now = True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '实例基本信息表'
        verbose_name_plural = verbose_name
        db_table = "tb_instances"



