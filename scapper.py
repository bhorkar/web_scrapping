import glob
import wget

from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
import socket
import wget
import os 

socket.setdefaulttimeout(30)

def main(url, out_folder="./street/", local = 1):
    print url
    soup = bs(open(url))
    #print url
    count = 0;
    for image in soup.findAll("img"):
        #print image
        count = count + 1;
        try: 
          #print image["src"].split(".")[-1]
           
          filename = url.split('/')[2].split('.')[0] +   '_' + str(count) + '_'+'.' + 'jpg'
        except:
          #  print "image not found", 
            continue
        try: 
           wgeturl = 'wget ' + ' -O ' + out_folder + filename +  ' ' +  image['src']
           #print wgeturl
           os.system(wgeturl);
           #wget.download(image['src'])
           continue
        except:
           print "errori1111"
          # print "error11", wgeturl
      #     print "Unexpected error:", sys.exc_info()

        image_url = urlparse.urljoin(url, image['src'])
        try: 
           #print out_folder+filename
           #urlretrieve(image_url,out_folder+filename)
           #wget.download(image_url)
           wgeturl = 'wget ' + ' -O ' + out_folder + filename  + ' ' + image_url
           #print wgeturl
           os.system(wgeturl);
           
        except:
           #print "Unexpected error:", sys.exc_info()
        #except:
           print "error"
          #  pass
 

          


out_folder = "./shop/"
urls = glob.glob(out_folder+'/*.html');

for url in urls:
 print "*****************************************" 
 try:
    main(url, out_folder)
 except:
    print url
    #break
