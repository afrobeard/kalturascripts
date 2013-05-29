import os;

DEFAULT_KALTURA_PATH = "kalturahost.com"
DEFAULT_PARTNER_ID = "10"
DEFAULT_ADMIN_SECRET = "asfasfasfasfasfasdfasfasdfasdf"
DEFAULT_SECRET = "asfasdfasfasfasfdasfd"
DEFAULT_USER_NAME = "xyz@pqr.com"
DEFAULT_ACTION_PROFILE_ID = 5 #ProfileID to Apply

def load_settings(SETTINGS):
    SETTINGS['KALTURA_PATH'] = os.environ.get('KALTURA_PATH', DEFAULT_KALTURA_PATH)
    SETTINGS['PARTNER_ID'] =  int(os.environ.get('PARTNER_ID', DEFAULT_PARTNER_ID))
    SETTINGS['SERVICE_URL'] = "http://" + os.environ.get('KALTURA_PATH', DEFAULT_KALTURA_PATH)
    SETTINGS['ADMIN_SECRET'] = os.environ.get('ADMIN_SECRET', DEFAULT_ADMIN_SECRET)
    SETTINGS['SECRET'] = os.environ.get('SECRET', DEFAULT_SECRET)
    SETTINGS['USER_NAME'] =  os.environ.get('USER_NAME', DEFAULT_USER_NAME)
    SETTINGS['ACTION_PROFILE_ID'] =  os.environ.get('ACTION_PROFILE_ID', DEFAULT_ACTION_PROFILE_ID)
