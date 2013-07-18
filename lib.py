from lxml.html import tostring

def codes(html):
    'Extract the code links.'
    codeList = html.cssselect('p.CodeList > a')
    return [(a.xpath('text()')[0], a.xpath('@href')[0]) for a in codeList]

def articles(html):
    'Extract the article links.'
    trs = html.xpath('//tr[descendant::p[@class="ChapAn"]]')
    def _features(tr):
        number = tr.xpath('td[position()=1]/p')[0].text_content().strip()
        href = tr.xpath('td[position()=1]/p/a/@href')[0]
        title = tr.xpath('td[position()=2]/p/a/text()')[0]
        return (number, title, href)
    return map(_features, trs)

def sections(html):
    trs = html.xpath('//tr[descendant::p[@class="ChapAn"]]')
    def _features(tr):
        number = tr.xpath('td[position()=1]/p')[0].text_content().strip()
        href = tr.xpath('td[position()=1]/p/a/@href')[0]
        title = tr.xpath('td[position()=2]/p/text()')[0]
        return (number, title, href.split('#')[1])
    return map(_features, trs)

def section_text(html, section_hash):
    text = '<section>'
    elements = html.xpath('//a[@name="JD_515.01"]/following-sibling::p[position()=1]/following-sibling::*')
    for e in elements:
        if e.tag == 'a' and len(e.xpath('@name')) > 0:
            text += tostring(e)
            break
    text += '</section>'
    print text
    return text
