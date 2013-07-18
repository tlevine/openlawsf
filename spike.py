#!/usr/bin/env python2

from requests import session

def factory():
    s = session()
    s.get('http://www.amlegal.com/nxt/gateway.dll?f=templates&fn=default.htm&vid=amlegal:sanfrancisco_ca')
    def cache(self, url):
        try:
            os.mkdir('gateway')
        except OSError:
            pass
        filename = os.path.join('gateway', url.replace('http://www.amlegal.com/nxt/gateway.dll?', ''))
        if os.path.isfile(filename):
            return open(filename).read()
        else:
            handle = open(filename, 'w')
            r = self.get(url)
            handle.write(r.text)
            handle.close()
            return r.text
    s.cache = cache
    return s

s = factory()
s.cache('http://www.amlegal.com/nxt/gateway.dll/California/administrative/administrativecode')
s.cache('http://www.amlegal.com/nxt/gateway.dll/California/administrative/chapter3budgetprocedures')
