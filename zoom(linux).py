import os
import sys
dersler={'m':'zzzzz','b':'zzzzz','d':'zzzzz','i':'zzzzz','a':'zzzzz','fe':'zzzzz','be':'zzzzz','g':'zzzzz','e':'zzzzz','t':'zzzzz','k':'zzzzz','f':'zzzzz',}
dersler2={'mat':'zzzzz','biyo':'zzzzz','din':'zzzzz','ing':'zzzzz','alm':'zzzzz','fels':'zzzzz','beden':'zzzzz','zzzzz':'zzzzz','edeb':'zzzzz','tarih':'zzzzz','kimya':'zzzzz','fizik':'zzzzz',}
cho =''
def oss(a):
    os.system(a)
if len(sys.argv) == 1:
    cho=str(input("Hangi Ders?\n[M]atematik\n[E]debiyat\n[B]iyoloji\n[İ]ngilizce\n[F]izik\n[A]lmanca\n[K]imya\n[G]örsel\n[T]arih\n[Be]den\n[D]in\n[Fe]lsefe\n: ")).lower()
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler[cho]+'&pwd=xxxxxx"')
if len(sys.argv) != 1:
    oss('firefox "zoommtg://zoom.us/join?confno='+dersler2[sys.argv[-1]]+'&pwd=xxxxxx"')
