def sendMail(msg,maddr):
    import smtplib
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        fromaddr = maddr[0]
        toaddrs  = maddr[1]
        username = maddr[0]
        password = maddr[2]
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    except:
        pass

