from django.shortcuts import render

import datetime 
import timeago
# ******************************

from django.db.models import Max, Min, Sum, Avg
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from AppAGRI.serializer import batvannelSerializer,capsolSerializer,capsol2Serializer, capnpkSerializer, valveFlowSerializer

from .models import *

# Create your views here.

def home(request):
    print("*****************************************jes suis dans home***************")
    # print("date",str((datetime.datetime.now())))
    # print("date2", str((datetime.datetime.now()).strftime("%M")))
    tab=CapSol.objects.last()
    capnpk = CapNPK.objects.last()

    cap2 = CapSol2.objects.last()

    bv= batvanne.objects.last()
    flow = ValveFlow.objects.last()
    # print("last",str((tab.time)))

    f = CapSol.objects.first()
    print("dernière enrregister  : ", bv.dt)

    max_temp1=CapSol.objects.all().aggregate(Max('Temp'))
    min_temp1= CapSol.objects.all().aggregate(Min('Temp'))
    moyt1 = 0
    if (max_temp1["Temp__max"] != None and min_temp1["Temp__min"] != None):
        moyt1= (max_temp1["Temp__max"] + min_temp1["Temp__min"])/2

    max_hum1=CapSol.objects.all().aggregate(Max('Hum'))
    min_hum1 = CapSol.objects.all().aggregate(Min('Hum'))
    moyh1 = 0
    if (max_hum1["Hum__max"] != None and min_hum1["Hum__min"] != None):
        moyh1=(max_hum1["Hum__max"]+min_hum1["Hum__min"])/2
    
    max_sal1=CapSol.objects.all().aggregate(Max('Sal'))
    min_sal1 = CapSol.objects.all().aggregate(Min('Sal'))
    moys1 = 0
    if (max_sal1["Sal__max"] != None and min_sal1["Sal__min"] != None):
        moys1=(max_sal1["Sal__max"]+min_sal1["Sal__min"])/2

    max_ec1=CapSol.objects.all().aggregate(Max('Ec'))
    min_ec1 = CapSol.objects.all().aggregate(Min('Ec'))
    moyec1 = 0
    if (max_ec1["Ec__max"] != None and min_ec1["Ec__min"] != None):
        moyec1=(max_ec1["Ec__max"]+min_ec1["Ec__min"])/2
    
    max_bat1=CapSol.objects.all().aggregate(Max('Bat'))
    min_bat1 = CapSol.objects.all().aggregate(Min('Bat'))
    moyb1 = 0
    if (max_bat1["Bat__max"] != None and min_bat1["Bat__min"] != None):
        moyb1=(max_bat1["Bat__max"]+min_bat1["Bat__min"])/2

    # *************************************************************
    max_temp2=CapSol.objects.all().aggregate(Max('Temp'))
    min_temp2= CapSol.objects.all().aggregate(Min('Temp'))
    moyt2 = 0
    if (max_temp2["Temp__max"] != None and min_temp2["Temp__min"] != None):
        moyt2=(max_temp2["Temp__max"]+min_temp2["Temp__min"])/2

    max_hum2=CapSol.objects.all().aggregate(Max('Hum'))
    min_hum2 = CapSol.objects.all().aggregate(Min('Hum'))
    moyh2 = 0
    if (max_hum2["Hum__max"] != None and min_hum2["Hum__min"] != None):
        moyh2=(max_hum2["Hum__max"]+min_hum2["Hum__min"])/2
    
    max_sal2=CapSol.objects.all().aggregate(Max('Sal'))
    min_sal2 = CapSol.objects.all().aggregate(Min('Sal'))
    moys2 = 0
    if (max_sal2["Sal__max"] != None and min_sal2["Sal__min"] != None):
        moys2=(max_sal2["Sal__max"]+min_sal2["Sal__min"])/2

    max_ec2=CapSol.objects.all().aggregate(Max('Ec'))
    min_ec2 = CapSol.objects.all().aggregate(Min('Ec'))
    moyec2 = 0
    if (max_ec2["Ec__max"] != None and min_ec2["Ec__min"] != None):
        moyec2=(max_ec2["Ec__max"]+min_ec2["Ec__min"])/2
    
    max_bat2=CapSol.objects.all().aggregate(Max('Bat'))
    min_bat2= CapSol.objects.all().aggregate(Min('Bat'))
    moyb2 = 0
    if (max_bat2["Bat__max"] != None and min_bat2["Bat__min"] != None):
        moyb2=(max_bat2["Bat__max"]+min_bat2["Bat__min"])/2
# **********************************************************************************************************
    max_azoute = CapNPK.objects.all().aggregate(Max('Azoute'))
    min_azoute = CapNPK.objects.all().aggregate(Min('Azoute'))
    moy_az = 0
    if (max_azoute["Azoute__max"] != None and min_azoute["Azoute__min"] != None):
        moy_az=(max_azoute["Azoute__max"]+min_azoute["Azoute__min"])/2
    

    max_pho = CapNPK.objects.all().aggregate(Max('Phosphore'))
    min_pho = CapNPK.objects.all().aggregate(Min('Phosphore'))
    moy_pho = 0
    if (max_pho["Phosphore__max"] != None and min_pho["Phosphore__min"] != None):
        moy_pho=(max_pho["Phosphore__max"]+min_pho["Phosphore__min"])/2
    
    max_po = CapNPK.objects.all().aggregate(Max('Potassium'))
    min_po = CapNPK.objects.all().aggregate(Min('Potassium'))
    moy_po = 0
    if (max_po["Potassium__max"] != None and min_po["Potassium__min"] != None):
        moy_po=(max_po["Potassium__max"]+min_po["Potassium__min"])/2


    max_batnpk = CapNPK.objects.all().aggregate(Max('Bat'))
    min_batnpk = CapNPK.objects.all().aggregate(Min('Bat'))
    moy_batnpk = 0
    if (max_batnpk["Bat__max"] != None and min_batnpk["Bat__min"] != None):
        moy_batnpk=(max_batnpk["Bat__max"]+min_batnpk["Bat__min"])/2


# ********************************************************************************************************************

    context = {'flow':flow,'tab': tab,'max_temp1':max_temp1,'min_temp1':min_temp1,'moyt1':moyt1,"max_hum1":max_hum1,"min_hum1":min_hum1, "moyh1":moyh1, "max_sal1":max_sal1, "moys1":moys1,
                "min_sal1":min_sal1, "max_ec1":max_ec1, "min_ec1":min_ec1, "moyec1":moyec1,"max_bat1":max_bat1, "moyb1":moyb1, "min_bat1":min_bat1,'max_temp2':max_temp2,
                'min_temp2':min_temp2,'moyt2':moyt2,"max_hum2":max_hum2,"min_hum2":min_hum2, "moyh2":moyh2, "max_sal2":max_sal2, "moys2":moys2,"min_sal2":min_sal2, "max_ec2":max_ec2, 
                "min_ec2":min_ec2, "moyec2":moyec2,"max_bat2":max_bat2, "moyb2":moyb2, "min_bat2":min_bat2,'f':f,'cap2':cap2, 'bv':bv,'capnpk':capnpk, 'max_azoute':max_azoute, 
                'min_azoute':min_azoute, 'moy_az':moy_az, 'max_pho':max_pho, 'min_pho':min_pho, 'moy_pho':moy_pho, 'max_po':max_po, 'min_po':min_po, 'moy_po':moy_po, 'max_batnpk':max_batnpk,
                'min_batnpk':min_batnpk, 'moy_batnpk':moy_batnpk}
    print("******************context*****************: ", context)
    return render(request, "index.html", context)

def home_refresh(request):
    print("*****************************************home_refresh***********************")
    flow = valveFlowSerializer(ValveFlow.objects.last()).data
    capnpk = capnpkSerializer(CapNPK.objects.last()).data
    tab= capsolSerializer(CapSol.objects.last()).data
    cap2 = capsol2Serializer(CapSol2.objects.last()).data
    bv= batvannelSerializer(batvanne.objects.last()).data
    f = capsolSerializer(CapSol.objects.first()).data

    date_format(bv)
    date_format(tab)
    date_format(cap2)
    date_format(capnpk)
    max_temp=CapSol.objects.all().aggregate(Max('Temp'))
    min_temp = CapSol.objects.all().aggregate(Min('Temp'))
    moy = 0
    if (max_temp["Temp__max"] != None and min_temp["Temp__min"] != None):
        moy=(max_temp["Temp__max"]+min_temp["Temp__min"])/2

    max_azt=CapNPK.objects.all().aggregate(Max('Azoute'))
    min_azt = CapNPK.objects.all().aggregate(Min('Azoute'))
    moyazt = 0
    if (max_azt["Azoute__max"] != None and min_azt["Azoute__min"] != None):
        moyazt=(max_azt["Azoute__max"]+min_azt["Azoute__min"])/2
    
    context = {'flow':flow,'tab': tab,"max_azt":max_azt, "min_azt" : min_azt, "moyazt":moyazt,'max_temp':max_temp,'min_temp':min_temp,'moy':moy,'f':f,'cap2':cap2, 'bv':bv, 'capnpk':capnpk}
    print(context)
    {"test" : 'json.dumps(context)'}
    return JsonResponse(context)

def chart(request):
    tab=CapSol.objects.all()
    labels = []
    dataa = []
    dataa2 = []
    for data in tab:
        labels.append((data.dt).strftime("%Y-%m-%d %H:%M:%S"))
        dataa.append(data.Temp)
        dataa2.append(data.Hum)
        print("labels0", type(labels))
    if (request.method == "POST"):
        labels.clear()
        dataa.clear()
        dataa2.clear()

        fromdate = request.POST.get('startdate')
        # print(type(datetime.datetime.now()))
        print("fromdate")
        print(fromdate)
        todate = request.POST.get('enddate')
        print("todate")
        print(todate)
        first = CapSol.objects.first()
        print("first date", str(first.dt))
        lastdate = CapSol.objects.last()
        print("last date", str(lastdate.dt))
        if fromdate != "" and todate != "":
            # to = datetime.datetime.strptime(todate, '%Y-%m-%d')+datetime.timedelta(days=1)
            to = datetime.datetime.strptime(todate, '%Y-%m-%d') + datetime.timedelta(days=1)
            print("to", to)
            # fromdate = datetime.datetime("07-07")
            created_documents5 = CapSol.objects.filter(dt__range=[fromdate, to]).order_by('dt')
            print("created_documents5", created_documents5)
            for data in created_documents5:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Temp)
                dataa2.append(data.Hum)
                print("labelfiltter", labels)
                # return HttpResponseRedirect('/')
            # print("labelfiltter",labels)
        if fromdate == "":
            fromdate = first.dt

        if todate == "":
            to = (lastdate.dt) + datetime.timedelta(days=1)
            todate = to + datetime.timedelta(days=1)
            labels.clear()
            dataa.clear()
            dataa2.clear()
            created_documents6 = CapSol.objects.filter(dt__range=[fromdate, todate]).order_by('id')
            # print("created_documents6", created_documents6)

            for data in created_documents6:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Temp)
                dataa2.append(data.Hum)
                # print("lab", labels)
                return HttpResponseRedirect('/Chart')

            print("todate", type(todate))

    context={'tab':tab,'labels':labels,'dataa':dataa}
    return render(request,"charts.html",context)

def charthum(request):
    tab=CapSol.objects.all()
    labels = []
    dataa = []
    dataa2 = []
    for data in tab:
        labels.append((data.dt).strftime("%Y-%m-%d %H:%M:%S"))
        dataa.append(data.Temp)
        dataa2.append(data.Hum)
        print("labels0", type(labels))
    if (request.method == "POST"):
        labels.clear()
        dataa.clear()
        dataa2.clear()

        fromdate = request.POST.get('startdate')
        # print(type(datetime.datetime.now()))
        print("fromdate")
        print(fromdate)
        todate = request.POST.get('enddate')
        print("todate")
        print(todate)
        first = CapSol.objects.first()
        print("first date", str(first.dt))
        lastdate = CapSol.objects.last()
        print("last date", str(lastdate.dt))
        if fromdate != "" and todate != "":
            # to = datetime.datetime.strptime(todate, '%Y-%m-%d')+datetime.timedelta(days=1)
            to = datetime.datetime.strptime(todate, '%Y-%m-%d') + datetime.timedelta(days=1)
            print("to", to)
            # fromdate = datetime.datetime("07-07")
            created_documents5 = CapSol.objects.filter(dt__range=[fromdate, to]).order_by('dt')
            print("created_documents5", created_documents5)
            for data in created_documents5:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Temp)
                dataa2.append(data.Hum)
                print("labelfiltter", labels)
                # return HttpResponseRedirect('/')
            # print("labelfiltter",labels)
        if fromdate == "":
            fromdate = first.dt

        if todate == "":
            to = (lastdate.dt) + datetime.timedelta(days=1)
            todate = to + datetime.timedelta(days=1)
            labels.clear()
            dataa.clear()
            dataa2.clear()
            created_documents6 = CapSol.objects.filter(dt__range=[fromdate, todate]).order_by('id')
            print("created_documents6", created_documents6)

            for data in created_documents6:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Temp)
                dataa2.append(data.Hum)
                print("lab", labels)
                return HttpResponseRedirect('/Charthum')

            print("todate", type(todate))

    context={'tab':tab,'labels':labels,'dataa':dataa,'dataa2':dataa2}
    return render(request,"chartshum.html",context)

def chartsal(request):
    tab=CapSol.objects.all()
    labels = []
    dataa = []
    for data in tab:
        labels.append((data.dt).strftime("%Y-%m-%d %H:%M:%S"))
        dataa.append(data.Sal)
        print("labels0", type(labels))
    if (request.method == "POST"):
        labels.clear()
        dataa.clear()

        fromdate = request.POST.get('startdate')
        # print(type(datetime.datetime.now()))
        print("fromdate")
        print(fromdate)
        todate = request.POST.get('enddate')
        print("todate")
        print(todate)
        first = CapSol.objects.first()
        print("first date", str(first.dt))
        lastdate = CapSol.objects.last()
        print("last date", str(lastdate.dt))
        if fromdate != "" and todate != "":
            # to = datetime.datetime.strptime(todate, '%Y-%m-%d')+datetime.timedelta(days=1)
            to = datetime.datetime.strptime(todate, '%Y-%m-%d') + datetime.timedelta(days=1)
            print("to", to)
            # fromdate = datetime.datetime("07-07")
            created_documents5 = CapSol.objects.filter(dt__range=[fromdate, to]).order_by('dt')
            print("created_documents5", created_documents5)
            for data in created_documents5:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Sal)

                print("labelfiltter", labels)
                # return HttpResponseRedirect('/')
            # print("labelfiltter",labels)
        if fromdate == "":
            fromdate = first.dt

        if todate == "":
            to = (lastdate.dt) + datetime.timedelta(days=1)
            todate = to + datetime.timedelta(days=1)
            labels.clear()
            dataa.clear()

            created_documents6 = CapSol.objects.filter(dt__range=[fromdate, todate]).order_by('id')
            print("created_documents6", created_documents6)

            for data in created_documents6:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Sal)

                print("lab", labels)
                return HttpResponseRedirect('/Chartsal')

            print("todate", type(todate))

    context={'tab':tab,'labels':labels,'dataa':dataa}
    return render(request,"chartssal.html",context)

def chartec(request):
    tab=CapSol.objects.all()
    labels = []
    dataa = []
    for data in tab:
        labels.append((data.dt).strftime("%Y-%m-%d %H:%M:%S"))
        dataa.append(data.Ec)
        print("labels0", type(labels))
    if (request.method == "POST"):
        labels.clear()
        dataa.clear()

        fromdate = request.POST.get('startdate')
        # print(type(datetime.datetime.now()))
        print("fromdate")
        print(fromdate)
        todate = request.POST.get('enddate')
        print("todate")
        print(todate)
        first = CapSol.objects.first()
        print("first date", str(first.dt))
        lastdate = CapSol.objects.last()
        print("last date", str(lastdate.dt))
        if fromdate != "" and todate != "":
            # to = datetime.datetime.strptime(todate, '%Y-%m-%d')+datetime.timedelta(days=1)
            to = datetime.datetime.strptime(todate, '%Y-%m-%d') + datetime.timedelta(days=1)
            print("to", to)
            # fromdate = datetime.datetime("07-07")
            created_documents5 = CapSol.objects.filter(dt__range=[fromdate, to]).order_by('dt')
            print("created_documents5", created_documents5)
            for data in created_documents5:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Ec)

                print("labelfiltter", labels)
                # return HttpResponseRedirect('/')
            # print("labelfiltter",labels)
        if fromdate == "":
            fromdate = first.dt

        if todate == "":
            to = (lastdate.dt) + datetime.timedelta(days=1)
            todate = to + datetime.timedelta(days=1)
            labels.clear()
            dataa.clear()

            created_documents6 = CapSol.objects.filter(dt__range=[fromdate, todate]).order_by('id')
            print("created_documents6", created_documents6)

            for data in created_documents6:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Ec)

                print("lab", labels)
                return HttpResponseRedirect('/Chartec')

            print("todate", type(todate))

    context={'tab':tab,'labels':labels,'dataa':dataa}
    return render(request,"chartsec.html",context)

def chartbat(request):
    tab=CapSol.objects.all()
    labels = []
    dataa = []
    for data in tab:
        labels.append((data.dt).strftime("%Y-%m-%d %H:%M:%S"))
        dataa.append(data.Bat)
        print("labels0", type(labels))
    if (request.method == "POST"):
        labels.clear()
        dataa.clear()

        fromdate = request.POST.get('startdate')
        # print(type(datetime.datetime.now()))
        print("fromdate")
        print(fromdate)
        todate = request.POST.get('enddate')
        print("todate")
        print(todate)
        first = CapSol.objects.first()
        print("first date", str(first.dt))
        lastdate = CapSol.objects.last()
        print("last date", str(lastdate.dt))
        if fromdate != "" and todate != "":
            # to = datetime.datetime.strptime(todate, '%Y-%m-%d')+datetime.timedelta(days=1)
            to = datetime.datetime.strptime(todate, '%Y-%m-%d') + datetime.timedelta(days=1)
            print("to", to)
            # fromdate = datetime.datetime("07-07")
            created_documents5 = CapSol.objects.filter(dt__range=[fromdate, to]).order_by('dt')
            print("created_documents5", created_documents5)
            for data in created_documents5:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Bat)

                print("labelfiltter", labels)
                # return HttpResponseRedirect('/')
            # print("labelfiltter",labels)
        if fromdate == "":
            fromdate = first.dt

        if todate == "":
            to = (lastdate.dt) + datetime.timedelta(days=1)
            todate = to + datetime.timedelta(days=1)
            labels.clear()
            dataa.clear()

            created_documents6 = CapSol.objects.filter(dt__range=[fromdate, todate]).order_by('id')
            print("created_documents6", created_documents6)

            for data in created_documents6:
                labels.append((data.dt).strftime("%d %b %Y %H:%M:%S"))
                dataa.append(data.Bat)

                print("lab", labels)
                return HttpResponseRedirect('/Chartec')

            print("todate", type(todate))

    context={'tab':tab,'labels':labels,'dataa':dataa}
    return render(request,"chartsbat.html",context)

""" temperature capteur de sol"""
def tsol1(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    # print((datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0))
    # print("oui ......",one_day_ago)
    print('##############################################')
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Tsol1.html", context)

def tsol3(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Tsol3.html", context)

def tsol7(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Tsol7.html", context)

def tsol15(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Tsol15.html", context)

def tsol21(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Tsol1.html", context)

def tsol23(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Tsol3.html", context)

def tsol27(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Tsol7.html", context)

def tsol215(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Temp)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Tsol15.html", context)

""" humidité sol """
def hsol1(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Hsol1.html", context)

def hsol3(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Hsol3.html", context)

def hsol7(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Hsol7.html", context)

def hsol15(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Hsol15.html", context)

def hsol21(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Hsol1.html", context)

def hsol23(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Hsol3.html", context)

def hsol27(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Hsol7.html", context)

def hsol215(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Hum)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Hsol15.html", context)

""" salinite """
def ssol1(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Ssol1.html", context)

def ssol3(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Ssol3.html", context)

def ssol7(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Ssol7.html", context)

def ssol15(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Ssol15.html", context)

def ssol21(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Ssol1.html", context)

def ssol23(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Ssol3.html", context)

def ssol27(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Ssol7.html", context)

def ssol215(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Sal)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Ssol15.html", context)

# EC
def esol1(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Esol1.html", context)

def esol3(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        #print("labels", labels)
        dataa.append(i.Ec)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Esol3.html", context)

def esol7(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Esol7.html", context)

def esol15(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Esol15.html", context)

""" e2"""

def esol21(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Esol1.html", context)

def esol23(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Esol3.html", context)

def esol27(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Esol7.html", context)

def esol215(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Ec)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Esol15.html", context)

#Batterie
def bsol1(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Bsol1.html", context)

def bsol3(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Bsol3.html", context)

def bsol7(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Bsol7.html", context)

def bsol15(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol/Bsol15.html", context)

def bsol21(request):
    # one_day_ago = (datetime.datetime.today()).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    # print("oui ......",one_day_ago)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Bsol1.html", context)

def bsol23(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Bsol3.html", context)

def bsol27(request):
    # one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Bsol7.html", context)

def bsol215(request):
    one_day_ago = (datetime.datetime.now() - datetime.timedelta(days=15)).replace(hour=0,minute=0,second=0,microsecond=0)
    one_day_ago = CapSol2.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0) - datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapSol2.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)
    lst = Data.objects.last()
    context = {'all': all, 'lst': lst, 'labels': labels, 'dataa': dataa}
    return render(request, "sol2/Bsol15.html", context)
# **************************************************************************************************************************************

def asol1(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Azoute)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/azsol1.html", context)

def asol3(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Azoute)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/azsol3.html", context)

def asol7(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Azoute)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/azsol7.html", context)

def asol15(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Azoute)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/azsol15.html", context)

def phsol1(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Phosphore)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/phsol1.html", context)

def phsol3(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Phosphore)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/phsol3.html", context)

def phsol7(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Phosphore)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/phsol7.html", context)

def phsol15(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Phosphore)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/phsol15.html", context)

def psol1(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Potassium)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/posol1.html", context)

def psol3(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Potassium)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/posol3.html", context)


def psol7(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Potassium)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/posol7.html", context)


def psol15(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Potassium)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/posol15.html", context)


def npkbsol1(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/npkbsol1.html", context)

def npkbsol3(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=3)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/npkbsol3.html", context)


def npkbsol7(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=7)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/npkbsol7.html", context)


def npkbsol15(request):
    one_day_ago = CapNPK.objects.last().dt.replace(hour=0,minute=0,second=0,microsecond=0)- datetime.timedelta(days=15)
    labels = []
    dataa = []
    all = CapNPK.objects.filter(dt__gte=one_day_ago)
    # print("all", all)
    for i in all:
        labels.append((i.dt).strftime("%Y-%m-%d %H:%M:%S"))
        # print("labels", labels)
        dataa.append(i.Bat)

    context = {'all': all, 'labels': labels, 'dataa': dataa}
    return render(request, "npk/npkbsol1.html5", context)


import datetime

def date_format(a): 
    date_str = a["dt"][:-1]  
    date_given = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    date_with_added_hour = date_given + datetime.timedelta(hours=1)
    time_elapsed = datetime.datetime.now() - date_with_added_hour

    years = time_elapsed.days // 365
    remaining_days = time_elapsed.days % 365
    months = remaining_days // 30
    remaining_days %= 30
    days = remaining_days
    hours = time_elapsed.seconds // 3600
    minutes = (time_elapsed.seconds // 60) % 60

    formatted_timeago = ""
    
    if years > 0:
        formatted_timeago += f"{years} an{'s' if years > 1 else ''}, "
    if months > 0:
        formatted_timeago += f"{months} mois, "
    if days > 0:
        formatted_timeago += f"{days} jour{'s' if days > 1 else ''}, "
    if hours > 0:
        formatted_timeago += f"{hours} heure{'s' if hours > 1 else ''}, "
    if minutes > 0 or formatted_timeago == "":
        formatted_timeago += f"{minutes} minute{'s' if minutes > 1 else ''}"
        
    a["timeago"] = formatted_timeago
    return a["timeago"]





