import sys
import os

from KalturaClient import *
from KalturaMetadataClientPlugin import *
import KalturaClientBase
import logging
import urllib
import time
import re
from httplib2 import Http
from urllib import urlencode

import properties

logging.basicConfig(level = logging.WARN,
                    format = '%(asctime)s %(levelname)s %(message)s',
                    stream = sys.stdout)



SETTINGS = {}
properties.load_settings(SETTINGS)

class KalturaLogger(IKalturaLogger):
    def log(self, msg):
        logging.info(msg)

def GetConfig():
    config = KalturaConfiguration(SETTINGS['PARTNER_ID'])
    config.serviceUrl = SETTINGS['SERVICE_URL']
    config.setLogger(KalturaLogger())
    return config

def list_kaltura_ids(clientObj=None):
    if clientObj is None:
        client = auth()
    else:
        client = clientObj
    media_entries = client.media.list().getObjects()
    print "Total Count", client.media.list().getTotalCount()
    media_ids = map(lambda x: x.getId(), media_entries)
    return media_ids

def auth():
    client = KalturaClient(GetConfig())
    ks = client.session.start(SETTINGS['ADMIN_SECRET'], SETTINGS['USER_NAME'], KalturaSessionType.ADMIN, SETTINGS['PARTNER_ID'], 86400, "")
    client.setKs(ks)
    return client

def reencode_profile(media_id, conversion_id, clientObj=None):
    #Todo Separate this out into a decorator
    if clientObj:
        client = clientObj
    else:
        client = KalturaClient(GetConfig())
        ks = client.session.start(SETTINGS['ADMIN_SECRET'], SETTINGS['USER_NAME'], KalturaSessionType.ADMIN, SETTINGS['PARTNER_ID'], 86400, "")
        client.setKs(ks)
    entry = client.media.get(media_id)
    client.media.convert(media_id, conversion_id)

if __name__ == '__main__':
    client = auth()
    kaltura_ids = list_kaltura_ids()
    errors = []
    for kaltura_id in kaltura_ids:
        #if kaltura_id != "0_wwfyuiuj":
        #    continue
        print "Processing ID", kaltura_id
        try:
            reencode_profile(kaltura_id, SETTINGS['ACTION_PROFILE_ID'], client)
        except KalturaClientBase.KalturaException, e:
            if e.code == "ORIGINAL_FLAVOR_ASSET_IS_MISSING":
                logging.warn("Media ID %s Error Code %s Error Message %s"%(kaltura_id, e.code, e.message))
                errors.append((kaltura_id, e.code))
