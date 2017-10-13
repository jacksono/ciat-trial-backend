"""Module to create the models for the app."""

from inm import db, JsonEncodedDict


class Observation(db.Model):
    """Maps bucketlists table which contains bucketlist inforamtion."""

    id = db.Column(db.Integer, primary_key=True)
    plot_num = db.Column(db.Integer, nullable=False)
    combination = db.Column(JsonEncodedDict)
    _2004 = db.Column(JsonEncodedDict)
    _2005 = db.Column(JsonEncodedDict)
    _2006 = db.Column(JsonEncodedDict)
    _2007 = db.Column(JsonEncodedDict)
    _2008 = db.Column(JsonEncodedDict)
    _2009 = db.Column(JsonEncodedDict)
    _2010 = db.Column(JsonEncodedDict)
    _2011 = db.Column(JsonEncodedDict)
    _2012 = db.Column(JsonEncodedDict)
    _2013 = db.Column(JsonEncodedDict)
    _2014 = db.Column(JsonEncodedDict)
    _2015 = db.Column(JsonEncodedDict)
