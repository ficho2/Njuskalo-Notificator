def kreni(url,price,oib):
    import scraper as sc
    import mail
    oib=[]
    i=0
    msg='Ovo je novo:\n '
    flag=1

    oglasi=[]
    for item in url:
        print i,price[i]
        oglasi=sc.getOglasi(item,price[i])
        i=i+1
        for ogl in oglasi:
            if ogl.oib not in oib:
                msg=msg + ogl.ime + '\n'  + str(ogl.cijena) +'\n' + ogl.link +'\n\n\n'
                oib.append(ogl.oib)
                flag=1
    if flag==1:
        flag=0
        print msg
        mail.sendMail(msg)

    return oib
