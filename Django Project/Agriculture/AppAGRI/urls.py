from django.urls import path

from AppAGRI import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home/refresh', views.home_refresh,name="home_refresh"),
    path('Chart/', views.chart,name="chart"),
    path('Charthum/', views.charthum,name="charthum"),
    path('Chartsal/', views.chartsal, name="chartsal"),
    path('Chartec/', views.chartec, name="chartec"),
    path('Chartbat/', views.chartbat, name="chartbat"),
    
    # path('data/', views.weatherS,name="data"),
    path('data/', views.home,name="data"),
    path('wso/', views.home,name="wso"),

    #temperature sol
    path('st24h/', views.tsol1,name="tsacc"),
    path('st3jrs/', views.tsol3,name="ts3acc"),
    path('st7jrs/', views.tsol7,name="ts7acc"),
    path('st15jrs/', views.tsol15,name="ts15acc"),

    path('2st24h/', views.tsol21,name="2tsacc"),
    path('2st3jrs/', views.tsol23,name="2ts3acc"),
    path('2st7jrs/', views.tsol27,name="2ts7acc"),
    path('2st15jrs/', views.tsol215,name="2ts15acc"),
    #humidite dsol
    path('sh24h/', views.hsol1,name="hsacc"),
    path('sh3jrs/', views.hsol3,name="hs3acc"),
    path('sh7jrs/', views.hsol7,name="hs7acc"),
    path('sh15jrs/', views.hsol15,name="hs15acc"),

    path('2sh24h/', views.hsol21, name="2hsacc"),
    path('2sh3jrs/', views.hsol23, name="2hs3acc"),
    path('2sh7jrs/', views.hsol27, name="2hs7acc"),
    path('2sh15jrs/', views.hsol215, name="2hs15acc"),
    #salinité
    path('ss24h/', views.ssol1, name="ssacc"),
    path('ss3jrs/', views.ssol3, name="ss3acc"),
    path('ss7jrs/', views.ssol7, name="ss7acc"),
    path('ss15jrs/', views.ssol15, name="ss15acc"),

    path('2ss24h/', views.ssol21, name="2ssacc"),
    path('2ss3jrs/', views.ssol23, name="2ss3acc"),
    path('2ss7jrs/', views.ssol27, name="2ss7acc"),
    path('2ss15jrs/', views.ssol215, name="2ss15acc"),
    #EC
    path('es24h/', views.esol1, name="esacc"),
    path('es3jrs/', views.esol3, name="es3acc"),
    path('es7jrs/', views.esol7, name="es7acc"),
    path('es15jrs/', views.esol15, name="es15acc"),

    path('2es24h/', views.esol21, name="2esacc"),
    path('2es3jrs/', views.esol23, name="2es3acc"),
    path('2es7jrs/', views.esol27, name="2es7acc"),
    path('2es15jrs/', views.esol215, name="2es15acc"),
    #batterie sol
    path('bs24h/', views.bsol1, name="bsacc"),
    path('bs3jrs/', views.bsol3, name="bs3acc"),
    path('bs7jrs/', views.bsol7, name="bs7acc"),
    path('bs15jrs/', views.bsol15, name="bs15acc"),

    path('2bs24h/', views.bsol21, name="2bsacc"),
    path('2bs3jrs/', views.bsol23, name="2bs3acc"),
    path('2bs7jrs/', views.bsol27, name="2bs7acc"),
    path('2bs15jrs/', views.bsol215, name="2bs15acc"),
    # **********************************************************************************************************
    path('sa24h/', views.asol1,name="asacc"),
    path('sa3jrs/', views.asol3,name="as3acc"),
    path('sa7jrs/', views.asol7,name="as7acc"),
    path('sa15jrs/', views.asol15,name="as15acc"),

    path('sph24h/', views.phsol1,name="phsacc"),
    path('sph3jrs/', views.phsol3,name="phs3acc"),
    path('sph7jrs/', views.phsol7,name="phs7acc"),
    path('sph15jrs/', views.phsol15,name="phs15acc"),

    path('sp24h/', views.psol1,name="psacc"),
    path('sp3jrs/', views.psol3,name="ps3acc"),
    path('sp7jrs/', views.psol7,name="ps7acc"),
    path('sp15jrs/', views.psol15,name="ps15acc"),

    path('snpkb24h/', views.npkbsol1,name="npkbsacc"),
    path('snpkb3jrs/', views.npkbsol3,name="npkbs3acc"),
    path('snpkb7jrs/', views.npkbsol7,name="npkbs7acc"),
    path('snpkbt15jrs/', views.npkbsol15,name="npkbs15acc"),
]

