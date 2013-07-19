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

def download():
    'Download all of the files so we have a local cache.'
    # Set the cookie.
    s = session()
    s.get('http://www.amlegal.com/nxt/gateway.dll?f=templates&fn=default.htm&vid=amlegal:sanfrancisco_ca')

    # Get the list of codes.
    html = get(s, 'http://www.amlegal.com/nxt/gateway.dll/California/sfbuilding/cityandcountyofsanfranciscobuildingindus?f=templates$fn=document-frame.htm$3.0')
    for _, code_url in lib.codes(html):
        print code_url
        for _, _, article_url in lib.articles(get(s, code_url)):
            print article_url
            get(s, article_url)

def index():
    'Build index.json.'

    out = {"sections":[],"titles":[]}

    # Set the cookie.
    s = session()
    s.get('http://www.amlegal.com/nxt/gateway.dll?f=templates&fn=default.htm&vid=amlegal:sanfrancisco_ca')

    # Get the list of codes.
    html = get(s, 'http://www.amlegal.com/nxt/gateway.dll/California/sfbuilding/cityandcountyofsanfranciscobuildingindus?f=templates$fn=document-frame.htm$3.0')
    for (code_number, (code_name, code_url)) in enumerate(lib.codes(html)):
        out['titles'].append([code_number, code_name])
        for code_number, code_, article_url in lib.articles(get(s, code_url)):
            print article_url
            get(s, article_url)



# Set cookie.
s = session()
s.get('http://www.amlegal.com/nxt/gateway.dll?f=templates&fn=default.htm&vid=amlegal:sanfrancisco_ca')

# Get the list of codes.
html = get(s, 'http://www.amlegal.com/nxt/gateway.dll/?fn=altmain-nf.htm$f=templates$3.0') # Enter the mobile site
html = get(s, html.xpath('//*[text()="Table of Contents"]/@href')[0]) # Click to the table of contents
html = get(s, html.xpath('//table[position()=3]/descendant::a/@href')[0]) # Click on california
for code_url in html.xpath('//table[position()=4]/descendant::a/@href'):
    code_html = get(s, code_url)
    for article_url in code_html.xpath('//table[position()=4]/descendant::a/@href'):
        article_html = get(s, article_url)
        break
    break
