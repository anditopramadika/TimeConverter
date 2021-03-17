#IMPORT MATH UNTUK FLOOR
import math

def timeConverter():
    #INPUT SECONDS
    seconds = input('Masukkan detik : ')

    #CONVERT SECONDS KE HOURS, MINUTES, SECONDS dengan MOD
    b = math.floor(int(seconds)/3600)
    c = math.floor((int(seconds)%3600)/60)
    d = math.floor(((int(seconds)%3600)%60)/1)

    #PRINT HASIL
    if int(seconds) > 0 and int(seconds) <360000 :
        print(b,':',c,':',d,)
    elif int(seconds) > 359999 :
        print('Invalid Input!')
    elif int(seconds) <= 0:
        print('Invalid Input!')

timeConverter()