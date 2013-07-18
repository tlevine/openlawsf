#!/usr/bin/env python2
import os, re
from requests import session

def set_cookie():
    s = session()
    s.get('http://www.amlegal.com/nxt/gateway.dll?f=templates&fn=default.htm&vid=amlegal:sanfrancisco_ca')
    return s

def cache(s, url):
    'Given a session, get or cache the url.'
    try:
        os.mkdir('gateway')
    except OSError:
        pass
    filename = os.path.join('gateway', re.sub(r'', '', url))

    print filename
    if os.path.isfile(filename):
        return open(filename).read()
    else:
        handle = open(filename, 'w')
        r = s.get(url)
        handle.write(r.text)
        handle.close()
        return r.text

def get(url, cachedir = '.'):
    'Download a web file, or load the version from disk.'
    tmp1 = url.replace('http://www.amlegal.com/nxt/gateway.dll/California/', '')
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
       urlretrieve(url, filename = local_file)
       randomsleep(1, 0.5)

    return open(local_file).read()

s = set_cookie()
cache(s, 'http://www.amlegal.com/nxt/gateway.dll/California/administrative/administrativecode')
cache(s, 'http://www.amlegal.com/nxt/gateway.dll/California/administrative/chapter3budgetprocedures')
