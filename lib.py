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
