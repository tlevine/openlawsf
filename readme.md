Open San Francisco's law!

It's all here.
http://www.amlegal.com/library/ca/sfrancisco.shtml

It could go into a site like this.

* http://chicagocouncilmatic.org/
* http://marylandcode.org/

But for now, it's just gonna look like [OpenLaw DC](http://dccode.org/).


## Schema
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
