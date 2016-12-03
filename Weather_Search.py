# -*- coding: utf-8 -*-
from httplib2 import Http
from urllib import urlencode
import re
import os
########################################################################################################################
def pogoda_dzis():
    h = Http()
    resp, content = h.request("http://www.twojapogoda.pl/polska/wielkopolskie/poznan")
    data = re.search('<h3 class="underline">Dzi(.*?)</h3>.*?<strong>([0-9]+)</strong>', content, re.DOTALL)
    # print(content)
    return data.group(2)
########################################################################################################################
def pogoda_jutro():
   h = Http()
   resp, content = h.request("http://www.twojapogoda.pl/polska/wielkopolskie/poznan")
   data1=re.search('<h3 class="underline">Jutro</h3>.*?<strong>([0-9]+)</strong>',content,re.DOTALL)
   if data1:
        return (data1.group(1))

########################################################################################################################

print(pogoda_dzis())

print(pogoda_jutro())

########################################################################################################################
