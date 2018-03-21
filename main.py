import scraper as sc
import mail
import face
import time


def kreni(url,price,oib,maddr,fdata):
    i=0
    msg='Ovo je novo:\n '
    flag=0

    oglasi=[]
    for item in url:
        #print i,price[i]
        try:
            oglasi=sc.getOglasi(item,price[i])
        except:
            pass
        i=i+1
        for ogl in oglasi:
            if ogl.oib not in oib:
                msg=msg + ogl.ime + '\n'  + str(ogl.cijena) +'\n' + ogl.link +'\n\n\n'
                oib.append(ogl.oib)
                flag=1
    if flag==1:
        flag=0
        print msg
        #print "radim"
        #**********************************************************************
        #Maknuti # ispred mail/face.sendMail da bi se slala obavjest tim putem
        #**********************************************************************
        try:
            mail.sendMail(msg,maddr)
        except:
            pass
        try:
            face.sendMail(msg,fdata)
        except:
            pass

    return oib


oib=[]
#***************************************************************************************************************************************************************
# U url ubacujes linkove koje da pregleda
url=['http://www.njuskalo.hr/iphone-7-plus', 'http://www.njuskalo.hr/iphone-7', 'http://www.njuskalo.hr/iphone-se', 'http://www.njuskalo.hr/iphone-6s-plus',
     'http://www.njuskalo.hr/iphone-6-plus', 'http://www.njuskalo.hr/iphone-6s', 'http://www.njuskalo.hr/iphone-6', 'http://www.njuskalo.hr/iphone-5s',
     'http://www.njuskalo.hr/iphone-5c', 'http://www.njuskalo.hr/iphone-5']

#U price ubacujes cijene za svaku kategoriju, moraju biti u istom redosljedu ko i linkovi
price=[3500,3500,1800,1800,1800,1600,1600,700,600,500]


maddr=["user_name@gmail.com","primatelj@gmail.com","sifra"]
#['mail sa kojeg saljes','mail koji prima','sifra od maila sa kojeg saljes']

fdata=["user_name@nesto.nes", "sifra", "ime prijatelja"]
#["mail od fejsa sa kojeg se salje","sifra od fejsa","ime na koje zelite slat"]

#***************************************************************************************************************************************************************

while 0<1:
    oib=kreni(url,price,oib,maddr,fdata)
    time.sleep(300)

