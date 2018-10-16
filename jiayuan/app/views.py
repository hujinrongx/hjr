from django.shortcuts import render


import os

from app.models import*
def ziliao(request):
    return render(request,"user2.html")
# 注册功能
# -----------------------------------------------------------------------------
def loginn(request):
    return render(request,"login.html")
def login(request):

        # 获取HTML数据并与数据库匹配
    usernum = request.POST.get("usertell")
    password = request.POST.get("password")


    try:
        st = Zhuce.objects.get(idname=usernum)
        print(st.idname)
        print(usernum)
        if (str(st.password)==str(password)):

            return render(request,"main.html")
    except:
            print("未登录2")
            return render(request,"login.html")
    else:
        print("未登录1")
        return render(request, "login.html")

def zhucee(request):
    return render(request,"zhuce.html")
def zhucea(request):
    # 链接数据库,存入数据库
    try:
    # 获取index.html的信息
        usernum = request.POST.get("phone")
        nan = request.POST.get("sex")
        nv=request.POST.get("nv")
        sex=str(nan)+str(nv)
        year= request.POST.get("year")
        month = request.POST.get("month")
        day = request.POST.get("day")
        province= request.POST.get("province")
        city = request.POST.get("city")
        town = request.POST.get("town")
        hunyin= request.POST.get("marriage")
        tall= request.POST.get("tall")
        xueli= request.POST.get("xueli")
        salary = request.POST.get("salary")
        password = request.POST.get("password")
        nam = request.POST.get("name")
        a = request.POST.get("a")
        b = request.POST.get("b")
        c = request.POST.get("c")
        d = request.POST.get("d")
        e = request.POST.get("e")
        f = request.POST.get("f")
        g = request.POST.get("g")

        request.session["idname"]=usernum
        request.session.set_expiry(10000000)
        print(request.session["idname"])
        jieshao=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)

        birthday=str(year)+str(month)+str(day)
        area=province+ city+town
        print(area)
        print(usernum+"————————————————————————————————————————-")
        # 存储账号密码
        stu=Zhuce(usernum,sex,birthday,area,
                             hunyin,tall,xueli,salary,password,nam,jieshao)
        stu.save()
    except:
        return render(request,"zhuce.html")

    return render(request,"login.html")
# 上传照片
# -------------------------------------------------------------------------
def upload(request):
    # 每次先判断是否有图片，有则删除，没有直接上传图片
    path=r"D:\新建文件夹\新建文件夹\jiayuan\static\photo"
    namelist = os.listdir(path)
    for name in namelist:
        if name.endswith(".jpg"):
            os.remove(os.path.join(path, name))

    image1 = request.FILES.get("f")
    image = open(os.path.join(path, str(image1)), "wb")

    while True:
        bytes = image1.read(1024)
        if bytes == b"":
            break
        else:
            image.write(bytes)
    imagename=str(image1)
    image.close()
    return render(request,"up_photo.html",{"image":imagename})




def main(request):
    return render(request,"main.html")


def up_photo(request):
    return render(request,"up_photo.html")

# 生活信息表查询
# ____________________________________________________________________

def basics(request,num):
    stu=Basics.objects.get(idname=request.session["idname"])

    return render(request,"",{"idname":stu.idname,"chird":stu.chird,
                              "area":stu.area,"register":stu.register,"ethnic":stu.ethnic
                              ,"salary":stu.salary,"house":stu.house,"car":stu.car,
                              "password":stu.password})

def inbasics(request):
    idname=request.session["idname"]
    chird = request.POST.get("chird")
    province = request.POST.get("province")
    city = request.POST.get("city")
    town = request.POST.get("town")

    area=str(province)+str(city)+str(town)

    xuexing = request.POST.get("xue")
    ethnic = request.POST.get("ethnic")
    salary = "暂无信息"
    house = request.POST.get("house")
    car = request.POST.get("car")
    password = "暂无信息"
    lifename = request.POST.get("lifename")
    shengfen = request.POST.get("shengfen")
    qq = request.POST.get("qq")
    adrr = request.POST.get("adr")
    youbian = request.POST.get("youbian")
    stu=Basics(idname,chird,area,xuexing,ethnic,salary,house,car,
               password,lifename,shengfen,qq,adrr,youbian)
    stu.save()
    return render(request,"user3.html")





# def bodyshape(request,num):
#     sql = "select * from bodyshape WHERE idnum=s%"
#     cur.execute(sql, (num))
#     usertell,weight,bodyshape,face,air,hair,\
#     skin,muscle,health,dress=cur.fetchone()
#     return render(request, "", {"usertell":usertell,"muscle":muscle,
#                                 "weight":weight,"bodyshape":bodyshape,
#                                 "face": face, "air": air,"hair":hair," skin":skin,
#                                 "health": health,"dress":dress})


def inbodyshape(request,num):
    weight = request.POST.get("")
    bodyshape = request.POST.get("")
    face = request.POST.get("")
    eyes = request.POST.get("")
    hair = request.POST.get("")
    skin = request.POST.get("")
    muscle = request.POST.get("")
    health = request.POST.get("")
    dress = request.POST.get("")

# 晒幸福功能
# ---------------------------------------------------------------------------------
def xingfu(request):
    usernum = request.POST.get("usertell")
    name = request.POST.get("usertell")
    condition = request.POST.get("usertell")
#上传幸福照(存数据库)
    path=r"D:\新建文件夹\新建文件夹\hjr\static\xfimg"
    image1 = request.FILES.get("f")
    image = open(os.path.join(path, str(image1)), "wb")

    while True:
        bytes = image1.read(1024)
        if bytes == b"":
            break
        else:
            image.write(bytes)
    picture = str(image1)
    image.close()

#     独白
def dubai(request):
    return render(request,"user3.html")
def indubai(request):
    idname=request.session["idname"]
    neixindubai=request.POST.get("neixindubai")
    print(neixindubai)
    stu=Dubai(idname,neixindubai)
    stu.save()
    return render(request,"user5.html")

# def shaixf(request,num):
#
#
#     return render(request,"",{"Usertell":usertell,"name":name,
#                               "picture":picture,"condition":condition})
def vip(request):
    return render(request,"VIPgoumai.html")


# 经济
def user5(request):
    return render(request,"user5.html")
def inuser5(request):
    idname = request.session["idname"]
    a = request.POST.get("cunkuan")
    b = request.POST.get("jijin")
    c = request.POST.get("zhengquan")
    d = request.POST.get("licai")
    e = request.POST.get("baoxian")
    f = request.POST.get("waihui")
    g = request.POST.get("qihuo")
    h = request.POST.get("jinshu")
    l = request.POST.get("fangchan")

    li=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(l)

    m = request.POST.get("waizhai")
    n = request.POST.get("fangdai")
    o = request.POST.get("chedai")
    p = request.POST.get("liu")
    q = request.POST.get("zhuxue")
    r = request.POST.get("geren")
    dai= str(m) + str(n) + str(o) + str(p) + str(q) + str(r)
    salary= request.POST.get("salary")
    stu=Econ(idname,li,dai,salary)
    stu.save()
    return render(request,"user6.html")

# 生活方式
def user6(request):
    return render(request,"user6.html")
def inuser6(request):
    idname=request.session["idname"]
    smoke = request.POST.get("somke")
    drink = request.POST.get("drink")
    exercise = request.POST.get("exercise")
    eat = request.POST.get("food")
    shopping = request.POST.get("shopping")
    religious = request.POST.get("religious")
    resttime = request.POST.get("resttime")
    network = request.POST.get("network")
    maxspend = request.POST.get("maxspend")

    house= request.POST.get("housework")
    work= request.POST.get("work")
    jiawu=str(house)+str(work)

    pe = request.POST.get("pet")
    pt=request.POST.get("an")
    pet=str(pe)+str(pt)

    stu=Lifestyle(idname,smoke,drink,exercise,
            eat,shopping,religious,resttime,network,maxspend,jiawu,pet)
    stu.save()
    return render(request,"user7.html")

# def Lifestyle(request):
#
#
#     stu=Lifestyle.objects.get(idname=num)
#
#     return render(request,"",{"idname":stu.idname,"smoke":stu.smoke,"drink":stu.drink,
#                               "exercise":stu.exercise,"eat":stu.eat,"shopping":stu.shopping,\
#     "religious":stu.religious,"resttime":stu.resttime,"network":stu.network,
#                               "maxspend":stu.maxspend,"housework":stu.housework,"pet":stu.pet})

# 工作学习
def user7(request):
    return render(request,"user7.html")
def inuser7(request):
    idname = request.session["idname"]
    danwei = request.POST.get("danwei")
    hangye = request.POST.get("hangye")
    jobtype = request.POST.get("jobtype")
    daiyu = request.POST.get("daiyu")
    workingstate = request.POST.get("workingstate")
    diaodong = request.POST.get("diaodong")
    haiwai = request.POST.get("haiwai")
    careerfamliy = request.POST.get("careerfamliy")
    gratitudefrom = request.POST.get("gratitudefrom")
    major = request.POST.get("major")
    l1 = request.POST.get("l1")
    la = request.POST.get("la")
    lan = request.POST.get("lan")
    language=str(l1)+str(la)+str(lan)
    stu=Workandstudy(idname,danwei,hangye,jobtype,daiyu,workingstate,
                     diaodong,haiwai,careerfamliy,gratitudefrom,major,language)
    stu.save()
    return render(request,"user8.html")
# 外貌体型
def user8(request):
    return render(request,"user8.html")
def inuser8(request):
    idname = request.session["idname"]
    weight=request.POST.get("weight")
    bodyshape = request.POST.get("shape")
    face = request.POST.get("face_type")

    es = request.POST.get("rank_consumption")
    eye=request.POST.get("eye_type")
    eyes=str(es)+str(eye)

    h = request.POST.get("hair_color")
    ha = request.POST.get("hair_type")
    hai = request.POST.get("hair_length")
    hair = str(h)+str(ha)+str(hai)

    skin = request.POST.get("skin")
    color = request.POST.get("skin_color")
    muscle = request.POST.get("cupormuscle")
    health = request.POST.get("health")
    dress = request.POST.get("dress")
    stu=Bodyshape(idname,weight,bodyshape,face,eyes,hair,skin,color,
                  muscle,health,dress)
    stu.save()
    return render(request,"user9.html")

def user9(request):
    return render(request,"user9.html")
def inuser9(request):
    idname = request.session["idname"]

    ji= request.POST.get("province")
    g= request.POST.get("city")
    an = request.POST.get("town")
    jiguan = str(ji)+str(g)+str(an)

    guoji = request.POST.get("nationality")
    gexing = request.POST.get("personality")
    youmo = request.POST.get("humor")
    piqi = request.POST.get("temper")
    taidu = request.POST.get("emotional_attitude")
    chird = request.POST.get("child_want")
    jiehun = request.POST.get("marriage_time")
    yidilian = request.POST.get("ld_relationship")
    nicehunyin = request.POST.get("ideal-marriage")
    tongzhu = request.POST.get("parent_together")
    paihang = request.POST.get("paihang")
    jiemei = request.POST.get("elder-sister")
    fumu = request.POST.get("parents")
    fuwork = request.POST.get("father_work")
    muwork = request.POST.get("mother_work")
    fumuqian = request.POST.get("parents_economic")
    fmyibao = request.POST.get("parents_health_care")
    stu=Hunyin(idname,jiguan,guoji,gexing,youmo,piqi,taidu,chird,jiehun,
               yidilian,nicehunyin,tongzhu,paihang,jiemei,fumu,fuwork,muwork,
               fumuqian,fmyibao)
    stu.save()
    return render(request,"user10.html")

def user10(request):
    return render(request,"user10.html")
def inuser10(request):

    return render(request,"main.html")
def sousuo(request):
    return render(request,'sousuo.html')
def select(request):
   s= request.POST.get('salary')
   age1 = request.POST.get('a')
   age2= request.POST.get('b')
   stu=Zhuce.objects.filter(salary="8000以上")
   return render(request,"ppp.html",{'stu':stu})
def sai(request):
    return render(request,"shaixingfu.html")
def s(request):
    return render(request,"jinrituijian.html")