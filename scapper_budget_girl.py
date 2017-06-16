
# coding: utf-8

# In[2]:

# The standard library modules
import os
import sys

# The wget module
import wget

# The BeautifulSoup module
from bs4 import BeautifulSoup
import re

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import stem
from stem import Signal
from stem.control import Controller
from stem.connection import connect
import time

executable_path='/home/bhorkar/node_modules/phantomjs-prebuilt/lib/phantom/bin//phantomjs'


# In[10]:

'''
Python script to connect to Tor via Stem and Privoxy, requesting a new connection (hence a new IP as well) as desired.
'''

import stem
import stem.connection

import time
import urllib2

from stem import Signal
from stem.control import Controller
import random

# initialize some HTTP headers
# for later usage in URL requests
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent}

# initialize some
# holding variables
global oldIP
oldIP = "0.0.0.0"
newIP = "0.0.0.0"

# how many IP addresses
# through which to iterate?
nbrOfIpAddresses = 1

# seconds between
# IP address checks
secondsBetweenChecks = 2

# request a URL 
def request(url):
    # communicate with TOR via a local proxy (privoxy)
    def _set_urlproxy():
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)

    # request a URL
    # via the proxy
    _set_urlproxy()
    request=urllib2.Request(url, None, headers)
    return urllib2.urlopen(request).read()

# signal TOR for a new connection 
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password = 'garbage123')
        controller.signal(Signal.NEWNYM)
        controller.close()
        


ua_list = []
with open('ualist.txt') as ua:
    for line in ua:
        ua_list.append(line.strip())
#print ua_list
ua_list_len = len(ua_list)

    

from TorCtl import TorCtl
import urllib2
 
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent}
 
def request(url):
    def _set_urlproxy():
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
    _set_urlproxy()
    ua = ua_list[random.randint(0,ua_list_len-1)]
    headers={'User-Agent': ua}
    request=urllib2.Request(url, None, headers)
    return urllib2.urlopen(request).read()
 
def renew_connection():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="garbage123")
    conn.send_signal("NEWNYM")
    conn.close()
 
for i in range(0, 2):
    renew_connection()
    print request("http://icanhazip.com/")



# In[13]:


# cycle through
# the specified number
# of IP addresses via TOR 
def changeip(newIP):
 for i in range(0, nbrOfIpAddresses):

    # if it's the first pass
    if newIP == "0.0.0.0":
        # renew the TOR connection
        oldIP = newIP
        renew_connection()
        # obtain the "new" IP address
        newIP = request("http://icanhazip.com/")
    # otherwise
    else:
        # remember the
        # "new" IP address
        # as the "old" IP address
        oldIP = newIP
        # refresh the TOR connection
        renew_connection()
        # obtain the "new" IP address
        newIP = request("http://icanhazip.com/")
        print newIP

    # zero the 
    # elapsed seconds    
    seconds = 0

    # loop until the "new" IP address
    # is different than the "old" IP address,
    # as it may take the TOR network some
    # time to effect a different IP address
    while oldIP == newIP:
        # sleep this thread
        # for the specified duration
        time.sleep(secondsBetweenChecks)
        # track the elapsed seconds
        seconds += secondsBetweenChecks
        # obtain the current IP address
        newIP = request("http://icanhazip.com/")
        if (seconds > 20):
            break;
        # signal that the program is still awaiting a different IP address
        #print ("%d seconds elapsed awaiting a different IP address." % seconds)
    # output the
    # new IP address
 #   print ("")
    print ("newIP: %s" % newIP)
    return 


# In[14]:

newIP = changeip(newIP);


# In[ ]:




# In[ ]:





# In[15]:

link = "http://stealherstyle.net/" # load the web page

driver = webdriver.PhantomJS(executable_path = executable_path)
# it takes forever to load the page, therefore we are setting a threshold
driver.set_page_load_timeout(500)







 

# In[20]:

#print shop_urls 
import pickle
with open('objs.pickle_thebudgetbabe','r') as f:
    [street_urls,shop_urls, shop_urls1] = pickle.load(f);

print "number of sttreet urls {} {} ".format(len(street_urls), len(shop_urls))

# In[ ]:

print (2)


# In[21]:

from time import sleep 
from multiprocessing import Pool


def job(url,directory, count):
  try: 
    print count
    driver = webdriver.PhantomJS(executable_path = executable_path)
    driver.get(url[2]);
    slp_flt =   random.uniform(3,6)                                                                                 
   # print 'sleeping',slp_flt                                                                                        
    sleep(slp_flt)                                                                                                                                                                                                                                          
    pgsrc  = driver.page_source 
    soup = BeautifulSoup(pgsrc, 'html.parser')
    fname= directory + str(url[0]) + '_'  + str(url[1]) + '_' +  "_image-gallery.html" 
    outf = open(fname,"w")           
    if len(pgsrc.encode('utf-8')) > 1500:
    	outf.write(pgsrc.encode('utf-8'))
    else:
         print pgsrc.encode('utf-8');
    driver.close();
    print fname 
  except:
    pass;



# In[ ]:

import multiprocessing as mp

from functools import partial
pool = Pool()



# In[ ]:

print "starting with street" 

directory = './street_2/'
if not os.path.exists(directory):
    os.makedirs(directory)
count = 0;
for url in street_urls:
   
    count = count + 1;
    pool.apply_async(job, args = (url,directory,count));
   # job(url,directory)
#pool.map(  partial(job, directory=directory), street_urls)

pool.close()
pool.join()

pool = Pool()
#print "done with street" 
directory = './shop_2/'
if not os.path.exists(directory):
    os.makedirs(directory)

print "len shop", len(shop_urls)
count = 0;
for url in shop_urls:
    count = count + 1;
#    if count < 3000:
 #      continue; # they are already done
    print count;
    pool.apply_async(job, args = (url,directory,count));
pool.close()
pool.join()

    #job(url,directory)
#pool.map( partial(job,directory=directory), shop_urls)
print "done with shop" 

# In[ ]:

import glob
import wget

from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
import socket


def main(url, out_folder="./shop/", ct = 0):
    socket.setdefaulttimeout(10)
    print ct;
    """Downloads all the images at 'url' """
    soup = bs(open(url))
    count = 0;
    for image in soup.findAll("img"):
       # print image
        count = count  + 1;
        try: 
            
          filename = url.split('/')[2].split('.')[0] + '_' + str(count) + '_' + '.'+image["src"].split(".")[-1]
         # print filename
        except:
            print "image not found", 
            continue
        image_url = urlparse.urljoin(url, image['src'])
        #try: 
        #print image_url
        try: 
           #wget.download(image_url);
           urlretrieve(image_url,out_folder+filename)
        except:
            pass
   

          

            


# In[ ]:


out_folder = "./shop_2/"
urls = glob.glob(directory+'/*.html');
#print urls[0]
#main(urls[0], out_folder)
#main(urls[1], out_folder)
#main(urls[2], out_folder)

#pool = Pool();
pool = Pool()
count = 0;
for url in urls:
    count = count + 1;
    print count
    pool.apply_async(main, args = (url,out_folder,count));
  #  main(url, out_folder)


# In[ ]:
pool.close()
pool.join()



pool = Pool()


# In[ ]:


out_folder = "./street_2/"
urls = glob.glob(directory+'/*.html');
count = 0
for url in urls:
    count = count + 1;
    print count
    pool.apply_async(main, args = (url,out_folder,count));
  #  main(url, out_folder)


#pool = Pool()
#pool.map(main, urls)
#for i in xrange(1, len(urls)):
#    main(urls[i], out_folder)


# In[ ]:




# In[ ]:




# In[ ]:




# In[11]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[33]:




# In[ ]:




# In[ ]:




# In[89]:





# In[ ]:




# In[90]:

#for img in soup2.findAll('a href'):
#    print img


# In[ ]:




# In[92]:

#import re
#urls = re.findall(r'href=[\'"]?(http://rstyle.me[^\'" >]+)', soup2.prettify())
#print ', '.join(urls)


# In[93]:




# In[ ]:




# In[ ]:




# In[ ]:



