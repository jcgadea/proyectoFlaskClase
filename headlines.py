# -*- coding: utf-8 -*-
from flask import Flask
import feedparser
from flask import render_template
from flask import request
from flask import make_response
import json
import urllib
import urllib2
import datetime
from lxml import etree
import urllib2

app= Flask(__name__)

RSS_FEED = { 'elp':'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
             'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'lav':'http://www.lavanguardia.com/mvc/feed/rss/politica',
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'abc':'http://sevilla.abc.es/rss/feeds/Sevilla_Sevilla.xml',
             'elm':'http://estaticos.elmundo.es/elmundo/rss/portada.xml',
	     'mot':'http://feeds.weblogssl.com/motorpasion',
	     'jpl':'https://www.jpl.nasa.gov/rss/'
}
Titles = {'elp':'El Pais: Ultimas noticas',
          'bbc':'BBC headlines',
          'lav':u'La Vanguardia: Política',
          'cnn':'CNN headlines',
          'abc':'ABC: Sevilla',
          'elm':'El Mundo',
	  'mot':'Motorpasion',
	  'jpl':'Jet Propulsion Laboratory'
}

articles = {}
articles['elp'] = feedparser.parse(RSS_FEED['elp'])['entries'][:1]
articles['bbc'] = feedparser.parse(RSS_FEED['bbc'])['entries'][:1]
articles['lav'] = feedparser.parse(RSS_FEED['lav'])['entries'][:1]
articles['cnn'] = feedparser.parse(RSS_FEED['cnn'])['entries'][:1]
articles['abc'] = feedparser.parse(RSS_FEED['abc'])['entries'][:1]
articles['elm'] = feedparser.parse(RSS_FEED['elm'])['entries'][:1]


ns={"Atom" : "http://www.w3.org/2005/Atom"}
parser=etree.XMLParser()
tree=etree.parse(urllib2.urlopen('https://api.flickr.com/services/feeds/photos_public.gne?tags=tesla'),parser)


@app.route("/")
def get_news():
  return render_template("home.html", articles=articles,titles=Titles)

@app.route("/fotos")
def get_photos():
  return render_template("home1.html", tree=tree)


if __name__ == '__main__':
  app.run(port=5301,debug=True)

