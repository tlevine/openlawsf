import lxml.html
import nose.tools as n

import lib

html = lxml.html.parse('charter.html')
observed = lib.articles(html)

def test_article_count():
    'There should be 30 links.'
    n.assert_equal(len(observed), 30)

def test_folder():
    'Folders of sections should be recognized appropriately.'
    n.assert_equal(observed[4]['type'], 'folder')

def test_page():
    'Pages of introductions and whatnot should be recognized appropriately.'
    n.assert_equal(observed[1]['type'], 'page')

def test_data():
    expected = {
        'type': 'folder',
        'expand_link': 'http://www.amlegal.com/nxt/gateway.dll?f=templates$fn=altmain-nf-contents.htm$cp=California%2Fcharter_sf%2Farticlexiemployer-employeerelationssyste$tt=altmain-nf.htm$3.0',
        'page_link': 'http://www.amlegal.com/nxt/gateway.dll/California/charter_sf/articlexiemployer-employeerelationssyste?fn=altmain-nf.htm$f=templates$3.0',
        'name': 'ARTICLE XI: EMPLOYER-EMPLOYEE RELATIONS SYSTEM',
    }
    n.assert_dict_equal(observed, expected)
