def codes(html):
    codeList = html.cssselect('p.CodeList > a')
    print codeList
    return [(a.xpath('text()')[0], a.xpath('@href')[0]) for a in codeList]
