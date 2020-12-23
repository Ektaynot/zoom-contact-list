import os
dersler={'mat':'','biyo':'','din':'','ing':'','alm':'','fels':'','beden':'','görsel':'','edeb':'','tarih':'','kimya':'','fizik':'',}
def oss(a):
    os.system(a)
cho=int(input("Hangi Ders?\n(1)Matematik\n(2)Edebiyat\n(3)Biyoloji\n(4)İngilizce\n(5)Fizik\n(6)Almanca\n(7)Kimya\n(8)Görsel\n(9)Tarih\n(10)Beden\n(11)Din\n(12)Felsefe\n: "))
if cho==1:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['mat']+'&pwd=xxxxx"')
elif cho==2:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['edeb']+'&pwd=xxxxx"')
elif cho==3:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['biyo']+'&pwd=xxxxx"')
elif cho==4:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['ing']+'&pwd=xxxxx"')
elif cho==5:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['fizik']+'&pwd=xxxxx"')
elif cho==6:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['alm']+'&pwd=xxxxx"')
elif cho==7:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['kimya']+'&pwd=xxxxx"')
elif cho==8:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['görsel']+'&pwd=xxxxx"')
elif cho==9:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['tarih']+'&pwd=xxxxx"')
elif cho==10:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['beden']+'&pwd=xxxxx"')
elif cho==11:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['din']+'&pwd=xxxxx"')
elif cho==12:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler['fels']+'&pwd=xxxxx"')
