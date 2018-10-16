from django.db import models

# Create your models here.
class Zhuce(models.Model):

    idname=models.IntegerField(primary_key=True)

    sex=models.CharField(max_length=255,null=True,blank=True)
    birthday=models.CharField(max_length=255,null=True,blank=True)
    area=models.CharField(max_length=255,null=True,blank=True)
    hunyin=models.CharField(max_length=255,null=True,blank=True)
    tall=models.CharField(max_length=255,null=True,blank=True)
    xueli=models.CharField(max_length=255,null=True,blank=True)
    salary=models.CharField(max_length=255,null=True,blank=True)
    password=models.IntegerField()
    nam=models.CharField(max_length=255,null=True,blank=True)
    jieshao=models.CharField(max_length=255,null=True,blank=True)

class Bodyshape(models.Model):
    idname = models.IntegerField(primary_key=True)
    weight=models.CharField(max_length=255,null=True,blank=True)
    bodyshape=models.CharField(max_length=255,null=True,blank=True)
    face=models.CharField(max_length=255,null=True,blank=True)
    eyes=models.CharField(max_length=255,null=True,blank=True)
    hair=models.CharField(max_length=255,null=True,blank=True)
    skin=models.CharField(max_length=255,null=True,blank=True)
    color=models.CharField(max_length=255,null=True,blank=True)
    muscle=models.CharField(max_length=255,null=True,blank=True)
    health=models.CharField(max_length=255,null=True,blank=True)
    dress=models.CharField(max_length=255,null=True,blank=True)

class Econ(models.Model):
    idname = models.IntegerField(primary_key=True)
    licai = models.CharField(max_length=255,null=True,blank=True)
    wazhai=models.CharField(max_length=255,null=True,blank=True)
    jingjiguang=models.CharField(max_length=255,null=True,blank=True)

class Lifestyle(models.Model):
    idname = models.IntegerField(primary_key=True)
    smoke=models.CharField(max_length=255,null=True,blank=True)
    drink=models.CharField(max_length=255,null=True,blank=True)
    exercise=models.CharField(max_length=255,null=True,blank=True)
    eat=models.CharField(max_length=255,null=True,blank=True)
    shopping=models.CharField(max_length=255,null=True,blank=True)
    religious=models.CharField(max_length=255,null=True,blank=True)
    testtime=models.CharField(max_length=255,null=True,blank=True)
    network=models.CharField(max_length=255,null=True,blank=True)
    maxspend = models.CharField(max_length=255,null=True,blank=True)
    jiawu=models.CharField(max_length=255,null=True,blank=True)

    housework=models.CharField(max_length=255,null=True,blank=True)
    pet=models.CharField(max_length=255,null=True,blank=True)
    aboutpet=models.CharField(max_length=255,null=True,blank=True)

class Workandstudy(models.Model):
    idname = models.IntegerField(primary_key=True)
    danwei=models.CharField(max_length=255,null=True,blank=True)
    hangye=models.CharField(max_length=255,null=True,blank=True)
    jobtype=models.CharField(max_length=255,null=True,blank=True)
    daiyu=models.CharField(max_length=255,null=True,blank=True)
    workingstate=models.CharField(max_length=255,null=True,blank=True)
    diaodong=models.CharField(max_length=255,null=True,blank=True)
    haiwai=models.CharField(max_length=255,null=True,blank=True)
    careerfamily=models.CharField(max_length=255,null=True,blank=True)
    gratitudefrom=models.CharField(max_length=255,null=True,blank=True)
    major=models.CharField(max_length=255,null=True,blank=True)
    language=models.CharField(max_length=255,null=True,blank=True)
class Xingfu(models.Model):
    idname = models.IntegerField(primary_key=True)
    nam=models.CharField(max_length=255,null=True,blank=True)
    picture=models.CharField(max_length=255,null=True,blank=True)
    time=models.CharField(max_length=255,null=True,blank=True)
    area=models.CharField(max_length=255,null=True,blank=True)
    condition=models.CharField(max_length=255,null=True,blank=True)
    age=models.CharField(max_length=255,null=True,blank=True)
    liuyan = models.CharField(max_length=255, null=True, blank=True)

class Basics(models.Model):
    idname = models.IntegerField(primary_key=True)
    chird=models.CharField(max_length=255,null=True,blank=True)
    area=models.CharField(max_length=255,null=True,blank=True)
    xuexing=models.CharField(max_length=255,null=True,blank=True)
    ethnic=models.CharField(max_length=255,null=True,blank=True)
    salary=models.CharField(max_length=255,null=True,blank=True)
    house=models.CharField(max_length=255,null=True,blank=True)
    car=models.CharField(max_length=255,null=True,blank=True)
    password=models.CharField(max_length=255,null=True,blank=True)
    lifename = models.CharField(max_length=255,null=True,blank=True)
    shenfen = models.CharField(max_length=255,null=True,blank=True)
    qq = models.CharField(max_length=255,null=True,blank=True)
    adrr = models.CharField(max_length=255,null=True,blank=True)
    youbian = models.CharField(max_length=255,null=True,blank=True)

class Dubai(models.Model):
    idname = models.IntegerField(primary_key=True)
    dubai=models.CharField(max_length=255,null=True,blank=True)

class Zhaopian(models.Model):
    idname = models.IntegerField(primary_key=True)
    pic=models.CharField(max_length=255,null=True,blank=True)
class Hunyin(models.Model):
    idname = models.IntegerField(primary_key=True)
    jiguan = models.CharField(max_length=255,null=True,blank=True)
    guoji=models.CharField(max_length=255,null=True,blank=True)
    gexing=models.CharField(max_length=255,null=True,blank=True)
    youmo=models.CharField(max_length=255,null=True,blank=True)
    piqi=models.CharField(max_length=255,null=True,blank=True)
    taidu=models.CharField(max_length=255,null=True,blank=True)
    chird=models.CharField(max_length=255,null=True,blank=True)
    jiehun=models.CharField(max_length=255,null=True,blank=True)
    yidilian=models.CharField(max_length=255,null=True,blank=True)
    nicehunyin=models.CharField(max_length=255,null=True,blank=True)
    tongzhu=models.CharField(max_length=255,null=True,blank=True)
    paihang=models.CharField(max_length=255,null=True,blank=True)
    jiemei=models.CharField(max_length=255,null=True,blank=True)
    fumu=models.CharField(max_length=255,null=True,blank=True)
    fuwork=models.CharField(max_length=255,null=True,blank=True)
    muwork=models.CharField(max_length=255,null=True,blank=True)
    fumuqian=models.CharField(max_length=255,null=True,blank=True)
    fmyibao=models.CharField(max_length=255,null=True,blank=True)


class Aihao(models.Model):
    idname = models.IntegerField(primary_key=True)
    tiyu=models.CharField(max_length=255,null=True,blank=True)
    food=models.CharField(max_length=255,null=True,blank=True)
    book=models.CharField(max_length=255,null=True,blank=True)
    movies=models.CharField(max_length=255,null=True,blank=True)
    jiemu=models.CharField(max_length=255,null=True,blank=True)
    xiuxian=models.CharField(max_length=255,null=True,blank=True)
    aihao=models.CharField(max_length=255,null=True,blank=True)
    trip=models.CharField(max_length=255,null=True,blank=True)

