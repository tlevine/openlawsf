#!/usr/bin/env python2
import os, re
from requests import session
from lxml.html import fromstring

import lib

def get(sess, url, cachedir = 'downloads'):
    'Download a web file, or load the version from disk.'
    tmp1 = url.replace('http://', '')
    tmp2 = [cachedir] + filter(None, tmp1.split('/'))
    local_file = os.path.join(*tmp2)
    local_dir = os.path.join(*tmp2[:-1])
    del(tmp1)
    del(tmp2)

    # mkdir -p
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Download
    if not os.path.exists(local_file):
       print 'Downloading and saving %s' % url
       r = sess.get(url)
       handle = open(local_file, 'w')
       handle.write(r.text.encode('utf-8'))
       handle.close()

    html = fromstring(open(local_file).read().decode('utf-8'))
    html.make_links_absolute(url)
    return html

# Set the cookie.
s = session()
s.get('http://www.amlegal.com/nxt/gateway.dll?f=templates&fn=default.htm&vid=amlegal:sanfrancisco_ca')

# Get the list of codes.
html = get(s, 'http://www.amlegal.com/nxt/gateway.dll/California/sfbuilding/cityandcountyofsanfranciscobuildingindus?f=templates$fn=document-frame.htm$3.0')
for name, url in lib.codes(html):
    get(s, url)
