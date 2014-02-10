__author__ = 'Tramel Jones'
"""
2014
RSS Reader created with the intention of viewing Valve Software blog posts and other dev blogs with RSS.
"""

import feedparser.feedparser
d = feedparser.parse("http://blogs.valvesoftware.com/feed/")

for item in d.entries:
    print(item.link)
