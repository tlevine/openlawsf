Open San Francisco's law!

It's all here.
http://www.amlegal.com/library/ca/sfrancisco.shtml

The mobile version might be easier.
http://www.amlegal.com/nxt/gateway.dll/?fn=altmain-nf.htm$f=templates$3.0

It could go into a site like this.

* http://chicagocouncilmatic.org/
* http://marylandcode.org/

But for now, it's just gonna look like [OpenLaw DC](http://dccode.org/).


## Schema of the DC code browser
I'm fitting this into OpenLaw DC's schema. It's not documented,
so I document it here.

### Directory structure
The code is in JSON files and is accessed via AJAX requests.
There are two index files.

* [`/browser/index.json`](schema/index.json)
* [`/browser/sids.json`](schema/sids.json)

And there are a bunch of section files.

* [`/browser/sections/:section.json`](schema/4-102.json)

A section might be "[4-102](schema/4-102.json)"

### `index.json`
`index.json` has a list of titles and a list of sections.
Each title or section is a two-element list of the number
followed by the heading.

    {
      "sections":[
        ["1-101","Territorial area."],
        ["1-102","District created body corporate for municipal purposes."],
        ["1-103","Officers of corporation."],
        ...
      ],
      "titles":[
        ["1","Government Organization"],
        ["2","Government Administration"],
        ["3","District of Columbia Boards and Commissions"],
        ...
      ]
    }

I have a feeling that a DC "section" is equivalent to an
SF "section" and that a DC "title" is equivalent to a SF "code".

### `sids.json`
`sids.json` to be a list of most of the sections in `index.json`.
All sections in `index.json` are contained within `sids.json`, but
not vice-versa.

```python
sids = json.load(open('schema/sids.json'))
index = json.load(open('schema/index.json'))
print set(map(tuple, sids)).difference(set(map(tuple, index['sections'])))
print set(map(tuple, index['sections'])).difference(set(map(tuple, sids)))
```

### `:section.json`
This file is named after one of the sections in `sids.json`, and it looks like this.

    { "text":"",
      "historical":"Omission of text\n\nThe provisions of former § 4-102 have been omitted as obsolete, the Board referred to herein having been abolished.\n\nBoard of Public Welfare abolished\n\nThe Board of Public Welfare was abolished and the functions thereof transferred to the Board of Commissioners of the District of Columbia by Reorganization Plan No. 5 of 1952. Reorganization Order No. 58, as amended, redesignated as Organization Order No. 140 and amended, established, under the direction and control of a Commissioner, a Department of Public Welfare, headed by a Director with the purpose of planning, implementing, and directing public welfare programs. Reorganization Order No. 58 provided that the previously existing Board of Public Welfare would be abolished. That Order also transferred specified functions of the former Board to the Department of Public Health and the Department of Public Welfare. Functions of the Department of Public Welfare and of the Department of Public Health, as set forth in Organization Order Nos. 140 and 141, respectively, were transferred to the Department of Human Resources by Commissioner's Order No. 69-96, dated March 7, 1969, as amended by Commissioner's Order No. 70-83, dated March 6, 1970. The Department of Human Resources was replaced by the Department of Human Services by Reorganization Plan No. 2 of 1979, dated February 21, 1980.\n\nDC CODE § 4-102\n\nCurrent through December 11, 2012",
      "credits":"",
      "sections":[],
      "division":{
        "identifier":"I",
        "text":"Government of District."
      },
      "title":{
        "identifier":"4",
        "text":"Public Care Systems. (Refs & Annos)"
      },
      "chapter":{
        "identifier":"1",
        "text":"Public Welfare Supervision. (Refs & Annos)"
      },
      "heading":{
        "title":"4",
        "chaptersection":"102",
        "identifier":"4-102",
        "catch_text":"Board of Public Welfare--Created; successor to abolished Boards; employees transferred. [Omitted]"
      }
    }

I haven't yet figured out what all of that means.

## Changes in Schema for SF
In DC, the hierarchy is title, section, 
