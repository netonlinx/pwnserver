#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import getopt
import os
from prettytable import PrettyTable

#PATH
path = os.getcwd()
cache = (path+'/cache')


opts,args = getopt.getopt(sys.argv[1:],'-h-v-t:-m:-c',['help','version','target','autoscan','clean','module','allpoc'])
for opt_name,opt_value in opts:

  if opt_name in ('-h','--help'):
    print(" [+] Usage: python3 pwnserver.py [options]\n")
    print(" [+] Options:")
    print("\t  -h,--help            Show  help message")
    print("\t  -v,--version         Show program's version number")
    print("\t  -t,--target          Set scan target")
    print("\t  --autoscan           Execution scanner")
    print("\t  -c,--clean           Clean up the cache files generated by the program")
    print("\t  -m,--module          Specified module scan")

    exit()

  if opt_name == '-w':
    print("save")
    exit()

  if opt_name in ('-v','--version'):

    print(' [+] version:1.0.2')
    exit()

  if opt_name in ('-t','--target'):
       target = (sys.argv[2])
       with open(cache+'/url.cache', 'w') as f:
          f.write(target)
       print("[+]",target)
       exit()

  if opt_name in ('--autoscan'):
       from plugins import autoscan
       exit()


  if opt_name in ('-c','--clean'):
       print(" [+] The cache file has been cleaned up.")
       os.system("rm -rf *.log && rm -rf cache/*")
       exit()

  if opt_name in ('-m','--module'):
       module = (sys.argv[2])
       print( ' [+] The module you choose is:',module)
       exit()

  if opt_name in ('--allpoc'):
      table = PrettyTable(['Serial number', 'Service', 'Number of POC', 'Date added'])
      table.add_row(['1', 'httpd', '0', 'December 30,2020'])
      table.add_row(['2','discuz','0','December 30,2020'])
      print(table)





       #t = PrettyTable(['Serial number','Service', 'Number of POC','Date added',''])
       #t.add_row(['1','httpd', '10' , 'December 30, 2020'])
       #t.add_row(['fastjson', 19])
       #print(t)
'''

       t.add_row(['flask', 19])
       t.add_row(['influxdb', 19])
       t.add_row(['jupyter', 19])
       t.add_row(['mongo', 19])
       t.add_row(['ofbiz', 19])
       t.add_row(['phpmyadmin', 19])
       t.add_row(['samba', 19])
       t.add_row(['django', 19])
       t.add_row(['gitea', 19])
       t.add_row(['java', 19])
       t.add_row(['jenkins', 19])
       t.add_row(['mysql', 19])
       t.add_row(['openssh', 19])
       t.add_row(['postgres', 19])
       t.add_row(['shiro', 19])
       t.add_row(['thinkphp', 19])
       t.add_row(['durpal', 19])
       t.add_row(['gitlab', 19])
       t.add_row(['jboss', 19])
       t.add_row(['libssh', 19])
       t.add_row(['nexus', 19])
       t.add_row(['openssl', 19])
       t.add_row(['redis', 19])
       t.add_row(['solr', 19])
       t.add_row(['tomcat', 19])
       t.add_row(['joomla', 19])
       t.add_row(['log4j', 19])
       t.add_row(['nginx', 19])
       t.add_row(['phpmailer', 19])
       t.add_row(['rsync', 19])
       t.add_row(['spring', 19])
       t.add_row(['weblogic', 19])
'''
       #print(t)
       #exit()

