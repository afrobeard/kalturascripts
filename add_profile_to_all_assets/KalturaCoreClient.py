from KalturaClientBase import *

API_VERSION = '3.1.1'

########## enums ##########
class KalturaAccessControlOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAdminUserOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaApiActionPermissionItemOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaApiParameterPermissionItemAction:
    READ = "read"
    UPDATE = "update"
    INSERT = "insert"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaApiParameterPermissionItemOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAssetType:
    FLAVOR = "1"
    THUMBNAIL = "2"
    DOCUMENT = "document.Document"
    SWF = "document.SWF"
    PDF = "document.PDF"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaAudioCodec:
    NONE = ""
    MP3 = "mp3"
    AAC = "aac"
    VORBIS = "vorbis"
    WMA = "wma"
    COPY = "copy"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBaseEntryOrderBy:
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBaseJobOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBaseSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobErrorTypes:
    APP = 0
    RUNTIME = 1
    HTTP = 2
    CURL = 3
    KALTURA_API = 4
    KALTURA_CLIENT = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobOrderBy:
    STATUS_ASC = "+status"
    STATUS_DESC = "-status"
    CHECK_AGAIN_TIMEOUT_ASC = "+checkAgainTimeout"
    CHECK_AGAIN_TIMEOUT_DESC = "-checkAgainTimeout"
    PROGRESS_ASC = "+progress"
    PROGRESS_DESC = "-progress"
    UPDATES_COUNT_ASC = "+updatesCount"
    UPDATES_COUNT_DESC = "-updatesCount"
    PRIORITY_ASC = "+priority"
    PRIORITY_DESC = "-priority"
    QUEUE_TIME_ASC = "+queueTime"
    QUEUE_TIME_DESC = "-queueTime"
    FINISH_TIME_ASC = "+finishTime"
    FINISH_TIME_DESC = "-finishTime"
    FILE_SIZE_ASC = "+fileSize"
    FILE_SIZE_DESC = "-fileSize"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobStatus:
    PENDING = 0
    QUEUED = 1
    PROCESSING = 2
    PROCESSED = 3
    MOVEFILE = 4
    FINISHED = 5
    FAILED = 6
    ABORTED = 7
    ALMOST_DONE = 8
    RETRY = 9
    FATAL = 10
    DONT_PROCESS = 11

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBatchJobType:
    CONVERT = "0"
    IMPORT = "1"
    DELETE = "2"
    FLATTEN = "3"
    BULKUPLOAD = "4"
    DVDCREATOR = "5"
    DOWNLOAD = "6"
    OOCONVERT = "7"
    CONVERT_PROFILE = "10"
    POSTCONVERT = "11"
    PULL = "12"
    REMOTE_CONVERT = "13"
    EXTRACT_MEDIA = "14"
    MAIL = "15"
    NOTIFICATION = "16"
    CLEANUP = "17"
    SCHEDULER_HELPER = "18"
    BULKDOWNLOAD = "19"
    DB_CLEANUP = "20"
    PROVISION_PROVIDE = "21"
    CONVERT_COLLECTION = "22"
    STORAGE_EXPORT = "23"
    PROVISION_DELETE = "24"
    STORAGE_DELETE = "25"
    EMAIL_INGESTION = "26"
    METADATA_IMPORT = "27"
    METADATA_TRANSFORM = "28"
    FILESYNC_IMPORT = "29"
    CAPTURE_THUMB = "30"
    VIRUS_SCAN = "virusScan.VirusScan"
    DISTRIBUTION_SUBMIT = "contentDistribution.DistributionSubmit"
    DISTRIBUTION_UPDATE = "contentDistribution.DistributionUpdate"
    DISTRIBUTION_DELETE = "contentDistribution.DistributionDelete"
    DISTRIBUTION_FETCH_REPORT = "contentDistribution.DistributionFetchReport"
    DISTRIBUTION_ENABLE = "contentDistribution.DistributionEnable"
    DISTRIBUTION_DISABLE = "contentDistribution.DistributionDisable"
    DISTRIBUTION_SYNC = "contentDistribution.DistributionSync"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaBitRateMode:
    CBR = 1
    VBR = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaCategoryOrderBy:
    DEPTH_ASC = "+depth"
    DEPTH_DESC = "-depth"
    FULL_NAME_ASC = "+fullName"
    FULL_NAME_DESC = "-fullName"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaCommercialUseType:
    COMMERCIAL_USE = 1
    NON_COMMERCIAL_USE = 0

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaContainerFormat:
    FLV = "flv"
    MP4 = "mp4"
    AVI = "avi"
    MOV = "mov"
    MP3 = "mp3"
    _3GP = "3gp"
    OGG = "ogg"
    WMV = "wmv"
    WMA = "wma"
    ISMV = "ismv"
    MKV = "mkv"
    WEBM = "webm"
    MPEG = "mpeg"
    MPEGTS = "mpegts"
    APPLEHTTP = "applehttp"
    SWF = "swf"
    PDF = "pdf"
    JPG = "jpg"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandStatus:
    PENDING = 1
    HANDLED = 2
    DONE = 3
    FAILED = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandTargetType:
    DATA_CENTER = 1
    SCHEDULER = 2
    JOB_TYPE = 3
    JOB = 4
    BATCH = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaControlPanelCommandType:
    STOP = 1
    START = 2
    CONFIG = 3
    KILL = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaConversionEngineType:
    KALTURA_COM = "0"
    ON2 = "1"
    FFMPEG = "2"
    MENCODER = "3"
    ENCODING_COM = "4"
    EXPRESSION_ENCODER3 = "5"
    FFMPEG_VP8 = "98"
    FFMPEG_AUX = "99"
    PDF2SWF = "201"
    PDF_CREATOR = "202"
    QUICK_TIME_PLAYER_TOOLS = "quickTimeTools.QuickTimeTools"
    FAST_START = "fastStart.FastStart"
    EXPRESSION_ENCODER = "expressionEncoder.ExpressionEncoder"
    AVIDEMUX = "avidemux.Avidemux"
    SEGMENTER = "segmenter.Segmenter"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaConversionProfileOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaCountryRestrictionType:
    RESTRICT_COUNTRY_LIST = 0
    ALLOW_COUNTRY_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDataEntryOrderBy:
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDirectoryRestrictionType:
    DONT_DISPLAY = 0
    DISPLAY_WITH_LINK = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaDurationType:
    NOT_AVAILABLE = "notavailable"
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEditorType:
    SIMPLE = 1
    ADVANCED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEmailIngestionProfileStatus:
    INACTIVE = 0
    ACTIVE = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryModerationStatus:
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3
    FLAGGED_FOR_REVIEW = 5
    AUTO_APPROVED = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryStatus:
    ERROR_IMPORTING = "-2"
    ERROR_CONVERTING = "-1"
    IMPORT = "0"
    PRECONVERT = "1"
    READY = "2"
    DELETED = "3"
    PENDING = "4"
    MODERATE = "5"
    BLOCKED = "6"
    INFECTED = "virusScan.Infected"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaEntryType:
    AUTOMATIC = "-1"
    MEDIA_CLIP = "1"
    MIX = "2"
    PLAYLIST = "5"
    DATA = "6"
    LIVE_STREAM = "7"
    DOCUMENT = "10"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFileSyncObjectType:
    ENTRY = "1"
    UICONF = "2"
    BATCHJOB = "3"
    FLAVOR_ASSET = "4"
    METADATA = "5"
    METADATA_PROFILE = "6"
    SYNDICATION_FEED = "7"
    GENERIC_DISTRIBUTION_ACTION = "contentDistribution.GenericDistributionAction"
    ENTRY_DISTRIBUTION = "contentDistribution.EntryDistribution"
    DISTRIBUTION_PROFILE = "contentDistribution.DistributionProfile"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorAssetStatus:
    ERROR = -1
    QUEUED = 0
    CONVERTING = 1
    READY = 2
    DELETED = 3
    NOT_APPLICABLE = 4
    TEMP = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGender:
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGenericXsltSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGoogleSyndicationFeedAdultValues:
    YES = "Yes"
    NO = "No"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaGoogleVideoSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaITunesSyndicationFeedAdultValues:
    YES = "yes"
    NO = "no"
    CLEAN = "clean"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaITunesSyndicationFeedCategories:
    ARTS = "Arts"
    ARTS_DESIGN = "Arts/Design"
    ARTS_FASHION_BEAUTY = "Arts/Fashion &amp; Beauty"
    ARTS_FOOD = "Arts/Food"
    ARTS_LITERATURE = "Arts/Literature"
    ARTS_PERFORMING_ARTS = "Arts/Performing Arts"
    ARTS_VISUAL_ARTS = "Arts/Visual Arts"
    BUSINESS = "Business"
    BUSINESS_BUSINESS_NEWS = "Business/Business News"
    BUSINESS_CAREERS = "Business/Careers"
    BUSINESS_INVESTING = "Business/Investing"
    BUSINESS_MANAGEMENT_MARKETING = "Business/Management &amp; Marketing"
    BUSINESS_SHOPPING = "Business/Shopping"
    COMEDY = "Comedy"
    EDUCATION = "Education"
    EDUCATION_TECHNOLOGY = "Education/Education Technology"
    EDUCATION_HIGHER_EDUCATION = "Education/Higher Education"
    EDUCATION_K_12 = "Education/K-12"
    EDUCATION_LANGUAGE_COURSES = "Education/Language Courses"
    EDUCATION_TRAINING = "Education/Training"
    GAMES_HOBBIES = "Games &amp; Hobbies"
    GAMES_HOBBIES_AUTOMOTIVE = "Games &amp; Hobbies/Automotive"
    GAMES_HOBBIES_AVIATION = "Games &amp; Hobbies/Aviation"
    GAMES_HOBBIES_HOBBIES = "Games &amp; Hobbies/Hobbies"
    GAMES_HOBBIES_OTHER_GAMES = "Games &amp; Hobbies/Other Games"
    GAMES_HOBBIES_VIDEO_GAMES = "Games &amp; Hobbies/Video Games"
    GOVERNMENT_ORGANIZATIONS = "Government &amp; Organizations"
    GOVERNMENT_ORGANIZATIONS_LOCAL = "Government &amp; Organizations/Local"
    GOVERNMENT_ORGANIZATIONS_NATIONAL = "Government &amp; Organizations/National"
    GOVERNMENT_ORGANIZATIONS_NON_PROFIT = "Government &amp; Organizations/Non-Profit"
    GOVERNMENT_ORGANIZATIONS_REGIONAL = "Government &amp; Organizations/Regional"
    HEALTH = "Health"
    HEALTH_ALTERNATIVE_HEALTH = "Health/Alternative Health"
    HEALTH_FITNESS_NUTRITION = "Health/Fitness &amp; Nutrition"
    HEALTH_SELF_HELP = "Health/Self-Help"
    HEALTH_SEXUALITY = "Health/Sexuality"
    KIDS_FAMILY = "Kids &amp; Family"
    MUSIC = "Music"
    NEWS_POLITICS = "News &amp; Politics"
    RELIGION_SPIRITUALITY = "Religion &amp; Spirituality"
    RELIGION_SPIRITUALITY_BUDDHISM = "Religion &amp; Spirituality/Buddhism"
    RELIGION_SPIRITUALITY_CHRISTIANITY = "Religion &amp; Spirituality/Christianity"
    RELIGION_SPIRITUALITY_HINDUISM = "Religion &amp; Spirituality/Hinduism"
    RELIGION_SPIRITUALITY_ISLAM = "Religion &amp; Spirituality/Islam"
    RELIGION_SPIRITUALITY_JUDAISM = "Religion &amp; Spirituality/Judaism"
    RELIGION_SPIRITUALITY_OTHER = "Religion &amp; Spirituality/Other"
    RELIGION_SPIRITUALITY_SPIRITUALITY = "Religion &amp; Spirituality/Spirituality"
    SCIENCE_MEDICINE = "Science &amp; Medicine"
    SCIENCE_MEDICINE_MEDICINE = "Science &amp; Medicine/Medicine"
    SCIENCE_MEDICINE_NATURAL_SCIENCES = "Science &amp; Medicine/Natural Sciences"
    SCIENCE_MEDICINE_SOCIAL_SCIENCES = "Science &amp; Medicine/Social Sciences"
    SOCIETY_CULTURE = "Society &amp; Culture"
    SOCIETY_CULTURE_HISTORY = "Society &amp; Culture/History"
    SOCIETY_CULTURE_PERSONAL_JOURNALS = "Society &amp; Culture/Personal Journals"
    SOCIETY_CULTURE_PHILOSOPHY = "Society &amp; Culture/Philosophy"
    SOCIETY_CULTURE_PLACES_TRAVEL = "Society &amp; Culture/Places &amp; Travel"
    SPORTS_RECREATION = "Sports &amp; Recreation"
    SPORTS_RECREATION_AMATEUR = "Sports &amp; Recreation/Amateur"
    SPORTS_RECREATION_COLLEGE_HIGH_SCHOOL = "Sports &amp; Recreation/College &amp; High School"
    SPORTS_RECREATION_OUTDOOR = "Sports &amp; Recreation/Outdoor"
    SPORTS_RECREATION_PROFESSIONAL = "Sports &amp; Recreation/Professional"
    TECHNOLOGY = "Technology"
    TECHNOLOGY_GADGETS = "Technology/Gadgets"
    TECHNOLOGY_TECH_NEWS = "Technology/Tech News"
    TECHNOLOGY_PODCASTING = "Technology/Podcasting"
    TECHNOLOGY_SOFTWARE_HOW_TO = "Technology/Software How-To"
    TV_FILM = "TV &amp; Film"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaITunesSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaIpAddressRestrictionType:
    RESTRICT_LIST = 0
    ALLOW_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLicenseType:
    UNKNOWN = -1
    NONE = 0
    COPYRIGHTED = 1
    PUBLIC_DOMAIN = 2
    CREATIVECOMMONS_ATTRIBUTION = 3
    CREATIVECOMMONS_ATTRIBUTION_SHARE_ALIKE = 4
    CREATIVECOMMONS_ATTRIBUTION_NO_DERIVATIVES = 5
    CREATIVECOMMONS_ATTRIBUTION_NON_COMMERCIAL = 6
    CREATIVECOMMONS_ATTRIBUTION_NON_COMMERCIAL_SHARE_ALIKE = 7
    CREATIVECOMMONS_ATTRIBUTION_NON_COMMERCIAL_NO_DERIVATIVES = 8
    GFDL = 9
    GPL = 10
    AFFERO_GPL = 11
    LGPL = 12
    BSD = 13
    APACHE = 14
    MOZILLA = 15

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLiveStreamAdminEntryOrderBy:
    MEDIA_TYPE_ASC = "+mediaType"
    MEDIA_TYPE_DESC = "-mediaType"
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaLiveStreamEntryOrderBy:
    MEDIA_TYPE_ASC = "+mediaType"
    MEDIA_TYPE_DESC = "-mediaType"
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMailJobOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaEntryOrderBy:
    MEDIA_TYPE_ASC = "+mediaType"
    MEDIA_TYPE_DESC = "-mediaType"
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaFlavorParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaFlavorParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaInfoOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMediaType:
    VIDEO = 1
    IMAGE = 2
    AUDIO = 5
    LIVE_STREAM_FLASH = 201
    LIVE_STREAM_WINDOWS_MEDIA = 202
    LIVE_STREAM_REAL_MEDIA = 203
    LIVE_STREAM_QUICKTIME = 204

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaMixEntryOrderBy:
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaModerationFlagStatus:
    PENDING = 1
    MODERATED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaModerationFlagType:
    SEXUAL_CONTENT = 1
    VIOLENT_REPULSIVE = 2
    HARMFUL_DANGEROUS = 3
    SPAM_COMMERCIALS = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaModerationObjectType:
    ENTRY = 2
    USER = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaNotificationOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    PROCESSOR_EXPIRATION_ASC = "+processorExpiration"
    PROCESSOR_EXPIRATION_DESC = "-processorExpiration"
    EXECUTION_ATTEMPTS_ASC = "+executionAttempts"
    EXECUTION_ATTEMPTS_DESC = "-executionAttempts"
    LOCK_VERSION_ASC = "+lockVersion"
    LOCK_VERSION_DESC = "-lockVersion"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaNotificationType:
    ENTRY_ADD = 1
    ENTR_UPDATE_PERMISSIONS = 2
    ENTRY_DELETE = 3
    ENTRY_BLOCK = 4
    ENTRY_UPDATE = 5
    ENTRY_UPDATE_THUMBNAIL = 6
    ENTRY_UPDATE_MODERATION = 7
    USER_ADD = 21
    USER_BANNED = 26

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaNullableBoolean:
    NULL_VALUE = -1
    FALSE_VALUE = 0
    TRUE_VALUE = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    WEBSITE_ASC = "+website"
    WEBSITE_DESC = "-website"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    ADMIN_NAME_ASC = "+adminName"
    ADMIN_NAME_DESC = "-adminName"
    ADMIN_EMAIL_ASC = "+adminEmail"
    ADMIN_EMAIL_DESC = "-adminEmail"
    STATUS_ASC = "+status"
    STATUS_DESC = "-status"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerStatus:
    ACTIVE = 1
    BLOCKED = 2
    FULL_BLOCK = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPartnerType:
    KMC = 1
    WIKI = 100
    WORDPRESS = 101
    DRUPAL = 102
    DEKIWIKI = 103
    MOODLE = 104
    COMMUNITY_EDITION = 105
    JOOMLA = 106
    BLACKBOARD = 107
    SAKAI = 108

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionItemOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionItemType:
    API_ACTION_ITEM = "kApiActionPermissionItem"
    API_PARAMETER_ITEM = "kApiParameterPermissionItem"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionName:
    FEATURE_ANALYTICS_TAB = "FEATURE_ANALYTICS_TAB"
    FEATURE_508_PLAYERS = "FEATURE_508_PLAYERS"
    FEATURE_LIVE_STREAM = "FEATURE_LIVE_STREAM"
    FEATURE_VAST = "FEATURE_VAST"
    FEATURE_SILVERLIGHT = "FEATURE_SILVERLIGHT"
    FEATURE_PS2_PERMISSIONS_VALIDATION = "FEATURE_PS2_PERMISSIONS_VALIDATION"
    FEATURE_MOBILE_FLAVORS = "FEATURE_MOBILE_FLAVORS"
    USER_SESSION_PERMISSION = "BASE_USER_SESSION_PERMISSION"
    ALWAYS_ALLOWED_ACTIONS = "ALWAYS_ALLOWED_ACTIONS"
    SYSTEM_FILESYNC = "SYSTEM_FILESYNC"
    SYSTEM_INTERNAL = "SYSTEM_INTERNAL"
    KMC_ACCESS = "KMC_ACCESS"
    KMC_READ_ONLY = "KMC_READ_ONLY"
    SYSTEM_ADMIN_BASE = "SYSTEM_ADMIN_BASE"
    SYSTEM_ADMIN_PUBLISHER_BASE = "SYSTEM_ADMIN_PUBLISHER_BASE"
    SYSTEM_ADMIN_PUBLISHER_KMC_ACCESS = "SYSTEM_ADMIN_PUBLISHER_KMC_ACCESS"
    SYSTEM_ADMIN_PUBLISHER_CONFIG = "SYSTEM_ADMIN_PUBLISHER_CONFIG"
    SYSTEM_ADMIN_PUBLISHER_BLOCK = "SYSTEM_ADMIN_PUBLISHER_BLOCK"
    SYSTEM_ADMIN_PUBLISHER_REMOVE = "SYSTEM_ADMIN_PUBLISHER_REMOVE"
    SYSTEM_ADMIN_PUBLISHER_ADD = "SYSTEM_ADMIN_PUBLISHER_ADD"
    SYSTEM_ADMIN_PUBLISHER_USAGE = "SYSTEM_ADMIN_PUBLISHER_USAGE"
    SYSTEM_ADMIN_USER_MANAGE = "SYSTEM_ADMIN_USER_MANAGE"
    SYSTEM_ADMIN_SYSTEM_MONITOR = "SYSTEM_ADMIN_SYSTEM_MONITOR"
    SYSTEM_ADMIN_DEVELOPERS_TAB = "SYSTEM_ADMIN_DEVELOPERS_TAB"
    SYSTEM_ADMIN_BATCH_CONTROL = "SYSTEM_ADMIN_BATCH_CONTROL"
    SYSTEM_ADMIN_BATCH_CONTROL_INPROGRESS = "SYSTEM_ADMIN_BATCH_CONTROL_INPROGRESS"
    SYSTEM_ADMIN_BATCH_CONTROL_FAILED = "SYSTEM_ADMIN_BATCH_CONTROL_FAILED"
    SYSTEM_ADMIN_BATCH_CONTROL_SETUP = "SYSTEM_ADMIN_BATCH_CONTROL_SETUP"
    SYSTEM_ADMIN_STORAGE = "SYSTEM_ADMIN_STORAGE"
    SYSTEM_ADMIN_VIRUS_SCAN = "SYSTEM_ADMIN_VIRUS_SCAN"
    SYSTEM_ADMIN_EMAIL_INGESTION = "SYSTEM_ADMIN_EMAIL_INGESTION"
    SYSTEM_ADMIN_CONTENT_DISTRIBUTION_BASE = "SYSTEM_ADMIN_CONTENT_DISTRIBUTION_BASE"
    SYSTEM_ADMIN_CONTENT_DISTRIBUTION_MODIFY = "SYSTEM_ADMIN_CONTENT_DISTRIBUTION_MODIFY"
    SYSTEM_ADMIN_PERMISSIONS_MANAGE = "SYSTEM_ADMIN_PERMISSIONS_MANAGE"
    SYSTEM_ADMIN_ENTRY_INVESTIGATION = "SYSTEM_ADMIN_ENTRY_INVESTIGATION"
    BATCH_BASE = "BATCH_BASE"
    CONTENT_INGEST_UPLOAD = "CONTENT_INGEST_UPLOAD"
    CONTENT_INGEST_BULK_UPLOAD = "CONTENT_INGEST_BULK_UPLOAD"
    CONTENT_INGEST_FEED = "CONTENT_INGEST_FEED"
    CONTENT_MANAGE_DISTRIBUTION_BASE = "CONTENT_MANAGE_DISTRIBUTION_BASE"
    CONTENT_MANAGE_DISTRIBUTION_WHERE = "CONTENT_MANAGE_DISTRIBUTION_WHERE"
    CONTENT_MANAGE_DISTRIBUTION_SEND = "CONTENT_MANAGE_DISTRIBUTION_SEND"
    CONTENT_MANAGE_DISTRIBUTION_REMOVE = "CONTENT_MANAGE_DISTRIBUTION_REMOVE"
    CONTENT_MANAGE_DISTRIBUTION_PROFILE_MODIFY = "CONTENT_MANAGE_DISTRIBUTION_PROFILE_MODIFY"
    CONTENT_MANAGE_VIRUS_SCAN = "CONTENT_MANAGE_VIRUS_SCAN"
    CONTENT_MANAGE_MIX = "CONTENT_MANAGE_MIX"
    CONTENT_MANAGE_BASE = "CONTENT_MANAGE_BASE"
    CONTENT_MANAGE_METADATA = "CONTENT_MANAGE_METADATA"
    CONTENT_MANAGE_ASSIGN_CATEGORIES = "CONTENT_MANAGE_ASSIGN_CATEGORIES"
    CONTENT_MANAGE_THUMBNAIL = "CONTENT_MANAGE_THUMBNAIL"
    CONTENT_MANAGE_SCHEDULE = "CONTENT_MANAGE_SCHEDULE"
    CONTENT_MANAGE_ACCESS_CONTROL = "CONTENT_MANAGE_ACCESS_CONTROL"
    CONTENT_MANAGE_CUSTOM_DATA = "CONTENT_MANAGE_CUSTOM_DATA"
    CONTENT_MANAGE_DELETE = "CONTENT_MANAGE_DELETE"
    CONTENT_MANAGE_RECONVERT = "CONTENT_MANAGE_RECONVERT"
    CONTENT_MANAGE_EDIT_CATEGORIES = "CONTENT_MANAGE_EDIT_CATEGORIES"
    CONTENT_MANAGE_ANNOTATION = "CONTENT_MANAGE_ANNOTATION"
    CONTENT_MANAGE_SHARE = "CONTENT_MANAGE_SHARE"
    CONTENT_MANAGE_DOWNLOAD = "CONTENT_MANAGE_DOWNLOAD"
    LIVE_STREAM_ADD = "LIVE_STREAM_ADD"
    LIVE_STREAM_UPDATE = "LIVE_STREAM_UPDATE"
    CONTENT_MODERATE_BASE = "CONTENT_MODERATE_BASE"
    CONTENT_MODERATE_METADATA = "CONTENT_MODERATE_METADATA"
    CONTENT_MODERATE_CUSTOM_DATA = "CONTENT_MODERATE_CUSTOM_DATA"
    CONTENT_MODERATE_APPROVE_REJECT = "CONTENT_MODERATE_APPROVE_REJECT"
    PLAYLIST_BASE = "PLAYLIST_BASE"
    PLAYLIST_ADD = "PLAYLIST_ADD"
    PLAYLIST_UPDATE = "PLAYLIST_UPDATE"
    PLAYLIST_DELETE = "PLAYLIST_DELETE"
    SYNDICATION_BASE = "SYNDICATION_BASE"
    SYNDICATION_ADD = "SYNDICATION_ADD"
    SYNDICATION_UPDATE = "SYNDICATION_UPDATE"
    SYNDICATION_DELETE = "SYNDICATION_DELETE"
    STUDIO_BASE = "STUDIO_BASE"
    STUDIO_ADD_UICONF = "STUDIO_ADD_UICONF"
    STUDIO_UPDATE_UICONF = "STUDIO_UPDATE_UICONF"
    STUDIO_DELETE_UICONF = "STUDIO_DELETE_UICONF"
    ACCOUNT_BASE = "ACCOUNT_BASE"
    ACCOUNT_UPDATE_SETTINGS = "ACCOUNT_UPDATE_SETTINGS"
    INTEGRATION_BASE = "INTEGRATION_BASE"
    INTEGRATION_UPDATE_SETTINGS = "INTEGRATION_UPDATE_SETTINGS"
    ACCESS_CONTROL_BASE = "ACCESS_CONTROL_BASE"
    ACCESS_CONTROL_ADD = "ACCESS_CONTROL_ADD"
    ACCESS_CONTROL_UPDATE = "ACCESS_CONTROL_UPDATE"
    ACCESS_CONTROL_DELETE = "ACCESS_CONTROL_DELETE"
    TRANSCODING_BASE = "TRANSCODING_BASE"
    TRANSCODING_ADD = "TRANSCODING_ADD"
    TRANSCODING_UPDATE = "TRANSCODING_UPDATE"
    TRANSCODING_DELETE = "TRANSCODING_DELETE"
    CUSTOM_DATA_PROFILE_BASE = "CUSTOM_DATA_PROFILE_BASE"
    CUSTOM_DATA_PROFILE_ADD = "CUSTOM_DATA_PROFILE_ADD"
    CUSTOM_DATA_PROFILE_UPDATE = "CUSTOM_DATA_PROFILE_UPDATE"
    CUSTOM_DATA_PROFILE_DELETE = "CUSTOM_DATA_PROFILE_DELETE"
    CUSTOM_DATA_FIELD_ADD = "CUSTOM_DATA_FIELD_ADD"
    CUSTOM_DATA_FIELD_UPDATE = "CUSTOM_DATA_FIELD_UPDATE"
    CUSTOM_DATA_FIELD_DELETE = "CUSTOM_DATA_FIELD_DELETE"
    ADMIN_BASE = "ADMIN_BASE"
    ADMIN_USER_ADD = "ADMIN_USER_ADD"
    ADMIN_USER_UPDATE = "ADMIN_USER_UPDATE"
    ADMIN_USER_DELETE = "ADMIN_USER_DELETE"
    ADMIN_ROLE_ADD = "ADMIN_ROLE_ADD"
    ADMIN_ROLE_UPDATE = "ADMIN_ROLE_UPDATE"
    ADMIN_ROLE_DELETE = "ADMIN_ROLE_DELETE"
    ADMIN_PERMISSION_ADD = "ADMIN_PERMISSION_ADD"
    ADMIN_PERMISSION_UPDATE = "ADMIN_PERMISSION_UPDATE"
    ADMIN_PERMISSION_DELETE = "ADMIN_PERMISSION_DELETE"
    ADMIN_PUBLISHER_MANAGE = "ADMIN_PUBLISHER_MANAGE"
    ANALYTICS_BASE = "ANALYTICS_BASE"
    WIDGET_ADMIN = "WIDGET_ADMIN"
    SEARCH_SERVICE = "SEARCH_SERVICE"
    ANALYTICS_SEND_DATA = "ANALYTICS_SEND_DATA"
    AUDIT_TRAIL_BASE = "AUDIT_TRAIL_BASE"
    AUDIT_TRAIL_ADD = "AUDIT_TRAIL_ADD"
    ADVERTISING_BASE = "ADVERTISING_BASE"
    ADVERTISING_UPDATE_SETTINGS = "ADVERTISING_UPDATE_SETTINGS"
    PLAYLIST_EMBED_CODE = "PLAYLIST_EMBED_CODE"
    STUDIO_BRAND_UICONF = "STUDIO_BRAND_UICONF"
    STUDIO_SELECT_CONTENT = "STUDIO_SELECT_CONTENT"
    CONTENT_MANAGE_EMBED_CODE = "CONTENT_MANAGE_EMBED_CODE"
    ADMIN_WHITE_BRANDING = "ADMIN_WHITE_BRANDING"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionStatus:
    ACTIVE = 1
    BLOCKED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPermissionType:
    NORMAL = 1
    SPECIAL_FEATURE = 2
    PLUGIN = 3
    PARTNER_GROUP = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPlayableEntryOrderBy:
    PLAYS_ASC = "+plays"
    PLAYS_DESC = "-plays"
    VIEWS_ASC = "+views"
    VIEWS_DESC = "-views"
    DURATION_ASC = "+duration"
    DURATION_DESC = "-duration"
    MS_DURATION_ASC = "+msDuration"
    MS_DURATION_DESC = "-msDuration"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPlaylistOrderBy:
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    MODERATION_COUNT_ASC = "+moderationCount"
    MODERATION_COUNT_DESC = "-moderationCount"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    RANK_ASC = "+rank"
    RANK_DESC = "-rank"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaPlaylistType:
    DYNAMIC = 10
    STATIC_LIST = 3
    EXTERNAL = 101

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaReportType:
    TOP_CONTENT = 1
    CONTENT_DROPOFF = 2
    CONTENT_INTERACTIONS = 3
    MAP_OVERLAY = 4
    TOP_CONTRIBUTORS = 5
    TOP_SYNDICATION = 6
    CONTENT_CONTRIBUTIONS = 7

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSearchConditionComparison:
    EQUEL = 1
    GREATER_THAN = 2
    GREATER_THAN_OR_EQUEL = 3
    LESS_THAN = 4
    LESS_THAN_OR_EQUEL = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSearchOperatorType:
    SEARCH_AND = 1
    SEARCH_OR = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSearchProviderType:
    FLICKR = 3
    YOUTUBE = 4
    MYSPACE = 7
    PHOTOBUCKET = 8
    JAMENDO = 9
    CCMIXTER = 10
    NYPL = 11
    CURRENT = 12
    MEDIA_COMMONS = 13
    KALTURA = 20
    KALTURA_USER_CLIPS = 21
    ARCHIVE_ORG = 22
    KALTURA_PARTNER = 23
    METACAFE = 24
    SEARCH_PROXY = 28
    PARTNER_SPECIFIC = 100

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSessionType:
    USER = 0
    ADMIN = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSiteRestrictionType:
    RESTRICT_SITE_LIST = 0
    ALLOW_SITE_LIST = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSourceType:
    FILE = 1
    WEBCAM = 2
    URL = 5
    SEARCH_PROVIDER = 6
    AKAMAI_LIVE = 29

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStatsEventType:
    WIDGET_LOADED = 1
    MEDIA_LOADED = 2
    PLAY = 3
    PLAY_REACHED_25 = 4
    PLAY_REACHED_50 = 5
    PLAY_REACHED_75 = 6
    PLAY_REACHED_100 = 7
    OPEN_EDIT = 8
    OPEN_VIRAL = 9
    OPEN_DOWNLOAD = 10
    OPEN_REPORT = 11
    BUFFER_START = 12
    BUFFER_END = 13
    OPEN_FULL_SCREEN = 14
    CLOSE_FULL_SCREEN = 15
    REPLAY = 16
    SEEK = 17
    OPEN_UPLOAD = 18
    SAVE_PUBLISH = 19
    CLOSE_EDITOR = 20
    PRE_BUMPER_PLAYED = 21
    POST_BUMPER_PLAYED = 22
    BUMPER_CLICKED = 23
    PREROLL_STARTED = 24
    MIDROLL_STARTED = 25
    POSTROLL_STARTED = 26
    OVERLAY_STARTED = 27
    PREROLL_CLICKED = 28
    MIDROLL_CLICKED = 29
    POSTROLL_CLICKED = 30
    OVERLAY_CLICKED = 31
    PREROLL_25 = 32
    PREROLL_50 = 33
    PREROLL_75 = 34
    MIDROLL_25 = 35
    MIDROLL_50 = 36
    MIDROLL_75 = 37
    POSTROLL_25 = 38
    POSTROLL_50 = 39
    POSTROLL_75 = 40

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaStatsKmcEventType:
    CONTENT_PAGE_VIEW = 1001
    CONTENT_ADD_PLAYLIST = 1010
    CONTENT_EDIT_PLAYLIST = 1011
    CONTENT_DELETE_PLAYLIST = 1012
    CONTENT_DELETE_ITEM = 1058
    CONTENT_DELETE_MIX = 1059
    CONTENT_EDIT_ENTRY = 1013
    CONTENT_CHANGE_THUMBNAIL = 1014
    CONTENT_ADD_TAGS = 1015
    CONTENT_REMOVE_TAGS = 1016
    CONTENT_ADD_ADMIN_TAGS = 1017
    CONTENT_REMOVE_ADMIN_TAGS = 1018
    CONTENT_DOWNLOAD = 1019
    CONTENT_APPROVE_MODERATION = 1020
    CONTENT_REJECT_MODERATION = 1021
    CONTENT_BULK_UPLOAD = 1022
    CONTENT_ADMIN_KCW_UPLOAD = 1023
    CONTENT_CONTENT_GO_TO_PAGE = 1057
    CONTENT_ENTRY_DRILLDOWN = 1088
    CONTENT_OPEN_PREVIEW_AND_EMBED = 1089
    ACCOUNT_CHANGE_PARTNER_INFO = 1030
    ACCOUNT_CHANGE_LOGIN_INFO = 1031
    ACCOUNT_CONTACT_US_USAGE = 1032
    ACCOUNT_UPDATE_SERVER_SETTINGS = 1033
    ACCOUNT_ACCOUNT_OVERVIEW = 1034
    ACCOUNT_ACCESS_CONTROL = 1035
    ACCOUNT_TRANSCODING_SETTINGS = 1036
    ACCOUNT_ACCOUNT_UPGRADE = 1037
    ACCOUNT_SAVE_SERVER_SETTINGS = 1038
    ACCOUNT_ACCESS_CONTROL_DELETE = 1039
    ACCOUNT_SAVE_TRANSCODING_SETTINGS = 1040
    LOGIN = 1041
    DASHBOARD_IMPORT_CONTENT = 1042
    DASHBOARD_UPDATE_CONTENT = 1043
    DASHBOARD_ACCOUNT_CONTACT_US = 1044
    DASHBOARD_VIEW_REPORTS = 1045
    DASHBOARD_EMBED_PLAYER = 1046
    DASHBOARD_EMBED_PLAYLIST = 1047
    DASHBOARD_CUSTOMIZE_PLAYERS = 1048
    APP_STUDIO_NEW_PLAYER_SINGLE_VIDEO = 1050
    APP_STUDIO_NEW_PLAYER_PLAYLIST = 1051
    APP_STUDIO_NEW_PLAYER_MULTI_TAB_PLAYLIST = 1052
    APP_STUDIO_EDIT_PLAYER_SINGLE_VIDEO = 1053
    APP_STUDIO_EDIT_PLAYER_PLAYLIST = 1054
    APP_STUDIO_EDIT_PLAYER_MULTI_TAB_PLAYLIST = 1055
    APP_STUDIO_DUPLICATE_PLAYER = 1056
    REPORTS_AND_ANALYTICS_BANDWIDTH_USAGE_TAB = 1070
    REPORTS_AND_ANALYTICS_CONTENT_REPORTS_TAB = 1071
    REPORTS_AND_ANALYTICS_USERS_AND_COMMUNITY_REPORTS_TAB = 1072
    REPORTS_AND_ANALYTICS_TOP_CONTRIBUTORS = 1073
    REPORTS_AND_ANALYTICS_MAP_OVERLAYS = 1074
    REPORTS_AND_ANALYTICS_TOP_SYNDICATIONS = 1075
    REPORTS_AND_ANALYTICS_TOP_CONTENT = 1076
    REPORTS_AND_ANALYTICS_CONTENT_DROPOFF = 1077
    REPORTS_AND_ANALYTICS_CONTENT_INTERACTIONS = 1078
    REPORTS_AND_ANALYTICS_CONTENT_CONTRIBUTIONS = 1079
    REPORTS_AND_ANALYTICS_VIDEO_DRILL_DOWN = 1080
    REPORTS_AND_ANALYTICS_CONTENT_DRILL_DOWN_INTERACTION = 1081
    REPORTS_AND_ANALYTICS_CONTENT_CONTRIBUTIONS_DRILLDOWN = 1082
    REPORTS_AND_ANALYTICS_VIDEO_DRILL_DOWN_DROPOFF = 1083
    REPORTS_AND_ANALYTICS_MAP_OVERLAYS_DRILLDOWN = 1084
    REPORTS_AND_ANALYTICS_TOP_SYNDICATIONS_DRILL_DOWN = 1085
    REPORTS_AND_ANALYTICS_BANDWIDTH_USAGE_VIEW_MONTHLY = 1086
    REPORTS_AND_ANALYTICS_BANDWIDTH_USAGE_VIEW_YEARLY = 1087

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSyndicationFeedStatus:
    DELETED = -1
    ACTIVE = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaSyndicationFeedType:
    GOOGLE_VIDEO = 1
    YAHOO = 2
    ITUNES = 3
    TUBE_MOGUL = 4
    KALTURA = 5
    KALTURA_XSLT = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbAssetOrderBy:
    SIZE_ASC = "+size"
    SIZE_DESC = "-size"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"
    DELETED_AT_ASC = "+deletedAt"
    DELETED_AT_DESC = "-deletedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbCropType:
    RESIZE = 1
    RESIZE_WITH_PADDING = 2
    CROP = 3
    CROP_FROM_TOP = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbParamsOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaThumbParamsOutputOrderBy:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaTubeMogulSyndicationFeedCategories:
    ARTS_AND_ANIMATION = "Arts &amp; Animation"
    COMEDY = "Comedy"
    ENTERTAINMENT = "Entertainment"
    MUSIC = "Music"
    NEWS_AND_BLOGS = "News &amp; Blogs"
    SCIENCE_AND_TECHNOLOGY = "Science &amp; Technology"
    SPORTS = "Sports"
    TRAVEL_AND_PLACES = "Travel &amp; Places"
    VIDEO_GAMES = "Video Games"
    ANIMALS_AND_PETS = "Animals &amp; Pets"
    AUTOS = "Autos"
    VLOGS_PEOPLE = "Vlogs &amp; People"
    HOW_TO_INSTRUCTIONAL_DIY = "How To/Instructional/DIY"
    COMMERCIALS_PROMOTIONAL = "Commercials/Promotional"
    FAMILY_AND_KIDS = "Family &amp; Kids"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaTubeMogulSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUiConfCreationMode:
    WIZARD = 2
    ADVANCED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUiConfObjType:
    PLAYER = 1
    CONTRIBUTION_WIZARD = 2
    SIMPLE_EDITOR = 3
    ADVANCED_EDITOR = 4
    PLAYLIST = 5
    APP_STUDIO = 6
    KRECORD = 7
    PLAYER_V3 = 8
    KMC_ACCOUNT = 9
    KMC_ANALYTICS = 10
    KMC_CONTENT = 11
    KMC_DASHBOARD = 12
    KMC_LOGIN = 13
    PLAYER_SL = 14
    CLIENTSIDE_ENCODER = 15
    KMC_GENERAL = 16
    KMC_ROLES_AND_PERMISSIONS = 17

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUiConfOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUploadErrorCode:
    NO_ERROR = 0
    GENERAL_ERROR = 1
    PARTIAL_UPLOAD = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUploadTokenOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUploadTokenStatus:
    PENDING = 0
    PARTIAL_UPLOAD = 1
    FULL_UPLOAD = 2
    CLOSED = 3
    TIMED_OUT = 4
    DELETED = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserRoleOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserRoleStatus:
    ACTIVE = 1
    BLOCKED = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaUserStatus:
    BLOCKED = 0
    ACTIVE = 1
    DELETED = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaVideoCodec:
    NONE = ""
    VP6 = "vp6"
    H263 = "h263"
    H264 = "h264"
    H264B = "h264b"
    H264M = "h264m"
    H264H = "h264h"
    FLV = "flv"
    MPEG4 = "mpeg4"
    THEORA = "theora"
    WMV2 = "wmv2"
    WMV3 = "wmv3"
    WVC1A = "wvc1a"
    VP8 = "vp8"
    COPY = "copy"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaWidgetOrderBy:
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaWidgetSecurityType:
    NONE = 1
    TIMEHASH = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYahooSyndicationFeedAdultValues:
    ADULT = "adult"
    NON_ADULT = "nonadult"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYahooSyndicationFeedCategories:
    ACTION = "Action"
    ART_AND_ANIMATION = "Art &amp; Animation"
    ENTERTAINMENT_AND_TV = "Entertainment &amp; TV"
    FOOD = "Food"
    GAMES = "Games"
    HOW_TO = "How-To"
    MUSIC = "Music"
    PEOPLE_AND_VLOGS = "People &amp; Vlogs"
    SCIENCE_AND_ENVIRONMENT = "Science &amp; Environment"
    TRANSPORTATION = "Transportation"
    ANIMALS = "Animals"
    COMMERCIALS = "Commercials"
    FAMILY = "Family"
    FUNNY_VIDEOS = "Funny Videos"
    HEALTH_AND_BEAUTY = "Health &amp; Beauty"
    MOVIES_AND_SHORTS = "Movies &amp; Shorts"
    NEWS_AND_POLITICS = "News &amp; Politics"
    PRODUCTS_AND_TECH = "Products &amp; Tech."
    SPORTS = "Sports"
    TRAVEL = "Travel"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class KalturaYahooSyndicationFeedOrderBy:
    PLAYLIST_ID_ASC = "+playlistId"
    PLAYLIST_ID_DESC = "-playlistId"
    NAME_ASC = "+name"
    NAME_DESC = "-name"
    TYPE_ASC = "+type"
    TYPE_DESC = "-type"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
class KalturaBaseRestriction(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseRestriction")
        return kparams


class KalturaAccessControl(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the Access Control Profile
        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # The name of the Access Control Profile
        # @var string
        self.name = None

        # The description of the Access Control Profile
        # @var string
        self.description = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # True if this Conversion Profile is the default
        # @var KalturaNullableBoolean
        self.isDefault = None

        # Array of Access Control Restrictions
        # @var array of KalturaBaseRestriction
        self.restrictions = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'isDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'restrictions': (KalturaObjectFactory.createArray, KalturaBaseRestriction), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControl.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAccessControl")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addIntEnumIfNotNone("isDefault", self.isDefault)
        kparams.addObjectIfNotNone("restrictions", self.restrictions)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getRestrictions(self):
        return self.restrictions

    def setRestrictions(self, newRestrictions):
        self.restrictions = newRestrictions


class KalturaSearchItem(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchItem")
        return kparams


class KalturaFilter(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.orderBy = None

        # @var KalturaSearchItem
        self.advancedSearch = None


    PROPERTY_LOADERS = {
        'orderBy': getXmlNodeText, 
        'advancedSearch': (KalturaObjectFactory.create, KalturaSearchItem), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilter")
        kparams.addStringIfNotNone("orderBy", self.orderBy)
        kparams.addObjectIfNotNone("advancedSearch", self.advancedSearch)
        return kparams

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy

    def getAdvancedSearch(self):
        return self.advancedSearch

    def setAdvancedSearch(self, newAdvancedSearch):
        self.advancedSearch = newAdvancedSearch


class KalturaAccessControlBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAccessControlBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual


class KalturaAccessControlFilter(KalturaAccessControlBaseFilter):
    def __init__(self):
        KalturaAccessControlBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAccessControlBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAccessControlBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAccessControlFilter")
        return kparams


class KalturaFilterPager(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The number of objects to retrieve. (Default is 30, maximum page size is 500).
        # @var int
        self.pageSize = None

        # The page number for which {pageSize} of objects should be retrieved (Default is 1).
        # @var int
        self.pageIndex = None


    PROPERTY_LOADERS = {
        'pageSize': getXmlNodeInt, 
        'pageIndex': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilterPager.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilterPager")
        kparams.addIntIfNotNone("pageSize", self.pageSize)
        kparams.addIntIfNotNone("pageIndex", self.pageIndex)
        return kparams

    def getPageSize(self):
        return self.pageSize

    def setPageSize(self, newPageSize):
        self.pageSize = newPageSize

    def getPageIndex(self):
        return self.pageIndex

    def setPageIndex(self, newPageIndex):
        self.pageIndex = newPageIndex


class KalturaAccessControlListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaAccessControl
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAccessControl), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAccessControlListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUser(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.screenName = None

        # @var string
        self.fullName = None

        # @var string
        self.email = None

        # @var int
        self.dateOfBirth = None

        # @var string
        self.country = None

        # @var string
        self.state = None

        # @var string
        self.city = None

        # @var string
        self.zip = None

        # @var string
        self.thumbnailUrl = None

        # @var string
        self.description = None

        # @var string
        self.tags = None

        # Admin tags can be updated only by using an admin session
        # @var string
        self.adminTags = None

        # @var KalturaGender
        self.gender = None

        # @var KalturaUserStatus
        self.status = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # Can be used to store various partner related data as a string
        # @var string
        self.partnerData = None

        # @var int
        self.indexedPartnerDataInt = None

        # @var string
        self.indexedPartnerDataString = None

        # @var int
        # @readonly
        self.storageSize = None

        # @var string
        # @insertonly
        self.password = None

        # @var string
        self.firstName = None

        # @var string
        self.lastName = None

        # @var bool
        self.isAdmin = None

        # @var int
        # @readonly
        self.lastLoginTime = None

        # @var int
        # @readonly
        self.statusUpdatedAt = None

        # @var int
        # @readonly
        self.deletedAt = None

        # @var bool
        # @readonly
        self.loginEnabled = None

        # @var string
        self.roleIds = None

        # @var string
        # @readonly
        self.roleNames = None

        # @var bool
        # @readonly
        self.isAccountOwner = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'screenName': getXmlNodeText, 
        'fullName': getXmlNodeText, 
        'email': getXmlNodeText, 
        'dateOfBirth': getXmlNodeInt, 
        'country': getXmlNodeText, 
        'state': getXmlNodeText, 
        'city': getXmlNodeText, 
        'zip': getXmlNodeText, 
        'thumbnailUrl': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'adminTags': getXmlNodeText, 
        'gender': (KalturaEnumsFactory.createInt, "KalturaGender"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaUserStatus"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerData': getXmlNodeText, 
        'indexedPartnerDataInt': getXmlNodeInt, 
        'indexedPartnerDataString': getXmlNodeText, 
        'storageSize': getXmlNodeInt, 
        'password': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
        'isAdmin': getXmlNodeBool, 
        'lastLoginTime': getXmlNodeInt, 
        'statusUpdatedAt': getXmlNodeInt, 
        'deletedAt': getXmlNodeInt, 
        'loginEnabled': getXmlNodeBool, 
        'roleIds': getXmlNodeText, 
        'roleNames': getXmlNodeText, 
        'isAccountOwner': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUser")
        kparams.addStringIfNotNone("id", self.id)
        kparams.addStringIfNotNone("screenName", self.screenName)
        kparams.addStringIfNotNone("fullName", self.fullName)
        kparams.addStringIfNotNone("email", self.email)
        kparams.addIntIfNotNone("dateOfBirth", self.dateOfBirth)
        kparams.addStringIfNotNone("country", self.country)
        kparams.addStringIfNotNone("state", self.state)
        kparams.addStringIfNotNone("city", self.city)
        kparams.addStringIfNotNone("zip", self.zip)
        kparams.addStringIfNotNone("thumbnailUrl", self.thumbnailUrl)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("adminTags", self.adminTags)
        kparams.addIntEnumIfNotNone("gender", self.gender)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addStringIfNotNone("partnerData", self.partnerData)
        kparams.addIntIfNotNone("indexedPartnerDataInt", self.indexedPartnerDataInt)
        kparams.addStringIfNotNone("indexedPartnerDataString", self.indexedPartnerDataString)
        kparams.addStringIfNotNone("password", self.password)
        kparams.addStringIfNotNone("firstName", self.firstName)
        kparams.addStringIfNotNone("lastName", self.lastName)
        kparams.addBoolIfNotNone("isAdmin", self.isAdmin)
        kparams.addStringIfNotNone("roleIds", self.roleIds)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getPartnerId(self):
        return self.partnerId

    def getScreenName(self):
        return self.screenName

    def setScreenName(self, newScreenName):
        self.screenName = newScreenName

    def getFullName(self):
        return self.fullName

    def setFullName(self, newFullName):
        self.fullName = newFullName

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def getDateOfBirth(self):
        return self.dateOfBirth

    def setDateOfBirth(self, newDateOfBirth):
        self.dateOfBirth = newDateOfBirth

    def getCountry(self):
        return self.country

    def setCountry(self, newCountry):
        self.country = newCountry

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState

    def getCity(self):
        return self.city

    def setCity(self, newCity):
        self.city = newCity

    def getZip(self):
        return self.zip

    def setZip(self, newZip):
        self.zip = newZip

    def getThumbnailUrl(self):
        return self.thumbnailUrl

    def setThumbnailUrl(self, newThumbnailUrl):
        self.thumbnailUrl = newThumbnailUrl

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getAdminTags(self):
        return self.adminTags

    def setAdminTags(self, newAdminTags):
        self.adminTags = newAdminTags

    def getGender(self):
        return self.gender

    def setGender(self, newGender):
        self.gender = newGender

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getIndexedPartnerDataInt(self):
        return self.indexedPartnerDataInt

    def setIndexedPartnerDataInt(self, newIndexedPartnerDataInt):
        self.indexedPartnerDataInt = newIndexedPartnerDataInt

    def getIndexedPartnerDataString(self):
        return self.indexedPartnerDataString

    def setIndexedPartnerDataString(self, newIndexedPartnerDataString):
        self.indexedPartnerDataString = newIndexedPartnerDataString

    def getStorageSize(self):
        return self.storageSize

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getIsAdmin(self):
        return self.isAdmin

    def setIsAdmin(self, newIsAdmin):
        self.isAdmin = newIsAdmin

    def getLastLoginTime(self):
        return self.lastLoginTime

    def getStatusUpdatedAt(self):
        return self.statusUpdatedAt

    def getDeletedAt(self):
        return self.deletedAt

    def getLoginEnabled(self):
        return self.loginEnabled

    def getRoleIds(self):
        return self.roleIds

    def setRoleIds(self, newRoleIds):
        self.roleIds = newRoleIds

    def getRoleNames(self):
        return self.roleNames

    def getIsAccountOwner(self):
        return self.isAccountOwner


class KalturaDynamicEnum(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDynamicEnum.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDynamicEnum")
        return kparams


class KalturaBaseEntry(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Auto generated 10 characters alphanumeric string
        # @var string
        # @readonly
        self.id = None

        # Entry name (Min 1 chars)
        # @var string
        self.name = None

        # Entry description
        # @var string
        self.description = None

        # @var int
        # @readonly
        self.partnerId = None

        # The ID of the user who is the owner of this entry
        # @var string
        self.userId = None

        # Entry tags
        # @var string
        self.tags = None

        # Entry admin tags can be updated only by administrators
        # @var string
        self.adminTags = None

        # @var string
        self.categories = None

        # @var string
        self.categoriesIds = None

        # @var KalturaEntryStatus
        # @readonly
        self.status = None

        # Entry moderation status
        # @var KalturaEntryModerationStatus
        # @readonly
        self.moderationStatus = None

        # Number of moderation requests waiting for this entry
        # @var int
        # @readonly
        self.moderationCount = None

        # The type of the entry, this is auto filled by the derived entry object
        # @var KalturaEntryType
        self.type = None

        # Entry creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Entry update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # Calculated rank
        # @var float
        # @readonly
        self.rank = None

        # The total (sum) of all votes
        # @var int
        # @readonly
        self.totalRank = None

        # Number of votes
        # @var int
        # @readonly
        self.votes = None

        # @var int
        self.groupId = None

        # Can be used to store various partner related data as a string
        # @var string
        self.partnerData = None

        # Download URL for the entry
        # @var string
        # @readonly
        self.downloadUrl = None

        # Indexed search text for full text search
        # @var string
        # @readonly
        self.searchText = None

        # License type used for this entry
        # @var KalturaLicenseType
        self.licenseType = None

        # Version of the entry data
        # @var int
        # @readonly
        self.version = None

        # Thumbnail URL
        # @var string
        # @insertonly
        self.thumbnailUrl = None

        # The Access Control ID assigned to this entry (null when not set, send -1 to remove)
        # @var int
        self.accessControlId = None

        # Entry scheduling start date (null when not set, send -1 to remove)
        # @var int
        self.startDate = None

        # Entry scheduling end date (null when not set, send -1 to remove)
        # @var int
        self.endDate = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'adminTags': getXmlNodeText, 
        'categories': getXmlNodeText, 
        'categoriesIds': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaEntryStatus"), 
        'moderationStatus': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'moderationCount': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaEntryType"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'rank': getXmlNodeFloat, 
        'totalRank': getXmlNodeInt, 
        'votes': getXmlNodeInt, 
        'groupId': getXmlNodeInt, 
        'partnerData': getXmlNodeText, 
        'downloadUrl': getXmlNodeText, 
        'searchText': getXmlNodeText, 
        'licenseType': (KalturaEnumsFactory.createInt, "KalturaLicenseType"), 
        'version': getXmlNodeInt, 
        'thumbnailUrl': getXmlNodeText, 
        'accessControlId': getXmlNodeInt, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseEntry")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("userId", self.userId)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("adminTags", self.adminTags)
        kparams.addStringIfNotNone("categories", self.categories)
        kparams.addStringIfNotNone("categoriesIds", self.categoriesIds)
        kparams.addStringEnumIfNotNone("type", self.type)
        kparams.addIntIfNotNone("groupId", self.groupId)
        kparams.addStringIfNotNone("partnerData", self.partnerData)
        kparams.addIntEnumIfNotNone("licenseType", self.licenseType)
        kparams.addStringIfNotNone("thumbnailUrl", self.thumbnailUrl)
        kparams.addIntIfNotNone("accessControlId", self.accessControlId)
        kparams.addIntIfNotNone("startDate", self.startDate)
        kparams.addIntIfNotNone("endDate", self.endDate)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getAdminTags(self):
        return self.adminTags

    def setAdminTags(self, newAdminTags):
        self.adminTags = newAdminTags

    def getCategories(self):
        return self.categories

    def setCategories(self, newCategories):
        self.categories = newCategories

    def getCategoriesIds(self):
        return self.categoriesIds

    def setCategoriesIds(self, newCategoriesIds):
        self.categoriesIds = newCategoriesIds

    def getStatus(self):
        return self.status

    def getModerationStatus(self):
        return self.moderationStatus

    def getModerationCount(self):
        return self.moderationCount

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getRank(self):
        return self.rank

    def getTotalRank(self):
        return self.totalRank

    def getVotes(self):
        return self.votes

    def getGroupId(self):
        return self.groupId

    def setGroupId(self, newGroupId):
        self.groupId = newGroupId

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getDownloadUrl(self):
        return self.downloadUrl

    def getSearchText(self):
        return self.searchText

    def getLicenseType(self):
        return self.licenseType

    def setLicenseType(self, newLicenseType):
        self.licenseType = newLicenseType

    def getVersion(self):
        return self.version

    def getThumbnailUrl(self):
        return self.thumbnailUrl

    def setThumbnailUrl(self, newThumbnailUrl):
        self.thumbnailUrl = newThumbnailUrl

    def getAccessControlId(self):
        return self.accessControlId

    def setAccessControlId(self, newAccessControlId):
        self.accessControlId = newAccessControlId

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate


class KalturaBaseEntryBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # This filter should be in use for retrieving only a specific entry (identified by its entryId).
        # @var string
        # @var string
        self.idEqual = None

        # This filter should be in use for retrieving few specific entries (string should include comma separated list of entryId strings).
        # @var string
        # @var string
        self.idIn = None

        # @var string
        self.idNotIn = None

        # This filter should be in use for retrieving specific entries. It should include only one string to search for in entry names (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.nameLike = None

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry names, while applying an OR logic to retrieve entries that contain at least one input string (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.nameMultiLikeOr = None

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry names, while applying an AND logic to retrieve entries that contain all input strings (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.nameMultiLikeAnd = None

        # This filter should be in use for retrieving entries with a specific name.
        # @var string
        # @var string
        self.nameEqual = None

        # This filter should be in use for retrieving only entries which were uploaded by/assigned to users of a specific Kaltura Partner (identified by Partner ID).
        # @var int
        # @var int
        self.partnerIdEqual = None

        # This filter should be in use for retrieving only entries within Kaltura network which were uploaded by/assigned to users of few Kaltura Partners  (string should include comma separated list of PartnerIDs)
        # @var string
        # @var string
        self.partnerIdIn = None

        # This filter parameter should be in use for retrieving only entries, uploaded by/assigned to a specific user (identified by user Id).
        # @var string
        # @var string
        self.userIdEqual = None

        # This filter should be in use for retrieving specific entries. It should include only one string to search for in entry tags (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.tagsLike = None

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, while applying an OR logic to retrieve entries that contain at least one input string (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.tagsMultiLikeOr = None

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, while applying an AND logic to retrieve entries that contain all input strings (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.tagsMultiLikeAnd = None

        # This filter should be in use for retrieving specific entries. It should include only one string to search for in entry tags set by an ADMIN user (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.adminTagsLike = None

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, set by an ADMIN user, while applying an OR logic to retrieve entries that contain at least one input string (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.adminTagsMultiLikeOr = None

        # This filter should be in use for retrieving specific entries. It could include few (comma separated) strings for searching in entry tags, set by an ADMIN user, while applying an AND logic to retrieve entries that contain all input strings (no wildcards, spaces are treated as part of the string).
        # @var string
        # @var string
        self.adminTagsMultiLikeAnd = None

        # @var string
        self.categoriesMatchAnd = None

        # @var string
        self.categoriesMatchOr = None

        # @var string
        self.categoriesIdsMatchAnd = None

        # @var string
        self.categoriesIdsMatchOr = None

        # This filter should be in use for retrieving only entries, at a specific {@link ?object=KalturaEntryStatus KalturaEntryStatus}.
        # @var KalturaEntryStatus
        # @var KalturaEntryStatus
        self.statusEqual = None

        # This filter should be in use for retrieving only entries, not at a specific {@link ?object=KalturaEntryStatus KalturaEntryStatus}.
        # @var KalturaEntryStatus
        # @var KalturaEntryStatus
        self.statusNotEqual = None

        # This filter should be in use for retrieving only entries, at few specific {@link ?object=KalturaEntryStatus KalturaEntryStatus} (comma separated).
        # @dynamicType KalturaEntryStatus
        # @var string
        self.statusIn = None

        # This filter should be in use for retrieving only entries, not at few specific {@link ?object=KalturaEntryStatus KalturaEntryStatus} (comma separated).
        # @dynamicType KalturaEntryStatus
        # @var string
        self.statusNotIn = None

        # @var KalturaEntryModerationStatus
        self.moderationStatusEqual = None

        # @var KalturaEntryModerationStatus
        self.moderationStatusNotEqual = None

        # @var string
        self.moderationStatusIn = None

        # @var string
        self.moderationStatusNotIn = None

        # @var KalturaEntryType
        self.typeEqual = None

        # This filter should be in use for retrieving entries of few {@link ?object=KalturaEntryType KalturaEntryType} (string should include a comma separated list of {@link ?object=KalturaEntryType KalturaEntryType} enumerated parameters).
        # @dynamicType KalturaEntryType
        # @var string
        self.typeIn = None

        # This filter parameter should be in use for retrieving only entries which were created at Kaltura system after a specific time/date (standard timestamp format).
        # @var int
        # @var int
        self.createdAtGreaterThanOrEqual = None

        # This filter parameter should be in use for retrieving only entries which were created at Kaltura system before a specific time/date (standard timestamp format).
        # @var int
        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var int
        self.groupIdEqual = None

        # This filter should be in use for retrieving specific entries while search match the input string within all of the following metadata attributes: name, description, tags, adminTags.
        # @var string
        # @var string
        self.searchTextMatchAnd = None

        # This filter should be in use for retrieving specific entries while search match the input string within at least one of the following metadata attributes: name, description, tags, adminTags.
        # @var string
        # @var string
        self.searchTextMatchOr = None

        # @var int
        self.accessControlIdEqual = None

        # @var string
        self.accessControlIdIn = None

        # @var int
        self.startDateGreaterThanOrEqual = None

        # @var int
        self.startDateLessThanOrEqual = None

        # @var int
        self.startDateGreaterThanOrEqualOrNull = None

        # @var int
        self.startDateLessThanOrEqualOrNull = None

        # @var int
        self.endDateGreaterThanOrEqual = None

        # @var int
        self.endDateLessThanOrEqual = None

        # @var int
        self.endDateGreaterThanOrEqualOrNull = None

        # @var int
        self.endDateLessThanOrEqualOrNull = None

        # @var string
        self.tagsNameMultiLikeOr = None

        # @var string
        self.tagsAdminTagsMultiLikeOr = None

        # @var string
        self.tagsAdminTagsNameMultiLikeOr = None

        # @var string
        self.tagsNameMultiLikeAnd = None

        # @var string
        self.tagsAdminTagsMultiLikeAnd = None

        # @var string
        self.tagsAdminTagsNameMultiLikeAnd = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'idNotIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'nameMultiLikeOr': getXmlNodeText, 
        'nameMultiLikeAnd': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'tagsLike': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'adminTagsLike': getXmlNodeText, 
        'adminTagsMultiLikeOr': getXmlNodeText, 
        'adminTagsMultiLikeAnd': getXmlNodeText, 
        'categoriesMatchAnd': getXmlNodeText, 
        'categoriesMatchOr': getXmlNodeText, 
        'categoriesIdsMatchAnd': getXmlNodeText, 
        'categoriesIdsMatchOr': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createString, "KalturaEntryStatus"), 
        'statusNotEqual': (KalturaEnumsFactory.createString, "KalturaEntryStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
        'moderationStatusEqual': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'moderationStatusNotEqual': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'moderationStatusIn': getXmlNodeText, 
        'moderationStatusNotIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaEntryType"), 
        'typeIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'groupIdEqual': getXmlNodeInt, 
        'searchTextMatchAnd': getXmlNodeText, 
        'searchTextMatchOr': getXmlNodeText, 
        'accessControlIdEqual': getXmlNodeInt, 
        'accessControlIdIn': getXmlNodeText, 
        'startDateGreaterThanOrEqual': getXmlNodeInt, 
        'startDateLessThanOrEqual': getXmlNodeInt, 
        'startDateGreaterThanOrEqualOrNull': getXmlNodeInt, 
        'startDateLessThanOrEqualOrNull': getXmlNodeInt, 
        'endDateGreaterThanOrEqual': getXmlNodeInt, 
        'endDateLessThanOrEqual': getXmlNodeInt, 
        'endDateGreaterThanOrEqualOrNull': getXmlNodeInt, 
        'endDateLessThanOrEqualOrNull': getXmlNodeInt, 
        'tagsNameMultiLikeOr': getXmlNodeText, 
        'tagsAdminTagsMultiLikeOr': getXmlNodeText, 
        'tagsAdminTagsNameMultiLikeOr': getXmlNodeText, 
        'tagsNameMultiLikeAnd': getXmlNodeText, 
        'tagsAdminTagsMultiLikeAnd': getXmlNodeText, 
        'tagsAdminTagsNameMultiLikeAnd': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseEntryBaseFilter")
        kparams.addStringIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("idNotIn", self.idNotIn)
        kparams.addStringIfNotNone("nameLike", self.nameLike)
        kparams.addStringIfNotNone("nameMultiLikeOr", self.nameMultiLikeOr)
        kparams.addStringIfNotNone("nameMultiLikeAnd", self.nameMultiLikeAnd)
        kparams.addStringIfNotNone("nameEqual", self.nameEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("userIdEqual", self.userIdEqual)
        kparams.addStringIfNotNone("tagsLike", self.tagsLike)
        kparams.addStringIfNotNone("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addStringIfNotNone("adminTagsLike", self.adminTagsLike)
        kparams.addStringIfNotNone("adminTagsMultiLikeOr", self.adminTagsMultiLikeOr)
        kparams.addStringIfNotNone("adminTagsMultiLikeAnd", self.adminTagsMultiLikeAnd)
        kparams.addStringIfNotNone("categoriesMatchAnd", self.categoriesMatchAnd)
        kparams.addStringIfNotNone("categoriesMatchOr", self.categoriesMatchOr)
        kparams.addStringIfNotNone("categoriesIdsMatchAnd", self.categoriesIdsMatchAnd)
        kparams.addStringIfNotNone("categoriesIdsMatchOr", self.categoriesIdsMatchOr)
        kparams.addStringEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringEnumIfNotNone("statusNotEqual", self.statusNotEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addStringIfNotNone("statusNotIn", self.statusNotIn)
        kparams.addIntEnumIfNotNone("moderationStatusEqual", self.moderationStatusEqual)
        kparams.addIntEnumIfNotNone("moderationStatusNotEqual", self.moderationStatusNotEqual)
        kparams.addStringIfNotNone("moderationStatusIn", self.moderationStatusIn)
        kparams.addStringIfNotNone("moderationStatusNotIn", self.moderationStatusNotIn)
        kparams.addStringEnumIfNotNone("typeEqual", self.typeEqual)
        kparams.addStringIfNotNone("typeIn", self.typeIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("groupIdEqual", self.groupIdEqual)
        kparams.addStringIfNotNone("searchTextMatchAnd", self.searchTextMatchAnd)
        kparams.addStringIfNotNone("searchTextMatchOr", self.searchTextMatchOr)
        kparams.addIntIfNotNone("accessControlIdEqual", self.accessControlIdEqual)
        kparams.addStringIfNotNone("accessControlIdIn", self.accessControlIdIn)
        kparams.addIntIfNotNone("startDateGreaterThanOrEqual", self.startDateGreaterThanOrEqual)
        kparams.addIntIfNotNone("startDateLessThanOrEqual", self.startDateLessThanOrEqual)
        kparams.addIntIfNotNone("startDateGreaterThanOrEqualOrNull", self.startDateGreaterThanOrEqualOrNull)
        kparams.addIntIfNotNone("startDateLessThanOrEqualOrNull", self.startDateLessThanOrEqualOrNull)
        kparams.addIntIfNotNone("endDateGreaterThanOrEqual", self.endDateGreaterThanOrEqual)
        kparams.addIntIfNotNone("endDateLessThanOrEqual", self.endDateLessThanOrEqual)
        kparams.addIntIfNotNone("endDateGreaterThanOrEqualOrNull", self.endDateGreaterThanOrEqualOrNull)
        kparams.addIntIfNotNone("endDateLessThanOrEqualOrNull", self.endDateLessThanOrEqualOrNull)
        kparams.addStringIfNotNone("tagsNameMultiLikeOr", self.tagsNameMultiLikeOr)
        kparams.addStringIfNotNone("tagsAdminTagsMultiLikeOr", self.tagsAdminTagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsAdminTagsNameMultiLikeOr", self.tagsAdminTagsNameMultiLikeOr)
        kparams.addStringIfNotNone("tagsNameMultiLikeAnd", self.tagsNameMultiLikeAnd)
        kparams.addStringIfNotNone("tagsAdminTagsMultiLikeAnd", self.tagsAdminTagsMultiLikeAnd)
        kparams.addStringIfNotNone("tagsAdminTagsNameMultiLikeAnd", self.tagsAdminTagsNameMultiLikeAnd)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getIdNotIn(self):
        return self.idNotIn

    def setIdNotIn(self, newIdNotIn):
        self.idNotIn = newIdNotIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getNameMultiLikeOr(self):
        return self.nameMultiLikeOr

    def setNameMultiLikeOr(self, newNameMultiLikeOr):
        self.nameMultiLikeOr = newNameMultiLikeOr

    def getNameMultiLikeAnd(self):
        return self.nameMultiLikeAnd

    def setNameMultiLikeAnd(self, newNameMultiLikeAnd):
        self.nameMultiLikeAnd = newNameMultiLikeAnd

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getTagsLike(self):
        return self.tagsLike

    def setTagsLike(self, newTagsLike):
        self.tagsLike = newTagsLike

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getAdminTagsLike(self):
        return self.adminTagsLike

    def setAdminTagsLike(self, newAdminTagsLike):
        self.adminTagsLike = newAdminTagsLike

    def getAdminTagsMultiLikeOr(self):
        return self.adminTagsMultiLikeOr

    def setAdminTagsMultiLikeOr(self, newAdminTagsMultiLikeOr):
        self.adminTagsMultiLikeOr = newAdminTagsMultiLikeOr

    def getAdminTagsMultiLikeAnd(self):
        return self.adminTagsMultiLikeAnd

    def setAdminTagsMultiLikeAnd(self, newAdminTagsMultiLikeAnd):
        self.adminTagsMultiLikeAnd = newAdminTagsMultiLikeAnd

    def getCategoriesMatchAnd(self):
        return self.categoriesMatchAnd

    def setCategoriesMatchAnd(self, newCategoriesMatchAnd):
        self.categoriesMatchAnd = newCategoriesMatchAnd

    def getCategoriesMatchOr(self):
        return self.categoriesMatchOr

    def setCategoriesMatchOr(self, newCategoriesMatchOr):
        self.categoriesMatchOr = newCategoriesMatchOr

    def getCategoriesIdsMatchAnd(self):
        return self.categoriesIdsMatchAnd

    def setCategoriesIdsMatchAnd(self, newCategoriesIdsMatchAnd):
        self.categoriesIdsMatchAnd = newCategoriesIdsMatchAnd

    def getCategoriesIdsMatchOr(self):
        return self.categoriesIdsMatchOr

    def setCategoriesIdsMatchOr(self, newCategoriesIdsMatchOr):
        self.categoriesIdsMatchOr = newCategoriesIdsMatchOr

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusNotEqual(self):
        return self.statusNotEqual

    def setStatusNotEqual(self, newStatusNotEqual):
        self.statusNotEqual = newStatusNotEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn

    def getModerationStatusEqual(self):
        return self.moderationStatusEqual

    def setModerationStatusEqual(self, newModerationStatusEqual):
        self.moderationStatusEqual = newModerationStatusEqual

    def getModerationStatusNotEqual(self):
        return self.moderationStatusNotEqual

    def setModerationStatusNotEqual(self, newModerationStatusNotEqual):
        self.moderationStatusNotEqual = newModerationStatusNotEqual

    def getModerationStatusIn(self):
        return self.moderationStatusIn

    def setModerationStatusIn(self, newModerationStatusIn):
        self.moderationStatusIn = newModerationStatusIn

    def getModerationStatusNotIn(self):
        return self.moderationStatusNotIn

    def setModerationStatusNotIn(self, newModerationStatusNotIn):
        self.moderationStatusNotIn = newModerationStatusNotIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getGroupIdEqual(self):
        return self.groupIdEqual

    def setGroupIdEqual(self, newGroupIdEqual):
        self.groupIdEqual = newGroupIdEqual

    def getSearchTextMatchAnd(self):
        return self.searchTextMatchAnd

    def setSearchTextMatchAnd(self, newSearchTextMatchAnd):
        self.searchTextMatchAnd = newSearchTextMatchAnd

    def getSearchTextMatchOr(self):
        return self.searchTextMatchOr

    def setSearchTextMatchOr(self, newSearchTextMatchOr):
        self.searchTextMatchOr = newSearchTextMatchOr

    def getAccessControlIdEqual(self):
        return self.accessControlIdEqual

    def setAccessControlIdEqual(self, newAccessControlIdEqual):
        self.accessControlIdEqual = newAccessControlIdEqual

    def getAccessControlIdIn(self):
        return self.accessControlIdIn

    def setAccessControlIdIn(self, newAccessControlIdIn):
        self.accessControlIdIn = newAccessControlIdIn

    def getStartDateGreaterThanOrEqual(self):
        return self.startDateGreaterThanOrEqual

    def setStartDateGreaterThanOrEqual(self, newStartDateGreaterThanOrEqual):
        self.startDateGreaterThanOrEqual = newStartDateGreaterThanOrEqual

    def getStartDateLessThanOrEqual(self):
        return self.startDateLessThanOrEqual

    def setStartDateLessThanOrEqual(self, newStartDateLessThanOrEqual):
        self.startDateLessThanOrEqual = newStartDateLessThanOrEqual

    def getStartDateGreaterThanOrEqualOrNull(self):
        return self.startDateGreaterThanOrEqualOrNull

    def setStartDateGreaterThanOrEqualOrNull(self, newStartDateGreaterThanOrEqualOrNull):
        self.startDateGreaterThanOrEqualOrNull = newStartDateGreaterThanOrEqualOrNull

    def getStartDateLessThanOrEqualOrNull(self):
        return self.startDateLessThanOrEqualOrNull

    def setStartDateLessThanOrEqualOrNull(self, newStartDateLessThanOrEqualOrNull):
        self.startDateLessThanOrEqualOrNull = newStartDateLessThanOrEqualOrNull

    def getEndDateGreaterThanOrEqual(self):
        return self.endDateGreaterThanOrEqual

    def setEndDateGreaterThanOrEqual(self, newEndDateGreaterThanOrEqual):
        self.endDateGreaterThanOrEqual = newEndDateGreaterThanOrEqual

    def getEndDateLessThanOrEqual(self):
        return self.endDateLessThanOrEqual

    def setEndDateLessThanOrEqual(self, newEndDateLessThanOrEqual):
        self.endDateLessThanOrEqual = newEndDateLessThanOrEqual

    def getEndDateGreaterThanOrEqualOrNull(self):
        return self.endDateGreaterThanOrEqualOrNull

    def setEndDateGreaterThanOrEqualOrNull(self, newEndDateGreaterThanOrEqualOrNull):
        self.endDateGreaterThanOrEqualOrNull = newEndDateGreaterThanOrEqualOrNull

    def getEndDateLessThanOrEqualOrNull(self):
        return self.endDateLessThanOrEqualOrNull

    def setEndDateLessThanOrEqualOrNull(self, newEndDateLessThanOrEqualOrNull):
        self.endDateLessThanOrEqualOrNull = newEndDateLessThanOrEqualOrNull

    def getTagsNameMultiLikeOr(self):
        return self.tagsNameMultiLikeOr

    def setTagsNameMultiLikeOr(self, newTagsNameMultiLikeOr):
        self.tagsNameMultiLikeOr = newTagsNameMultiLikeOr

    def getTagsAdminTagsMultiLikeOr(self):
        return self.tagsAdminTagsMultiLikeOr

    def setTagsAdminTagsMultiLikeOr(self, newTagsAdminTagsMultiLikeOr):
        self.tagsAdminTagsMultiLikeOr = newTagsAdminTagsMultiLikeOr

    def getTagsAdminTagsNameMultiLikeOr(self):
        return self.tagsAdminTagsNameMultiLikeOr

    def setTagsAdminTagsNameMultiLikeOr(self, newTagsAdminTagsNameMultiLikeOr):
        self.tagsAdminTagsNameMultiLikeOr = newTagsAdminTagsNameMultiLikeOr

    def getTagsNameMultiLikeAnd(self):
        return self.tagsNameMultiLikeAnd

    def setTagsNameMultiLikeAnd(self, newTagsNameMultiLikeAnd):
        self.tagsNameMultiLikeAnd = newTagsNameMultiLikeAnd

    def getTagsAdminTagsMultiLikeAnd(self):
        return self.tagsAdminTagsMultiLikeAnd

    def setTagsAdminTagsMultiLikeAnd(self, newTagsAdminTagsMultiLikeAnd):
        self.tagsAdminTagsMultiLikeAnd = newTagsAdminTagsMultiLikeAnd

    def getTagsAdminTagsNameMultiLikeAnd(self):
        return self.tagsAdminTagsNameMultiLikeAnd

    def setTagsAdminTagsNameMultiLikeAnd(self, newTagsAdminTagsNameMultiLikeAnd):
        self.tagsAdminTagsNameMultiLikeAnd = newTagsAdminTagsNameMultiLikeAnd


class KalturaBaseEntryFilter(KalturaBaseEntryBaseFilter):
    def __init__(self):
        KalturaBaseEntryBaseFilter.__init__(self)

        # @var string
        self.freeText = None


    PROPERTY_LOADERS = {
        'freeText': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseEntryFilter")
        kparams.addStringIfNotNone("freeText", self.freeText)
        return kparams

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText


class KalturaBaseEntryListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaBaseEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBaseEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseEntryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseEntryListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaModerationFlag(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Moderation flag id
        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # The user id that added the moderation flag
        # @var string
        # @readonly
        self.userId = None

        # The type of the moderation flag (entry or user)
        # @var KalturaModerationObjectType
        # @readonly
        self.moderationObjectType = None

        # If moderation flag is set for entry, this is the flagged entry id
        # @var string
        self.flaggedEntryId = None

        # If moderation flag is set for user, this is the flagged user id
        # @var string
        self.flaggedUserId = None

        # The moderation flag status
        # @var KalturaModerationFlagStatus
        # @readonly
        self.status = None

        # The comment that was added to the flag
        # @var string
        self.comments = None

        # @var KalturaModerationFlagType
        self.flagType = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'moderationObjectType': (KalturaEnumsFactory.createInt, "KalturaModerationObjectType"), 
        'flaggedEntryId': getXmlNodeText, 
        'flaggedUserId': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaModerationFlagStatus"), 
        'comments': getXmlNodeText, 
        'flagType': (KalturaEnumsFactory.createInt, "KalturaModerationFlagType"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaModerationFlag.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaModerationFlag")
        kparams.addStringIfNotNone("flaggedEntryId", self.flaggedEntryId)
        kparams.addStringIfNotNone("flaggedUserId", self.flaggedUserId)
        kparams.addStringIfNotNone("comments", self.comments)
        kparams.addIntEnumIfNotNone("flagType", self.flagType)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def getModerationObjectType(self):
        return self.moderationObjectType

    def getFlaggedEntryId(self):
        return self.flaggedEntryId

    def setFlaggedEntryId(self, newFlaggedEntryId):
        self.flaggedEntryId = newFlaggedEntryId

    def getFlaggedUserId(self):
        return self.flaggedUserId

    def setFlaggedUserId(self, newFlaggedUserId):
        self.flaggedUserId = newFlaggedUserId

    def getStatus(self):
        return self.status

    def getComments(self):
        return self.comments

    def setComments(self, newComments):
        self.comments = newComments

    def getFlagType(self):
        return self.flagType

    def setFlagType(self, newFlagType):
        self.flagType = newFlagType

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaModerationFlagListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaModerationFlag
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaModerationFlag), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaModerationFlagListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaModerationFlagListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaEntryContextDataParams(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.referrer = None


    PROPERTY_LOADERS = {
        'referrer': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryContextDataParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryContextDataParams")
        kparams.addStringIfNotNone("referrer", self.referrer)
        return kparams

    def getReferrer(self):
        return self.referrer

    def setReferrer(self, newReferrer):
        self.referrer = newReferrer


class KalturaEntryContextDataResult(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var bool
        self.isSiteRestricted = None

        # @var bool
        self.isCountryRestricted = None

        # @var bool
        self.isSessionRestricted = None

        # @var bool
        self.isIpAddressRestricted = None

        # @var int
        self.previewLength = None

        # @var bool
        self.isScheduledNow = None

        # @var bool
        self.isAdmin = None


    PROPERTY_LOADERS = {
        'isSiteRestricted': getXmlNodeBool, 
        'isCountryRestricted': getXmlNodeBool, 
        'isSessionRestricted': getXmlNodeBool, 
        'isIpAddressRestricted': getXmlNodeBool, 
        'previewLength': getXmlNodeInt, 
        'isScheduledNow': getXmlNodeBool, 
        'isAdmin': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryContextDataResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryContextDataResult")
        kparams.addBoolIfNotNone("isSiteRestricted", self.isSiteRestricted)
        kparams.addBoolIfNotNone("isCountryRestricted", self.isCountryRestricted)
        kparams.addBoolIfNotNone("isSessionRestricted", self.isSessionRestricted)
        kparams.addBoolIfNotNone("isIpAddressRestricted", self.isIpAddressRestricted)
        kparams.addIntIfNotNone("previewLength", self.previewLength)
        kparams.addBoolIfNotNone("isScheduledNow", self.isScheduledNow)
        kparams.addBoolIfNotNone("isAdmin", self.isAdmin)
        return kparams

    def getIsSiteRestricted(self):
        return self.isSiteRestricted

    def setIsSiteRestricted(self, newIsSiteRestricted):
        self.isSiteRestricted = newIsSiteRestricted

    def getIsCountryRestricted(self):
        return self.isCountryRestricted

    def setIsCountryRestricted(self, newIsCountryRestricted):
        self.isCountryRestricted = newIsCountryRestricted

    def getIsSessionRestricted(self):
        return self.isSessionRestricted

    def setIsSessionRestricted(self, newIsSessionRestricted):
        self.isSessionRestricted = newIsSessionRestricted

    def getIsIpAddressRestricted(self):
        return self.isIpAddressRestricted

    def setIsIpAddressRestricted(self, newIsIpAddressRestricted):
        self.isIpAddressRestricted = newIsIpAddressRestricted

    def getPreviewLength(self):
        return self.previewLength

    def setPreviewLength(self, newPreviewLength):
        self.previewLength = newPreviewLength

    def getIsScheduledNow(self):
        return self.isScheduledNow

    def setIsScheduledNow(self, newIsScheduledNow):
        self.isScheduledNow = newIsScheduledNow

    def getIsAdmin(self):
        return self.isAdmin

    def setIsAdmin(self, newIsAdmin):
        self.isAdmin = newIsAdmin


class KalturaBulkUploadPluginData(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.field = None

        # @var string
        self.value = None


    PROPERTY_LOADERS = {
        'field': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadPluginData")
        kparams.addStringIfNotNone("field", self.field)
        kparams.addStringIfNotNone("value", self.value)
        return kparams

    def getField(self):
        return self.field

    def setField(self, newField):
        self.field = newField

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaBulkUploadResult(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the result
        # @var int
        # @readonly
        self.id = None

        # The id of the parent job
        # @var int
        self.bulkUploadJobId = None

        # The index of the line in the CSV
        # @var int
        self.lineIndex = None

        # @var int
        self.partnerId = None

        # @var string
        self.entryId = None

        # @var int
        self.entryStatus = None

        # The data as recieved in the csv
        # @var string
        self.rowData = None

        # @var string
        self.title = None

        # @var string
        self.description = None

        # @var string
        self.tags = None

        # @var string
        self.url = None

        # @var string
        self.contentType = None

        # @var int
        self.conversionProfileId = None

        # @var int
        self.accessControlProfileId = None

        # @var string
        self.category = None

        # @var int
        self.scheduleStartDate = None

        # @var int
        self.scheduleEndDate = None

        # @var string
        self.thumbnailUrl = None

        # @var bool
        self.thumbnailSaved = None

        # @var string
        self.partnerData = None

        # @var string
        self.errorDescription = None

        # @var array of KalturaBulkUploadPluginData
        self.pluginsData = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'bulkUploadJobId': getXmlNodeInt, 
        'lineIndex': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'entryStatus': getXmlNodeInt, 
        'rowData': getXmlNodeText, 
        'title': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'url': getXmlNodeText, 
        'contentType': getXmlNodeText, 
        'conversionProfileId': getXmlNodeInt, 
        'accessControlProfileId': getXmlNodeInt, 
        'category': getXmlNodeText, 
        'scheduleStartDate': getXmlNodeInt, 
        'scheduleEndDate': getXmlNodeInt, 
        'thumbnailUrl': getXmlNodeText, 
        'thumbnailSaved': getXmlNodeBool, 
        'partnerData': getXmlNodeText, 
        'errorDescription': getXmlNodeText, 
        'pluginsData': (KalturaObjectFactory.createArray, KalturaBulkUploadPluginData), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadResult")
        kparams.addIntIfNotNone("bulkUploadJobId", self.bulkUploadJobId)
        kparams.addIntIfNotNone("lineIndex", self.lineIndex)
        kparams.addIntIfNotNone("partnerId", self.partnerId)
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addIntIfNotNone("entryStatus", self.entryStatus)
        kparams.addStringIfNotNone("rowData", self.rowData)
        kparams.addStringIfNotNone("title", self.title)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("url", self.url)
        kparams.addStringIfNotNone("contentType", self.contentType)
        kparams.addIntIfNotNone("conversionProfileId", self.conversionProfileId)
        kparams.addIntIfNotNone("accessControlProfileId", self.accessControlProfileId)
        kparams.addStringIfNotNone("category", self.category)
        kparams.addIntIfNotNone("scheduleStartDate", self.scheduleStartDate)
        kparams.addIntIfNotNone("scheduleEndDate", self.scheduleEndDate)
        kparams.addStringIfNotNone("thumbnailUrl", self.thumbnailUrl)
        kparams.addBoolIfNotNone("thumbnailSaved", self.thumbnailSaved)
        kparams.addStringIfNotNone("partnerData", self.partnerData)
        kparams.addStringIfNotNone("errorDescription", self.errorDescription)
        kparams.addObjectIfNotNone("pluginsData", self.pluginsData)
        return kparams

    def getId(self):
        return self.id

    def getBulkUploadJobId(self):
        return self.bulkUploadJobId

    def setBulkUploadJobId(self, newBulkUploadJobId):
        self.bulkUploadJobId = newBulkUploadJobId

    def getLineIndex(self):
        return self.lineIndex

    def setLineIndex(self, newLineIndex):
        self.lineIndex = newLineIndex

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getEntryStatus(self):
        return self.entryStatus

    def setEntryStatus(self, newEntryStatus):
        self.entryStatus = newEntryStatus

    def getRowData(self):
        return self.rowData

    def setRowData(self, newRowData):
        self.rowData = newRowData

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getContentType(self):
        return self.contentType

    def setContentType(self, newContentType):
        self.contentType = newContentType

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId

    def getAccessControlProfileId(self):
        return self.accessControlProfileId

    def setAccessControlProfileId(self, newAccessControlProfileId):
        self.accessControlProfileId = newAccessControlProfileId

    def getCategory(self):
        return self.category

    def setCategory(self, newCategory):
        self.category = newCategory

    def getScheduleStartDate(self):
        return self.scheduleStartDate

    def setScheduleStartDate(self, newScheduleStartDate):
        self.scheduleStartDate = newScheduleStartDate

    def getScheduleEndDate(self):
        return self.scheduleEndDate

    def setScheduleEndDate(self, newScheduleEndDate):
        self.scheduleEndDate = newScheduleEndDate

    def getThumbnailUrl(self):
        return self.thumbnailUrl

    def setThumbnailUrl(self, newThumbnailUrl):
        self.thumbnailUrl = newThumbnailUrl

    def getThumbnailSaved(self):
        return self.thumbnailSaved

    def setThumbnailSaved(self, newThumbnailSaved):
        self.thumbnailSaved = newThumbnailSaved

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, newErrorDescription):
        self.errorDescription = newErrorDescription

    def getPluginsData(self):
        return self.pluginsData

    def setPluginsData(self, newPluginsData):
        self.pluginsData = newPluginsData


class KalturaBulkUpload(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = None

        # @var string
        self.uploadedBy = None

        # @var string
        self.uploadedByUserId = None

        # @var int
        self.uploadedOn = None

        # @var int
        self.numOfEntries = None

        # @var KalturaBatchJobStatus
        self.status = None

        # @var string
        self.logFileUrl = None

        # @var string
        self.csvFileUrl = None

        # @var array of KalturaBulkUploadResult
        self.results = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'uploadedBy': getXmlNodeText, 
        'uploadedByUserId': getXmlNodeText, 
        'uploadedOn': getXmlNodeInt, 
        'numOfEntries': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaBatchJobStatus"), 
        'logFileUrl': getXmlNodeText, 
        'csvFileUrl': getXmlNodeText, 
        'results': (KalturaObjectFactory.createArray, KalturaBulkUploadResult), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUpload.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUpload")
        kparams.addIntIfNotNone("id", self.id)
        kparams.addStringIfNotNone("uploadedBy", self.uploadedBy)
        kparams.addStringIfNotNone("uploadedByUserId", self.uploadedByUserId)
        kparams.addIntIfNotNone("uploadedOn", self.uploadedOn)
        kparams.addIntIfNotNone("numOfEntries", self.numOfEntries)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addStringIfNotNone("logFileUrl", self.logFileUrl)
        kparams.addStringIfNotNone("csvFileUrl", self.csvFileUrl)
        kparams.addObjectIfNotNone("results", self.results)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getUploadedBy(self):
        return self.uploadedBy

    def setUploadedBy(self, newUploadedBy):
        self.uploadedBy = newUploadedBy

    def getUploadedByUserId(self):
        return self.uploadedByUserId

    def setUploadedByUserId(self, newUploadedByUserId):
        self.uploadedByUserId = newUploadedByUserId

    def getUploadedOn(self):
        return self.uploadedOn

    def setUploadedOn(self, newUploadedOn):
        self.uploadedOn = newUploadedOn

    def getNumOfEntries(self):
        return self.numOfEntries

    def setNumOfEntries(self, newNumOfEntries):
        self.numOfEntries = newNumOfEntries

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getLogFileUrl(self):
        return self.logFileUrl

    def setLogFileUrl(self, newLogFileUrl):
        self.logFileUrl = newLogFileUrl

    def getCsvFileUrl(self):
        return self.csvFileUrl

    def setCsvFileUrl(self, newCsvFileUrl):
        self.csvFileUrl = newCsvFileUrl

    def getResults(self):
        return self.results

    def setResults(self, newResults):
        self.results = newResults


class KalturaBulkUploadListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaBulkUpload
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBulkUpload), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaCategory(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the Category
        # @var int
        # @readonly
        self.id = None

        # @var int
        self.parentId = None

        # @var int
        # @readonly
        self.depth = None

        # @var int
        # @readonly
        self.partnerId = None

        # The name of the Category. 
        # The following characters are not allowed: '<', '>', ','
        # @var string
        self.name = None

        # The full name of the Category
        # @var string
        # @readonly
        self.fullName = None

        # Number of entries in this Category (including child categories)
        # @var int
        # @readonly
        self.entriesCount = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'parentId': getXmlNodeInt, 
        'depth': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'fullName': getXmlNodeText, 
        'entriesCount': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCategory")
        kparams.addIntIfNotNone("parentId", self.parentId)
        kparams.addStringIfNotNone("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getParentId(self):
        return self.parentId

    def setParentId(self, newParentId):
        self.parentId = newParentId

    def getDepth(self):
        return self.depth

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getFullName(self):
        return self.fullName

    def getEntriesCount(self):
        return self.entriesCount

    def getCreatedAt(self):
        return self.createdAt


class KalturaCategoryBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var int
        self.parentIdEqual = None

        # @var string
        self.parentIdIn = None

        # @var int
        self.depthEqual = None

        # @var string
        self.fullNameEqual = None

        # @var string
        self.fullNameStartsWith = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'parentIdEqual': getXmlNodeInt, 
        'parentIdIn': getXmlNodeText, 
        'depthEqual': getXmlNodeInt, 
        'fullNameEqual': getXmlNodeText, 
        'fullNameStartsWith': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaCategoryBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("parentIdEqual", self.parentIdEqual)
        kparams.addStringIfNotNone("parentIdIn", self.parentIdIn)
        kparams.addIntIfNotNone("depthEqual", self.depthEqual)
        kparams.addStringIfNotNone("fullNameEqual", self.fullNameEqual)
        kparams.addStringIfNotNone("fullNameStartsWith", self.fullNameStartsWith)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getParentIdEqual(self):
        return self.parentIdEqual

    def setParentIdEqual(self, newParentIdEqual):
        self.parentIdEqual = newParentIdEqual

    def getParentIdIn(self):
        return self.parentIdIn

    def setParentIdIn(self, newParentIdIn):
        self.parentIdIn = newParentIdIn

    def getDepthEqual(self):
        return self.depthEqual

    def setDepthEqual(self, newDepthEqual):
        self.depthEqual = newDepthEqual

    def getFullNameEqual(self):
        return self.fullNameEqual

    def setFullNameEqual(self, newFullNameEqual):
        self.fullNameEqual = newFullNameEqual

    def getFullNameStartsWith(self):
        return self.fullNameStartsWith

    def setFullNameStartsWith(self, newFullNameStartsWith):
        self.fullNameStartsWith = newFullNameStartsWith


class KalturaCategoryFilter(KalturaCategoryBaseFilter):
    def __init__(self):
        KalturaCategoryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaCategoryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCategoryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCategoryFilter")
        return kparams


class KalturaCategoryListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaCategory
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaCategory), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCategoryListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaCropDimensions(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Crop left point
        # @var int
        self.left = None

        # Crop top point
        # @var int
        self.top = None

        # Crop width
        # @var int
        self.width = None

        # Crop height
        # @var int
        self.height = None


    PROPERTY_LOADERS = {
        'left': getXmlNodeInt, 
        'top': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCropDimensions.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCropDimensions")
        kparams.addIntIfNotNone("left", self.left)
        kparams.addIntIfNotNone("top", self.top)
        kparams.addIntIfNotNone("width", self.width)
        kparams.addIntIfNotNone("height", self.height)
        return kparams

    def getLeft(self):
        return self.left

    def setLeft(self, newLeft):
        self.left = newLeft

    def getTop(self):
        return self.top

    def setTop(self, newTop):
        self.top = newTop

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight


class KalturaConversionProfile(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the Conversion Profile
        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # The name of the Conversion Profile
        # @var string
        self.name = None

        # The description of the Conversion Profile
        # @var string
        self.description = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # List of included flavor ids (comma separated)
        # @var string
        self.flavorParamsIds = None

        # True if this Conversion Profile is the default
        # @var KalturaNullableBoolean
        self.isDefault = None

        # Cropping dimensions
        # @var KalturaCropDimensions
        self.cropDimensions = None

        # Clipping start position (in miliseconds)
        # @var int
        self.clipStart = None

        # Clipping duration (in miliseconds)
        # @var int
        self.clipDuration = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'flavorParamsIds': getXmlNodeText, 
        'isDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'cropDimensions': (KalturaObjectFactory.create, KalturaCropDimensions), 
        'clipStart': getXmlNodeInt, 
        'clipDuration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionProfile")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("flavorParamsIds", self.flavorParamsIds)
        kparams.addIntEnumIfNotNone("isDefault", self.isDefault)
        kparams.addObjectIfNotNone("cropDimensions", self.cropDimensions)
        kparams.addIntIfNotNone("clipStart", self.clipStart)
        kparams.addIntIfNotNone("clipDuration", self.clipDuration)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def getFlavorParamsIds(self):
        return self.flavorParamsIds

    def setFlavorParamsIds(self, newFlavorParamsIds):
        self.flavorParamsIds = newFlavorParamsIds

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getCropDimensions(self):
        return self.cropDimensions

    def setCropDimensions(self, newCropDimensions):
        self.cropDimensions = newCropDimensions

    def getClipStart(self):
        return self.clipStart

    def setClipStart(self, newClipStart):
        self.clipStart = newClipStart

    def getClipDuration(self):
        return self.clipDuration

    def setClipDuration(self, newClipDuration):
        self.clipDuration = newClipDuration


class KalturaConversionProfileBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.nameEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("nameEqual", self.nameEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual


class KalturaConversionProfileFilter(KalturaConversionProfileBaseFilter):
    def __init__(self):
        KalturaConversionProfileBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConversionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConversionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileFilter")
        return kparams


class KalturaConversionProfileListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaConversionProfile
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaConversionProfile), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaDataEntry(KalturaBaseEntry):
    def __init__(self):
        KalturaBaseEntry.__init__(self)

        # The data of the entry
        # @var string
        self.dataContent = None

        # indicator whether to return the object for get action with the dataContent field.
        # @var bool
        # @insertonly
        self.retrieveDataContentByGet = None


    PROPERTY_LOADERS = {
        'dataContent': getXmlNodeText, 
        'retrieveDataContentByGet': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaDataEntry")
        kparams.addStringIfNotNone("dataContent", self.dataContent)
        kparams.addBoolIfNotNone("retrieveDataContentByGet", self.retrieveDataContentByGet)
        return kparams

    def getDataContent(self):
        return self.dataContent

    def setDataContent(self, newDataContent):
        self.dataContent = newDataContent

    def getRetrieveDataContentByGet(self):
        return self.retrieveDataContentByGet

    def setRetrieveDataContentByGet(self, newRetrieveDataContentByGet):
        self.retrieveDataContentByGet = newRetrieveDataContentByGet


class KalturaDataEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self):
        KalturaBaseEntryFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaDataEntryBaseFilter")
        return kparams


class KalturaDataEntryFilter(KalturaDataEntryBaseFilter):
    def __init__(self):
        KalturaDataEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDataEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDataEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaDataEntryFilter")
        return kparams


class KalturaDataListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaDataEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaDataEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDataListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDataListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaConversionAttribute(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the flavor params, set to null for source flavor
        # @var int
        self.flavorParamsId = None

        # Attribute name
        # @var string
        self.name = None

        # Attribute value
        # @var string
        self.value = None


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConversionAttribute.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConversionAttribute")
        kparams.addIntIfNotNone("flavorParamsId", self.flavorParamsId)
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("value", self.value)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaEmailIngestionProfile(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var string
        self.name = None

        # @var string
        self.description = None

        # @var string
        self.emailAddress = None

        # @var string
        self.mailboxId = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var int
        self.conversionProfile2Id = None

        # @var KalturaEntryModerationStatus
        self.moderationStatus = None

        # @var KalturaEmailIngestionProfileStatus
        # @readonly
        self.status = None

        # @var string
        # @readonly
        self.createdAt = None

        # @var string
        self.defaultCategory = None

        # @var string
        self.defaultUserId = None

        # @var string
        self.defaultTags = None

        # @var string
        self.defaultAdminTags = None

        # @var int
        self.maxAttachmentSizeKbytes = None

        # @var int
        self.maxAttachmentsPerMail = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'emailAddress': getXmlNodeText, 
        'mailboxId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'conversionProfile2Id': getXmlNodeInt, 
        'moderationStatus': (KalturaEnumsFactory.createInt, "KalturaEntryModerationStatus"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaEmailIngestionProfileStatus"), 
        'createdAt': getXmlNodeText, 
        'defaultCategory': getXmlNodeText, 
        'defaultUserId': getXmlNodeText, 
        'defaultTags': getXmlNodeText, 
        'defaultAdminTags': getXmlNodeText, 
        'maxAttachmentSizeKbytes': getXmlNodeInt, 
        'maxAttachmentsPerMail': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEmailIngestionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEmailIngestionProfile")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("emailAddress", self.emailAddress)
        kparams.addStringIfNotNone("mailboxId", self.mailboxId)
        kparams.addIntIfNotNone("conversionProfile2Id", self.conversionProfile2Id)
        kparams.addIntEnumIfNotNone("moderationStatus", self.moderationStatus)
        kparams.addStringIfNotNone("defaultCategory", self.defaultCategory)
        kparams.addStringIfNotNone("defaultUserId", self.defaultUserId)
        kparams.addStringIfNotNone("defaultTags", self.defaultTags)
        kparams.addStringIfNotNone("defaultAdminTags", self.defaultAdminTags)
        kparams.addIntIfNotNone("maxAttachmentSizeKbytes", self.maxAttachmentSizeKbytes)
        kparams.addIntIfNotNone("maxAttachmentsPerMail", self.maxAttachmentsPerMail)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getEmailAddress(self):
        return self.emailAddress

    def setEmailAddress(self, newEmailAddress):
        self.emailAddress = newEmailAddress

    def getMailboxId(self):
        return self.mailboxId

    def setMailboxId(self, newMailboxId):
        self.mailboxId = newMailboxId

    def getPartnerId(self):
        return self.partnerId

    def getConversionProfile2Id(self):
        return self.conversionProfile2Id

    def setConversionProfile2Id(self, newConversionProfile2Id):
        self.conversionProfile2Id = newConversionProfile2Id

    def getModerationStatus(self):
        return self.moderationStatus

    def setModerationStatus(self, newModerationStatus):
        self.moderationStatus = newModerationStatus

    def getStatus(self):
        return self.status

    def getCreatedAt(self):
        return self.createdAt

    def getDefaultCategory(self):
        return self.defaultCategory

    def setDefaultCategory(self, newDefaultCategory):
        self.defaultCategory = newDefaultCategory

    def getDefaultUserId(self):
        return self.defaultUserId

    def setDefaultUserId(self, newDefaultUserId):
        self.defaultUserId = newDefaultUserId

    def getDefaultTags(self):
        return self.defaultTags

    def setDefaultTags(self, newDefaultTags):
        self.defaultTags = newDefaultTags

    def getDefaultAdminTags(self):
        return self.defaultAdminTags

    def setDefaultAdminTags(self, newDefaultAdminTags):
        self.defaultAdminTags = newDefaultAdminTags

    def getMaxAttachmentSizeKbytes(self):
        return self.maxAttachmentSizeKbytes

    def setMaxAttachmentSizeKbytes(self, newMaxAttachmentSizeKbytes):
        self.maxAttachmentSizeKbytes = newMaxAttachmentSizeKbytes

    def getMaxAttachmentsPerMail(self):
        return self.maxAttachmentsPerMail

    def setMaxAttachmentsPerMail(self, newMaxAttachmentsPerMail):
        self.maxAttachmentsPerMail = newMaxAttachmentsPerMail


class KalturaPlayableEntry(KalturaBaseEntry):
    def __init__(self):
        KalturaBaseEntry.__init__(self)

        # Number of plays
        # @var int
        # @readonly
        self.plays = None

        # Number of views
        # @var int
        # @readonly
        self.views = None

        # The width in pixels
        # @var int
        # @readonly
        self.width = None

        # The height in pixels
        # @var int
        # @readonly
        self.height = None

        # The duration in seconds
        # @var int
        # @readonly
        self.duration = None

        # The duration in miliseconds
        # @var int
        # @readonly
        self.msDuration = None

        # The duration type (short for 0-4 mins, medium for 4-20 mins, long for 20+ mins)
        # @var KalturaDurationType
        # @readonly
        self.durationType = None


    PROPERTY_LOADERS = {
        'plays': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'msDuration': getXmlNodeInt, 
        'durationType': (KalturaEnumsFactory.createString, "KalturaDurationType"), 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlayableEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaPlayableEntry")
        return kparams

    def getPlays(self):
        return self.plays

    def getViews(self):
        return self.views

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDuration(self):
        return self.duration

    def getMsDuration(self):
        return self.msDuration

    def getDurationType(self):
        return self.durationType


class KalturaMediaEntry(KalturaPlayableEntry):
    def __init__(self):
        KalturaPlayableEntry.__init__(self)

        # The media type of the entry
        # @var KalturaMediaType
        # @insertonly
        self.mediaType = None

        # Override the default conversion quality
        # @var string
        # @insertonly
        self.conversionQuality = None

        # The source type of the entry
        # @var KalturaSourceType
        # @insertonly
        self.sourceType = None

        # The search provider type used to import this entry
        # @var KalturaSearchProviderType
        # @insertonly
        self.searchProviderType = None

        # The ID of the media in the importing site
        # @var string
        # @insertonly
        self.searchProviderId = None

        # The user name used for credits
        # @var string
        self.creditUserName = None

        # The URL for credits
        # @var string
        self.creditUrl = None

        # The media date extracted from EXIF data (For images) as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.mediaDate = None

        # The URL used for playback. This is not the download URL.
        # @var string
        # @readonly
        self.dataUrl = None

        # Comma separated flavor params ids that exists for this media entry
        # @var string
        # @readonly
        self.flavorParamsIds = None


    PROPERTY_LOADERS = {
        'mediaType': (KalturaEnumsFactory.createInt, "KalturaMediaType"), 
        'conversionQuality': getXmlNodeText, 
        'sourceType': (KalturaEnumsFactory.createInt, "KalturaSourceType"), 
        'searchProviderType': (KalturaEnumsFactory.createInt, "KalturaSearchProviderType"), 
        'searchProviderId': getXmlNodeText, 
        'creditUserName': getXmlNodeText, 
        'creditUrl': getXmlNodeText, 
        'mediaDate': getXmlNodeInt, 
        'dataUrl': getXmlNodeText, 
        'flavorParamsIds': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPlayableEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntry.toParams(self)
        kparams.put("objectType", "KalturaMediaEntry")
        kparams.addIntEnumIfNotNone("mediaType", self.mediaType)
        kparams.addStringIfNotNone("conversionQuality", self.conversionQuality)
        kparams.addIntEnumIfNotNone("sourceType", self.sourceType)
        kparams.addIntEnumIfNotNone("searchProviderType", self.searchProviderType)
        kparams.addStringIfNotNone("searchProviderId", self.searchProviderId)
        kparams.addStringIfNotNone("creditUserName", self.creditUserName)
        kparams.addStringIfNotNone("creditUrl", self.creditUrl)
        return kparams

    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def getConversionQuality(self):
        return self.conversionQuality

    def setConversionQuality(self, newConversionQuality):
        self.conversionQuality = newConversionQuality

    def getSourceType(self):
        return self.sourceType

    def setSourceType(self, newSourceType):
        self.sourceType = newSourceType

    def getSearchProviderType(self):
        return self.searchProviderType

    def setSearchProviderType(self, newSearchProviderType):
        self.searchProviderType = newSearchProviderType

    def getSearchProviderId(self):
        return self.searchProviderId

    def setSearchProviderId(self, newSearchProviderId):
        self.searchProviderId = newSearchProviderId

    def getCreditUserName(self):
        return self.creditUserName

    def setCreditUserName(self, newCreditUserName):
        self.creditUserName = newCreditUserName

    def getCreditUrl(self):
        return self.creditUrl

    def setCreditUrl(self, newCreditUrl):
        self.creditUrl = newCreditUrl

    def getMediaDate(self):
        return self.mediaDate

    def getDataUrl(self):
        return self.dataUrl

    def getFlavorParamsIds(self):
        return self.flavorParamsIds


class KalturaAsset(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The ID of the Flavor Asset
        # @var string
        # @readonly
        self.id = None

        # The entry ID of the Flavor Asset
        # @var string
        # @readonly
        self.entryId = None

        # @var int
        # @readonly
        self.partnerId = None

        # The status of the Flavor Asset
        # @var KalturaFlavorAssetStatus
        # @readonly
        self.status = None

        # The version of the Flavor Asset
        # @var int
        # @readonly
        self.version = None

        # The size (in KBytes) of the Flavor Asset
        # @var int
        # @readonly
        self.size = None

        # Tags used to identify the Flavor Asset in various scenarios
        # @var string
        self.tags = None

        # The file extension
        # @var string
        self.fileExt = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # @var int
        # @readonly
        self.deletedAt = None

        # @var string
        # @readonly
        self.description = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaFlavorAssetStatus"), 
        'version': getXmlNodeInt, 
        'size': getXmlNodeInt, 
        'tags': getXmlNodeText, 
        'fileExt': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'deletedAt': getXmlNodeInt, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAsset")
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("fileExt", self.fileExt)
        return kparams

    def getId(self):
        return self.id

    def getEntryId(self):
        return self.entryId

    def getPartnerId(self):
        return self.partnerId

    def getStatus(self):
        return self.status

    def getVersion(self):
        return self.version

    def getSize(self):
        return self.size

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getFileExt(self):
        return self.fileExt

    def setFileExt(self, newFileExt):
        self.fileExt = newFileExt

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getDeletedAt(self):
        return self.deletedAt

    def getDescription(self):
        return self.description


class KalturaFlavorAsset(KalturaAsset):
    def __init__(self):
        KalturaAsset.__init__(self)

        # The Flavor Params used to create this Flavor Asset
        # @var int
        self.flavorParamsId = None

        # The width of the Flavor Asset
        # @var int
        # @readonly
        self.width = None

        # The height of the Flavor Asset
        # @var int
        # @readonly
        self.height = None

        # The overall bitrate (in KBits) of the Flavor Asset
        # @var int
        # @readonly
        self.bitrate = None

        # The frame rate (in FPS) of the Flavor Asset
        # @var int
        # @readonly
        self.frameRate = None

        # True if this Flavor Asset is the original source
        # @var bool
        self.isOriginal = None

        # True if this Flavor Asset is playable in KDP
        # @var bool
        # @readonly
        self.isWeb = None

        # The container format
        # @var string
        # @readonly
        self.containerFormat = None

        # The video codec
        # @var string
        # @readonly
        self.videoCodecId = None


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'bitrate': getXmlNodeInt, 
        'frameRate': getXmlNodeInt, 
        'isOriginal': getXmlNodeBool, 
        'isWeb': getXmlNodeBool, 
        'containerFormat': getXmlNodeText, 
        'videoCodecId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaFlavorAsset")
        kparams.addIntIfNotNone("flavorParamsId", self.flavorParamsId)
        kparams.addBoolIfNotNone("isOriginal", self.isOriginal)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getBitrate(self):
        return self.bitrate

    def getFrameRate(self):
        return self.frameRate

    def getIsOriginal(self):
        return self.isOriginal

    def setIsOriginal(self, newIsOriginal):
        self.isOriginal = newIsOriginal

    def getIsWeb(self):
        return self.isWeb

    def getContainerFormat(self):
        return self.containerFormat

    def getVideoCodecId(self):
        return self.videoCodecId


class KalturaAssetBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var string
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.entryIdEqual = None

        # @var string
        self.entryIdIn = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var KalturaFlavorAssetStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var string
        self.statusNotIn = None

        # @var int
        self.sizeGreaterThanOrEqual = None

        # @var int
        self.sizeLessThanOrEqual = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var int
        self.deletedAtGreaterThanOrEqual = None

        # @var int
        self.deletedAtLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'entryIdEqual': getXmlNodeText, 
        'entryIdIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaFlavorAssetStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
        'sizeGreaterThanOrEqual': getXmlNodeInt, 
        'sizeLessThanOrEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'deletedAtGreaterThanOrEqual': getXmlNodeInt, 
        'deletedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetBaseFilter")
        kparams.addStringIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("entryIdEqual", self.entryIdEqual)
        kparams.addStringIfNotNone("entryIdIn", self.entryIdIn)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addStringIfNotNone("statusNotIn", self.statusNotIn)
        kparams.addIntIfNotNone("sizeGreaterThanOrEqual", self.sizeGreaterThanOrEqual)
        kparams.addIntIfNotNone("sizeLessThanOrEqual", self.sizeLessThanOrEqual)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("deletedAtGreaterThanOrEqual", self.deletedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("deletedAtLessThanOrEqual", self.deletedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getEntryIdIn(self):
        return self.entryIdIn

    def setEntryIdIn(self, newEntryIdIn):
        self.entryIdIn = newEntryIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn

    def getSizeGreaterThanOrEqual(self):
        return self.sizeGreaterThanOrEqual

    def setSizeGreaterThanOrEqual(self, newSizeGreaterThanOrEqual):
        self.sizeGreaterThanOrEqual = newSizeGreaterThanOrEqual

    def getSizeLessThanOrEqual(self):
        return self.sizeLessThanOrEqual

    def setSizeLessThanOrEqual(self, newSizeLessThanOrEqual):
        self.sizeLessThanOrEqual = newSizeLessThanOrEqual

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getDeletedAtGreaterThanOrEqual(self):
        return self.deletedAtGreaterThanOrEqual

    def setDeletedAtGreaterThanOrEqual(self, newDeletedAtGreaterThanOrEqual):
        self.deletedAtGreaterThanOrEqual = newDeletedAtGreaterThanOrEqual

    def getDeletedAtLessThanOrEqual(self):
        return self.deletedAtLessThanOrEqual

    def setDeletedAtLessThanOrEqual(self, newDeletedAtLessThanOrEqual):
        self.deletedAtLessThanOrEqual = newDeletedAtLessThanOrEqual


class KalturaAssetFilter(KalturaAssetBaseFilter):
    def __init__(self):
        KalturaAssetBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetFilter")
        return kparams


class KalturaFlavorAssetListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaFlavorAsset
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFlavorAsset), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaString(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.value = None


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaString.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaString")
        kparams.addStringIfNotNone("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaAssetParams(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the Flavor Params
        # @var int
        # @readonly
        self.id = None

        # @var int
        # @readonly
        self.partnerId = None

        # The name of the Flavor Params
        # @var string
        self.name = None

        # The description of the Flavor Params
        # @var string
        self.description = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # True if those Flavor Params are part of system defaults
        # @var KalturaNullableBoolean
        # @readonly
        self.isSystemDefault = None

        # The Flavor Params tags are used to identify the flavor for different usage (e.g. web, hd, mobile)
        # @var string
        self.tags = None

        # The container format of the Flavor Params
        # @var KalturaContainerFormat
        self.format = None

        # Array of partner permisison names that required for using this asset params
        # @var array of KalturaString
        self.requiredPermissions = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'isSystemDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'tags': getXmlNodeText, 
        'format': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
        'requiredPermissions': (KalturaObjectFactory.createArray, KalturaString), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetParams")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringEnumIfNotNone("format", self.format)
        kparams.addObjectIfNotNone("requiredPermissions", self.requiredPermissions)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def getIsSystemDefault(self):
        return self.isSystemDefault

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getRequiredPermissions(self):
        return self.requiredPermissions

    def setRequiredPermissions(self, newRequiredPermissions):
        self.requiredPermissions = newRequiredPermissions


class KalturaFlavorParams(KalturaAssetParams):
    def __init__(self):
        KalturaAssetParams.__init__(self)

        # The video codec of the Flavor Params
        # @var KalturaVideoCodec
        self.videoCodec = None

        # The video bitrate (in KBits) of the Flavor Params
        # @var int
        self.videoBitrate = None

        # The audio codec of the Flavor Params
        # @var KalturaAudioCodec
        self.audioCodec = None

        # The audio bitrate (in KBits) of the Flavor Params
        # @var int
        self.audioBitrate = None

        # The number of audio channels for "downmixing"
        # @var int
        self.audioChannels = None

        # The audio sample rate of the Flavor Params
        # @var int
        self.audioSampleRate = None

        # The desired width of the Flavor Params
        # @var int
        self.width = None

        # The desired height of the Flavor Params
        # @var int
        self.height = None

        # The frame rate of the Flavor Params
        # @var int
        self.frameRate = None

        # The gop size of the Flavor Params
        # @var int
        self.gopSize = None

        # The list of conversion engines (comma separated)
        # @var string
        self.conversionEngines = None

        # The list of conversion engines extra params (separated with "|")
        # @var string
        self.conversionEnginesExtraParams = None

        # @var bool
        self.twoPass = None

        # @var int
        self.deinterlice = None

        # @var int
        self.rotate = None

        # @var string
        self.operators = None

        # @var int
        self.engineVersion = None


    PROPERTY_LOADERS = {
        'videoCodec': (KalturaEnumsFactory.createString, "KalturaVideoCodec"), 
        'videoBitrate': getXmlNodeInt, 
        'audioCodec': (KalturaEnumsFactory.createString, "KalturaAudioCodec"), 
        'audioBitrate': getXmlNodeInt, 
        'audioChannels': getXmlNodeInt, 
        'audioSampleRate': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'frameRate': getXmlNodeInt, 
        'gopSize': getXmlNodeInt, 
        'conversionEngines': getXmlNodeText, 
        'conversionEnginesExtraParams': getXmlNodeText, 
        'twoPass': getXmlNodeBool, 
        'deinterlice': getXmlNodeInt, 
        'rotate': getXmlNodeInt, 
        'operators': getXmlNodeText, 
        'engineVersion': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaFlavorParams")
        kparams.addStringEnumIfNotNone("videoCodec", self.videoCodec)
        kparams.addIntIfNotNone("videoBitrate", self.videoBitrate)
        kparams.addStringEnumIfNotNone("audioCodec", self.audioCodec)
        kparams.addIntIfNotNone("audioBitrate", self.audioBitrate)
        kparams.addIntIfNotNone("audioChannels", self.audioChannels)
        kparams.addIntIfNotNone("audioSampleRate", self.audioSampleRate)
        kparams.addIntIfNotNone("width", self.width)
        kparams.addIntIfNotNone("height", self.height)
        kparams.addIntIfNotNone("frameRate", self.frameRate)
        kparams.addIntIfNotNone("gopSize", self.gopSize)
        kparams.addStringIfNotNone("conversionEngines", self.conversionEngines)
        kparams.addStringIfNotNone("conversionEnginesExtraParams", self.conversionEnginesExtraParams)
        kparams.addBoolIfNotNone("twoPass", self.twoPass)
        kparams.addIntIfNotNone("deinterlice", self.deinterlice)
        kparams.addIntIfNotNone("rotate", self.rotate)
        kparams.addStringIfNotNone("operators", self.operators)
        kparams.addIntIfNotNone("engineVersion", self.engineVersion)
        return kparams

    def getVideoCodec(self):
        return self.videoCodec

    def setVideoCodec(self, newVideoCodec):
        self.videoCodec = newVideoCodec

    def getVideoBitrate(self):
        return self.videoBitrate

    def setVideoBitrate(self, newVideoBitrate):
        self.videoBitrate = newVideoBitrate

    def getAudioCodec(self):
        return self.audioCodec

    def setAudioCodec(self, newAudioCodec):
        self.audioCodec = newAudioCodec

    def getAudioBitrate(self):
        return self.audioBitrate

    def setAudioBitrate(self, newAudioBitrate):
        self.audioBitrate = newAudioBitrate

    def getAudioChannels(self):
        return self.audioChannels

    def setAudioChannels(self, newAudioChannels):
        self.audioChannels = newAudioChannels

    def getAudioSampleRate(self):
        return self.audioSampleRate

    def setAudioSampleRate(self, newAudioSampleRate):
        self.audioSampleRate = newAudioSampleRate

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getFrameRate(self):
        return self.frameRate

    def setFrameRate(self, newFrameRate):
        self.frameRate = newFrameRate

    def getGopSize(self):
        return self.gopSize

    def setGopSize(self, newGopSize):
        self.gopSize = newGopSize

    def getConversionEngines(self):
        return self.conversionEngines

    def setConversionEngines(self, newConversionEngines):
        self.conversionEngines = newConversionEngines

    def getConversionEnginesExtraParams(self):
        return self.conversionEnginesExtraParams

    def setConversionEnginesExtraParams(self, newConversionEnginesExtraParams):
        self.conversionEnginesExtraParams = newConversionEnginesExtraParams

    def getTwoPass(self):
        return self.twoPass

    def setTwoPass(self, newTwoPass):
        self.twoPass = newTwoPass

    def getDeinterlice(self):
        return self.deinterlice

    def setDeinterlice(self, newDeinterlice):
        self.deinterlice = newDeinterlice

    def getRotate(self):
        return self.rotate

    def setRotate(self, newRotate):
        self.rotate = newRotate

    def getOperators(self):
        return self.operators

    def setOperators(self, newOperators):
        self.operators = newOperators

    def getEngineVersion(self):
        return self.engineVersion

    def setEngineVersion(self, newEngineVersion):
        self.engineVersion = newEngineVersion


class KalturaFlavorAssetWithParams(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The Flavor Asset (Can be null when there are params without asset)
        # @var KalturaFlavorAsset
        self.flavorAsset = None

        # The Flavor Params
        # @var KalturaFlavorParams
        self.flavorParams = None

        # The entry id
        # @var string
        self.entryId = None


    PROPERTY_LOADERS = {
        'flavorAsset': (KalturaObjectFactory.create, KalturaFlavorAsset), 
        'flavorParams': (KalturaObjectFactory.create, KalturaFlavorParams), 
        'entryId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetWithParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetWithParams")
        kparams.addObjectIfNotNone("flavorAsset", self.flavorAsset)
        kparams.addObjectIfNotNone("flavorParams", self.flavorParams)
        kparams.addStringIfNotNone("entryId", self.entryId)
        return kparams

    def getFlavorAsset(self):
        return self.flavorAsset

    def setFlavorAsset(self, newFlavorAsset):
        self.flavorAsset = newFlavorAsset

    def getFlavorParams(self):
        return self.flavorParams

    def setFlavorParams(self, newFlavorParams):
        self.flavorParams = newFlavorParams

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId


class KalturaAssetParamsBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var KalturaNullableBoolean
        self.isSystemDefaultEqual = None

        # @var string
        self.tagsEqual = None

        # @var KalturaContainerFormat
        self.formatEqual = None


    PROPERTY_LOADERS = {
        'isSystemDefaultEqual': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'tagsEqual': getXmlNodeText, 
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaContainerFormat"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsBaseFilter")
        kparams.addIntEnumIfNotNone("isSystemDefaultEqual", self.isSystemDefaultEqual)
        kparams.addStringIfNotNone("tagsEqual", self.tagsEqual)
        kparams.addStringEnumIfNotNone("formatEqual", self.formatEqual)
        return kparams

    def getIsSystemDefaultEqual(self):
        return self.isSystemDefaultEqual

    def setIsSystemDefaultEqual(self, newIsSystemDefaultEqual):
        self.isSystemDefaultEqual = newIsSystemDefaultEqual

    def getTagsEqual(self):
        return self.tagsEqual

    def setTagsEqual(self, newTagsEqual):
        self.tagsEqual = newTagsEqual

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual


class KalturaAssetParamsFilter(KalturaAssetParamsBaseFilter):
    def __init__(self):
        KalturaAssetParamsBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsFilter")
        return kparams


class KalturaFlavorParamsBaseFilter(KalturaAssetParamsFilter):
    def __init__(self):
        KalturaAssetParamsFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsBaseFilter")
        return kparams


class KalturaFlavorParamsFilter(KalturaFlavorParamsBaseFilter):
    def __init__(self):
        KalturaFlavorParamsBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsFilter")
        return kparams


class KalturaFlavorParamsListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaFlavorParams
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFlavorParams), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaLiveStreamBitrate(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.bitrate = None

        # @var int
        self.width = None

        # @var int
        self.height = None


    PROPERTY_LOADERS = {
        'bitrate': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamBitrate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamBitrate")
        kparams.addIntIfNotNone("bitrate", self.bitrate)
        kparams.addIntIfNotNone("width", self.width)
        kparams.addIntIfNotNone("height", self.height)
        return kparams

    def getBitrate(self):
        return self.bitrate

    def setBitrate(self, newBitrate):
        self.bitrate = newBitrate

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight


class KalturaLiveStreamEntry(KalturaMediaEntry):
    def __init__(self):
        KalturaMediaEntry.__init__(self)

        # The message to be presented when the stream is offline
        # @var string
        self.offlineMessage = None

        # The stream id as provided by the provider
        # @var string
        # @readonly
        self.streamRemoteId = None

        # The backup stream id as provided by the provider
        # @var string
        # @readonly
        self.streamRemoteBackupId = None

        # Array of supported bitrates
        # @var array of KalturaLiveStreamBitrate
        self.bitrates = None

        # @var string
        self.primaryBroadcastingUrl = None

        # @var string
        self.secondaryBroadcastingUrl = None

        # @var string
        self.streamName = None


    PROPERTY_LOADERS = {
        'offlineMessage': getXmlNodeText, 
        'streamRemoteId': getXmlNodeText, 
        'streamRemoteBackupId': getXmlNodeText, 
        'bitrates': (KalturaObjectFactory.createArray, KalturaLiveStreamBitrate), 
        'primaryBroadcastingUrl': getXmlNodeText, 
        'secondaryBroadcastingUrl': getXmlNodeText, 
        'streamName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaMediaEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntry.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamEntry")
        kparams.addStringIfNotNone("offlineMessage", self.offlineMessage)
        kparams.addObjectIfNotNone("bitrates", self.bitrates)
        kparams.addStringIfNotNone("primaryBroadcastingUrl", self.primaryBroadcastingUrl)
        kparams.addStringIfNotNone("secondaryBroadcastingUrl", self.secondaryBroadcastingUrl)
        kparams.addStringIfNotNone("streamName", self.streamName)
        return kparams

    def getOfflineMessage(self):
        return self.offlineMessage

    def setOfflineMessage(self, newOfflineMessage):
        self.offlineMessage = newOfflineMessage

    def getStreamRemoteId(self):
        return self.streamRemoteId

    def getStreamRemoteBackupId(self):
        return self.streamRemoteBackupId

    def getBitrates(self):
        return self.bitrates

    def setBitrates(self, newBitrates):
        self.bitrates = newBitrates

    def getPrimaryBroadcastingUrl(self):
        return self.primaryBroadcastingUrl

    def setPrimaryBroadcastingUrl(self, newPrimaryBroadcastingUrl):
        self.primaryBroadcastingUrl = newPrimaryBroadcastingUrl

    def getSecondaryBroadcastingUrl(self):
        return self.secondaryBroadcastingUrl

    def setSecondaryBroadcastingUrl(self, newSecondaryBroadcastingUrl):
        self.secondaryBroadcastingUrl = newSecondaryBroadcastingUrl

    def getStreamName(self):
        return self.streamName

    def setStreamName(self, newStreamName):
        self.streamName = newStreamName


class KalturaLiveStreamAdminEntry(KalturaLiveStreamEntry):
    def __init__(self):
        KalturaLiveStreamEntry.__init__(self)

        # The broadcast primary ip
        # @var string
        self.encodingIP1 = None

        # The broadcast secondary ip
        # @var string
        self.encodingIP2 = None

        # The broadcast password
        # @var string
        self.streamPassword = None

        # The broadcast username
        # @var string
        # @readonly
        self.streamUsername = None


    PROPERTY_LOADERS = {
        'encodingIP1': getXmlNodeText, 
        'encodingIP2': getXmlNodeText, 
        'streamPassword': getXmlNodeText, 
        'streamUsername': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaLiveStreamEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamAdminEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamEntry.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamAdminEntry")
        kparams.addStringIfNotNone("encodingIP1", self.encodingIP1)
        kparams.addStringIfNotNone("encodingIP2", self.encodingIP2)
        kparams.addStringIfNotNone("streamPassword", self.streamPassword)
        return kparams

    def getEncodingIP1(self):
        return self.encodingIP1

    def setEncodingIP1(self, newEncodingIP1):
        self.encodingIP1 = newEncodingIP1

    def getEncodingIP2(self):
        return self.encodingIP2

    def setEncodingIP2(self, newEncodingIP2):
        self.encodingIP2 = newEncodingIP2

    def getStreamPassword(self):
        return self.streamPassword

    def setStreamPassword(self, newStreamPassword):
        self.streamPassword = newStreamPassword

    def getStreamUsername(self):
        return self.streamUsername


class KalturaPlayableEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self):
        KalturaBaseEntryFilter.__init__(self)

        # @var int
        self.durationLessThan = None

        # @var int
        self.durationGreaterThan = None

        # @var int
        self.durationLessThanOrEqual = None

        # @var int
        self.durationGreaterThanOrEqual = None

        # @var int
        self.msDurationLessThan = None

        # @var int
        self.msDurationGreaterThan = None

        # @var int
        self.msDurationLessThanOrEqual = None

        # @var int
        self.msDurationGreaterThanOrEqual = None

        # @var string
        self.durationTypeMatchOr = None


    PROPERTY_LOADERS = {
        'durationLessThan': getXmlNodeInt, 
        'durationGreaterThan': getXmlNodeInt, 
        'durationLessThanOrEqual': getXmlNodeInt, 
        'durationGreaterThanOrEqual': getXmlNodeInt, 
        'msDurationLessThan': getXmlNodeInt, 
        'msDurationGreaterThan': getXmlNodeInt, 
        'msDurationLessThanOrEqual': getXmlNodeInt, 
        'msDurationGreaterThanOrEqual': getXmlNodeInt, 
        'durationTypeMatchOr': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlayableEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaPlayableEntryBaseFilter")
        kparams.addIntIfNotNone("durationLessThan", self.durationLessThan)
        kparams.addIntIfNotNone("durationGreaterThan", self.durationGreaterThan)
        kparams.addIntIfNotNone("durationLessThanOrEqual", self.durationLessThanOrEqual)
        kparams.addIntIfNotNone("durationGreaterThanOrEqual", self.durationGreaterThanOrEqual)
        kparams.addIntIfNotNone("msDurationLessThan", self.msDurationLessThan)
        kparams.addIntIfNotNone("msDurationGreaterThan", self.msDurationGreaterThan)
        kparams.addIntIfNotNone("msDurationLessThanOrEqual", self.msDurationLessThanOrEqual)
        kparams.addIntIfNotNone("msDurationGreaterThanOrEqual", self.msDurationGreaterThanOrEqual)
        kparams.addStringIfNotNone("durationTypeMatchOr", self.durationTypeMatchOr)
        return kparams

    def getDurationLessThan(self):
        return self.durationLessThan

    def setDurationLessThan(self, newDurationLessThan):
        self.durationLessThan = newDurationLessThan

    def getDurationGreaterThan(self):
        return self.durationGreaterThan

    def setDurationGreaterThan(self, newDurationGreaterThan):
        self.durationGreaterThan = newDurationGreaterThan

    def getDurationLessThanOrEqual(self):
        return self.durationLessThanOrEqual

    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual):
        self.durationLessThanOrEqual = newDurationLessThanOrEqual

    def getDurationGreaterThanOrEqual(self):
        return self.durationGreaterThanOrEqual

    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual):
        self.durationGreaterThanOrEqual = newDurationGreaterThanOrEqual

    def getMsDurationLessThan(self):
        return self.msDurationLessThan

    def setMsDurationLessThan(self, newMsDurationLessThan):
        self.msDurationLessThan = newMsDurationLessThan

    def getMsDurationGreaterThan(self):
        return self.msDurationGreaterThan

    def setMsDurationGreaterThan(self, newMsDurationGreaterThan):
        self.msDurationGreaterThan = newMsDurationGreaterThan

    def getMsDurationLessThanOrEqual(self):
        return self.msDurationLessThanOrEqual

    def setMsDurationLessThanOrEqual(self, newMsDurationLessThanOrEqual):
        self.msDurationLessThanOrEqual = newMsDurationLessThanOrEqual

    def getMsDurationGreaterThanOrEqual(self):
        return self.msDurationGreaterThanOrEqual

    def setMsDurationGreaterThanOrEqual(self, newMsDurationGreaterThanOrEqual):
        self.msDurationGreaterThanOrEqual = newMsDurationGreaterThanOrEqual

    def getDurationTypeMatchOr(self):
        return self.durationTypeMatchOr

    def setDurationTypeMatchOr(self, newDurationTypeMatchOr):
        self.durationTypeMatchOr = newDurationTypeMatchOr


class KalturaPlayableEntryFilter(KalturaPlayableEntryBaseFilter):
    def __init__(self):
        KalturaPlayableEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPlayableEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlayableEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPlayableEntryFilter")
        return kparams


class KalturaMediaEntryBaseFilter(KalturaPlayableEntryFilter):
    def __init__(self):
        KalturaPlayableEntryFilter.__init__(self)

        # @var KalturaMediaType
        self.mediaTypeEqual = None

        # @var string
        self.mediaTypeIn = None

        # @var int
        self.mediaDateGreaterThanOrEqual = None

        # @var int
        self.mediaDateLessThanOrEqual = None

        # @var string
        self.flavorParamsIdsMatchOr = None

        # @var string
        self.flavorParamsIdsMatchAnd = None


    PROPERTY_LOADERS = {
        'mediaTypeEqual': (KalturaEnumsFactory.createInt, "KalturaMediaType"), 
        'mediaTypeIn': getXmlNodeText, 
        'mediaDateGreaterThanOrEqual': getXmlNodeInt, 
        'mediaDateLessThanOrEqual': getXmlNodeInt, 
        'flavorParamsIdsMatchOr': getXmlNodeText, 
        'flavorParamsIdsMatchAnd': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPlayableEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaEntryBaseFilter")
        kparams.addIntEnumIfNotNone("mediaTypeEqual", self.mediaTypeEqual)
        kparams.addStringIfNotNone("mediaTypeIn", self.mediaTypeIn)
        kparams.addIntIfNotNone("mediaDateGreaterThanOrEqual", self.mediaDateGreaterThanOrEqual)
        kparams.addIntIfNotNone("mediaDateLessThanOrEqual", self.mediaDateLessThanOrEqual)
        kparams.addStringIfNotNone("flavorParamsIdsMatchOr", self.flavorParamsIdsMatchOr)
        kparams.addStringIfNotNone("flavorParamsIdsMatchAnd", self.flavorParamsIdsMatchAnd)
        return kparams

    def getMediaTypeEqual(self):
        return self.mediaTypeEqual

    def setMediaTypeEqual(self, newMediaTypeEqual):
        self.mediaTypeEqual = newMediaTypeEqual

    def getMediaTypeIn(self):
        return self.mediaTypeIn

    def setMediaTypeIn(self, newMediaTypeIn):
        self.mediaTypeIn = newMediaTypeIn

    def getMediaDateGreaterThanOrEqual(self):
        return self.mediaDateGreaterThanOrEqual

    def setMediaDateGreaterThanOrEqual(self, newMediaDateGreaterThanOrEqual):
        self.mediaDateGreaterThanOrEqual = newMediaDateGreaterThanOrEqual

    def getMediaDateLessThanOrEqual(self):
        return self.mediaDateLessThanOrEqual

    def setMediaDateLessThanOrEqual(self, newMediaDateLessThanOrEqual):
        self.mediaDateLessThanOrEqual = newMediaDateLessThanOrEqual

    def getFlavorParamsIdsMatchOr(self):
        return self.flavorParamsIdsMatchOr

    def setFlavorParamsIdsMatchOr(self, newFlavorParamsIdsMatchOr):
        self.flavorParamsIdsMatchOr = newFlavorParamsIdsMatchOr

    def getFlavorParamsIdsMatchAnd(self):
        return self.flavorParamsIdsMatchAnd

    def setFlavorParamsIdsMatchAnd(self, newFlavorParamsIdsMatchAnd):
        self.flavorParamsIdsMatchAnd = newFlavorParamsIdsMatchAnd


class KalturaMediaEntryFilter(KalturaMediaEntryBaseFilter):
    def __init__(self):
        KalturaMediaEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaEntryFilter")
        return kparams


class KalturaLiveStreamEntryBaseFilter(KalturaMediaEntryFilter):
    def __init__(self):
        KalturaMediaEntryFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamEntryBaseFilter")
        return kparams


class KalturaLiveStreamEntryFilter(KalturaLiveStreamEntryBaseFilter):
    def __init__(self):
        KalturaLiveStreamEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaLiveStreamEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamEntryFilter")
        return kparams


class KalturaLiveStreamListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaLiveStreamEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaLiveStreamEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaSearch(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.keyWords = None

        # @var KalturaSearchProviderType
        self.searchSource = None

        # @var KalturaMediaType
        self.mediaType = None

        # Use this field to pass dynamic data for searching
        # For example - if you set this field to "mymovies_$partner_id"
        # The $partner_id will be automatically replcaed with your real partner Id
        # @var string
        self.extraData = None

        # @var string
        self.authData = None


    PROPERTY_LOADERS = {
        'keyWords': getXmlNodeText, 
        'searchSource': (KalturaEnumsFactory.createInt, "KalturaSearchProviderType"), 
        'mediaType': (KalturaEnumsFactory.createInt, "KalturaMediaType"), 
        'extraData': getXmlNodeText, 
        'authData': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearch.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearch")
        kparams.addStringIfNotNone("keyWords", self.keyWords)
        kparams.addIntEnumIfNotNone("searchSource", self.searchSource)
        kparams.addIntEnumIfNotNone("mediaType", self.mediaType)
        kparams.addStringIfNotNone("extraData", self.extraData)
        kparams.addStringIfNotNone("authData", self.authData)
        return kparams

    def getKeyWords(self):
        return self.keyWords

    def setKeyWords(self, newKeyWords):
        self.keyWords = newKeyWords

    def getSearchSource(self):
        return self.searchSource

    def setSearchSource(self, newSearchSource):
        self.searchSource = newSearchSource

    def getMediaType(self):
        return self.mediaType

    def setMediaType(self, newMediaType):
        self.mediaType = newMediaType

    def getExtraData(self):
        return self.extraData

    def setExtraData(self, newExtraData):
        self.extraData = newExtraData

    def getAuthData(self):
        return self.authData

    def setAuthData(self, newAuthData):
        self.authData = newAuthData


class KalturaSearchResult(KalturaSearch):
    def __init__(self):
        KalturaSearch.__init__(self)

        # @var string
        self.id = None

        # @var string
        self.title = None

        # @var string
        self.thumbUrl = None

        # @var string
        self.description = None

        # @var string
        self.tags = None

        # @var string
        self.url = None

        # @var string
        self.sourceLink = None

        # @var string
        self.credit = None

        # @var KalturaLicenseType
        self.licenseType = None

        # @var string
        self.flashPlaybackType = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'title': getXmlNodeText, 
        'thumbUrl': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'url': getXmlNodeText, 
        'sourceLink': getXmlNodeText, 
        'credit': getXmlNodeText, 
        'licenseType': (KalturaEnumsFactory.createInt, "KalturaLicenseType"), 
        'flashPlaybackType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearch.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearch.toParams(self)
        kparams.put("objectType", "KalturaSearchResult")
        kparams.addStringIfNotNone("id", self.id)
        kparams.addStringIfNotNone("title", self.title)
        kparams.addStringIfNotNone("thumbUrl", self.thumbUrl)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("url", self.url)
        kparams.addStringIfNotNone("sourceLink", self.sourceLink)
        kparams.addStringIfNotNone("credit", self.credit)
        kparams.addIntEnumIfNotNone("licenseType", self.licenseType)
        kparams.addStringIfNotNone("flashPlaybackType", self.flashPlaybackType)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getThumbUrl(self):
        return self.thumbUrl

    def setThumbUrl(self, newThumbUrl):
        self.thumbUrl = newThumbUrl

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getSourceLink(self):
        return self.sourceLink

    def setSourceLink(self, newSourceLink):
        self.sourceLink = newSourceLink

    def getCredit(self):
        return self.credit

    def setCredit(self, newCredit):
        self.credit = newCredit

    def getLicenseType(self):
        return self.licenseType

    def setLicenseType(self, newLicenseType):
        self.licenseType = newLicenseType

    def getFlashPlaybackType(self):
        return self.flashPlaybackType

    def setFlashPlaybackType(self, newFlashPlaybackType):
        self.flashPlaybackType = newFlashPlaybackType


class KalturaMediaListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMediaEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMediaEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMixEntry(KalturaPlayableEntry):
    def __init__(self):
        KalturaPlayableEntry.__init__(self)

        # Indicates whether the user has submited a real thumbnail to the mix (Not the one that was generated automaticaly)
        # @var bool
        # @readonly
        self.hasRealThumbnail = None

        # The editor type used to edit the metadata
        # @var KalturaEditorType
        self.editorType = None

        # The xml data of the mix
        # @var string
        self.dataContent = None


    PROPERTY_LOADERS = {
        'hasRealThumbnail': getXmlNodeBool, 
        'editorType': (KalturaEnumsFactory.createInt, "KalturaEditorType"), 
        'dataContent': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPlayableEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntry.toParams(self)
        kparams.put("objectType", "KalturaMixEntry")
        kparams.addIntEnumIfNotNone("editorType", self.editorType)
        kparams.addStringIfNotNone("dataContent", self.dataContent)
        return kparams

    def getHasRealThumbnail(self):
        return self.hasRealThumbnail

    def getEditorType(self):
        return self.editorType

    def setEditorType(self, newEditorType):
        self.editorType = newEditorType

    def getDataContent(self):
        return self.dataContent

    def setDataContent(self, newDataContent):
        self.dataContent = newDataContent


class KalturaMixEntryBaseFilter(KalturaPlayableEntryFilter):
    def __init__(self):
        KalturaPlayableEntryFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPlayableEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlayableEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaMixEntryBaseFilter")
        return kparams


class KalturaMixEntryFilter(KalturaMixEntryBaseFilter):
    def __init__(self):
        KalturaMixEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMixEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMixEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMixEntryFilter")
        return kparams


class KalturaMixListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaMixEntry
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaMixEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMixListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMixListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaClientNotification(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The URL where the notification should be sent to
        # @var string
        self.url = None

        # The serialized notification data to send
        # @var string
        self.data = None


    PROPERTY_LOADERS = {
        'url': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaClientNotification.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaClientNotification")
        kparams.addStringIfNotNone("url", self.url)
        kparams.addStringIfNotNone("data", self.data)
        return kparams

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaKeyValue(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.key = None

        # @var string
        self.value = None


    PROPERTY_LOADERS = {
        'key': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaKeyValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaKeyValue")
        kparams.addStringIfNotNone("key", self.key)
        kparams.addStringIfNotNone("value", self.value)
        return kparams

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaPartner(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var string
        self.name = None

        # @var string
        self.website = None

        # @var string
        self.notificationUrl = None

        # @var int
        self.appearInSearch = None

        # @var string
        # @readonly
        self.createdAt = None

        # deprecated - lastName and firstName replaces this field
        # @var string
        self.adminName = None

        # @var string
        self.adminEmail = None

        # @var string
        self.description = None

        # @var KalturaCommercialUseType
        self.commercialUse = None

        # @var string
        self.landingPage = None

        # @var string
        self.userLandingPage = None

        # @var string
        self.contentCategories = None

        # @var KalturaPartnerType
        self.type = None

        # @var string
        self.phone = None

        # @var string
        self.describeYourself = None

        # @var bool
        self.adultContent = None

        # @var string
        self.defConversionProfileType = None

        # @var int
        self.notify = None

        # @var int
        # @readonly
        self.status = None

        # @var int
        self.allowQuickEdit = None

        # @var int
        self.mergeEntryLists = None

        # @var string
        self.notificationsConfig = None

        # @var int
        self.maxUploadSize = None

        # @var int
        # @readonly
        self.partnerPackage = None

        # @var string
        # @readonly
        self.secret = None

        # @var string
        # @readonly
        self.adminSecret = None

        # @var string
        # @readonly
        self.cmsPassword = None

        # @var int
        self.allowMultiNotification = None

        # @var int
        # @readonly
        self.adminLoginUsersQuota = None

        # @var string
        self.adminUserId = None

        # firstName and lastName replace the old (deprecated) adminName
        # @var string
        self.firstName = None

        # lastName and firstName replace the old (deprecated) adminName
        # @var string
        self.lastName = None

        # country code (2char) - this field is optional
        # @var string
        self.country = None

        # state code (2char) - this field is optional
        # @var string
        self.state = None

        # @var array of KalturaKeyValue
        # @insertonly
        self.additionalParams = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'website': getXmlNodeText, 
        'notificationUrl': getXmlNodeText, 
        'appearInSearch': getXmlNodeInt, 
        'createdAt': getXmlNodeText, 
        'adminName': getXmlNodeText, 
        'adminEmail': getXmlNodeText, 
        'description': getXmlNodeText, 
        'commercialUse': (KalturaEnumsFactory.createInt, "KalturaCommercialUseType"), 
        'landingPage': getXmlNodeText, 
        'userLandingPage': getXmlNodeText, 
        'contentCategories': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createInt, "KalturaPartnerType"), 
        'phone': getXmlNodeText, 
        'describeYourself': getXmlNodeText, 
        'adultContent': getXmlNodeBool, 
        'defConversionProfileType': getXmlNodeText, 
        'notify': getXmlNodeInt, 
        'status': getXmlNodeInt, 
        'allowQuickEdit': getXmlNodeInt, 
        'mergeEntryLists': getXmlNodeInt, 
        'notificationsConfig': getXmlNodeText, 
        'maxUploadSize': getXmlNodeInt, 
        'partnerPackage': getXmlNodeInt, 
        'secret': getXmlNodeText, 
        'adminSecret': getXmlNodeText, 
        'cmsPassword': getXmlNodeText, 
        'allowMultiNotification': getXmlNodeInt, 
        'adminLoginUsersQuota': getXmlNodeInt, 
        'adminUserId': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
        'country': getXmlNodeText, 
        'state': getXmlNodeText, 
        'additionalParams': (KalturaObjectFactory.createArray, KalturaKeyValue), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartner.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartner")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("website", self.website)
        kparams.addStringIfNotNone("notificationUrl", self.notificationUrl)
        kparams.addIntIfNotNone("appearInSearch", self.appearInSearch)
        kparams.addStringIfNotNone("adminName", self.adminName)
        kparams.addStringIfNotNone("adminEmail", self.adminEmail)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addIntEnumIfNotNone("commercialUse", self.commercialUse)
        kparams.addStringIfNotNone("landingPage", self.landingPage)
        kparams.addStringIfNotNone("userLandingPage", self.userLandingPage)
        kparams.addStringIfNotNone("contentCategories", self.contentCategories)
        kparams.addIntEnumIfNotNone("type", self.type)
        kparams.addStringIfNotNone("phone", self.phone)
        kparams.addStringIfNotNone("describeYourself", self.describeYourself)
        kparams.addBoolIfNotNone("adultContent", self.adultContent)
        kparams.addStringIfNotNone("defConversionProfileType", self.defConversionProfileType)
        kparams.addIntIfNotNone("notify", self.notify)
        kparams.addIntIfNotNone("allowQuickEdit", self.allowQuickEdit)
        kparams.addIntIfNotNone("mergeEntryLists", self.mergeEntryLists)
        kparams.addStringIfNotNone("notificationsConfig", self.notificationsConfig)
        kparams.addIntIfNotNone("maxUploadSize", self.maxUploadSize)
        kparams.addIntIfNotNone("allowMultiNotification", self.allowMultiNotification)
        kparams.addStringIfNotNone("adminUserId", self.adminUserId)
        kparams.addStringIfNotNone("firstName", self.firstName)
        kparams.addStringIfNotNone("lastName", self.lastName)
        kparams.addStringIfNotNone("country", self.country)
        kparams.addStringIfNotNone("state", self.state)
        kparams.addObjectIfNotNone("additionalParams", self.additionalParams)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getWebsite(self):
        return self.website

    def setWebsite(self, newWebsite):
        self.website = newWebsite

    def getNotificationUrl(self):
        return self.notificationUrl

    def setNotificationUrl(self, newNotificationUrl):
        self.notificationUrl = newNotificationUrl

    def getAppearInSearch(self):
        return self.appearInSearch

    def setAppearInSearch(self, newAppearInSearch):
        self.appearInSearch = newAppearInSearch

    def getCreatedAt(self):
        return self.createdAt

    def getAdminName(self):
        return self.adminName

    def setAdminName(self, newAdminName):
        self.adminName = newAdminName

    def getAdminEmail(self):
        return self.adminEmail

    def setAdminEmail(self, newAdminEmail):
        self.adminEmail = newAdminEmail

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCommercialUse(self):
        return self.commercialUse

    def setCommercialUse(self, newCommercialUse):
        self.commercialUse = newCommercialUse

    def getLandingPage(self):
        return self.landingPage

    def setLandingPage(self, newLandingPage):
        self.landingPage = newLandingPage

    def getUserLandingPage(self):
        return self.userLandingPage

    def setUserLandingPage(self, newUserLandingPage):
        self.userLandingPage = newUserLandingPage

    def getContentCategories(self):
        return self.contentCategories

    def setContentCategories(self, newContentCategories):
        self.contentCategories = newContentCategories

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getPhone(self):
        return self.phone

    def setPhone(self, newPhone):
        self.phone = newPhone

    def getDescribeYourself(self):
        return self.describeYourself

    def setDescribeYourself(self, newDescribeYourself):
        self.describeYourself = newDescribeYourself

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent

    def getDefConversionProfileType(self):
        return self.defConversionProfileType

    def setDefConversionProfileType(self, newDefConversionProfileType):
        self.defConversionProfileType = newDefConversionProfileType

    def getNotify(self):
        return self.notify

    def setNotify(self, newNotify):
        self.notify = newNotify

    def getStatus(self):
        return self.status

    def getAllowQuickEdit(self):
        return self.allowQuickEdit

    def setAllowQuickEdit(self, newAllowQuickEdit):
        self.allowQuickEdit = newAllowQuickEdit

    def getMergeEntryLists(self):
        return self.mergeEntryLists

    def setMergeEntryLists(self, newMergeEntryLists):
        self.mergeEntryLists = newMergeEntryLists

    def getNotificationsConfig(self):
        return self.notificationsConfig

    def setNotificationsConfig(self, newNotificationsConfig):
        self.notificationsConfig = newNotificationsConfig

    def getMaxUploadSize(self):
        return self.maxUploadSize

    def setMaxUploadSize(self, newMaxUploadSize):
        self.maxUploadSize = newMaxUploadSize

    def getPartnerPackage(self):
        return self.partnerPackage

    def getSecret(self):
        return self.secret

    def getAdminSecret(self):
        return self.adminSecret

    def getCmsPassword(self):
        return self.cmsPassword

    def getAllowMultiNotification(self):
        return self.allowMultiNotification

    def setAllowMultiNotification(self, newAllowMultiNotification):
        self.allowMultiNotification = newAllowMultiNotification

    def getAdminLoginUsersQuota(self):
        return self.adminLoginUsersQuota

    def getAdminUserId(self):
        return self.adminUserId

    def setAdminUserId(self, newAdminUserId):
        self.adminUserId = newAdminUserId

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getCountry(self):
        return self.country

    def setCountry(self, newCountry):
        self.country = newCountry

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState

    def getAdditionalParams(self):
        return self.additionalParams

    def setAdditionalParams(self, newAdditionalParams):
        self.additionalParams = newAdditionalParams


class KalturaPartnerUsage(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var float
        # @readonly
        self.hostingGB = None

        # @var float
        # @readonly
        self.Percent = None

        # @var int
        # @readonly
        self.packageBW = None

        # @var int
        # @readonly
        self.usageGB = None

        # @var int
        # @readonly
        self.reachedLimitDate = None

        # @var string
        # @readonly
        self.usageGraph = None


    PROPERTY_LOADERS = {
        'hostingGB': getXmlNodeFloat, 
        'Percent': getXmlNodeFloat, 
        'packageBW': getXmlNodeInt, 
        'usageGB': getXmlNodeInt, 
        'reachedLimitDate': getXmlNodeInt, 
        'usageGraph': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerUsage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartnerUsage")
        return kparams

    def getHostingGB(self):
        return self.hostingGB

    def getPercent(self):
        return self.Percent

    def getPackageBW(self):
        return self.packageBW

    def getUsageGB(self):
        return self.usageGB

    def getReachedLimitDate(self):
        return self.reachedLimitDate

    def getUsageGraph(self):
        return self.usageGraph


class KalturaPermissionItem(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var KalturaPermissionItemType
        # @readonly
        self.type = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.tags = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaPermissionItemType"), 
        'partnerId': getXmlNodeInt, 
        'tags': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionItem")
        kparams.addStringIfNotNone("tags", self.tags)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getPartnerId(self):
        return self.partnerId

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaPermissionItemBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var KalturaPermissionItemType
        self.typeEqual = None

        # @var string
        self.typeIn = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var string
        self.tagsMultiLikeOr = None

        # @var string
        self.tagsMultiLikeAnd = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaPermissionItemType"), 
        'typeIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionItemBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringEnumIfNotNone("typeEqual", self.typeEqual)
        kparams.addStringIfNotNone("typeIn", self.typeIn)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual


class KalturaPermissionItemFilter(KalturaPermissionItemBaseFilter):
    def __init__(self):
        KalturaPermissionItemBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionItemFilter")
        return kparams


class KalturaPermissionItemListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPermissionItem
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPermissionItem), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItemListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionItemListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaPermission(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var KalturaPermissionType
        # @readonly
        self.type = None

        # @var string
        self.name = None

        # @var string
        self.friendlyName = None

        # @var string
        self.description = None

        # @var KalturaPermissionStatus
        self.status = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.dependsOnPermissionNames = None

        # @var string
        self.tags = None

        # @var string
        self.permissionItemsIds = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # @var string
        self.partnerGroup = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createInt, "KalturaPermissionType"), 
        'name': getXmlNodeText, 
        'friendlyName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaPermissionStatus"), 
        'partnerId': getXmlNodeInt, 
        'dependsOnPermissionNames': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'permissionItemsIds': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerGroup': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermission.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermission")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("friendlyName", self.friendlyName)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addStringIfNotNone("dependsOnPermissionNames", self.dependsOnPermissionNames)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("permissionItemsIds", self.permissionItemsIds)
        kparams.addStringIfNotNone("partnerGroup", self.partnerGroup)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getFriendlyName(self):
        return self.friendlyName

    def setFriendlyName(self, newFriendlyName):
        self.friendlyName = newFriendlyName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getPartnerId(self):
        return self.partnerId

    def getDependsOnPermissionNames(self):
        return self.dependsOnPermissionNames

    def setDependsOnPermissionNames(self, newDependsOnPermissionNames):
        self.dependsOnPermissionNames = newDependsOnPermissionNames

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getPermissionItemsIds(self):
        return self.permissionItemsIds

    def setPermissionItemsIds(self, newPermissionItemsIds):
        self.permissionItemsIds = newPermissionItemsIds

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerGroup(self):
        return self.partnerGroup

    def setPartnerGroup(self, newPartnerGroup):
        self.partnerGroup = newPartnerGroup


class KalturaPermissionBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var KalturaPermissionType
        self.typeEqual = None

        # @var string
        self.typeIn = None

        # @var string
        self.nameEqual = None

        # @var string
        self.nameIn = None

        # @var string
        self.friendlyNameLike = None

        # @var string
        self.descriptionLike = None

        # @var KalturaPermissionStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var string
        self.dependsOnPermissionNamesMultiLikeOr = None

        # @var string
        self.dependsOnPermissionNamesMultiLikeAnd = None

        # @var string
        self.tagsMultiLikeOr = None

        # @var string
        self.tagsMultiLikeAnd = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createInt, "KalturaPermissionType"), 
        'typeIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'nameIn': getXmlNodeText, 
        'friendlyNameLike': getXmlNodeText, 
        'descriptionLike': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaPermissionStatus"), 
        'statusIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'dependsOnPermissionNamesMultiLikeOr': getXmlNodeText, 
        'dependsOnPermissionNamesMultiLikeAnd': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntEnumIfNotNone("typeEqual", self.typeEqual)
        kparams.addStringIfNotNone("typeIn", self.typeIn)
        kparams.addStringIfNotNone("nameEqual", self.nameEqual)
        kparams.addStringIfNotNone("nameIn", self.nameIn)
        kparams.addStringIfNotNone("friendlyNameLike", self.friendlyNameLike)
        kparams.addStringIfNotNone("descriptionLike", self.descriptionLike)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("dependsOnPermissionNamesMultiLikeOr", self.dependsOnPermissionNamesMultiLikeOr)
        kparams.addStringIfNotNone("dependsOnPermissionNamesMultiLikeAnd", self.dependsOnPermissionNamesMultiLikeAnd)
        kparams.addStringIfNotNone("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getNameIn(self):
        return self.nameIn

    def setNameIn(self, newNameIn):
        self.nameIn = newNameIn

    def getFriendlyNameLike(self):
        return self.friendlyNameLike

    def setFriendlyNameLike(self, newFriendlyNameLike):
        self.friendlyNameLike = newFriendlyNameLike

    def getDescriptionLike(self):
        return self.descriptionLike

    def setDescriptionLike(self, newDescriptionLike):
        self.descriptionLike = newDescriptionLike

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getDependsOnPermissionNamesMultiLikeOr(self):
        return self.dependsOnPermissionNamesMultiLikeOr

    def setDependsOnPermissionNamesMultiLikeOr(self, newDependsOnPermissionNamesMultiLikeOr):
        self.dependsOnPermissionNamesMultiLikeOr = newDependsOnPermissionNamesMultiLikeOr

    def getDependsOnPermissionNamesMultiLikeAnd(self):
        return self.dependsOnPermissionNamesMultiLikeAnd

    def setDependsOnPermissionNamesMultiLikeAnd(self, newDependsOnPermissionNamesMultiLikeAnd):
        self.dependsOnPermissionNamesMultiLikeAnd = newDependsOnPermissionNamesMultiLikeAnd

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual


class KalturaPermissionFilter(KalturaPermissionBaseFilter):
    def __init__(self):
        KalturaPermissionBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionFilter")
        return kparams


class KalturaPermissionListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPermission
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPermission), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaMediaEntryFilterForPlaylist(KalturaMediaEntryFilter):
    def __init__(self):
        KalturaMediaEntryFilter.__init__(self)

        # @var int
        self.limit = None


    PROPERTY_LOADERS = {
        'limit': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaMediaEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaEntryFilterForPlaylist.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaEntryFilterForPlaylist")
        kparams.addIntIfNotNone("limit", self.limit)
        return kparams

    def getLimit(self):
        return self.limit

    def setLimit(self, newLimit):
        self.limit = newLimit


class KalturaPlaylist(KalturaBaseEntry):
    def __init__(self):
        KalturaBaseEntry.__init__(self)

        # Content of the playlist - 
        # XML if the playlistType is dynamic 
        # text if the playlistType is static 
        # url if the playlistType is mRss
        # @var string
        self.playlistContent = None

        # @var array of KalturaMediaEntryFilterForPlaylist
        self.filters = None

        # @var int
        self.totalResults = None

        # Type of playlist
        # @var KalturaPlaylistType
        self.playlistType = None

        # Number of plays
        # @var int
        # @readonly
        self.plays = None

        # Number of views
        # @var int
        # @readonly
        self.views = None

        # The duration in seconds
        # @var int
        # @readonly
        self.duration = None


    PROPERTY_LOADERS = {
        'playlistContent': getXmlNodeText, 
        'filters': (KalturaObjectFactory.createArray, KalturaMediaEntryFilterForPlaylist), 
        'totalResults': getXmlNodeInt, 
        'playlistType': (KalturaEnumsFactory.createInt, "KalturaPlaylistType"), 
        'plays': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylist.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaPlaylist")
        kparams.addStringIfNotNone("playlistContent", self.playlistContent)
        kparams.addObjectIfNotNone("filters", self.filters)
        kparams.addIntIfNotNone("totalResults", self.totalResults)
        kparams.addIntEnumIfNotNone("playlistType", self.playlistType)
        return kparams

    def getPlaylistContent(self):
        return self.playlistContent

    def setPlaylistContent(self, newPlaylistContent):
        self.playlistContent = newPlaylistContent

    def getFilters(self):
        return self.filters

    def setFilters(self, newFilters):
        self.filters = newFilters

    def getTotalResults(self):
        return self.totalResults

    def setTotalResults(self, newTotalResults):
        self.totalResults = newTotalResults

    def getPlaylistType(self):
        return self.playlistType

    def setPlaylistType(self, newPlaylistType):
        self.playlistType = newPlaylistType

    def getPlays(self):
        return self.plays

    def getViews(self):
        return self.views

    def getDuration(self):
        return self.duration


class KalturaPlaylistBaseFilter(KalturaBaseEntryFilter):
    def __init__(self):
        KalturaBaseEntryFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylistBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaPlaylistBaseFilter")
        return kparams


class KalturaPlaylistFilter(KalturaPlaylistBaseFilter):
    def __init__(self):
        KalturaPlaylistBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPlaylistBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylistFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPlaylistBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPlaylistFilter")
        return kparams


class KalturaPlaylistListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPlaylist
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPlaylist), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaylistListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPlaylistListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaReportInputFilter(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        self.fromDate = None

        # @var int
        self.toDate = None

        # @var string
        self.keywords = None

        # @var bool
        self.searchInTags = None

        # @var bool
        self.searchInAdminTags = None

        # @var string
        self.categories = None

        # time zone offset in minutes
        # @var int
        self.timeZoneOffset = None


    PROPERTY_LOADERS = {
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
        'keywords': getXmlNodeText, 
        'searchInTags': getXmlNodeBool, 
        'searchInAdminTags': getXmlNodeBool, 
        'categories': getXmlNodeText, 
        'timeZoneOffset': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportInputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportInputFilter")
        kparams.addIntIfNotNone("fromDate", self.fromDate)
        kparams.addIntIfNotNone("toDate", self.toDate)
        kparams.addStringIfNotNone("keywords", self.keywords)
        kparams.addBoolIfNotNone("searchInTags", self.searchInTags)
        kparams.addBoolIfNotNone("searchInAdminTags", self.searchInAdminTags)
        kparams.addStringIfNotNone("categories", self.categories)
        kparams.addIntIfNotNone("timeZoneOffset", self.timeZoneOffset)
        return kparams

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate

    def getKeywords(self):
        return self.keywords

    def setKeywords(self, newKeywords):
        self.keywords = newKeywords

    def getSearchInTags(self):
        return self.searchInTags

    def setSearchInTags(self, newSearchInTags):
        self.searchInTags = newSearchInTags

    def getSearchInAdminTags(self):
        return self.searchInAdminTags

    def setSearchInAdminTags(self, newSearchInAdminTags):
        self.searchInAdminTags = newSearchInAdminTags

    def getCategories(self):
        return self.categories

    def setCategories(self, newCategories):
        self.categories = newCategories

    def getTimeZoneOffset(self):
        return self.timeZoneOffset

    def setTimeZoneOffset(self, newTimeZoneOffset):
        self.timeZoneOffset = newTimeZoneOffset


class KalturaReportGraph(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.id = None

        # @var string
        self.data = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportGraph.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportGraph")
        kparams.addStringIfNotNone("id", self.id)
        kparams.addStringIfNotNone("data", self.data)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaReportTotal(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.header = None

        # @var string
        self.data = None


    PROPERTY_LOADERS = {
        'header': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportTotal.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportTotal")
        kparams.addStringIfNotNone("header", self.header)
        kparams.addStringIfNotNone("data", self.data)
        return kparams

    def getHeader(self):
        return self.header

    def setHeader(self, newHeader):
        self.header = newHeader

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaReportTable(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.header = None

        # @var string
        # @readonly
        self.data = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'header': getXmlNodeText, 
        'data': getXmlNodeText, 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportTable.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReportTable")
        return kparams

    def getHeader(self):
        return self.header

    def getData(self):
        return self.data

    def getTotalCount(self):
        return self.totalCount


class KalturaSearchResultResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaSearchResult
        # @readonly
        self.objects = None

        # @var bool
        # @readonly
        self.needMediaInfo = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSearchResult), 
        'needMediaInfo': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchResultResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchResultResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getNeedMediaInfo(self):
        return self.needMediaInfo


class KalturaSearchAuthData(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The authentication data that further should be used for search
        # @var string
        self.authData = None

        # Login URL when user need to sign-in and authorize the search
        # @var string
        self.loginUrl = None

        # Information when there was an error
        # @var string
        self.message = None


    PROPERTY_LOADERS = {
        'authData': getXmlNodeText, 
        'loginUrl': getXmlNodeText, 
        'message': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchAuthData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchAuthData")
        kparams.addStringIfNotNone("authData", self.authData)
        kparams.addStringIfNotNone("loginUrl", self.loginUrl)
        kparams.addStringIfNotNone("message", self.message)
        return kparams

    def getAuthData(self):
        return self.authData

    def setAuthData(self, newAuthData):
        self.authData = newAuthData

    def getLoginUrl(self):
        return self.loginUrl

    def setLoginUrl(self, newLoginUrl):
        self.loginUrl = newLoginUrl

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage


class KalturaStartWidgetSessionResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        # @readonly
        self.ks = None

        # @var string
        # @readonly
        self.userId = None


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'ks': getXmlNodeText, 
        'userId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStartWidgetSessionResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStartWidgetSessionResponse")
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def getKs(self):
        return self.ks

    def getUserId(self):
        return self.userId


class KalturaStatsEvent(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.clientVer = None

        # @var KalturaStatsEventType
        self.eventType = None

        # the client's timestamp of this event
        # @var float
        self.eventTimestamp = None

        # a unique string generated by the client that will represent the client-side session: the primary component will pass it on to other components that sprout from it
        # @var string
        self.sessionId = None

        # @var int
        self.partnerId = None

        # @var string
        self.entryId = None

        # the UV cookie - creates in the operational system and should be passed on ofr every event
        # @var string
        self.uniqueViewer = None

        # @var string
        self.widgetId = None

        # @var int
        self.uiconfId = None

        # the partner's user id
        # @var string
        self.userId = None

        # the timestamp along the video when the event happend
        # @var int
        self.currentPoint = None

        # the duration of the video in milliseconds - will make it much faster than quering the db for each entry
        # @var int
        self.duration = None

        # will be retrieved from the request of the user
        # @var string
        # @readonly
        self.userIp = None

        # the time in milliseconds the event took
        # @var int
        self.processDuration = None

        # the id of the GUI control - will be used in the future to better understand what the user clicked
        # @var string
        self.controlId = None

        # true if the user ever used seek in this session
        # @var bool
        self.seek = None

        # timestamp of the new point on the timeline of the video after the user seeks
        # @var int
        self.newPoint = None

        # the referrer of the client
        # @var string
        self.referrer = None

        # will indicate if the event is thrown for the first video in the session
        # @var bool
        self.isFirstInSession = None


    PROPERTY_LOADERS = {
        'clientVer': getXmlNodeText, 
        'eventType': (KalturaEnumsFactory.createInt, "KalturaStatsEventType"), 
        'eventTimestamp': getXmlNodeFloat, 
        'sessionId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'uniqueViewer': getXmlNodeText, 
        'widgetId': getXmlNodeText, 
        'uiconfId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'currentPoint': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'userIp': getXmlNodeText, 
        'processDuration': getXmlNodeInt, 
        'controlId': getXmlNodeText, 
        'seek': getXmlNodeBool, 
        'newPoint': getXmlNodeInt, 
        'referrer': getXmlNodeText, 
        'isFirstInSession': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStatsEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStatsEvent")
        kparams.addStringIfNotNone("clientVer", self.clientVer)
        kparams.addIntEnumIfNotNone("eventType", self.eventType)
        kparams.addFloatIfNotNone("eventTimestamp", self.eventTimestamp)
        kparams.addStringIfNotNone("sessionId", self.sessionId)
        kparams.addIntIfNotNone("partnerId", self.partnerId)
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addStringIfNotNone("uniqueViewer", self.uniqueViewer)
        kparams.addStringIfNotNone("widgetId", self.widgetId)
        kparams.addIntIfNotNone("uiconfId", self.uiconfId)
        kparams.addStringIfNotNone("userId", self.userId)
        kparams.addIntIfNotNone("currentPoint", self.currentPoint)
        kparams.addIntIfNotNone("duration", self.duration)
        kparams.addIntIfNotNone("processDuration", self.processDuration)
        kparams.addStringIfNotNone("controlId", self.controlId)
        kparams.addBoolIfNotNone("seek", self.seek)
        kparams.addIntIfNotNone("newPoint", self.newPoint)
        kparams.addStringIfNotNone("referrer", self.referrer)
        kparams.addBoolIfNotNone("isFirstInSession", self.isFirstInSession)
        return kparams

    def getClientVer(self):
        return self.clientVer

    def setClientVer(self, newClientVer):
        self.clientVer = newClientVer

    def getEventType(self):
        return self.eventType

    def setEventType(self, newEventType):
        self.eventType = newEventType

    def getEventTimestamp(self):
        return self.eventTimestamp

    def setEventTimestamp(self, newEventTimestamp):
        self.eventTimestamp = newEventTimestamp

    def getSessionId(self):
        return self.sessionId

    def setSessionId(self, newSessionId):
        self.sessionId = newSessionId

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getUniqueViewer(self):
        return self.uniqueViewer

    def setUniqueViewer(self, newUniqueViewer):
        self.uniqueViewer = newUniqueViewer

    def getWidgetId(self):
        return self.widgetId

    def setWidgetId(self, newWidgetId):
        self.widgetId = newWidgetId

    def getUiconfId(self):
        return self.uiconfId

    def setUiconfId(self, newUiconfId):
        self.uiconfId = newUiconfId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getCurrentPoint(self):
        return self.currentPoint

    def setCurrentPoint(self, newCurrentPoint):
        self.currentPoint = newCurrentPoint

    def getDuration(self):
        return self.duration

    def setDuration(self, newDuration):
        self.duration = newDuration

    def getUserIp(self):
        return self.userIp

    def getProcessDuration(self):
        return self.processDuration

    def setProcessDuration(self, newProcessDuration):
        self.processDuration = newProcessDuration

    def getControlId(self):
        return self.controlId

    def setControlId(self, newControlId):
        self.controlId = newControlId

    def getSeek(self):
        return self.seek

    def setSeek(self, newSeek):
        self.seek = newSeek

    def getNewPoint(self):
        return self.newPoint

    def setNewPoint(self, newNewPoint):
        self.newPoint = newNewPoint

    def getReferrer(self):
        return self.referrer

    def setReferrer(self, newReferrer):
        self.referrer = newReferrer

    def getIsFirstInSession(self):
        return self.isFirstInSession

    def setIsFirstInSession(self, newIsFirstInSession):
        self.isFirstInSession = newIsFirstInSession


class KalturaStatsKmcEvent(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.clientVer = None

        # @var string
        self.kmcEventActionPath = None

        # @var KalturaStatsKmcEventType
        self.kmcEventType = None

        # the client's timestamp of this event
        # @var float
        self.eventTimestamp = None

        # a unique string generated by the client that will represent the client-side session: the primary component will pass it on to other components that sprout from it
        # @var string
        self.sessionId = None

        # @var int
        self.partnerId = None

        # @var string
        self.entryId = None

        # @var string
        self.widgetId = None

        # @var int
        self.uiconfId = None

        # the partner's user id
        # @var string
        self.userId = None

        # will be retrieved from the request of the user
        # @var string
        # @readonly
        self.userIp = None


    PROPERTY_LOADERS = {
        'clientVer': getXmlNodeText, 
        'kmcEventActionPath': getXmlNodeText, 
        'kmcEventType': (KalturaEnumsFactory.createInt, "KalturaStatsKmcEventType"), 
        'eventTimestamp': getXmlNodeFloat, 
        'sessionId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'widgetId': getXmlNodeText, 
        'uiconfId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'userIp': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStatsKmcEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStatsKmcEvent")
        kparams.addStringIfNotNone("clientVer", self.clientVer)
        kparams.addStringIfNotNone("kmcEventActionPath", self.kmcEventActionPath)
        kparams.addIntEnumIfNotNone("kmcEventType", self.kmcEventType)
        kparams.addFloatIfNotNone("eventTimestamp", self.eventTimestamp)
        kparams.addStringIfNotNone("sessionId", self.sessionId)
        kparams.addIntIfNotNone("partnerId", self.partnerId)
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addStringIfNotNone("widgetId", self.widgetId)
        kparams.addIntIfNotNone("uiconfId", self.uiconfId)
        kparams.addStringIfNotNone("userId", self.userId)
        return kparams

    def getClientVer(self):
        return self.clientVer

    def setClientVer(self, newClientVer):
        self.clientVer = newClientVer

    def getKmcEventActionPath(self):
        return self.kmcEventActionPath

    def setKmcEventActionPath(self, newKmcEventActionPath):
        self.kmcEventActionPath = newKmcEventActionPath

    def getKmcEventType(self):
        return self.kmcEventType

    def setKmcEventType(self, newKmcEventType):
        self.kmcEventType = newKmcEventType

    def getEventTimestamp(self):
        return self.eventTimestamp

    def setEventTimestamp(self, newEventTimestamp):
        self.eventTimestamp = newEventTimestamp

    def getSessionId(self):
        return self.sessionId

    def setSessionId(self, newSessionId):
        self.sessionId = newSessionId

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getWidgetId(self):
        return self.widgetId

    def setWidgetId(self, newWidgetId):
        self.widgetId = newWidgetId

    def getUiconfId(self):
        return self.uiconfId

    def setUiconfId(self, newUiconfId):
        self.uiconfId = newUiconfId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getUserIp(self):
        return self.userIp


class KalturaCEError(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = None

        # @var int
        self.partnerId = None

        # @var string
        self.browser = None

        # @var string
        self.serverIp = None

        # @var string
        self.serverOs = None

        # @var string
        self.phpVersion = None

        # @var string
        self.ceAdminEmail = None

        # @var string
        self.type = None

        # @var string
        self.description = None

        # @var string
        self.data = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'browser': getXmlNodeText, 
        'serverIp': getXmlNodeText, 
        'serverOs': getXmlNodeText, 
        'phpVersion': getXmlNodeText, 
        'ceAdminEmail': getXmlNodeText, 
        'type': getXmlNodeText, 
        'description': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCEError.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCEError")
        kparams.addIntIfNotNone("partnerId", self.partnerId)
        kparams.addStringIfNotNone("browser", self.browser)
        kparams.addStringIfNotNone("serverIp", self.serverIp)
        kparams.addStringIfNotNone("serverOs", self.serverOs)
        kparams.addStringIfNotNone("phpVersion", self.phpVersion)
        kparams.addStringIfNotNone("ceAdminEmail", self.ceAdminEmail)
        kparams.addStringIfNotNone("type", self.type)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addStringIfNotNone("data", self.data)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getBrowser(self):
        return self.browser

    def setBrowser(self, newBrowser):
        self.browser = newBrowser

    def getServerIp(self):
        return self.serverIp

    def setServerIp(self, newServerIp):
        self.serverIp = newServerIp

    def getServerOs(self):
        return self.serverOs

    def setServerOs(self, newServerOs):
        self.serverOs = newServerOs

    def getPhpVersion(self):
        return self.phpVersion

    def setPhpVersion(self, newPhpVersion):
        self.phpVersion = newPhpVersion

    def getCeAdminEmail(self):
        return self.ceAdminEmail

    def setCeAdminEmail(self, newCeAdminEmail):
        self.ceAdminEmail = newCeAdminEmail

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


class KalturaBaseSyndicationFeed(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = None

        # @var string
        # @readonly
        self.feedUrl = None

        # @var int
        # @readonly
        self.partnerId = None

        # link a playlist that will set what content the feed will include
        # if empty, all content will be included in feed
        # @var string
        self.playlistId = None

        # feed name
        # @var string
        self.name = None

        # feed status
        # @var KalturaSyndicationFeedStatus
        # @readonly
        self.status = None

        # feed type
        # @var KalturaSyndicationFeedType
        # @readonly
        self.type = None

        # Base URL for each video, on the partners site
        # This is required by all syndication types.
        # @var string
        self.landingPage = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # allow_embed tells google OR yahoo weather to allow embedding the video on google OR yahoo video results
        # or just to provide a link to the landing page.
        # it is applied on the video-player_loc property in the XML (google)
        # and addes media-player tag (yahoo)
        # @var bool
        self.allowEmbed = None

        # Select a uiconf ID as player skin to include in the kwidget url
        # @var int
        self.playerUiconfId = None

        # @var int
        self.flavorParamId = None

        # @var bool
        self.transcodeExistingContent = None

        # @var bool
        self.addToDefaultConversionProfile = None

        # @var string
        self.categories = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'feedUrl': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'playlistId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaSyndicationFeedStatus"), 
        'type': (KalturaEnumsFactory.createInt, "KalturaSyndicationFeedType"), 
        'landingPage': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'allowEmbed': getXmlNodeBool, 
        'playerUiconfId': getXmlNodeInt, 
        'flavorParamId': getXmlNodeInt, 
        'transcodeExistingContent': getXmlNodeBool, 
        'addToDefaultConversionProfile': getXmlNodeBool, 
        'categories': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeed")
        kparams.addStringIfNotNone("playlistId", self.playlistId)
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("landingPage", self.landingPage)
        kparams.addBoolIfNotNone("allowEmbed", self.allowEmbed)
        kparams.addIntIfNotNone("playerUiconfId", self.playerUiconfId)
        kparams.addIntIfNotNone("flavorParamId", self.flavorParamId)
        kparams.addBoolIfNotNone("transcodeExistingContent", self.transcodeExistingContent)
        kparams.addBoolIfNotNone("addToDefaultConversionProfile", self.addToDefaultConversionProfile)
        kparams.addStringIfNotNone("categories", self.categories)
        return kparams

    def getId(self):
        return self.id

    def getFeedUrl(self):
        return self.feedUrl

    def getPartnerId(self):
        return self.partnerId

    def getPlaylistId(self):
        return self.playlistId

    def setPlaylistId(self, newPlaylistId):
        self.playlistId = newPlaylistId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getStatus(self):
        return self.status

    def getType(self):
        return self.type

    def getLandingPage(self):
        return self.landingPage

    def setLandingPage(self, newLandingPage):
        self.landingPage = newLandingPage

    def getCreatedAt(self):
        return self.createdAt

    def getAllowEmbed(self):
        return self.allowEmbed

    def setAllowEmbed(self, newAllowEmbed):
        self.allowEmbed = newAllowEmbed

    def getPlayerUiconfId(self):
        return self.playerUiconfId

    def setPlayerUiconfId(self, newPlayerUiconfId):
        self.playerUiconfId = newPlayerUiconfId

    def getFlavorParamId(self):
        return self.flavorParamId

    def setFlavorParamId(self, newFlavorParamId):
        self.flavorParamId = newFlavorParamId

    def getTranscodeExistingContent(self):
        return self.transcodeExistingContent

    def setTranscodeExistingContent(self, newTranscodeExistingContent):
        self.transcodeExistingContent = newTranscodeExistingContent

    def getAddToDefaultConversionProfile(self):
        return self.addToDefaultConversionProfile

    def setAddToDefaultConversionProfile(self, newAddToDefaultConversionProfile):
        self.addToDefaultConversionProfile = newAddToDefaultConversionProfile

    def getCategories(self):
        return self.categories

    def setCategories(self, newCategories):
        self.categories = newCategories


class KalturaBaseSyndicationFeedBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeedBaseFilter")
        return kparams


class KalturaBaseSyndicationFeedFilter(KalturaBaseSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaBaseSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeedFilter")
        return kparams


class KalturaBaseSyndicationFeedListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaBaseSyndicationFeed
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBaseSyndicationFeed), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSyndicationFeedListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseSyndicationFeedListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaSyndicationFeedEntryCount(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # the total count of entries that should appear in the feed without flavor filtering
        # @var int
        self.totalEntryCount = None

        # count of entries that will appear in the feed (including all relevant filters)
        # @var int
        self.actualEntryCount = None

        # count of entries that requires transcoding in order to be included in feed
        # @var int
        self.requireTranscodingCount = None


    PROPERTY_LOADERS = {
        'totalEntryCount': getXmlNodeInt, 
        'actualEntryCount': getXmlNodeInt, 
        'requireTranscodingCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSyndicationFeedEntryCount.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSyndicationFeedEntryCount")
        kparams.addIntIfNotNone("totalEntryCount", self.totalEntryCount)
        kparams.addIntIfNotNone("actualEntryCount", self.actualEntryCount)
        kparams.addIntIfNotNone("requireTranscodingCount", self.requireTranscodingCount)
        return kparams

    def getTotalEntryCount(self):
        return self.totalEntryCount

    def setTotalEntryCount(self, newTotalEntryCount):
        self.totalEntryCount = newTotalEntryCount

    def getActualEntryCount(self):
        return self.actualEntryCount

    def setActualEntryCount(self, newActualEntryCount):
        self.actualEntryCount = newActualEntryCount

    def getRequireTranscodingCount(self):
        return self.requireTranscodingCount

    def setRequireTranscodingCount(self, newRequireTranscodingCount):
        self.requireTranscodingCount = newRequireTranscodingCount


class KalturaThumbAsset(KalturaAsset):
    def __init__(self):
        KalturaAsset.__init__(self)

        # The Flavor Params used to create this Flavor Asset
        # @var int
        self.thumbParamsId = None

        # The width of the Flavor Asset
        # @var int
        # @readonly
        self.width = None

        # The height of the Flavor Asset
        # @var int
        # @readonly
        self.height = None


    PROPERTY_LOADERS = {
        'thumbParamsId': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaThumbAsset")
        kparams.addIntIfNotNone("thumbParamsId", self.thumbParamsId)
        return kparams

    def getThumbParamsId(self):
        return self.thumbParamsId

    def setThumbParamsId(self, newThumbParamsId):
        self.thumbParamsId = newThumbParamsId

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


class KalturaThumbParams(KalturaAssetParams):
    def __init__(self):
        KalturaAssetParams.__init__(self)

        # @var KalturaThumbCropType
        self.cropType = None

        # @var int
        self.quality = None

        # @var int
        self.cropX = None

        # @var int
        self.cropY = None

        # @var int
        self.cropWidth = None

        # @var int
        self.cropHeight = None

        # @var float
        self.videoOffset = None

        # @var int
        self.width = None

        # @var int
        self.height = None

        # @var float
        self.scaleWidth = None

        # @var float
        self.scaleHeight = None

        # Hexadecimal value
        # @var string
        self.backgroundColor = None

        # Id of the flavor params or the thumbnail params to be used as source for the thumbnail creation
        # @var int
        self.sourceParamsId = None


    PROPERTY_LOADERS = {
        'cropType': (KalturaEnumsFactory.createInt, "KalturaThumbCropType"), 
        'quality': getXmlNodeInt, 
        'cropX': getXmlNodeInt, 
        'cropY': getXmlNodeInt, 
        'cropWidth': getXmlNodeInt, 
        'cropHeight': getXmlNodeInt, 
        'videoOffset': getXmlNodeFloat, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'scaleWidth': getXmlNodeFloat, 
        'scaleHeight': getXmlNodeFloat, 
        'backgroundColor': getXmlNodeText, 
        'sourceParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaThumbParams")
        kparams.addIntEnumIfNotNone("cropType", self.cropType)
        kparams.addIntIfNotNone("quality", self.quality)
        kparams.addIntIfNotNone("cropX", self.cropX)
        kparams.addIntIfNotNone("cropY", self.cropY)
        kparams.addIntIfNotNone("cropWidth", self.cropWidth)
        kparams.addIntIfNotNone("cropHeight", self.cropHeight)
        kparams.addFloatIfNotNone("videoOffset", self.videoOffset)
        kparams.addIntIfNotNone("width", self.width)
        kparams.addIntIfNotNone("height", self.height)
        kparams.addFloatIfNotNone("scaleWidth", self.scaleWidth)
        kparams.addFloatIfNotNone("scaleHeight", self.scaleHeight)
        kparams.addStringIfNotNone("backgroundColor", self.backgroundColor)
        kparams.addIntIfNotNone("sourceParamsId", self.sourceParamsId)
        return kparams

    def getCropType(self):
        return self.cropType

    def setCropType(self, newCropType):
        self.cropType = newCropType

    def getQuality(self):
        return self.quality

    def setQuality(self, newQuality):
        self.quality = newQuality

    def getCropX(self):
        return self.cropX

    def setCropX(self, newCropX):
        self.cropX = newCropX

    def getCropY(self):
        return self.cropY

    def setCropY(self, newCropY):
        self.cropY = newCropY

    def getCropWidth(self):
        return self.cropWidth

    def setCropWidth(self, newCropWidth):
        self.cropWidth = newCropWidth

    def getCropHeight(self):
        return self.cropHeight

    def setCropHeight(self, newCropHeight):
        self.cropHeight = newCropHeight

    def getVideoOffset(self):
        return self.videoOffset

    def setVideoOffset(self, newVideoOffset):
        self.videoOffset = newVideoOffset

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getScaleWidth(self):
        return self.scaleWidth

    def setScaleWidth(self, newScaleWidth):
        self.scaleWidth = newScaleWidth

    def getScaleHeight(self):
        return self.scaleHeight

    def setScaleHeight(self, newScaleHeight):
        self.scaleHeight = newScaleHeight

    def getBackgroundColor(self):
        return self.backgroundColor

    def setBackgroundColor(self, newBackgroundColor):
        self.backgroundColor = newBackgroundColor

    def getSourceParamsId(self):
        return self.sourceParamsId

    def setSourceParamsId(self, newSourceParamsId):
        self.sourceParamsId = newSourceParamsId


class KalturaThumbAssetListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaThumbAsset
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaThumbAsset), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaThumbAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaThumbParamsBaseFilter(KalturaAssetParamsFilter):
    def __init__(self):
        KalturaAssetParamsFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsBaseFilter")
        return kparams


class KalturaThumbParamsFilter(KalturaThumbParamsBaseFilter):
    def __init__(self):
        KalturaThumbParamsBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaThumbParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsFilter")
        return kparams


class KalturaThumbParamsListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaThumbParams
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaThumbParams), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUiConf(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # Name of the uiConf, this is not a primary key
        # @var string
        self.name = None

        # @var string
        self.description = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var KalturaUiConfObjType
        self.objType = None

        # @var string
        # @readonly
        self.objTypeAsString = None

        # @var int
        self.width = None

        # @var int
        self.height = None

        # @var string
        self.htmlParams = None

        # @var string
        self.swfUrl = None

        # @var string
        # @readonly
        self.confFilePath = None

        # @var string
        self.confFile = None

        # @var string
        self.confFileFeatures = None

        # @var string
        self.confVars = None

        # @var bool
        self.useCdn = None

        # @var string
        self.tags = None

        # @var string
        self.swfUrlVersion = None

        # Entry creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Entry creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None

        # @var KalturaUiConfCreationMode
        self.creationMode = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'objType': (KalturaEnumsFactory.createInt, "KalturaUiConfObjType"), 
        'objTypeAsString': getXmlNodeText, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'htmlParams': getXmlNodeText, 
        'swfUrl': getXmlNodeText, 
        'confFilePath': getXmlNodeText, 
        'confFile': getXmlNodeText, 
        'confFileFeatures': getXmlNodeText, 
        'confVars': getXmlNodeText, 
        'useCdn': getXmlNodeBool, 
        'tags': getXmlNodeText, 
        'swfUrlVersion': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'creationMode': (KalturaEnumsFactory.createInt, "KalturaUiConfCreationMode"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConf.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConf")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addIntEnumIfNotNone("objType", self.objType)
        kparams.addIntIfNotNone("width", self.width)
        kparams.addIntIfNotNone("height", self.height)
        kparams.addStringIfNotNone("htmlParams", self.htmlParams)
        kparams.addStringIfNotNone("swfUrl", self.swfUrl)
        kparams.addStringIfNotNone("confFile", self.confFile)
        kparams.addStringIfNotNone("confFileFeatures", self.confFileFeatures)
        kparams.addStringIfNotNone("confVars", self.confVars)
        kparams.addBoolIfNotNone("useCdn", self.useCdn)
        kparams.addStringIfNotNone("tags", self.tags)
        kparams.addStringIfNotNone("swfUrlVersion", self.swfUrlVersion)
        kparams.addIntEnumIfNotNone("creationMode", self.creationMode)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getPartnerId(self):
        return self.partnerId

    def getObjType(self):
        return self.objType

    def setObjType(self, newObjType):
        self.objType = newObjType

    def getObjTypeAsString(self):
        return self.objTypeAsString

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getHtmlParams(self):
        return self.htmlParams

    def setHtmlParams(self, newHtmlParams):
        self.htmlParams = newHtmlParams

    def getSwfUrl(self):
        return self.swfUrl

    def setSwfUrl(self, newSwfUrl):
        self.swfUrl = newSwfUrl

    def getConfFilePath(self):
        return self.confFilePath

    def getConfFile(self):
        return self.confFile

    def setConfFile(self, newConfFile):
        self.confFile = newConfFile

    def getConfFileFeatures(self):
        return self.confFileFeatures

    def setConfFileFeatures(self, newConfFileFeatures):
        self.confFileFeatures = newConfFileFeatures

    def getConfVars(self):
        return self.confVars

    def setConfVars(self, newConfVars):
        self.confVars = newConfVars

    def getUseCdn(self):
        return self.useCdn

    def setUseCdn(self, newUseCdn):
        self.useCdn = newUseCdn

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getSwfUrlVersion(self):
        return self.swfUrlVersion

    def setSwfUrlVersion(self, newSwfUrlVersion):
        self.swfUrlVersion = newSwfUrlVersion

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getCreationMode(self):
        return self.creationMode

    def setCreationMode(self, newCreationMode):
        self.creationMode = newCreationMode


class KalturaUiConfBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.nameLike = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var KalturaUiConfObjType
        self.objTypeEqual = None

        # @var string
        self.objTypeIn = None

        # @var string
        self.tagsMultiLikeOr = None

        # @var string
        self.tagsMultiLikeAnd = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var KalturaUiConfCreationMode
        self.creationModeEqual = None

        # @var string
        self.creationModeIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'objTypeEqual': (KalturaEnumsFactory.createInt, "KalturaUiConfObjType"), 
        'objTypeIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'creationModeEqual': (KalturaEnumsFactory.createInt, "KalturaUiConfCreationMode"), 
        'creationModeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUiConfBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("nameLike", self.nameLike)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addIntEnumIfNotNone("objTypeEqual", self.objTypeEqual)
        kparams.addStringIfNotNone("objTypeIn", self.objTypeIn)
        kparams.addStringIfNotNone("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfNotNone("creationModeEqual", self.creationModeEqual)
        kparams.addStringIfNotNone("creationModeIn", self.creationModeIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getObjTypeEqual(self):
        return self.objTypeEqual

    def setObjTypeEqual(self, newObjTypeEqual):
        self.objTypeEqual = newObjTypeEqual

    def getObjTypeIn(self):
        return self.objTypeIn

    def setObjTypeIn(self, newObjTypeIn):
        self.objTypeIn = newObjTypeIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getCreationModeEqual(self):
        return self.creationModeEqual

    def setCreationModeEqual(self, newCreationModeEqual):
        self.creationModeEqual = newCreationModeEqual

    def getCreationModeIn(self):
        return self.creationModeIn

    def setCreationModeIn(self, newCreationModeIn):
        self.creationModeIn = newCreationModeIn


class KalturaUiConfFilter(KalturaUiConfBaseFilter):
    def __init__(self):
        KalturaUiConfBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUiConfBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUiConfBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUiConfFilter")
        return kparams


class KalturaUiConfListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUiConf
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUiConf), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConfListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUiConfTypeInfo(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # UiConf Type
        # @var KalturaUiConfObjType
        self.type = None

        # Available versions
        # @var array of KalturaString
        self.versions = None

        # The direcotry this type is saved at
        # @var string
        self.directory = None

        # Filename for this UiConf type
        # @var string
        self.filename = None


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createInt, "KalturaUiConfObjType"), 
        'versions': (KalturaObjectFactory.createArray, KalturaString), 
        'directory': getXmlNodeText, 
        'filename': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfTypeInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConfTypeInfo")
        kparams.addIntEnumIfNotNone("type", self.type)
        kparams.addObjectIfNotNone("versions", self.versions)
        kparams.addStringIfNotNone("directory", self.directory)
        kparams.addStringIfNotNone("filename", self.filename)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getVersions(self):
        return self.versions

    def setVersions(self, newVersions):
        self.versions = newVersions

    def getDirectory(self):
        return self.directory

    def setDirectory(self, newDirectory):
        self.directory = newDirectory

    def getFilename(self):
        return self.filename

    def setFilename(self, newFilename):
        self.filename = newFilename


class KalturaUploadResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        self.uploadTokenId = None

        # @var int
        self.fileSize = None

        # @var KalturaUploadErrorCode
        self.errorCode = None

        # @var string
        self.errorDescription = None


    PROPERTY_LOADERS = {
        'uploadTokenId': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
        'errorCode': (KalturaEnumsFactory.createInt, "KalturaUploadErrorCode"), 
        'errorDescription': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUploadResponse")
        kparams.addStringIfNotNone("uploadTokenId", self.uploadTokenId)
        kparams.addIntIfNotNone("fileSize", self.fileSize)
        kparams.addIntEnumIfNotNone("errorCode", self.errorCode)
        kparams.addStringIfNotNone("errorDescription", self.errorDescription)
        return kparams

    def getUploadTokenId(self):
        return self.uploadTokenId

    def setUploadTokenId(self, newUploadTokenId):
        self.uploadTokenId = newUploadTokenId

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, newErrorCode):
        self.errorCode = newErrorCode

    def getErrorDescription(self):
        return self.errorDescription

    def setErrorDescription(self, newErrorDescription):
        self.errorDescription = newErrorDescription


class KalturaUploadToken(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # Upload token unique ID
        # @var string
        # @readonly
        self.id = None

        # Partner ID of the upload token
        # @var int
        # @readonly
        self.partnerId = None

        # User id for the upload token
        # @var string
        # @readonly
        self.userId = None

        # Status of the upload token
        # @var KalturaUploadTokenStatus
        # @readonly
        self.status = None

        # Name of the file for the upload token, can be empty when the upload token is created and will be updated internally after the file is uploaded
        # @var string
        # @insertonly
        self.fileName = None

        # File size in bytes, can be empty when the upload token is created and will be updated internally after the file is uploaded
        # @var float
        # @insertonly
        self.fileSize = None

        # Uploaded file size in bytes, can be used to identify how many bytes were uploaded before resuming
        # @var float
        # @readonly
        self.uploadedFileSize = None

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = None

        # Last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaUploadTokenStatus"), 
        'fileName': getXmlNodeText, 
        'fileSize': getXmlNodeFloat, 
        'uploadedFileSize': getXmlNodeFloat, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadToken.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUploadToken")
        kparams.addStringIfNotNone("fileName", self.fileName)
        kparams.addFloatIfNotNone("fileSize", self.fileSize)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getUserId(self):
        return self.userId

    def getStatus(self):
        return self.status

    def getFileName(self):
        return self.fileName

    def setFileName(self, newFileName):
        self.fileName = newFileName

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getUploadedFileSize(self):
        return self.uploadedFileSize

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaUploadTokenBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var string
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.userIdEqual = None

        # @var KalturaUploadTokenStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaUploadTokenStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadTokenBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUploadTokenBaseFilter")
        kparams.addStringIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("userIdEqual", self.userIdEqual)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaUploadTokenFilter(KalturaUploadTokenBaseFilter):
    def __init__(self):
        KalturaUploadTokenBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUploadTokenBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadTokenFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUploadTokenBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUploadTokenFilter")
        return kparams


class KalturaUploadTokenListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUploadToken
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUploadToken), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUploadTokenListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUploadTokenListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUserRole(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = None

        # @var string
        self.name = None

        # @var string
        self.description = None

        # @var KalturaUserRoleStatus
        self.status = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.permissionNames = None

        # @var string
        self.tags = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaUserRoleStatus"), 
        'partnerId': getXmlNodeInt, 
        'permissionNames': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRole.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserRole")
        kparams.addStringIfNotNone("name", self.name)
        kparams.addStringIfNotNone("description", self.description)
        kparams.addIntEnumIfNotNone("status", self.status)
        kparams.addStringIfNotNone("permissionNames", self.permissionNames)
        kparams.addStringIfNotNone("tags", self.tags)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getPartnerId(self):
        return self.partnerId

    def getPermissionNames(self):
        return self.permissionNames

    def setPermissionNames(self, newPermissionNames):
        self.permissionNames = newPermissionNames

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt


class KalturaUserRoleBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.nameEqual = None

        # @var string
        self.nameIn = None

        # @var string
        self.descriptionLike = None

        # @var KalturaUserRoleStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var string
        self.tagsMultiLikeOr = None

        # @var string
        self.tagsMultiLikeAnd = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'nameIn': getXmlNodeText, 
        'descriptionLike': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaUserRoleStatus"), 
        'statusIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserRoleBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("nameEqual", self.nameEqual)
        kparams.addStringIfNotNone("nameIn", self.nameIn)
        kparams.addStringIfNotNone("descriptionLike", self.descriptionLike)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getNameIn(self):
        return self.nameIn

    def setNameIn(self, newNameIn):
        self.nameIn = newNameIn

    def getDescriptionLike(self):
        return self.descriptionLike

    def setDescriptionLike(self, newDescriptionLike):
        self.descriptionLike = newDescriptionLike

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual


class KalturaUserRoleFilter(KalturaUserRoleBaseFilter):
    def __init__(self):
        KalturaUserRoleBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserRoleBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserRoleBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUserRoleFilter")
        return kparams


class KalturaUserRoleListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUserRole
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUserRole), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserRoleListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaUserBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.screenNameLike = None

        # @var string
        self.screenNameStartsWith = None

        # @var string
        self.emailLike = None

        # @var string
        self.emailStartsWith = None

        # @var string
        self.tagsMultiLikeOr = None

        # @var string
        self.tagsMultiLikeAnd = None

        # @var KalturaUserStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var bool
        self.isAdminEqual = None


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
        'screenNameLike': getXmlNodeText, 
        'screenNameStartsWith': getXmlNodeText, 
        'emailLike': getXmlNodeText, 
        'emailStartsWith': getXmlNodeText, 
        'tagsMultiLikeOr': getXmlNodeText, 
        'tagsMultiLikeAnd': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaUserStatus"), 
        'statusIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'isAdminEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserBaseFilter")
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("screenNameLike", self.screenNameLike)
        kparams.addStringIfNotNone("screenNameStartsWith", self.screenNameStartsWith)
        kparams.addStringIfNotNone("emailLike", self.emailLike)
        kparams.addStringIfNotNone("emailStartsWith", self.emailStartsWith)
        kparams.addStringIfNotNone("tagsMultiLikeOr", self.tagsMultiLikeOr)
        kparams.addStringIfNotNone("tagsMultiLikeAnd", self.tagsMultiLikeAnd)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addBoolIfNotNone("isAdminEqual", self.isAdminEqual)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getScreenNameLike(self):
        return self.screenNameLike

    def setScreenNameLike(self, newScreenNameLike):
        self.screenNameLike = newScreenNameLike

    def getScreenNameStartsWith(self):
        return self.screenNameStartsWith

    def setScreenNameStartsWith(self, newScreenNameStartsWith):
        self.screenNameStartsWith = newScreenNameStartsWith

    def getEmailLike(self):
        return self.emailLike

    def setEmailLike(self, newEmailLike):
        self.emailLike = newEmailLike

    def getEmailStartsWith(self):
        return self.emailStartsWith

    def setEmailStartsWith(self, newEmailStartsWith):
        self.emailStartsWith = newEmailStartsWith

    def getTagsMultiLikeOr(self):
        return self.tagsMultiLikeOr

    def setTagsMultiLikeOr(self, newTagsMultiLikeOr):
        self.tagsMultiLikeOr = newTagsMultiLikeOr

    def getTagsMultiLikeAnd(self):
        return self.tagsMultiLikeAnd

    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd):
        self.tagsMultiLikeAnd = newTagsMultiLikeAnd

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getIsAdminEqual(self):
        return self.isAdminEqual

    def setIsAdminEqual(self, newIsAdminEqual):
        self.isAdminEqual = newIsAdminEqual


class KalturaUserFilter(KalturaUserBaseFilter):
    def __init__(self):
        KalturaUserBaseFilter.__init__(self)

        # @var string
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var bool
        self.loginEnabledEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'loginEnabledEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaUserBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUserFilter")
        kparams.addStringIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addBoolIfNotNone("loginEnabledEqual", self.loginEnabledEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getLoginEnabledEqual(self):
        return self.loginEnabledEqual

    def setLoginEnabledEqual(self, newLoginEnabledEqual):
        self.loginEnabledEqual = newLoginEnabledEqual


class KalturaUserListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUser
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUser), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaWidget(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.id = None

        # @var string
        self.sourceWidgetId = None

        # @var string
        # @readonly
        self.rootWidgetId = None

        # @var int
        # @readonly
        self.partnerId = None

        # @var string
        self.entryId = None

        # @var int
        self.uiConfId = None

        # @var KalturaWidgetSecurityType
        self.securityType = None

        # @var int
        self.securityPolicy = None

        # @var int
        # @readonly
        self.createdAt = None

        # @var int
        # @readonly
        self.updatedAt = None

        # Can be used to store various partner related data as a string
        # @var string
        self.partnerData = None

        # @var string
        # @readonly
        self.widgetHTML = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'sourceWidgetId': getXmlNodeText, 
        'rootWidgetId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'uiConfId': getXmlNodeInt, 
        'securityType': (KalturaEnumsFactory.createInt, "KalturaWidgetSecurityType"), 
        'securityPolicy': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'partnerData': getXmlNodeText, 
        'widgetHTML': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidget.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaWidget")
        kparams.addStringIfNotNone("sourceWidgetId", self.sourceWidgetId)
        kparams.addStringIfNotNone("entryId", self.entryId)
        kparams.addIntIfNotNone("uiConfId", self.uiConfId)
        kparams.addIntEnumIfNotNone("securityType", self.securityType)
        kparams.addIntIfNotNone("securityPolicy", self.securityPolicy)
        kparams.addStringIfNotNone("partnerData", self.partnerData)
        return kparams

    def getId(self):
        return self.id

    def getSourceWidgetId(self):
        return self.sourceWidgetId

    def setSourceWidgetId(self, newSourceWidgetId):
        self.sourceWidgetId = newSourceWidgetId

    def getRootWidgetId(self):
        return self.rootWidgetId

    def getPartnerId(self):
        return self.partnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getUiConfId(self):
        return self.uiConfId

    def setUiConfId(self, newUiConfId):
        self.uiConfId = newUiConfId

    def getSecurityType(self):
        return self.securityType

    def setSecurityType(self, newSecurityType):
        self.securityType = newSecurityType

    def getSecurityPolicy(self):
        return self.securityPolicy

    def setSecurityPolicy(self, newSecurityPolicy):
        self.securityPolicy = newSecurityPolicy

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getWidgetHTML(self):
        return self.widgetHTML


class KalturaWidgetBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var string
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.sourceWidgetIdEqual = None

        # @var string
        self.rootWidgetIdEqual = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.entryIdEqual = None

        # @var int
        self.uiConfIdEqual = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var string
        self.partnerDataLike = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'sourceWidgetIdEqual': getXmlNodeText, 
        'rootWidgetIdEqual': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'entryIdEqual': getXmlNodeText, 
        'uiConfIdEqual': getXmlNodeInt, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'partnerDataLike': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidgetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaWidgetBaseFilter")
        kparams.addStringIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("sourceWidgetIdEqual", self.sourceWidgetIdEqual)
        kparams.addStringIfNotNone("rootWidgetIdEqual", self.rootWidgetIdEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("entryIdEqual", self.entryIdEqual)
        kparams.addIntIfNotNone("uiConfIdEqual", self.uiConfIdEqual)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addStringIfNotNone("partnerDataLike", self.partnerDataLike)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getSourceWidgetIdEqual(self):
        return self.sourceWidgetIdEqual

    def setSourceWidgetIdEqual(self, newSourceWidgetIdEqual):
        self.sourceWidgetIdEqual = newSourceWidgetIdEqual

    def getRootWidgetIdEqual(self):
        return self.rootWidgetIdEqual

    def setRootWidgetIdEqual(self, newRootWidgetIdEqual):
        self.rootWidgetIdEqual = newRootWidgetIdEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getUiConfIdEqual(self):
        return self.uiConfIdEqual

    def setUiConfIdEqual(self, newUiConfIdEqual):
        self.uiConfIdEqual = newUiConfIdEqual

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getPartnerDataLike(self):
        return self.partnerDataLike

    def setPartnerDataLike(self, newPartnerDataLike):
        self.partnerDataLike = newPartnerDataLike


class KalturaWidgetFilter(KalturaWidgetBaseFilter):
    def __init__(self):
        KalturaWidgetBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaWidgetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidgetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaWidgetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaWidgetFilter")
        return kparams


class KalturaWidgetListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaWidget
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaWidget), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWidgetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaWidgetListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaPartnerBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var string
        self.nameLike = None

        # @var string
        self.nameMultiLikeOr = None

        # @var string
        self.nameMultiLikeAnd = None

        # @var string
        self.nameEqual = None

        # @var int
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var string
        self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'nameLike': getXmlNodeText, 
        'nameMultiLikeOr': getXmlNodeText, 
        'nameMultiLikeAnd': getXmlNodeText, 
        'nameEqual': getXmlNodeText, 
        'statusEqual': getXmlNodeInt, 
        'statusIn': getXmlNodeText, 
        'partnerNameDescriptionWebsiteAdminNameAdminEmailLike': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPartnerBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addStringIfNotNone("nameLike", self.nameLike)
        kparams.addStringIfNotNone("nameMultiLikeOr", self.nameMultiLikeOr)
        kparams.addStringIfNotNone("nameMultiLikeAnd", self.nameMultiLikeAnd)
        kparams.addStringIfNotNone("nameEqual", self.nameEqual)
        kparams.addIntIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addStringIfNotNone("partnerNameDescriptionWebsiteAdminNameAdminEmailLike", self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getNameLike(self):
        return self.nameLike

    def setNameLike(self, newNameLike):
        self.nameLike = newNameLike

    def getNameMultiLikeOr(self):
        return self.nameMultiLikeOr

    def setNameMultiLikeOr(self, newNameMultiLikeOr):
        self.nameMultiLikeOr = newNameMultiLikeOr

    def getNameMultiLikeAnd(self):
        return self.nameMultiLikeAnd

    def setNameMultiLikeAnd(self, newNameMultiLikeAnd):
        self.nameMultiLikeAnd = newNameMultiLikeAnd

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getPartnerNameDescriptionWebsiteAdminNameAdminEmailLike(self):
        return self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike

    def setPartnerNameDescriptionWebsiteAdminNameAdminEmailLike(self, newPartnerNameDescriptionWebsiteAdminNameAdminEmailLike):
        self.partnerNameDescriptionWebsiteAdminNameAdminEmailLike = newPartnerNameDescriptionWebsiteAdminNameAdminEmailLike


class KalturaPartnerFilter(KalturaPartnerBaseFilter):
    def __init__(self):
        KalturaPartnerBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPartnerBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPartnerFilter")
        return kparams


class KalturaPartnerListResponse(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaPartner
        # @readonly
        self.objects = None

        # @var int
        # @readonly
        self.totalCount = None


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPartner), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartnerListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


class KalturaFlavorParamsOutputBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self):
        KalturaFlavorParamsFilter.__init__(self)

        # @var int
        self.flavorParamsIdEqual = None

        # @var string
        self.flavorParamsVersionEqual = None

        # @var string
        self.flavorAssetIdEqual = None

        # @var string
        self.flavorAssetVersionEqual = None


    PROPERTY_LOADERS = {
        'flavorParamsIdEqual': getXmlNodeInt, 
        'flavorParamsVersionEqual': getXmlNodeText, 
        'flavorAssetIdEqual': getXmlNodeText, 
        'flavorAssetVersionEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutputBaseFilter")
        kparams.addIntIfNotNone("flavorParamsIdEqual", self.flavorParamsIdEqual)
        kparams.addStringIfNotNone("flavorParamsVersionEqual", self.flavorParamsVersionEqual)
        kparams.addStringIfNotNone("flavorAssetIdEqual", self.flavorAssetIdEqual)
        kparams.addStringIfNotNone("flavorAssetVersionEqual", self.flavorAssetVersionEqual)
        return kparams

    def getFlavorParamsIdEqual(self):
        return self.flavorParamsIdEqual

    def setFlavorParamsIdEqual(self, newFlavorParamsIdEqual):
        self.flavorParamsIdEqual = newFlavorParamsIdEqual

    def getFlavorParamsVersionEqual(self):
        return self.flavorParamsVersionEqual

    def setFlavorParamsVersionEqual(self, newFlavorParamsVersionEqual):
        self.flavorParamsVersionEqual = newFlavorParamsVersionEqual

    def getFlavorAssetIdEqual(self):
        return self.flavorAssetIdEqual

    def setFlavorAssetIdEqual(self, newFlavorAssetIdEqual):
        self.flavorAssetIdEqual = newFlavorAssetIdEqual

    def getFlavorAssetVersionEqual(self):
        return self.flavorAssetVersionEqual

    def setFlavorAssetVersionEqual(self, newFlavorAssetVersionEqual):
        self.flavorAssetVersionEqual = newFlavorAssetVersionEqual


class KalturaFlavorParamsOutputFilter(KalturaFlavorParamsOutputBaseFilter):
    def __init__(self):
        KalturaFlavorParamsOutputBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutputFilter")
        return kparams


class KalturaFlavorParamsOutput(KalturaFlavorParams):
    def __init__(self):
        KalturaFlavorParams.__init__(self)

        # @var int
        self.flavorParamsId = None

        # @var string
        self.commandLinesStr = None

        # @var string
        self.flavorParamsVersion = None

        # @var string
        self.flavorAssetId = None

        # @var string
        self.flavorAssetVersion = None

        # @var int
        self.readyBehavior = None


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'commandLinesStr': getXmlNodeText, 
        'flavorParamsVersion': getXmlNodeText, 
        'flavorAssetId': getXmlNodeText, 
        'flavorAssetVersion': getXmlNodeText, 
        'readyBehavior': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaFlavorParamsOutput")
        kparams.addIntIfNotNone("flavorParamsId", self.flavorParamsId)
        kparams.addStringIfNotNone("commandLinesStr", self.commandLinesStr)
        kparams.addStringIfNotNone("flavorParamsVersion", self.flavorParamsVersion)
        kparams.addStringIfNotNone("flavorAssetId", self.flavorAssetId)
        kparams.addStringIfNotNone("flavorAssetVersion", self.flavorAssetVersion)
        kparams.addIntIfNotNone("readyBehavior", self.readyBehavior)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getCommandLinesStr(self):
        return self.commandLinesStr

    def setCommandLinesStr(self, newCommandLinesStr):
        self.commandLinesStr = newCommandLinesStr

    def getFlavorParamsVersion(self):
        return self.flavorParamsVersion

    def setFlavorParamsVersion(self, newFlavorParamsVersion):
        self.flavorParamsVersion = newFlavorParamsVersion

    def getFlavorAssetId(self):
        return self.flavorAssetId

    def setFlavorAssetId(self, newFlavorAssetId):
        self.flavorAssetId = newFlavorAssetId

    def getFlavorAssetVersion(self):
        return self.flavorAssetVersion

    def setFlavorAssetVersion(self, newFlavorAssetVersion):
        self.flavorAssetVersion = newFlavorAssetVersion

    def getReadyBehavior(self):
        return self.readyBehavior

    def setReadyBehavior(self, newReadyBehavior):
        self.readyBehavior = newReadyBehavior


class KalturaThumbParamsOutputBaseFilter(KalturaThumbParamsFilter):
    def __init__(self):
        KalturaThumbParamsFilter.__init__(self)

        # @var int
        self.thumbParamsIdEqual = None

        # @var string
        self.thumbParamsVersionEqual = None

        # @var string
        self.thumbAssetIdEqual = None

        # @var string
        self.thumbAssetVersionEqual = None


    PROPERTY_LOADERS = {
        'thumbParamsIdEqual': getXmlNodeInt, 
        'thumbParamsVersionEqual': getXmlNodeText, 
        'thumbAssetIdEqual': getXmlNodeText, 
        'thumbAssetVersionEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaThumbParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutputBaseFilter")
        kparams.addIntIfNotNone("thumbParamsIdEqual", self.thumbParamsIdEqual)
        kparams.addStringIfNotNone("thumbParamsVersionEqual", self.thumbParamsVersionEqual)
        kparams.addStringIfNotNone("thumbAssetIdEqual", self.thumbAssetIdEqual)
        kparams.addStringIfNotNone("thumbAssetVersionEqual", self.thumbAssetVersionEqual)
        return kparams

    def getThumbParamsIdEqual(self):
        return self.thumbParamsIdEqual

    def setThumbParamsIdEqual(self, newThumbParamsIdEqual):
        self.thumbParamsIdEqual = newThumbParamsIdEqual

    def getThumbParamsVersionEqual(self):
        return self.thumbParamsVersionEqual

    def setThumbParamsVersionEqual(self, newThumbParamsVersionEqual):
        self.thumbParamsVersionEqual = newThumbParamsVersionEqual

    def getThumbAssetIdEqual(self):
        return self.thumbAssetIdEqual

    def setThumbAssetIdEqual(self, newThumbAssetIdEqual):
        self.thumbAssetIdEqual = newThumbAssetIdEqual

    def getThumbAssetVersionEqual(self):
        return self.thumbAssetVersionEqual

    def setThumbAssetVersionEqual(self, newThumbAssetVersionEqual):
        self.thumbAssetVersionEqual = newThumbAssetVersionEqual


class KalturaThumbParamsOutputFilter(KalturaThumbParamsOutputBaseFilter):
    def __init__(self):
        KalturaThumbParamsOutputBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaThumbParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutputFilter")
        return kparams


class KalturaThumbParamsOutput(KalturaThumbParams):
    def __init__(self):
        KalturaThumbParams.__init__(self)

        # @var int
        self.thumbParamsId = None

        # @var string
        self.thumbParamsVersion = None

        # @var string
        self.thumbAssetId = None

        # @var string
        self.thumbAssetVersion = None


    PROPERTY_LOADERS = {
        'thumbParamsId': getXmlNodeInt, 
        'thumbParamsVersion': getXmlNodeText, 
        'thumbAssetId': getXmlNodeText, 
        'thumbAssetVersion': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaThumbParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbParams.toParams(self)
        kparams.put("objectType", "KalturaThumbParamsOutput")
        kparams.addIntIfNotNone("thumbParamsId", self.thumbParamsId)
        kparams.addStringIfNotNone("thumbParamsVersion", self.thumbParamsVersion)
        kparams.addStringIfNotNone("thumbAssetId", self.thumbAssetId)
        kparams.addStringIfNotNone("thumbAssetVersion", self.thumbAssetVersion)
        return kparams

    def getThumbParamsId(self):
        return self.thumbParamsId

    def setThumbParamsId(self, newThumbParamsId):
        self.thumbParamsId = newThumbParamsId

    def getThumbParamsVersion(self):
        return self.thumbParamsVersion

    def setThumbParamsVersion(self, newThumbParamsVersion):
        self.thumbParamsVersion = newThumbParamsVersion

    def getThumbAssetId(self):
        return self.thumbAssetId

    def setThumbAssetId(self, newThumbAssetId):
        self.thumbAssetId = newThumbAssetId

    def getThumbAssetVersion(self):
        return self.thumbAssetVersion

    def setThumbAssetVersion(self, newThumbAssetVersion):
        self.thumbAssetVersion = newThumbAssetVersion


class KalturaMediaInfoBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var string
        self.flavorAssetIdEqual = None


    PROPERTY_LOADERS = {
        'flavorAssetIdEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfoBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaInfoBaseFilter")
        kparams.addStringIfNotNone("flavorAssetIdEqual", self.flavorAssetIdEqual)
        return kparams

    def getFlavorAssetIdEqual(self):
        return self.flavorAssetIdEqual

    def setFlavorAssetIdEqual(self, newFlavorAssetIdEqual):
        self.flavorAssetIdEqual = newFlavorAssetIdEqual


class KalturaMediaInfoFilter(KalturaMediaInfoBaseFilter):
    def __init__(self):
        KalturaMediaInfoBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaInfoBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfoFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaInfoBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaInfoFilter")
        return kparams


class KalturaMediaInfo(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)

        # The id of the media info
        # @var int
        # @readonly
        self.id = None

        # The id of the related flavor asset
        # @var string
        self.flavorAssetId = None

        # The file size
        # @var int
        self.fileSize = None

        # The container format
        # @var string
        self.containerFormat = None

        # The container id
        # @var string
        self.containerId = None

        # The container profile
        # @var string
        self.containerProfile = None

        # The container duration
        # @var int
        self.containerDuration = None

        # The container bit rate
        # @var int
        self.containerBitRate = None

        # The video format
        # @var string
        self.videoFormat = None

        # The video codec id
        # @var string
        self.videoCodecId = None

        # The video duration
        # @var int
        self.videoDuration = None

        # The video bit rate
        # @var int
        self.videoBitRate = None

        # The video bit rate mode
        # @var KalturaBitRateMode
        self.videoBitRateMode = None

        # The video width
        # @var int
        self.videoWidth = None

        # The video height
        # @var int
        self.videoHeight = None

        # The video frame rate
        # @var float
        self.videoFrameRate = None

        # The video display aspect ratio (dar)
        # @var float
        self.videoDar = None

        # @var int
        self.videoRotation = None

        # The audio format
        # @var string
        self.audioFormat = None

        # The audio codec id
        # @var string
        self.audioCodecId = None

        # The audio duration
        # @var int
        self.audioDuration = None

        # The audio bit rate
        # @var int
        self.audioBitRate = None

        # The audio bit rate mode
        # @var KalturaBitRateMode
        self.audioBitRateMode = None

        # The number of audio channels
        # @var int
        self.audioChannels = None

        # The audio sampling rate
        # @var int
        self.audioSamplingRate = None

        # The audio resolution
        # @var int
        self.audioResolution = None

        # The writing library
        # @var string
        self.writingLib = None

        # The data as returned by the mediainfo command line
        # @var string
        self.rawData = None

        # @var string
        self.multiStreamInfo = None

        # @var int
        self.scanType = None

        # @var string
        self.multiStream = None


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'flavorAssetId': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
        'containerFormat': getXmlNodeText, 
        'containerId': getXmlNodeText, 
        'containerProfile': getXmlNodeText, 
        'containerDuration': getXmlNodeInt, 
        'containerBitRate': getXmlNodeInt, 
        'videoFormat': getXmlNodeText, 
        'videoCodecId': getXmlNodeText, 
        'videoDuration': getXmlNodeInt, 
        'videoBitRate': getXmlNodeInt, 
        'videoBitRateMode': (KalturaEnumsFactory.createInt, "KalturaBitRateMode"), 
        'videoWidth': getXmlNodeInt, 
        'videoHeight': getXmlNodeInt, 
        'videoFrameRate': getXmlNodeFloat, 
        'videoDar': getXmlNodeFloat, 
        'videoRotation': getXmlNodeInt, 
        'audioFormat': getXmlNodeText, 
        'audioCodecId': getXmlNodeText, 
        'audioDuration': getXmlNodeInt, 
        'audioBitRate': getXmlNodeInt, 
        'audioBitRateMode': (KalturaEnumsFactory.createInt, "KalturaBitRateMode"), 
        'audioChannels': getXmlNodeInt, 
        'audioSamplingRate': getXmlNodeInt, 
        'audioResolution': getXmlNodeInt, 
        'writingLib': getXmlNodeText, 
        'rawData': getXmlNodeText, 
        'multiStreamInfo': getXmlNodeText, 
        'scanType': getXmlNodeInt, 
        'multiStream': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaInfo")
        kparams.addStringIfNotNone("flavorAssetId", self.flavorAssetId)
        kparams.addIntIfNotNone("fileSize", self.fileSize)
        kparams.addStringIfNotNone("containerFormat", self.containerFormat)
        kparams.addStringIfNotNone("containerId", self.containerId)
        kparams.addStringIfNotNone("containerProfile", self.containerProfile)
        kparams.addIntIfNotNone("containerDuration", self.containerDuration)
        kparams.addIntIfNotNone("containerBitRate", self.containerBitRate)
        kparams.addStringIfNotNone("videoFormat", self.videoFormat)
        kparams.addStringIfNotNone("videoCodecId", self.videoCodecId)
        kparams.addIntIfNotNone("videoDuration", self.videoDuration)
        kparams.addIntIfNotNone("videoBitRate", self.videoBitRate)
        kparams.addIntEnumIfNotNone("videoBitRateMode", self.videoBitRateMode)
        kparams.addIntIfNotNone("videoWidth", self.videoWidth)
        kparams.addIntIfNotNone("videoHeight", self.videoHeight)
        kparams.addFloatIfNotNone("videoFrameRate", self.videoFrameRate)
        kparams.addFloatIfNotNone("videoDar", self.videoDar)
        kparams.addIntIfNotNone("videoRotation", self.videoRotation)
        kparams.addStringIfNotNone("audioFormat", self.audioFormat)
        kparams.addStringIfNotNone("audioCodecId", self.audioCodecId)
        kparams.addIntIfNotNone("audioDuration", self.audioDuration)
        kparams.addIntIfNotNone("audioBitRate", self.audioBitRate)
        kparams.addIntEnumIfNotNone("audioBitRateMode", self.audioBitRateMode)
        kparams.addIntIfNotNone("audioChannels", self.audioChannels)
        kparams.addIntIfNotNone("audioSamplingRate", self.audioSamplingRate)
        kparams.addIntIfNotNone("audioResolution", self.audioResolution)
        kparams.addStringIfNotNone("writingLib", self.writingLib)
        kparams.addStringIfNotNone("rawData", self.rawData)
        kparams.addStringIfNotNone("multiStreamInfo", self.multiStreamInfo)
        kparams.addIntIfNotNone("scanType", self.scanType)
        kparams.addStringIfNotNone("multiStream", self.multiStream)
        return kparams

    def getId(self):
        return self.id

    def getFlavorAssetId(self):
        return self.flavorAssetId

    def setFlavorAssetId(self, newFlavorAssetId):
        self.flavorAssetId = newFlavorAssetId

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getContainerFormat(self):
        return self.containerFormat

    def setContainerFormat(self, newContainerFormat):
        self.containerFormat = newContainerFormat

    def getContainerId(self):
        return self.containerId

    def setContainerId(self, newContainerId):
        self.containerId = newContainerId

    def getContainerProfile(self):
        return self.containerProfile

    def setContainerProfile(self, newContainerProfile):
        self.containerProfile = newContainerProfile

    def getContainerDuration(self):
        return self.containerDuration

    def setContainerDuration(self, newContainerDuration):
        self.containerDuration = newContainerDuration

    def getContainerBitRate(self):
        return self.containerBitRate

    def setContainerBitRate(self, newContainerBitRate):
        self.containerBitRate = newContainerBitRate

    def getVideoFormat(self):
        return self.videoFormat

    def setVideoFormat(self, newVideoFormat):
        self.videoFormat = newVideoFormat

    def getVideoCodecId(self):
        return self.videoCodecId

    def setVideoCodecId(self, newVideoCodecId):
        self.videoCodecId = newVideoCodecId

    def getVideoDuration(self):
        return self.videoDuration

    def setVideoDuration(self, newVideoDuration):
        self.videoDuration = newVideoDuration

    def getVideoBitRate(self):
        return self.videoBitRate

    def setVideoBitRate(self, newVideoBitRate):
        self.videoBitRate = newVideoBitRate

    def getVideoBitRateMode(self):
        return self.videoBitRateMode

    def setVideoBitRateMode(self, newVideoBitRateMode):
        self.videoBitRateMode = newVideoBitRateMode

    def getVideoWidth(self):
        return self.videoWidth

    def setVideoWidth(self, newVideoWidth):
        self.videoWidth = newVideoWidth

    def getVideoHeight(self):
        return self.videoHeight

    def setVideoHeight(self, newVideoHeight):
        self.videoHeight = newVideoHeight

    def getVideoFrameRate(self):
        return self.videoFrameRate

    def setVideoFrameRate(self, newVideoFrameRate):
        self.videoFrameRate = newVideoFrameRate

    def getVideoDar(self):
        return self.videoDar

    def setVideoDar(self, newVideoDar):
        self.videoDar = newVideoDar

    def getVideoRotation(self):
        return self.videoRotation

    def setVideoRotation(self, newVideoRotation):
        self.videoRotation = newVideoRotation

    def getAudioFormat(self):
        return self.audioFormat

    def setAudioFormat(self, newAudioFormat):
        self.audioFormat = newAudioFormat

    def getAudioCodecId(self):
        return self.audioCodecId

    def setAudioCodecId(self, newAudioCodecId):
        self.audioCodecId = newAudioCodecId

    def getAudioDuration(self):
        return self.audioDuration

    def setAudioDuration(self, newAudioDuration):
        self.audioDuration = newAudioDuration

    def getAudioBitRate(self):
        return self.audioBitRate

    def setAudioBitRate(self, newAudioBitRate):
        self.audioBitRate = newAudioBitRate

    def getAudioBitRateMode(self):
        return self.audioBitRateMode

    def setAudioBitRateMode(self, newAudioBitRateMode):
        self.audioBitRateMode = newAudioBitRateMode

    def getAudioChannels(self):
        return self.audioChannels

    def setAudioChannels(self, newAudioChannels):
        self.audioChannels = newAudioChannels

    def getAudioSamplingRate(self):
        return self.audioSamplingRate

    def setAudioSamplingRate(self, newAudioSamplingRate):
        self.audioSamplingRate = newAudioSamplingRate

    def getAudioResolution(self):
        return self.audioResolution

    def setAudioResolution(self, newAudioResolution):
        self.audioResolution = newAudioResolution

    def getWritingLib(self):
        return self.writingLib

    def setWritingLib(self, newWritingLib):
        self.writingLib = newWritingLib

    def getRawData(self):
        return self.rawData

    def setRawData(self, newRawData):
        self.rawData = newRawData

    def getMultiStreamInfo(self):
        return self.multiStreamInfo

    def setMultiStreamInfo(self, newMultiStreamInfo):
        self.multiStreamInfo = newMultiStreamInfo

    def getScanType(self):
        return self.scanType

    def setScanType(self, newScanType):
        self.scanType = newScanType

    def getMultiStream(self):
        return self.multiStream

    def setMultiStream(self, newMultiStream):
        self.multiStream = newMultiStream


class KalturaCountryRestriction(KalturaBaseRestriction):
    def __init__(self):
        KalturaBaseRestriction.__init__(self)

        # Country restriction type (Allow or deny)
        # @var KalturaCountryRestrictionType
        self.countryRestrictionType = None

        # Comma separated list of country codes to allow to deny
        # @var string
        self.countryList = None


    PROPERTY_LOADERS = {
        'countryRestrictionType': (KalturaEnumsFactory.createInt, "KalturaCountryRestrictionType"), 
        'countryList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountryRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaCountryRestriction")
        kparams.addIntEnumIfNotNone("countryRestrictionType", self.countryRestrictionType)
        kparams.addStringIfNotNone("countryList", self.countryList)
        return kparams

    def getCountryRestrictionType(self):
        return self.countryRestrictionType

    def setCountryRestrictionType(self, newCountryRestrictionType):
        self.countryRestrictionType = newCountryRestrictionType

    def getCountryList(self):
        return self.countryList

    def setCountryList(self, newCountryList):
        self.countryList = newCountryList


class KalturaDirectoryRestriction(KalturaBaseRestriction):
    def __init__(self):
        KalturaBaseRestriction.__init__(self)

        # Kaltura directory restriction type
        # @var KalturaDirectoryRestrictionType
        self.directoryRestrictionType = None


    PROPERTY_LOADERS = {
        'directoryRestrictionType': (KalturaEnumsFactory.createInt, "KalturaDirectoryRestrictionType"), 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDirectoryRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaDirectoryRestriction")
        kparams.addIntEnumIfNotNone("directoryRestrictionType", self.directoryRestrictionType)
        return kparams

    def getDirectoryRestrictionType(self):
        return self.directoryRestrictionType

    def setDirectoryRestrictionType(self, newDirectoryRestrictionType):
        self.directoryRestrictionType = newDirectoryRestrictionType


class KalturaIpAddressRestriction(KalturaBaseRestriction):
    def __init__(self):
        KalturaBaseRestriction.__init__(self)

        # Ip address restriction type (Allow or deny)
        # @var KalturaIpAddressRestrictionType
        self.ipAddressRestrictionType = None

        # Comma separated list of ip address to allow to deny
        # @var string
        self.ipAddressList = None


    PROPERTY_LOADERS = {
        'ipAddressRestrictionType': (KalturaEnumsFactory.createInt, "KalturaIpAddressRestrictionType"), 
        'ipAddressList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIpAddressRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaIpAddressRestriction")
        kparams.addIntEnumIfNotNone("ipAddressRestrictionType", self.ipAddressRestrictionType)
        kparams.addStringIfNotNone("ipAddressList", self.ipAddressList)
        return kparams

    def getIpAddressRestrictionType(self):
        return self.ipAddressRestrictionType

    def setIpAddressRestrictionType(self, newIpAddressRestrictionType):
        self.ipAddressRestrictionType = newIpAddressRestrictionType

    def getIpAddressList(self):
        return self.ipAddressList

    def setIpAddressList(self, newIpAddressList):
        self.ipAddressList = newIpAddressList


class KalturaSessionRestriction(KalturaBaseRestriction):
    def __init__(self):
        KalturaBaseRestriction.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSessionRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaSessionRestriction")
        return kparams


class KalturaPreviewRestriction(KalturaSessionRestriction):
    def __init__(self):
        KalturaSessionRestriction.__init__(self)

        # The preview restriction length
        # @var int
        self.previewLength = None


    PROPERTY_LOADERS = {
        'previewLength': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaSessionRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPreviewRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSessionRestriction.toParams(self)
        kparams.put("objectType", "KalturaPreviewRestriction")
        kparams.addIntIfNotNone("previewLength", self.previewLength)
        return kparams

    def getPreviewLength(self):
        return self.previewLength

    def setPreviewLength(self, newPreviewLength):
        self.previewLength = newPreviewLength


class KalturaSiteRestriction(KalturaBaseRestriction):
    def __init__(self):
        KalturaBaseRestriction.__init__(self)

        # The site restriction type (allow or deny)
        # @var KalturaSiteRestrictionType
        self.siteRestrictionType = None

        # Comma separated list of sites (domains) to allow or deny
        # @var string
        self.siteList = None


    PROPERTY_LOADERS = {
        'siteRestrictionType': (KalturaEnumsFactory.createInt, "KalturaSiteRestrictionType"), 
        'siteList': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseRestriction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSiteRestriction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseRestriction.toParams(self)
        kparams.put("objectType", "KalturaSiteRestriction")
        kparams.addIntEnumIfNotNone("siteRestrictionType", self.siteRestrictionType)
        kparams.addStringIfNotNone("siteList", self.siteList)
        return kparams

    def getSiteRestrictionType(self):
        return self.siteRestrictionType

    def setSiteRestrictionType(self, newSiteRestrictionType):
        self.siteRestrictionType = newSiteRestrictionType

    def getSiteList(self):
        return self.siteList

    def setSiteList(self, newSiteList):
        self.siteList = newSiteList


class KalturaSearchCondition(KalturaSearchItem):
    def __init__(self):
        KalturaSearchItem.__init__(self)

        # @var string
        self.field = None

        # @var string
        self.value = None


    PROPERTY_LOADERS = {
        'field': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaSearchCondition")
        kparams.addStringIfNotNone("field", self.field)
        kparams.addStringIfNotNone("value", self.value)
        return kparams

    def getField(self):
        return self.field

    def setField(self, newField):
        self.field = newField

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


class KalturaSearchComparableCondition(KalturaSearchCondition):
    def __init__(self):
        KalturaSearchCondition.__init__(self)

        # @var KalturaSearchConditionComparison
        self.comparison = None


    PROPERTY_LOADERS = {
        'comparison': (KalturaEnumsFactory.createInt, "KalturaSearchConditionComparison"), 
    }

    def fromXml(self, node):
        KalturaSearchCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchComparableCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchCondition.toParams(self)
        kparams.put("objectType", "KalturaSearchComparableCondition")
        kparams.addIntEnumIfNotNone("comparison", self.comparison)
        return kparams

    def getComparison(self):
        return self.comparison

    def setComparison(self, newComparison):
        self.comparison = newComparison


class KalturaSearchOperator(KalturaSearchItem):
    def __init__(self):
        KalturaSearchItem.__init__(self)

        # @var KalturaSearchOperatorType
        self.type = None

        # @var array of KalturaSearchItem
        self.items = None


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createInt, "KalturaSearchOperatorType"), 
        'items': (KalturaObjectFactory.createArray, KalturaSearchItem), 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaSearchOperator")
        kparams.addIntEnumIfNotNone("type", self.type)
        kparams.addObjectIfNotNone("items", self.items)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getItems(self):
        return self.items

    def setItems(self, newItems):
        self.items = newItems


class KalturaBaseJobBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var int
        self.idGreaterThanOrEqual = None

        # @var int
        self.partnerIdEqual = None

        # @var string
        self.partnerIdIn = None

        # @var string
        self.partnerIdNotIn = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.updatedAtGreaterThanOrEqual = None

        # @var int
        self.updatedAtLessThanOrEqual = None

        # @var int
        self.processorExpirationGreaterThanOrEqual = None

        # @var int
        self.processorExpirationLessThanOrEqual = None

        # @var int
        self.executionAttemptsGreaterThanOrEqual = None

        # @var int
        self.executionAttemptsLessThanOrEqual = None

        # @var int
        self.lockVersionGreaterThanOrEqual = None

        # @var int
        self.lockVersionLessThanOrEqual = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idGreaterThanOrEqual': getXmlNodeInt, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'partnerIdNotIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'processorExpirationGreaterThanOrEqual': getXmlNodeInt, 
        'processorExpirationLessThanOrEqual': getXmlNodeInt, 
        'executionAttemptsGreaterThanOrEqual': getXmlNodeInt, 
        'executionAttemptsLessThanOrEqual': getXmlNodeInt, 
        'lockVersionGreaterThanOrEqual': getXmlNodeInt, 
        'lockVersionLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseJobBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseJobBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addIntIfNotNone("idGreaterThanOrEqual", self.idGreaterThanOrEqual)
        kparams.addIntIfNotNone("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfNotNone("partnerIdIn", self.partnerIdIn)
        kparams.addStringIfNotNone("partnerIdNotIn", self.partnerIdNotIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfNotNone("processorExpirationGreaterThanOrEqual", self.processorExpirationGreaterThanOrEqual)
        kparams.addIntIfNotNone("processorExpirationLessThanOrEqual", self.processorExpirationLessThanOrEqual)
        kparams.addIntIfNotNone("executionAttemptsGreaterThanOrEqual", self.executionAttemptsGreaterThanOrEqual)
        kparams.addIntIfNotNone("executionAttemptsLessThanOrEqual", self.executionAttemptsLessThanOrEqual)
        kparams.addIntIfNotNone("lockVersionGreaterThanOrEqual", self.lockVersionGreaterThanOrEqual)
        kparams.addIntIfNotNone("lockVersionLessThanOrEqual", self.lockVersionLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdGreaterThanOrEqual(self):
        return self.idGreaterThanOrEqual

    def setIdGreaterThanOrEqual(self, newIdGreaterThanOrEqual):
        self.idGreaterThanOrEqual = newIdGreaterThanOrEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getPartnerIdNotIn(self):
        return self.partnerIdNotIn

    def setPartnerIdNotIn(self, newPartnerIdNotIn):
        self.partnerIdNotIn = newPartnerIdNotIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getProcessorExpirationGreaterThanOrEqual(self):
        return self.processorExpirationGreaterThanOrEqual

    def setProcessorExpirationGreaterThanOrEqual(self, newProcessorExpirationGreaterThanOrEqual):
        self.processorExpirationGreaterThanOrEqual = newProcessorExpirationGreaterThanOrEqual

    def getProcessorExpirationLessThanOrEqual(self):
        return self.processorExpirationLessThanOrEqual

    def setProcessorExpirationLessThanOrEqual(self, newProcessorExpirationLessThanOrEqual):
        self.processorExpirationLessThanOrEqual = newProcessorExpirationLessThanOrEqual

    def getExecutionAttemptsGreaterThanOrEqual(self):
        return self.executionAttemptsGreaterThanOrEqual

    def setExecutionAttemptsGreaterThanOrEqual(self, newExecutionAttemptsGreaterThanOrEqual):
        self.executionAttemptsGreaterThanOrEqual = newExecutionAttemptsGreaterThanOrEqual

    def getExecutionAttemptsLessThanOrEqual(self):
        return self.executionAttemptsLessThanOrEqual

    def setExecutionAttemptsLessThanOrEqual(self, newExecutionAttemptsLessThanOrEqual):
        self.executionAttemptsLessThanOrEqual = newExecutionAttemptsLessThanOrEqual

    def getLockVersionGreaterThanOrEqual(self):
        return self.lockVersionGreaterThanOrEqual

    def setLockVersionGreaterThanOrEqual(self, newLockVersionGreaterThanOrEqual):
        self.lockVersionGreaterThanOrEqual = newLockVersionGreaterThanOrEqual

    def getLockVersionLessThanOrEqual(self):
        return self.lockVersionLessThanOrEqual

    def setLockVersionLessThanOrEqual(self, newLockVersionLessThanOrEqual):
        self.lockVersionLessThanOrEqual = newLockVersionLessThanOrEqual


class KalturaBaseJobFilter(KalturaBaseJobBaseFilter):
    def __init__(self):
        KalturaBaseJobBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseJobBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseJobFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseJobFilter")
        return kparams


class KalturaBatchJobBaseFilter(KalturaBaseJobFilter):
    def __init__(self):
        KalturaBaseJobFilter.__init__(self)

        # @var string
        self.entryIdEqual = None

        # @var KalturaBatchJobType
        self.jobTypeEqual = None

        # @var string
        self.jobTypeIn = None

        # @var string
        self.jobTypeNotIn = None

        # @var int
        self.jobSubTypeEqual = None

        # @var string
        self.jobSubTypeIn = None

        # @var string
        self.jobSubTypeNotIn = None

        # @var int
        self.onStressDivertToEqual = None

        # @var string
        self.onStressDivertToIn = None

        # @var string
        self.onStressDivertToNotIn = None

        # @var KalturaBatchJobStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None

        # @var string
        self.statusNotIn = None

        # @var int
        self.abortEqual = None

        # @var int
        self.checkAgainTimeoutGreaterThanOrEqual = None

        # @var int
        self.checkAgainTimeoutLessThanOrEqual = None

        # @var int
        self.progressGreaterThanOrEqual = None

        # @var int
        self.progressLessThanOrEqual = None

        # @var int
        self.updatesCountGreaterThanOrEqual = None

        # @var int
        self.updatesCountLessThanOrEqual = None

        # @var int
        self.priorityGreaterThanOrEqual = None

        # @var int
        self.priorityLessThanOrEqual = None

        # @var int
        self.priorityEqual = None

        # @var string
        self.priorityIn = None

        # @var string
        self.priorityNotIn = None

        # @var int
        self.twinJobIdEqual = None

        # @var string
        self.twinJobIdIn = None

        # @var string
        self.twinJobIdNotIn = None

        # @var int
        self.bulkJobIdEqual = None

        # @var string
        self.bulkJobIdIn = None

        # @var string
        self.bulkJobIdNotIn = None

        # @var int
        self.parentJobIdEqual = None

        # @var string
        self.parentJobIdIn = None

        # @var string
        self.parentJobIdNotIn = None

        # @var int
        self.rootJobIdEqual = None

        # @var string
        self.rootJobIdIn = None

        # @var string
        self.rootJobIdNotIn = None

        # @var int
        self.queueTimeGreaterThanOrEqual = None

        # @var int
        self.queueTimeLessThanOrEqual = None

        # @var int
        self.finishTimeGreaterThanOrEqual = None

        # @var int
        self.finishTimeLessThanOrEqual = None

        # @var KalturaBatchJobErrorTypes
        self.errTypeEqual = None

        # @var string
        self.errTypeIn = None

        # @var string
        self.errTypeNotIn = None

        # @var int
        self.errNumberEqual = None

        # @var string
        self.errNumberIn = None

        # @var string
        self.errNumberNotIn = None

        # @var int
        self.fileSizeLessThan = None

        # @var int
        self.fileSizeGreaterThan = None

        # @var bool
        self.lastWorkerRemoteEqual = None

        # @var int
        self.schedulerIdEqual = None

        # @var string
        self.schedulerIdIn = None

        # @var string
        self.schedulerIdNotIn = None

        # @var int
        self.workerIdEqual = None

        # @var string
        self.workerIdIn = None

        # @var string
        self.workerIdNotIn = None

        # @var int
        self.batchIndexEqual = None

        # @var string
        self.batchIndexIn = None

        # @var string
        self.batchIndexNotIn = None

        # @var int
        self.lastSchedulerIdEqual = None

        # @var string
        self.lastSchedulerIdIn = None

        # @var string
        self.lastSchedulerIdNotIn = None

        # @var int
        self.lastWorkerIdEqual = None

        # @var string
        self.lastWorkerIdIn = None

        # @var string
        self.lastWorkerIdNotIn = None

        # @var int
        self.dcEqual = None

        # @var string
        self.dcIn = None

        # @var string
        self.dcNotIn = None


    PROPERTY_LOADERS = {
        'entryIdEqual': getXmlNodeText, 
        'jobTypeEqual': (KalturaEnumsFactory.createString, "KalturaBatchJobType"), 
        'jobTypeIn': getXmlNodeText, 
        'jobTypeNotIn': getXmlNodeText, 
        'jobSubTypeEqual': getXmlNodeInt, 
        'jobSubTypeIn': getXmlNodeText, 
        'jobSubTypeNotIn': getXmlNodeText, 
        'onStressDivertToEqual': getXmlNodeInt, 
        'onStressDivertToIn': getXmlNodeText, 
        'onStressDivertToNotIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaBatchJobStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
        'abortEqual': getXmlNodeInt, 
        'checkAgainTimeoutGreaterThanOrEqual': getXmlNodeInt, 
        'checkAgainTimeoutLessThanOrEqual': getXmlNodeInt, 
        'progressGreaterThanOrEqual': getXmlNodeInt, 
        'progressLessThanOrEqual': getXmlNodeInt, 
        'updatesCountGreaterThanOrEqual': getXmlNodeInt, 
        'updatesCountLessThanOrEqual': getXmlNodeInt, 
        'priorityGreaterThanOrEqual': getXmlNodeInt, 
        'priorityLessThanOrEqual': getXmlNodeInt, 
        'priorityEqual': getXmlNodeInt, 
        'priorityIn': getXmlNodeText, 
        'priorityNotIn': getXmlNodeText, 
        'twinJobIdEqual': getXmlNodeInt, 
        'twinJobIdIn': getXmlNodeText, 
        'twinJobIdNotIn': getXmlNodeText, 
        'bulkJobIdEqual': getXmlNodeInt, 
        'bulkJobIdIn': getXmlNodeText, 
        'bulkJobIdNotIn': getXmlNodeText, 
        'parentJobIdEqual': getXmlNodeInt, 
        'parentJobIdIn': getXmlNodeText, 
        'parentJobIdNotIn': getXmlNodeText, 
        'rootJobIdEqual': getXmlNodeInt, 
        'rootJobIdIn': getXmlNodeText, 
        'rootJobIdNotIn': getXmlNodeText, 
        'queueTimeGreaterThanOrEqual': getXmlNodeInt, 
        'queueTimeLessThanOrEqual': getXmlNodeInt, 
        'finishTimeGreaterThanOrEqual': getXmlNodeInt, 
        'finishTimeLessThanOrEqual': getXmlNodeInt, 
        'errTypeEqual': (KalturaEnumsFactory.createInt, "KalturaBatchJobErrorTypes"), 
        'errTypeIn': getXmlNodeText, 
        'errTypeNotIn': getXmlNodeText, 
        'errNumberEqual': getXmlNodeInt, 
        'errNumberIn': getXmlNodeText, 
        'errNumberNotIn': getXmlNodeText, 
        'fileSizeLessThan': getXmlNodeInt, 
        'fileSizeGreaterThan': getXmlNodeInt, 
        'lastWorkerRemoteEqual': getXmlNodeBool, 
        'schedulerIdEqual': getXmlNodeInt, 
        'schedulerIdIn': getXmlNodeText, 
        'schedulerIdNotIn': getXmlNodeText, 
        'workerIdEqual': getXmlNodeInt, 
        'workerIdIn': getXmlNodeText, 
        'workerIdNotIn': getXmlNodeText, 
        'batchIndexEqual': getXmlNodeInt, 
        'batchIndexIn': getXmlNodeText, 
        'batchIndexNotIn': getXmlNodeText, 
        'lastSchedulerIdEqual': getXmlNodeInt, 
        'lastSchedulerIdIn': getXmlNodeText, 
        'lastSchedulerIdNotIn': getXmlNodeText, 
        'lastWorkerIdEqual': getXmlNodeInt, 
        'lastWorkerIdIn': getXmlNodeText, 
        'lastWorkerIdNotIn': getXmlNodeText, 
        'dcEqual': getXmlNodeInt, 
        'dcIn': getXmlNodeText, 
        'dcNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBatchJobBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobFilter.toParams(self)
        kparams.put("objectType", "KalturaBatchJobBaseFilter")
        kparams.addStringIfNotNone("entryIdEqual", self.entryIdEqual)
        kparams.addStringEnumIfNotNone("jobTypeEqual", self.jobTypeEqual)
        kparams.addStringIfNotNone("jobTypeIn", self.jobTypeIn)
        kparams.addStringIfNotNone("jobTypeNotIn", self.jobTypeNotIn)
        kparams.addIntIfNotNone("jobSubTypeEqual", self.jobSubTypeEqual)
        kparams.addStringIfNotNone("jobSubTypeIn", self.jobSubTypeIn)
        kparams.addStringIfNotNone("jobSubTypeNotIn", self.jobSubTypeNotIn)
        kparams.addIntIfNotNone("onStressDivertToEqual", self.onStressDivertToEqual)
        kparams.addStringIfNotNone("onStressDivertToIn", self.onStressDivertToIn)
        kparams.addStringIfNotNone("onStressDivertToNotIn", self.onStressDivertToNotIn)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        kparams.addStringIfNotNone("statusNotIn", self.statusNotIn)
        kparams.addIntIfNotNone("abortEqual", self.abortEqual)
        kparams.addIntIfNotNone("checkAgainTimeoutGreaterThanOrEqual", self.checkAgainTimeoutGreaterThanOrEqual)
        kparams.addIntIfNotNone("checkAgainTimeoutLessThanOrEqual", self.checkAgainTimeoutLessThanOrEqual)
        kparams.addIntIfNotNone("progressGreaterThanOrEqual", self.progressGreaterThanOrEqual)
        kparams.addIntIfNotNone("progressLessThanOrEqual", self.progressLessThanOrEqual)
        kparams.addIntIfNotNone("updatesCountGreaterThanOrEqual", self.updatesCountGreaterThanOrEqual)
        kparams.addIntIfNotNone("updatesCountLessThanOrEqual", self.updatesCountLessThanOrEqual)
        kparams.addIntIfNotNone("priorityGreaterThanOrEqual", self.priorityGreaterThanOrEqual)
        kparams.addIntIfNotNone("priorityLessThanOrEqual", self.priorityLessThanOrEqual)
        kparams.addIntIfNotNone("priorityEqual", self.priorityEqual)
        kparams.addStringIfNotNone("priorityIn", self.priorityIn)
        kparams.addStringIfNotNone("priorityNotIn", self.priorityNotIn)
        kparams.addIntIfNotNone("twinJobIdEqual", self.twinJobIdEqual)
        kparams.addStringIfNotNone("twinJobIdIn", self.twinJobIdIn)
        kparams.addStringIfNotNone("twinJobIdNotIn", self.twinJobIdNotIn)
        kparams.addIntIfNotNone("bulkJobIdEqual", self.bulkJobIdEqual)
        kparams.addStringIfNotNone("bulkJobIdIn", self.bulkJobIdIn)
        kparams.addStringIfNotNone("bulkJobIdNotIn", self.bulkJobIdNotIn)
        kparams.addIntIfNotNone("parentJobIdEqual", self.parentJobIdEqual)
        kparams.addStringIfNotNone("parentJobIdIn", self.parentJobIdIn)
        kparams.addStringIfNotNone("parentJobIdNotIn", self.parentJobIdNotIn)
        kparams.addIntIfNotNone("rootJobIdEqual", self.rootJobIdEqual)
        kparams.addStringIfNotNone("rootJobIdIn", self.rootJobIdIn)
        kparams.addStringIfNotNone("rootJobIdNotIn", self.rootJobIdNotIn)
        kparams.addIntIfNotNone("queueTimeGreaterThanOrEqual", self.queueTimeGreaterThanOrEqual)
        kparams.addIntIfNotNone("queueTimeLessThanOrEqual", self.queueTimeLessThanOrEqual)
        kparams.addIntIfNotNone("finishTimeGreaterThanOrEqual", self.finishTimeGreaterThanOrEqual)
        kparams.addIntIfNotNone("finishTimeLessThanOrEqual", self.finishTimeLessThanOrEqual)
        kparams.addIntEnumIfNotNone("errTypeEqual", self.errTypeEqual)
        kparams.addStringIfNotNone("errTypeIn", self.errTypeIn)
        kparams.addStringIfNotNone("errTypeNotIn", self.errTypeNotIn)
        kparams.addIntIfNotNone("errNumberEqual", self.errNumberEqual)
        kparams.addStringIfNotNone("errNumberIn", self.errNumberIn)
        kparams.addStringIfNotNone("errNumberNotIn", self.errNumberNotIn)
        kparams.addIntIfNotNone("fileSizeLessThan", self.fileSizeLessThan)
        kparams.addIntIfNotNone("fileSizeGreaterThan", self.fileSizeGreaterThan)
        kparams.addBoolIfNotNone("lastWorkerRemoteEqual", self.lastWorkerRemoteEqual)
        kparams.addIntIfNotNone("schedulerIdEqual", self.schedulerIdEqual)
        kparams.addStringIfNotNone("schedulerIdIn", self.schedulerIdIn)
        kparams.addStringIfNotNone("schedulerIdNotIn", self.schedulerIdNotIn)
        kparams.addIntIfNotNone("workerIdEqual", self.workerIdEqual)
        kparams.addStringIfNotNone("workerIdIn", self.workerIdIn)
        kparams.addStringIfNotNone("workerIdNotIn", self.workerIdNotIn)
        kparams.addIntIfNotNone("batchIndexEqual", self.batchIndexEqual)
        kparams.addStringIfNotNone("batchIndexIn", self.batchIndexIn)
        kparams.addStringIfNotNone("batchIndexNotIn", self.batchIndexNotIn)
        kparams.addIntIfNotNone("lastSchedulerIdEqual", self.lastSchedulerIdEqual)
        kparams.addStringIfNotNone("lastSchedulerIdIn", self.lastSchedulerIdIn)
        kparams.addStringIfNotNone("lastSchedulerIdNotIn", self.lastSchedulerIdNotIn)
        kparams.addIntIfNotNone("lastWorkerIdEqual", self.lastWorkerIdEqual)
        kparams.addStringIfNotNone("lastWorkerIdIn", self.lastWorkerIdIn)
        kparams.addStringIfNotNone("lastWorkerIdNotIn", self.lastWorkerIdNotIn)
        kparams.addIntIfNotNone("dcEqual", self.dcEqual)
        kparams.addStringIfNotNone("dcIn", self.dcIn)
        kparams.addStringIfNotNone("dcNotIn", self.dcNotIn)
        return kparams

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getJobTypeEqual(self):
        return self.jobTypeEqual

    def setJobTypeEqual(self, newJobTypeEqual):
        self.jobTypeEqual = newJobTypeEqual

    def getJobTypeIn(self):
        return self.jobTypeIn

    def setJobTypeIn(self, newJobTypeIn):
        self.jobTypeIn = newJobTypeIn

    def getJobTypeNotIn(self):
        return self.jobTypeNotIn

    def setJobTypeNotIn(self, newJobTypeNotIn):
        self.jobTypeNotIn = newJobTypeNotIn

    def getJobSubTypeEqual(self):
        return self.jobSubTypeEqual

    def setJobSubTypeEqual(self, newJobSubTypeEqual):
        self.jobSubTypeEqual = newJobSubTypeEqual

    def getJobSubTypeIn(self):
        return self.jobSubTypeIn

    def setJobSubTypeIn(self, newJobSubTypeIn):
        self.jobSubTypeIn = newJobSubTypeIn

    def getJobSubTypeNotIn(self):
        return self.jobSubTypeNotIn

    def setJobSubTypeNotIn(self, newJobSubTypeNotIn):
        self.jobSubTypeNotIn = newJobSubTypeNotIn

    def getOnStressDivertToEqual(self):
        return self.onStressDivertToEqual

    def setOnStressDivertToEqual(self, newOnStressDivertToEqual):
        self.onStressDivertToEqual = newOnStressDivertToEqual

    def getOnStressDivertToIn(self):
        return self.onStressDivertToIn

    def setOnStressDivertToIn(self, newOnStressDivertToIn):
        self.onStressDivertToIn = newOnStressDivertToIn

    def getOnStressDivertToNotIn(self):
        return self.onStressDivertToNotIn

    def setOnStressDivertToNotIn(self, newOnStressDivertToNotIn):
        self.onStressDivertToNotIn = newOnStressDivertToNotIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn

    def getAbortEqual(self):
        return self.abortEqual

    def setAbortEqual(self, newAbortEqual):
        self.abortEqual = newAbortEqual

    def getCheckAgainTimeoutGreaterThanOrEqual(self):
        return self.checkAgainTimeoutGreaterThanOrEqual

    def setCheckAgainTimeoutGreaterThanOrEqual(self, newCheckAgainTimeoutGreaterThanOrEqual):
        self.checkAgainTimeoutGreaterThanOrEqual = newCheckAgainTimeoutGreaterThanOrEqual

    def getCheckAgainTimeoutLessThanOrEqual(self):
        return self.checkAgainTimeoutLessThanOrEqual

    def setCheckAgainTimeoutLessThanOrEqual(self, newCheckAgainTimeoutLessThanOrEqual):
        self.checkAgainTimeoutLessThanOrEqual = newCheckAgainTimeoutLessThanOrEqual

    def getProgressGreaterThanOrEqual(self):
        return self.progressGreaterThanOrEqual

    def setProgressGreaterThanOrEqual(self, newProgressGreaterThanOrEqual):
        self.progressGreaterThanOrEqual = newProgressGreaterThanOrEqual

    def getProgressLessThanOrEqual(self):
        return self.progressLessThanOrEqual

    def setProgressLessThanOrEqual(self, newProgressLessThanOrEqual):
        self.progressLessThanOrEqual = newProgressLessThanOrEqual

    def getUpdatesCountGreaterThanOrEqual(self):
        return self.updatesCountGreaterThanOrEqual

    def setUpdatesCountGreaterThanOrEqual(self, newUpdatesCountGreaterThanOrEqual):
        self.updatesCountGreaterThanOrEqual = newUpdatesCountGreaterThanOrEqual

    def getUpdatesCountLessThanOrEqual(self):
        return self.updatesCountLessThanOrEqual

    def setUpdatesCountLessThanOrEqual(self, newUpdatesCountLessThanOrEqual):
        self.updatesCountLessThanOrEqual = newUpdatesCountLessThanOrEqual

    def getPriorityGreaterThanOrEqual(self):
        return self.priorityGreaterThanOrEqual

    def setPriorityGreaterThanOrEqual(self, newPriorityGreaterThanOrEqual):
        self.priorityGreaterThanOrEqual = newPriorityGreaterThanOrEqual

    def getPriorityLessThanOrEqual(self):
        return self.priorityLessThanOrEqual

    def setPriorityLessThanOrEqual(self, newPriorityLessThanOrEqual):
        self.priorityLessThanOrEqual = newPriorityLessThanOrEqual

    def getPriorityEqual(self):
        return self.priorityEqual

    def setPriorityEqual(self, newPriorityEqual):
        self.priorityEqual = newPriorityEqual

    def getPriorityIn(self):
        return self.priorityIn

    def setPriorityIn(self, newPriorityIn):
        self.priorityIn = newPriorityIn

    def getPriorityNotIn(self):
        return self.priorityNotIn

    def setPriorityNotIn(self, newPriorityNotIn):
        self.priorityNotIn = newPriorityNotIn

    def getTwinJobIdEqual(self):
        return self.twinJobIdEqual

    def setTwinJobIdEqual(self, newTwinJobIdEqual):
        self.twinJobIdEqual = newTwinJobIdEqual

    def getTwinJobIdIn(self):
        return self.twinJobIdIn

    def setTwinJobIdIn(self, newTwinJobIdIn):
        self.twinJobIdIn = newTwinJobIdIn

    def getTwinJobIdNotIn(self):
        return self.twinJobIdNotIn

    def setTwinJobIdNotIn(self, newTwinJobIdNotIn):
        self.twinJobIdNotIn = newTwinJobIdNotIn

    def getBulkJobIdEqual(self):
        return self.bulkJobIdEqual

    def setBulkJobIdEqual(self, newBulkJobIdEqual):
        self.bulkJobIdEqual = newBulkJobIdEqual

    def getBulkJobIdIn(self):
        return self.bulkJobIdIn

    def setBulkJobIdIn(self, newBulkJobIdIn):
        self.bulkJobIdIn = newBulkJobIdIn

    def getBulkJobIdNotIn(self):
        return self.bulkJobIdNotIn

    def setBulkJobIdNotIn(self, newBulkJobIdNotIn):
        self.bulkJobIdNotIn = newBulkJobIdNotIn

    def getParentJobIdEqual(self):
        return self.parentJobIdEqual

    def setParentJobIdEqual(self, newParentJobIdEqual):
        self.parentJobIdEqual = newParentJobIdEqual

    def getParentJobIdIn(self):
        return self.parentJobIdIn

    def setParentJobIdIn(self, newParentJobIdIn):
        self.parentJobIdIn = newParentJobIdIn

    def getParentJobIdNotIn(self):
        return self.parentJobIdNotIn

    def setParentJobIdNotIn(self, newParentJobIdNotIn):
        self.parentJobIdNotIn = newParentJobIdNotIn

    def getRootJobIdEqual(self):
        return self.rootJobIdEqual

    def setRootJobIdEqual(self, newRootJobIdEqual):
        self.rootJobIdEqual = newRootJobIdEqual

    def getRootJobIdIn(self):
        return self.rootJobIdIn

    def setRootJobIdIn(self, newRootJobIdIn):
        self.rootJobIdIn = newRootJobIdIn

    def getRootJobIdNotIn(self):
        return self.rootJobIdNotIn

    def setRootJobIdNotIn(self, newRootJobIdNotIn):
        self.rootJobIdNotIn = newRootJobIdNotIn

    def getQueueTimeGreaterThanOrEqual(self):
        return self.queueTimeGreaterThanOrEqual

    def setQueueTimeGreaterThanOrEqual(self, newQueueTimeGreaterThanOrEqual):
        self.queueTimeGreaterThanOrEqual = newQueueTimeGreaterThanOrEqual

    def getQueueTimeLessThanOrEqual(self):
        return self.queueTimeLessThanOrEqual

    def setQueueTimeLessThanOrEqual(self, newQueueTimeLessThanOrEqual):
        self.queueTimeLessThanOrEqual = newQueueTimeLessThanOrEqual

    def getFinishTimeGreaterThanOrEqual(self):
        return self.finishTimeGreaterThanOrEqual

    def setFinishTimeGreaterThanOrEqual(self, newFinishTimeGreaterThanOrEqual):
        self.finishTimeGreaterThanOrEqual = newFinishTimeGreaterThanOrEqual

    def getFinishTimeLessThanOrEqual(self):
        return self.finishTimeLessThanOrEqual

    def setFinishTimeLessThanOrEqual(self, newFinishTimeLessThanOrEqual):
        self.finishTimeLessThanOrEqual = newFinishTimeLessThanOrEqual

    def getErrTypeEqual(self):
        return self.errTypeEqual

    def setErrTypeEqual(self, newErrTypeEqual):
        self.errTypeEqual = newErrTypeEqual

    def getErrTypeIn(self):
        return self.errTypeIn

    def setErrTypeIn(self, newErrTypeIn):
        self.errTypeIn = newErrTypeIn

    def getErrTypeNotIn(self):
        return self.errTypeNotIn

    def setErrTypeNotIn(self, newErrTypeNotIn):
        self.errTypeNotIn = newErrTypeNotIn

    def getErrNumberEqual(self):
        return self.errNumberEqual

    def setErrNumberEqual(self, newErrNumberEqual):
        self.errNumberEqual = newErrNumberEqual

    def getErrNumberIn(self):
        return self.errNumberIn

    def setErrNumberIn(self, newErrNumberIn):
        self.errNumberIn = newErrNumberIn

    def getErrNumberNotIn(self):
        return self.errNumberNotIn

    def setErrNumberNotIn(self, newErrNumberNotIn):
        self.errNumberNotIn = newErrNumberNotIn

    def getFileSizeLessThan(self):
        return self.fileSizeLessThan

    def setFileSizeLessThan(self, newFileSizeLessThan):
        self.fileSizeLessThan = newFileSizeLessThan

    def getFileSizeGreaterThan(self):
        return self.fileSizeGreaterThan

    def setFileSizeGreaterThan(self, newFileSizeGreaterThan):
        self.fileSizeGreaterThan = newFileSizeGreaterThan

    def getLastWorkerRemoteEqual(self):
        return self.lastWorkerRemoteEqual

    def setLastWorkerRemoteEqual(self, newLastWorkerRemoteEqual):
        self.lastWorkerRemoteEqual = newLastWorkerRemoteEqual

    def getSchedulerIdEqual(self):
        return self.schedulerIdEqual

    def setSchedulerIdEqual(self, newSchedulerIdEqual):
        self.schedulerIdEqual = newSchedulerIdEqual

    def getSchedulerIdIn(self):
        return self.schedulerIdIn

    def setSchedulerIdIn(self, newSchedulerIdIn):
        self.schedulerIdIn = newSchedulerIdIn

    def getSchedulerIdNotIn(self):
        return self.schedulerIdNotIn

    def setSchedulerIdNotIn(self, newSchedulerIdNotIn):
        self.schedulerIdNotIn = newSchedulerIdNotIn

    def getWorkerIdEqual(self):
        return self.workerIdEqual

    def setWorkerIdEqual(self, newWorkerIdEqual):
        self.workerIdEqual = newWorkerIdEqual

    def getWorkerIdIn(self):
        return self.workerIdIn

    def setWorkerIdIn(self, newWorkerIdIn):
        self.workerIdIn = newWorkerIdIn

    def getWorkerIdNotIn(self):
        return self.workerIdNotIn

    def setWorkerIdNotIn(self, newWorkerIdNotIn):
        self.workerIdNotIn = newWorkerIdNotIn

    def getBatchIndexEqual(self):
        return self.batchIndexEqual

    def setBatchIndexEqual(self, newBatchIndexEqual):
        self.batchIndexEqual = newBatchIndexEqual

    def getBatchIndexIn(self):
        return self.batchIndexIn

    def setBatchIndexIn(self, newBatchIndexIn):
        self.batchIndexIn = newBatchIndexIn

    def getBatchIndexNotIn(self):
        return self.batchIndexNotIn

    def setBatchIndexNotIn(self, newBatchIndexNotIn):
        self.batchIndexNotIn = newBatchIndexNotIn

    def getLastSchedulerIdEqual(self):
        return self.lastSchedulerIdEqual

    def setLastSchedulerIdEqual(self, newLastSchedulerIdEqual):
        self.lastSchedulerIdEqual = newLastSchedulerIdEqual

    def getLastSchedulerIdIn(self):
        return self.lastSchedulerIdIn

    def setLastSchedulerIdIn(self, newLastSchedulerIdIn):
        self.lastSchedulerIdIn = newLastSchedulerIdIn

    def getLastSchedulerIdNotIn(self):
        return self.lastSchedulerIdNotIn

    def setLastSchedulerIdNotIn(self, newLastSchedulerIdNotIn):
        self.lastSchedulerIdNotIn = newLastSchedulerIdNotIn

    def getLastWorkerIdEqual(self):
        return self.lastWorkerIdEqual

    def setLastWorkerIdEqual(self, newLastWorkerIdEqual):
        self.lastWorkerIdEqual = newLastWorkerIdEqual

    def getLastWorkerIdIn(self):
        return self.lastWorkerIdIn

    def setLastWorkerIdIn(self, newLastWorkerIdIn):
        self.lastWorkerIdIn = newLastWorkerIdIn

    def getLastWorkerIdNotIn(self):
        return self.lastWorkerIdNotIn

    def setLastWorkerIdNotIn(self, newLastWorkerIdNotIn):
        self.lastWorkerIdNotIn = newLastWorkerIdNotIn

    def getDcEqual(self):
        return self.dcEqual

    def setDcEqual(self, newDcEqual):
        self.dcEqual = newDcEqual

    def getDcIn(self):
        return self.dcIn

    def setDcIn(self, newDcIn):
        self.dcIn = newDcIn

    def getDcNotIn(self):
        return self.dcNotIn

    def setDcNotIn(self, newDcNotIn):
        self.dcNotIn = newDcNotIn


class KalturaControlPanelCommandBaseFilter(KalturaFilter):
    def __init__(self):
        KalturaFilter.__init__(self)

        # @var int
        self.idEqual = None

        # @var string
        self.idIn = None

        # @var int
        self.createdAtGreaterThanOrEqual = None

        # @var int
        self.createdAtLessThanOrEqual = None

        # @var int
        self.createdByIdEqual = None

        # @var KalturaControlPanelCommandType
        self.typeEqual = None

        # @var string
        self.typeIn = None

        # @var KalturaControlPanelCommandTargetType
        self.targetTypeEqual = None

        # @var string
        self.targetTypeIn = None

        # @var KalturaControlPanelCommandStatus
        self.statusEqual = None

        # @var string
        self.statusIn = None


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'createdByIdEqual': getXmlNodeInt, 
        'typeEqual': (KalturaEnumsFactory.createInt, "KalturaControlPanelCommandType"), 
        'typeIn': getXmlNodeText, 
        'targetTypeEqual': (KalturaEnumsFactory.createInt, "KalturaControlPanelCommandTargetType"), 
        'targetTypeIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaControlPanelCommandStatus"), 
        'statusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaControlPanelCommandBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaControlPanelCommandBaseFilter")
        kparams.addIntIfNotNone("idEqual", self.idEqual)
        kparams.addStringIfNotNone("idIn", self.idIn)
        kparams.addIntIfNotNone("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfNotNone("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfNotNone("createdByIdEqual", self.createdByIdEqual)
        kparams.addIntEnumIfNotNone("typeEqual", self.typeEqual)
        kparams.addStringIfNotNone("typeIn", self.typeIn)
        kparams.addIntEnumIfNotNone("targetTypeEqual", self.targetTypeEqual)
        kparams.addStringIfNotNone("targetTypeIn", self.targetTypeIn)
        kparams.addIntEnumIfNotNone("statusEqual", self.statusEqual)
        kparams.addStringIfNotNone("statusIn", self.statusIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getCreatedByIdEqual(self):
        return self.createdByIdEqual

    def setCreatedByIdEqual(self, newCreatedByIdEqual):
        self.createdByIdEqual = newCreatedByIdEqual

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getTargetTypeEqual(self):
        return self.targetTypeEqual

    def setTargetTypeEqual(self, newTargetTypeEqual):
        self.targetTypeEqual = newTargetTypeEqual

    def getTargetTypeIn(self):
        return self.targetTypeIn

    def setTargetTypeIn(self, newTargetTypeIn):
        self.targetTypeIn = newTargetTypeIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn


class KalturaMailJobBaseFilter(KalturaBaseJobFilter):
    def __init__(self):
        KalturaBaseJobFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMailJobBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobFilter.toParams(self)
        kparams.put("objectType", "KalturaMailJobBaseFilter")
        return kparams


class KalturaNotificationBaseFilter(KalturaBaseJobFilter):
    def __init__(self):
        KalturaBaseJobFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNotificationBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseJobFilter.toParams(self)
        kparams.put("objectType", "KalturaNotificationBaseFilter")
        return kparams


class KalturaBatchJobFilter(KalturaBatchJobBaseFilter):
    def __init__(self):
        KalturaBatchJobBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBatchJobBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBatchJobFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBatchJobBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBatchJobFilter")
        return kparams


class KalturaControlPanelCommandFilter(KalturaControlPanelCommandBaseFilter):
    def __init__(self):
        KalturaControlPanelCommandBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaControlPanelCommandBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaControlPanelCommandFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaControlPanelCommandBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaControlPanelCommandFilter")
        return kparams


class KalturaMailJobFilter(KalturaMailJobBaseFilter):
    def __init__(self):
        KalturaMailJobBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMailJobBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMailJobFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMailJobBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMailJobFilter")
        return kparams


class KalturaNotificationFilter(KalturaNotificationBaseFilter):
    def __init__(self):
        KalturaNotificationBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaNotificationBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNotificationFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaNotificationBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaNotificationFilter")
        return kparams


class KalturaBatchJobFilterExt(KalturaBatchJobFilter):
    def __init__(self):
        KalturaBatchJobFilter.__init__(self)

        # @var string
        self.jobTypeAndSubTypeIn = None


    PROPERTY_LOADERS = {
        'jobTypeAndSubTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBatchJobFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBatchJobFilterExt.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBatchJobFilter.toParams(self)
        kparams.put("objectType", "KalturaBatchJobFilterExt")
        kparams.addStringIfNotNone("jobTypeAndSubTypeIn", self.jobTypeAndSubTypeIn)
        return kparams

    def getJobTypeAndSubTypeIn(self):
        return self.jobTypeAndSubTypeIn

    def setJobTypeAndSubTypeIn(self, newJobTypeAndSubTypeIn):
        self.jobTypeAndSubTypeIn = newJobTypeAndSubTypeIn


class KalturaAssetParamsOutputBaseFilter(KalturaAssetParamsFilter):
    def __init__(self):
        KalturaAssetParamsFilter.__init__(self)

        # @var int
        self.assetParamsIdEqual = None

        # @var string
        self.assetParamsVersionEqual = None

        # @var string
        self.assetIdEqual = None

        # @var string
        self.assetVersionEqual = None


    PROPERTY_LOADERS = {
        'assetParamsIdEqual': getXmlNodeInt, 
        'assetParamsVersionEqual': getXmlNodeText, 
        'assetIdEqual': getXmlNodeText, 
        'assetVersionEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsOutputBaseFilter")
        kparams.addIntIfNotNone("assetParamsIdEqual", self.assetParamsIdEqual)
        kparams.addStringIfNotNone("assetParamsVersionEqual", self.assetParamsVersionEqual)
        kparams.addStringIfNotNone("assetIdEqual", self.assetIdEqual)
        kparams.addStringIfNotNone("assetVersionEqual", self.assetVersionEqual)
        return kparams

    def getAssetParamsIdEqual(self):
        return self.assetParamsIdEqual

    def setAssetParamsIdEqual(self, newAssetParamsIdEqual):
        self.assetParamsIdEqual = newAssetParamsIdEqual

    def getAssetParamsVersionEqual(self):
        return self.assetParamsVersionEqual

    def setAssetParamsVersionEqual(self, newAssetParamsVersionEqual):
        self.assetParamsVersionEqual = newAssetParamsVersionEqual

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetVersionEqual(self):
        return self.assetVersionEqual

    def setAssetVersionEqual(self, newAssetVersionEqual):
        self.assetVersionEqual = newAssetVersionEqual


class KalturaFlavorAssetBaseFilter(KalturaAssetFilter):
    def __init__(self):
        KalturaAssetFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetBaseFilter")
        return kparams


class KalturaMediaFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self):
        KalturaFlavorParamsFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsBaseFilter")
        return kparams


class KalturaMediaFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self):
        KalturaFlavorParamsOutputFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsOutputBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutputFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsOutputBaseFilter")
        return kparams


class KalturaThumbAssetBaseFilter(KalturaAssetFilter):
    def __init__(self):
        KalturaAssetFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbAssetBaseFilter")
        return kparams


class KalturaAssetParamsOutputFilter(KalturaAssetParamsOutputBaseFilter):
    def __init__(self):
        KalturaAssetParamsOutputBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsOutputFilter")
        return kparams


class KalturaFlavorAssetFilter(KalturaFlavorAssetBaseFilter):
    def __init__(self):
        KalturaFlavorAssetBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFlavorAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaFlavorAssetFilter")
        return kparams


class KalturaMediaFlavorParamsFilter(KalturaMediaFlavorParamsBaseFilter):
    def __init__(self):
        KalturaMediaFlavorParamsBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaFlavorParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaFlavorParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsFilter")
        return kparams


class KalturaMediaFlavorParamsOutputFilter(KalturaMediaFlavorParamsOutputBaseFilter):
    def __init__(self):
        KalturaMediaFlavorParamsOutputBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaFlavorParamsOutputBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsOutputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaFlavorParamsOutputBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsOutputFilter")
        return kparams


class KalturaThumbAssetFilter(KalturaThumbAssetBaseFilter):
    def __init__(self):
        KalturaThumbAssetBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaThumbAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaThumbAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaThumbAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaThumbAssetFilter")
        return kparams


class KalturaLiveStreamAdminEntryBaseFilter(KalturaLiveStreamEntryFilter):
    def __init__(self):
        KalturaLiveStreamEntryFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaLiveStreamEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamAdminEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamAdminEntryBaseFilter")
        return kparams


class KalturaLiveStreamAdminEntryFilter(KalturaLiveStreamAdminEntryBaseFilter):
    def __init__(self):
        KalturaLiveStreamAdminEntryBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaLiveStreamAdminEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveStreamAdminEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveStreamAdminEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveStreamAdminEntryFilter")
        return kparams


class KalturaAdminUserBaseFilter(KalturaUserFilter):
    def __init__(self):
        KalturaUserFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdminUserBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserFilter.toParams(self)
        kparams.put("objectType", "KalturaAdminUserBaseFilter")
        return kparams


class KalturaAdminUserFilter(KalturaAdminUserBaseFilter):
    def __init__(self):
        KalturaAdminUserBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAdminUserBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAdminUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAdminUserBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaAdminUserFilter")
        return kparams


class KalturaGoogleVideoSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self):
        KalturaBaseSyndicationFeedFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGoogleVideoSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaGoogleVideoSyndicationFeedBaseFilter")
        return kparams


class KalturaGoogleVideoSyndicationFeedFilter(KalturaGoogleVideoSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaGoogleVideoSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGoogleVideoSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGoogleVideoSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGoogleVideoSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGoogleVideoSyndicationFeedFilter")
        return kparams


class KalturaITunesSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self):
        KalturaBaseSyndicationFeedFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaITunesSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaITunesSyndicationFeedBaseFilter")
        return kparams


class KalturaITunesSyndicationFeedFilter(KalturaITunesSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaITunesSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaITunesSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaITunesSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaITunesSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaITunesSyndicationFeedFilter")
        return kparams


class KalturaTubeMogulSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self):
        KalturaBaseSyndicationFeedFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTubeMogulSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaTubeMogulSyndicationFeedBaseFilter")
        return kparams


class KalturaTubeMogulSyndicationFeedFilter(KalturaTubeMogulSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaTubeMogulSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTubeMogulSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTubeMogulSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTubeMogulSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaTubeMogulSyndicationFeedFilter")
        return kparams


class KalturaYahooSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self):
        KalturaBaseSyndicationFeedFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYahooSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaYahooSyndicationFeedBaseFilter")
        return kparams


class KalturaYahooSyndicationFeedFilter(KalturaYahooSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaYahooSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaYahooSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYahooSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaYahooSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaYahooSyndicationFeedFilter")
        return kparams


class KalturaApiActionPermissionItemBaseFilter(KalturaPermissionItemFilter):
    def __init__(self):
        KalturaPermissionItemFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItemFilter.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItemBaseFilter")
        return kparams


class KalturaApiParameterPermissionItemBaseFilter(KalturaPermissionItemFilter):
    def __init__(self):
        KalturaPermissionItemFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPermissionItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItemFilter.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItemBaseFilter")
        return kparams


class KalturaApiActionPermissionItemFilter(KalturaApiActionPermissionItemBaseFilter):
    def __init__(self):
        KalturaApiActionPermissionItemBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaApiActionPermissionItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaApiActionPermissionItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItemFilter")
        return kparams


class KalturaApiParameterPermissionItemFilter(KalturaApiParameterPermissionItemBaseFilter):
    def __init__(self):
        KalturaApiParameterPermissionItemBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaApiParameterPermissionItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaApiParameterPermissionItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItemFilter")
        return kparams


class KalturaGenericSyndicationFeedBaseFilter(KalturaBaseSyndicationFeedFilter):
    def __init__(self):
        KalturaBaseSyndicationFeedFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericSyndicationFeedBaseFilter")
        return kparams


class KalturaGenericSyndicationFeedFilter(KalturaGenericSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaGenericSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericSyndicationFeedFilter")
        return kparams


class KalturaGenericXsltSyndicationFeedBaseFilter(KalturaGenericSyndicationFeedFilter):
    def __init__(self):
        KalturaGenericSyndicationFeedFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericSyndicationFeedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericXsltSyndicationFeedBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericSyndicationFeedFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericXsltSyndicationFeedBaseFilter")
        return kparams


class KalturaGenericXsltSyndicationFeedFilter(KalturaGenericXsltSyndicationFeedBaseFilter):
    def __init__(self):
        KalturaGenericXsltSyndicationFeedBaseFilter.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaGenericXsltSyndicationFeedBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericXsltSyndicationFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericXsltSyndicationFeedBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaGenericXsltSyndicationFeedFilter")
        return kparams


class KalturaAssetParamsOutput(KalturaAssetParams):
    def __init__(self):
        KalturaAssetParams.__init__(self)

        # @var int
        self.assetParamsId = None

        # @var string
        self.assetParamsVersion = None

        # @var string
        self.assetId = None

        # @var string
        self.assetVersion = None

        # @var int
        self.readyBehavior = None


    PROPERTY_LOADERS = {
        'assetParamsId': getXmlNodeInt, 
        'assetParamsVersion': getXmlNodeText, 
        'assetId': getXmlNodeText, 
        'assetVersion': getXmlNodeText, 
        'readyBehavior': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaAssetParamsOutput")
        kparams.addIntIfNotNone("assetParamsId", self.assetParamsId)
        kparams.addStringIfNotNone("assetParamsVersion", self.assetParamsVersion)
        kparams.addStringIfNotNone("assetId", self.assetId)
        kparams.addStringIfNotNone("assetVersion", self.assetVersion)
        kparams.addIntIfNotNone("readyBehavior", self.readyBehavior)
        return kparams

    def getAssetParamsId(self):
        return self.assetParamsId

    def setAssetParamsId(self, newAssetParamsId):
        self.assetParamsId = newAssetParamsId

    def getAssetParamsVersion(self):
        return self.assetParamsVersion

    def setAssetParamsVersion(self, newAssetParamsVersion):
        self.assetParamsVersion = newAssetParamsVersion

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getAssetVersion(self):
        return self.assetVersion

    def setAssetVersion(self, newAssetVersion):
        self.assetVersion = newAssetVersion

    def getReadyBehavior(self):
        return self.readyBehavior

    def setReadyBehavior(self, newReadyBehavior):
        self.readyBehavior = newReadyBehavior


class KalturaMediaFlavorParamsOutput(KalturaFlavorParamsOutput):
    def __init__(self):
        KalturaFlavorParamsOutput.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParamsOutput.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParamsOutput.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParamsOutput.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParamsOutput")
        return kparams


class KalturaMediaFlavorParams(KalturaFlavorParams):
    def __init__(self):
        KalturaFlavorParams.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFlavorParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFlavorParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFlavorParams.toParams(self)
        kparams.put("objectType", "KalturaMediaFlavorParams")
        return kparams


class KalturaApiActionPermissionItem(KalturaPermissionItem):
    def __init__(self):
        KalturaPermissionItem.__init__(self)

        # @var string
        self.service = None

        # @var string
        self.action = None


    PROPERTY_LOADERS = {
        'service': getXmlNodeText, 
        'action': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItem")
        kparams.addStringIfNotNone("service", self.service)
        kparams.addStringIfNotNone("action", self.action)
        return kparams

    def getService(self):
        return self.service

    def setService(self, newService):
        self.service = newService

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction


class KalturaApiParameterPermissionItem(KalturaPermissionItem):
    def __init__(self):
        KalturaPermissionItem.__init__(self)

        # @var string
        self.object = None

        # @var string
        self.parameter = None

        # @var KalturaApiParameterPermissionItemAction
        self.action = None


    PROPERTY_LOADERS = {
        'object': getXmlNodeText, 
        'parameter': getXmlNodeText, 
        'action': (KalturaEnumsFactory.createString, "KalturaApiParameterPermissionItemAction"), 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItem")
        kparams.addStringIfNotNone("object", self.object)
        kparams.addStringIfNotNone("parameter", self.parameter)
        kparams.addStringEnumIfNotNone("action", self.action)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject

    def getParameter(self):
        return self.parameter

    def setParameter(self, newParameter):
        self.parameter = newParameter

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction


class KalturaGenericSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self):
        KalturaBaseSyndicationFeed.__init__(self)

        # feed description
        # @var string
        self.feedDescription = None

        # feed landing page (i.e publisher website)
        # @var string
        self.feedLandingPage = None


    PROPERTY_LOADERS = {
        'feedDescription': getXmlNodeText, 
        'feedLandingPage': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaGenericSyndicationFeed")
        kparams.addStringIfNotNone("feedDescription", self.feedDescription)
        kparams.addStringIfNotNone("feedLandingPage", self.feedLandingPage)
        return kparams

    def getFeedDescription(self):
        return self.feedDescription

    def setFeedDescription(self, newFeedDescription):
        self.feedDescription = newFeedDescription

    def getFeedLandingPage(self):
        return self.feedLandingPage

    def setFeedLandingPage(self, newFeedLandingPage):
        self.feedLandingPage = newFeedLandingPage


class KalturaGenericXsltSyndicationFeed(KalturaGenericSyndicationFeed):
    def __init__(self):
        KalturaGenericSyndicationFeed.__init__(self)

        # @var string
        self.xslt = None


    PROPERTY_LOADERS = {
        'xslt': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaGenericSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericXsltSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaGenericSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaGenericXsltSyndicationFeed")
        kparams.addStringIfNotNone("xslt", self.xslt)
        return kparams

    def getXslt(self):
        return self.xslt

    def setXslt(self, newXslt):
        self.xslt = newXslt


class KalturaGoogleVideoSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self):
        KalturaBaseSyndicationFeed.__init__(self)

        # @var KalturaGoogleSyndicationFeedAdultValues
        self.adultContent = None


    PROPERTY_LOADERS = {
        'adultContent': (KalturaEnumsFactory.createString, "KalturaGoogleSyndicationFeedAdultValues"), 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGoogleVideoSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaGoogleVideoSyndicationFeed")
        kparams.addStringEnumIfNotNone("adultContent", self.adultContent)
        return kparams

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent


class KalturaITunesSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self):
        KalturaBaseSyndicationFeed.__init__(self)

        # feed description
        # @var string
        self.feedDescription = None

        # feed language
        # @var string
        self.language = None

        # feed landing page (i.e publisher website)
        # @var string
        self.feedLandingPage = None

        # author/publisher name
        # @var string
        self.ownerName = None

        # publisher email
        # @var string
        self.ownerEmail = None

        # podcast thumbnail
        # @var string
        self.feedImageUrl = None

        # @var KalturaITunesSyndicationFeedCategories
        # @readonly
        self.category = None

        # @var KalturaITunesSyndicationFeedAdultValues
        self.adultContent = None

        # @var string
        self.feedAuthor = None


    PROPERTY_LOADERS = {
        'feedDescription': getXmlNodeText, 
        'language': getXmlNodeText, 
        'feedLandingPage': getXmlNodeText, 
        'ownerName': getXmlNodeText, 
        'ownerEmail': getXmlNodeText, 
        'feedImageUrl': getXmlNodeText, 
        'category': (KalturaEnumsFactory.createString, "KalturaITunesSyndicationFeedCategories"), 
        'adultContent': (KalturaEnumsFactory.createString, "KalturaITunesSyndicationFeedAdultValues"), 
        'feedAuthor': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaITunesSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaITunesSyndicationFeed")
        kparams.addStringIfNotNone("feedDescription", self.feedDescription)
        kparams.addStringIfNotNone("language", self.language)
        kparams.addStringIfNotNone("feedLandingPage", self.feedLandingPage)
        kparams.addStringIfNotNone("ownerName", self.ownerName)
        kparams.addStringIfNotNone("ownerEmail", self.ownerEmail)
        kparams.addStringIfNotNone("feedImageUrl", self.feedImageUrl)
        kparams.addStringEnumIfNotNone("adultContent", self.adultContent)
        kparams.addStringIfNotNone("feedAuthor", self.feedAuthor)
        return kparams

    def getFeedDescription(self):
        return self.feedDescription

    def setFeedDescription(self, newFeedDescription):
        self.feedDescription = newFeedDescription

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getFeedLandingPage(self):
        return self.feedLandingPage

    def setFeedLandingPage(self, newFeedLandingPage):
        self.feedLandingPage = newFeedLandingPage

    def getOwnerName(self):
        return self.ownerName

    def setOwnerName(self, newOwnerName):
        self.ownerName = newOwnerName

    def getOwnerEmail(self):
        return self.ownerEmail

    def setOwnerEmail(self, newOwnerEmail):
        self.ownerEmail = newOwnerEmail

    def getFeedImageUrl(self):
        return self.feedImageUrl

    def setFeedImageUrl(self, newFeedImageUrl):
        self.feedImageUrl = newFeedImageUrl

    def getCategory(self):
        return self.category

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent

    def getFeedAuthor(self):
        return self.feedAuthor

    def setFeedAuthor(self, newFeedAuthor):
        self.feedAuthor = newFeedAuthor


class KalturaTubeMogulSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self):
        KalturaBaseSyndicationFeed.__init__(self)

        # @var KalturaTubeMogulSyndicationFeedCategories
        # @readonly
        self.category = None


    PROPERTY_LOADERS = {
        'category': (KalturaEnumsFactory.createString, "KalturaTubeMogulSyndicationFeedCategories"), 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTubeMogulSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaTubeMogulSyndicationFeed")
        return kparams

    def getCategory(self):
        return self.category


class KalturaYahooSyndicationFeed(KalturaBaseSyndicationFeed):
    def __init__(self):
        KalturaBaseSyndicationFeed.__init__(self)

        # @var KalturaYahooSyndicationFeedCategories
        # @readonly
        self.category = None

        # @var KalturaYahooSyndicationFeedAdultValues
        self.adultContent = None

        # feed description
        # @var string
        self.feedDescription = None

        # feed landing page (i.e publisher website)
        # @var string
        self.feedLandingPage = None


    PROPERTY_LOADERS = {
        'category': (KalturaEnumsFactory.createString, "KalturaYahooSyndicationFeedCategories"), 
        'adultContent': (KalturaEnumsFactory.createString, "KalturaYahooSyndicationFeedAdultValues"), 
        'feedDescription': getXmlNodeText, 
        'feedLandingPage': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSyndicationFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaYahooSyndicationFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSyndicationFeed.toParams(self)
        kparams.put("objectType", "KalturaYahooSyndicationFeed")
        kparams.addStringEnumIfNotNone("adultContent", self.adultContent)
        kparams.addStringIfNotNone("feedDescription", self.feedDescription)
        kparams.addStringIfNotNone("feedLandingPage", self.feedLandingPage)
        return kparams

    def getCategory(self):
        return self.category

    def getAdultContent(self):
        return self.adultContent

    def setAdultContent(self, newAdultContent):
        self.adultContent = newAdultContent

    def getFeedDescription(self):
        return self.feedDescription

    def setFeedDescription(self, newFeedDescription):
        self.feedDescription = newFeedDescription

    def getFeedLandingPage(self):
        return self.feedLandingPage

    def setFeedLandingPage(self, newFeedLandingPage):
        self.feedLandingPage = newFeedLandingPage


########## services ##########

class KalturaAccessControlService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, accessControl):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("accessControl", accessControl)
        self.client.queueServiceActionCall("accesscontrol", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControl)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("accesscontrol", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControl)

    def update(self, id, accessControl):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("accessControl", accessControl)
        self.client.queueServiceActionCall("accesscontrol", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControl)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("accesscontrol", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("accesscontrol", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAccessControlListResponse)


class KalturaAdminUserService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def updatePassword(self, email, password, newEmail = "", newPassword = ""):
        kparams = KalturaParams()
        kparams.put("email", email)
        kparams.put("password", password)
        kparams.put("newEmail", newEmail)
        kparams.put("newPassword", newPassword)
        self.client.queueServiceActionCall("adminuser", "updatePassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAdminUser)

    def resetPassword(self, email):
        kparams = KalturaParams()
        kparams.put("email", email)
        self.client.queueServiceActionCall("adminuser", "resetPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def login(self, email, password, partnerId = ""):
        kparams = KalturaParams()
        kparams.put("email", email)
        kparams.put("password", password)
        kparams.put("partnerId", partnerId)
        self.client.queueServiceActionCall("adminuser", "login", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def setInitialPassword(self, hashKey, newPassword):
        kparams = KalturaParams()
        kparams.put("hashKey", hashKey)
        kparams.put("newPassword", newPassword)
        self.client.queueServiceActionCall("adminuser", "setInitialPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaBaseEntryService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def addFromUploadedFile(self, entry, uploadTokenId, type = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("entry", entry)
        kparams.put("uploadTokenId", uploadTokenId)
        kparams.put("type", type)
        self.client.queueServiceActionCall("baseentry", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("baseentry", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def update(self, entryId, baseEntry):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("baseEntry", baseEntry)
        self.client.queueServiceActionCall("baseentry", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getByIds(self, entryIds):
        kparams = KalturaParams()
        kparams.put("entryIds", entryIds)
        self.client.queueServiceActionCall("baseentry", "getByIds", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def delete(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("baseentry", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntryListResponse)

    def count(self, filter = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        self.client.queueServiceActionCall("baseentry", "count", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def upload(self, fileData):
        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("baseentry", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateThumbnailJpeg(self, entryId, fileData):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("baseentry", "updateThumbnailJpeg", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def updateThumbnailFromUrl(self, entryId, url):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("url", url)
        self.client.queueServiceActionCall("baseentry", "updateThumbnailFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def updateThumbnailFromSourceEntry(self, entryId, sourceEntryId, timeOffset):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("sourceEntryId", sourceEntryId)
        kparams.put("timeOffset", timeOffset)
        self.client.queueServiceActionCall("baseentry", "updateThumbnailFromSourceEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def flag(self, moderationFlag):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("moderationFlag", moderationFlag)
        self.client.queueServiceActionCall("baseentry", "flag", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reject(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "reject", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def approve(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("baseentry", "approve", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listFlags(self, entryId, pager = None):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("baseentry", "listFlags", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaModerationFlagListResponse)

    def anonymousRank(self, entryId, rank):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("rank", rank)
        self.client.queueServiceActionCall("baseentry", "anonymousRank", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getContextData(self, entryId, contextDataParams):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("contextDataParams", contextDataParams)
        self.client.queueServiceActionCall("baseentry", "getContextData", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntryContextDataResult)


class KalturaBulkUploadService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, conversionProfileId, csvFileData):
        kparams = KalturaParams()
        kparams.put("conversionProfileId", conversionProfileId)
        kfiles = KalturaFiles()
        kfiles.put("csvFileData", csvFileData)
        self.client.queueServiceActionCall("bulkupload", "add", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUpload)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("bulkupload", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUpload)

    def list(self, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("bulkupload", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBulkUploadListResponse)


class KalturaCategoryService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, category):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("category", category)
        self.client.queueServiceActionCall("category", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategory)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("category", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategory)

    def update(self, id, category):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("category", category)
        self.client.queueServiceActionCall("category", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategory)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("category", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        self.client.queueServiceActionCall("category", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCategoryListResponse)


class KalturaConversionProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, conversionProfile):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("conversionProfile", conversionProfile)
        self.client.queueServiceActionCall("conversionprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("conversionprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def update(self, id, conversionProfile):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("conversionProfile", conversionProfile)
        self.client.queueServiceActionCall("conversionprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfile)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("conversionprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("conversionprofile", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaConversionProfileListResponse)


class KalturaDataService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, dataEntry):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("dataEntry", dataEntry)
        self.client.queueServiceActionCall("data", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataEntry)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("data", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataEntry)

    def update(self, entryId, documentEntry):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("documentEntry", documentEntry)
        self.client.queueServiceActionCall("data", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataEntry)

    def delete(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("data", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("data", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDataListResponse)


class KalturaEmailIngestionProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, EmailIP):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("EmailIP", EmailIP)
        self.client.queueServiceActionCall("emailingestionprofile", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def getByEmailAddress(self, emailAddress):
        kparams = KalturaParams()
        kparams.put("emailAddress", emailAddress)
        self.client.queueServiceActionCall("emailingestionprofile", "getByEmailAddress", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("emailingestionprofile", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def update(self, id, EmailIP):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("EmailIP", EmailIP)
        self.client.queueServiceActionCall("emailingestionprofile", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEmailIngestionProfile)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("emailingestionprofile", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def addMediaEntry(self, mediaEntry, uploadTokenId, emailProfId, fromAddress, emailMsgId):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        kparams.put("uploadTokenId", uploadTokenId)
        kparams.put("emailProfId", emailProfId)
        kparams.put("fromAddress", fromAddress)
        kparams.put("emailMsgId", emailMsgId)
        self.client.queueServiceActionCall("emailingestionprofile", "addMediaEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)


class KalturaFlavorAssetService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("flavorasset", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAsset)

    def getByEntryId(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("flavorasset", "getByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorAsset)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("flavorasset", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorAssetListResponse)

    def getWebPlayableByEntryId(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("flavorasset", "getWebPlayableByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorAsset)

    def convert(self, entryId, flavorParamsId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("flavorParamsId", flavorParamsId)
        self.client.queueServiceActionCall("flavorasset", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reconvert(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("flavorasset", "reconvert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("flavorasset", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getDownloadUrl(self, id, useCdn = False):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("useCdn", useCdn)
        self.client.queueServiceActionCall("flavorasset", "getDownloadUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getFlavorAssetsWithParams(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("flavorasset", "getFlavorAssetsWithParams", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorAssetWithParams)


class KalturaFlavorParamsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, flavorParams):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("flavorParams", flavorParams)
        self.client.queueServiceActionCall("flavorparams", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParams)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("flavorparams", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParams)

    def update(self, id, flavorParams):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("flavorParams", flavorParams)
        self.client.queueServiceActionCall("flavorparams", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParams)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("flavorparams", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("flavorparams", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFlavorParamsListResponse)

    def getByConversionProfileId(self, conversionProfileId):
        kparams = KalturaParams()
        kparams.put("conversionProfileId", conversionProfileId)
        self.client.queueServiceActionCall("flavorparams", "getByConversionProfileId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaFlavorParams)


class KalturaLiveStreamService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, liveStreamEntry, sourceType = ""):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("liveStreamEntry", liveStreamEntry)
        kparams.put("sourceType", sourceType)
        self.client.queueServiceActionCall("livestream", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamAdminEntry)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("livestream", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamEntry)

    def update(self, entryId, liveStreamEntry):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("liveStreamEntry", liveStreamEntry)
        self.client.queueServiceActionCall("livestream", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamAdminEntry)

    def delete(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("livestream", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("livestream", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamListResponse)

    def updateOfflineThumbnailJpeg(self, entryId, fileData):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("livestream", "updateOfflineThumbnailJpeg", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamEntry)

    def updateOfflineThumbnailFromUrl(self, entryId, url):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("url", url)
        self.client.queueServiceActionCall("livestream", "updateOfflineThumbnailFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLiveStreamEntry)


class KalturaMediaService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def addFromUrl(self, mediaEntry, url):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        kparams.put("url", url)
        self.client.queueServiceActionCall("media", "addFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromSearchResult(self, mediaEntry = None, searchResult = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        kparams.addObjectIfNotNone("searchResult", searchResult)
        self.client.queueServiceActionCall("media", "addFromSearchResult", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromUploadedFile(self, mediaEntry, uploadTokenId):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        kparams.put("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("media", "addFromUploadedFile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromRecordedWebcam(self, mediaEntry, webcamTokenId):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        kparams.put("webcamTokenId", webcamTokenId)
        self.client.queueServiceActionCall("media", "addFromRecordedWebcam", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromEntry(self, sourceEntryId, mediaEntry = None, sourceFlavorParamsId = ""):
        kparams = KalturaParams()
        kparams.put("sourceEntryId", sourceEntryId)
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        kparams.put("sourceFlavorParamsId", sourceFlavorParamsId)
        self.client.queueServiceActionCall("media", "addFromEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def addFromFlavorAsset(self, sourceFlavorAssetId, mediaEntry = None):
        kparams = KalturaParams()
        kparams.put("sourceFlavorAssetId", sourceFlavorAssetId)
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        self.client.queueServiceActionCall("media", "addFromFlavorAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def convert(self, entryId, conversionProfileId = "", dynamicConversionAttributes = None):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("conversionProfileId", conversionProfileId)
        kparams.addArrayIfNotNone("dynamicConversionAttributes", dynamicConversionAttributes)
        self.client.queueServiceActionCall("media", "convert", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("media", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def update(self, entryId, mediaEntry):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("mediaEntry", mediaEntry)
        self.client.queueServiceActionCall("media", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaEntry)

    def delete(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("media", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("media", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMediaListResponse)

    def count(self, filter = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        self.client.queueServiceActionCall("media", "count", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def upload(self, fileData):
        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("media", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def requestConversion(self, entryId, fileFormat):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("fileFormat", fileFormat)
        self.client.queueServiceActionCall("media", "requestConversion", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def flag(self, moderationFlag):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("moderationFlag", moderationFlag)
        self.client.queueServiceActionCall("media", "flag", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reject(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("media", "reject", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def approve(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("media", "approve", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listFlags(self, entryId, pager = None):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("media", "listFlags", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaModerationFlagListResponse)

    def anonymousRank(self, entryId, rank):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("rank", rank)
        self.client.queueServiceActionCall("media", "anonymousRank", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaMixingService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, mixEntry):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("mixEntry", mixEntry)
        self.client.queueServiceActionCall("mixing", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def get(self, entryId, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("mixing", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def update(self, entryId, mixEntry):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("mixEntry", mixEntry)
        self.client.queueServiceActionCall("mixing", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def delete(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("mixing", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("mixing", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixListResponse)

    def count(self, filter = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        self.client.queueServiceActionCall("mixing", "count", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def clone(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("mixing", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def appendMediaEntry(self, mixEntryId, mediaEntryId):
        kparams = KalturaParams()
        kparams.put("mixEntryId", mixEntryId)
        kparams.put("mediaEntryId", mediaEntryId)
        self.client.queueServiceActionCall("mixing", "appendMediaEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMixEntry)

    def requestFlattening(self, entryId, fileFormat, version = -1):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("fileFormat", fileFormat)
        kparams.put("version", version)
        self.client.queueServiceActionCall("mixing", "requestFlattening", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def getMixesByMediaId(self, mediaEntryId):
        kparams = KalturaParams()
        kparams.put("mediaEntryId", mediaEntryId)
        self.client.queueServiceActionCall("mixing", "getMixesByMediaId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaMixEntry)

    def getReadyMediaEntries(self, mixId, version = -1):
        kparams = KalturaParams()
        kparams.put("mixId", mixId)
        kparams.put("version", version)
        self.client.queueServiceActionCall("mixing", "getReadyMediaEntries", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaMediaEntry)

    def anonymousRank(self, entryId, rank):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("rank", rank)
        self.client.queueServiceActionCall("mixing", "anonymousRank", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaNotificationService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getClientNotification(self, entryId, type):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("type", type)
        self.client.queueServiceActionCall("notification", "getClientNotification", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaClientNotification)


class KalturaPartnerService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def register(self, partner, cmsPassword = ""):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("partner", partner)
        kparams.put("cmsPassword", cmsPassword)
        self.client.queueServiceActionCall("partner", "register", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def update(self, partner, allowEmpty = False):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("partner", partner)
        kparams.put("allowEmpty", allowEmpty)
        self.client.queueServiceActionCall("partner", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getSecrets(self, partnerId, adminEmail, cmsPassword):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        kparams.put("adminEmail", adminEmail)
        kparams.put("cmsPassword", cmsPassword)
        self.client.queueServiceActionCall("partner", "getSecrets", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getInfo(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("partner", "getInfo", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getUsage(self, year = "", month = 1, resolution = "days"):
        kparams = KalturaParams()
        kparams.put("year", year)
        kparams.put("month", month)
        kparams.put("resolution", resolution)
        self.client.queueServiceActionCall("partner", "getUsage", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartnerUsage)


class KalturaPermissionItemService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, permissionItem):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("permissionItem", permissionItem)
        self.client.queueServiceActionCall("permissionitem", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def get(self, permissionItemId):
        kparams = KalturaParams()
        kparams.put("permissionItemId", permissionItemId)
        self.client.queueServiceActionCall("permissionitem", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def update(self, permissionItemId, permissionItem):
        kparams = KalturaParams()
        kparams.put("permissionItemId", permissionItemId)
        kparams.addObjectIfNotNone("permissionItem", permissionItem)
        self.client.queueServiceActionCall("permissionitem", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def delete(self, permissionItemId):
        kparams = KalturaParams()
        kparams.put("permissionItemId", permissionItemId)
        self.client.queueServiceActionCall("permissionitem", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItem)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("permissionitem", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionItemListResponse)


class KalturaPermissionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, permission):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("permission", permission)
        self.client.queueServiceActionCall("permission", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def get(self, permissionName):
        kparams = KalturaParams()
        kparams.put("permissionName", permissionName)
        self.client.queueServiceActionCall("permission", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def update(self, permissionName, permission):
        kparams = KalturaParams()
        kparams.put("permissionName", permissionName)
        kparams.addObjectIfNotNone("permission", permission)
        self.client.queueServiceActionCall("permission", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def delete(self, permissionName):
        kparams = KalturaParams()
        kparams.put("permissionName", permissionName)
        self.client.queueServiceActionCall("permission", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermission)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("permission", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPermissionListResponse)

    def getCurrentPermissions(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("permission", "getCurrentPermissions", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)


class KalturaPlaylistService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, playlist, updateStats = False):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("playlist", playlist)
        kparams.put("updateStats", updateStats)
        self.client.queueServiceActionCall("playlist", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def get(self, id, version = -1):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("version", version)
        self.client.queueServiceActionCall("playlist", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def update(self, id, playlist, updateStats = False):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("playlist", playlist)
        kparams.put("updateStats", updateStats)
        self.client.queueServiceActionCall("playlist", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("playlist", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def clone(self, id, newPlaylist = None):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("newPlaylist", newPlaylist)
        self.client.queueServiceActionCall("playlist", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("playlist", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylistListResponse)

    def execute(self, id, detailed = ""):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.put("detailed", detailed)
        self.client.queueServiceActionCall("playlist", "execute", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def executeFromContent(self, playlistType, playlistContent, detailed = ""):
        kparams = KalturaParams()
        kparams.put("playlistType", playlistType)
        kparams.put("playlistContent", playlistContent)
        kparams.put("detailed", detailed)
        self.client.queueServiceActionCall("playlist", "executeFromContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def executeFromFilters(self, filters, totalResults, detailed = ""):
        kparams = KalturaParams()
        kparams.addArrayIfNotNone("filters", filters)
        kparams.put("totalResults", totalResults)
        kparams.put("detailed", detailed)
        self.client.queueServiceActionCall("playlist", "executeFromFilters", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaBaseEntry)

    def getStatsFromContent(self, playlistType, playlistContent):
        kparams = KalturaParams()
        kparams.put("playlistType", playlistType)
        kparams.put("playlistContent", playlistContent)
        self.client.queueServiceActionCall("playlist", "getStatsFromContent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPlaylist)


class KalturaReportService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getGraphs(self, reportType, reportInputFilter, dimension = "", objectIds = ""):
        kparams = KalturaParams()
        kparams.put("reportType", reportType)
        kparams.addObjectIfNotNone("reportInputFilter", reportInputFilter)
        kparams.put("dimension", dimension)
        kparams.put("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getGraphs", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaReportGraph)

    def getTotal(self, reportType, reportInputFilter, objectIds = ""):
        kparams = KalturaParams()
        kparams.put("reportType", reportType)
        kparams.addObjectIfNotNone("reportInputFilter", reportInputFilter)
        kparams.put("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getTotal", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportTotal)

    def getTable(self, reportType, reportInputFilter, pager, order = "", objectIds = ""):
        kparams = KalturaParams()
        kparams.put("reportType", reportType)
        kparams.addObjectIfNotNone("reportInputFilter", reportInputFilter)
        kparams.addObjectIfNotNone("pager", pager)
        kparams.put("order", order)
        kparams.put("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getTable", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportTable)

    def getUrlForReportAsCsv(self, reportTitle, reportText, headers, reportType, reportInputFilter, dimension = "", pager = None, order = "", objectIds = ""):
        kparams = KalturaParams()
        kparams.put("reportTitle", reportTitle)
        kparams.put("reportText", reportText)
        kparams.put("headers", headers)
        kparams.put("reportType", reportType)
        kparams.addObjectIfNotNone("reportInputFilter", reportInputFilter)
        kparams.put("dimension", dimension)
        kparams.addObjectIfNotNone("pager", pager)
        kparams.put("order", order)
        kparams.put("objectIds", objectIds)
        self.client.queueServiceActionCall("report", "getUrlForReportAsCsv", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)


class KalturaSearchService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def search(self, search, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("search", search)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("search", "search", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchResultResponse)

    def getMediaInfo(self, searchResult):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("searchResult", searchResult)
        self.client.queueServiceActionCall("search", "getMediaInfo", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchResult)

    def searchUrl(self, mediaType, url):
        kparams = KalturaParams()
        kparams.put("mediaType", mediaType)
        kparams.put("url", url)
        self.client.queueServiceActionCall("search", "searchUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchResult)

    def externalLogin(self, searchSource, userName, password):
        kparams = KalturaParams()
        kparams.put("searchSource", searchSource)
        kparams.put("userName", userName)
        kparams.put("password", password)
        self.client.queueServiceActionCall("search", "externalLogin", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSearchAuthData)


class KalturaSessionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def start(self, secret, userId = "", type = 0, partnerId = "", expiry = 86400, privileges = ""):
        kparams = KalturaParams()
        kparams.put("secret", secret)
        kparams.put("userId", userId)
        kparams.put("type", type)
        kparams.put("partnerId", partnerId)
        kparams.put("expiry", expiry)
        kparams.put("privileges", privileges)
        self.client.queueServiceActionCall("session", "start", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def end(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("session", "end", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def impersonate(self, secret, impersonatedPartnerId, userId = "", type = 0, partnerId = "", expiry = 86400, privileges = ""):
        kparams = KalturaParams()
        kparams.put("secret", secret)
        kparams.put("impersonatedPartnerId", impersonatedPartnerId)
        kparams.put("userId", userId)
        kparams.put("type", type)
        kparams.put("partnerId", partnerId)
        kparams.put("expiry", expiry)
        kparams.put("privileges", privileges)
        self.client.queueServiceActionCall("session", "impersonate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def startWidgetSession(self, widgetId, expiry = 86400):
        kparams = KalturaParams()
        kparams.put("widgetId", widgetId)
        kparams.put("expiry", expiry)
        self.client.queueServiceActionCall("session", "startWidgetSession", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStartWidgetSessionResponse)


class KalturaStatsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def collect(self, event):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("event", event)
        self.client.queueServiceActionCall("stats", "collect", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def kmcCollect(self, kmcEvent):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("kmcEvent", kmcEvent)
        self.client.queueServiceActionCall("stats", "kmcCollect", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def reportKceError(self, kalturaCEError):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("kalturaCEError", kalturaCEError)
        self.client.queueServiceActionCall("stats", "reportKceError", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCEError)


class KalturaSyndicationFeedService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, syndicationFeed):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("syndicationFeed", syndicationFeed)
        self.client.queueServiceActionCall("syndicationfeed", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeed)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("syndicationfeed", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeed)

    def update(self, id, syndicationFeed):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("syndicationFeed", syndicationFeed)
        self.client.queueServiceActionCall("syndicationfeed", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeed)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("syndicationfeed", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("syndicationfeed", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseSyndicationFeedListResponse)

    def getEntryCount(self, feedId):
        kparams = KalturaParams()
        kparams.put("feedId", feedId)
        self.client.queueServiceActionCall("syndicationfeed", "getEntryCount", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSyndicationFeedEntryCount)

    def requestConversion(self, feedId):
        kparams = KalturaParams()
        kparams.put("feedId", feedId)
        self.client.queueServiceActionCall("syndicationfeed", "requestConversion", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)


class KalturaSystemService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def ping(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("system", "ping", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


class KalturaThumbAssetService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def setAsDefault(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.put("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "setAsDefault", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def generateByEntryId(self, entryId, destThumbParamsId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("destThumbParamsId", destThumbParamsId)
        self.client.queueServiceActionCall("thumbasset", "generateByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def generate(self, entryId, thumbParams, sourceAssetId = ""):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.addObjectIfNotNone("thumbParams", thumbParams)
        kparams.put("sourceAssetId", sourceAssetId)
        self.client.queueServiceActionCall("thumbasset", "generate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def regenerate(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.put("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "regenerate", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def get(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.put("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def getByEntryId(self, entryId):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        self.client.queueServiceActionCall("thumbasset", "getByEntryId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaThumbAsset)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("thumbasset", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAssetListResponse)

    def addFromUrl(self, entryId, url):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kparams.put("url", url)
        self.client.queueServiceActionCall("thumbasset", "addFromUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def addFromImage(self, entryId, fileData):
        kparams = KalturaParams()
        kparams.put("entryId", entryId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("thumbasset", "addFromImage", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbAsset)

    def delete(self, thumbAssetId):
        kparams = KalturaParams()
        kparams.put("thumbAssetId", thumbAssetId)
        self.client.queueServiceActionCall("thumbasset", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()


class KalturaThumbParamsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, thumbParams):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("thumbParams", thumbParams)
        self.client.queueServiceActionCall("thumbparams", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParams)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("thumbparams", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParams)

    def update(self, id, thumbParams):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("thumbParams", thumbParams)
        self.client.queueServiceActionCall("thumbparams", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParams)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("thumbparams", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("thumbparams", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaThumbParamsListResponse)

    def getByConversionProfileId(self, conversionProfileId):
        kparams = KalturaParams()
        kparams.put("conversionProfileId", conversionProfileId)
        self.client.queueServiceActionCall("thumbparams", "getByConversionProfileId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaThumbParams)


class KalturaUiConfService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, uiConf):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("uiConf", uiConf)
        self.client.queueServiceActionCall("uiconf", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def update(self, id, uiConf):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("uiConf", uiConf)
        self.client.queueServiceActionCall("uiconf", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("uiconf", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("uiconf", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def clone(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("uiconf", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConf)

    def listTemplates(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("uiconf", "listTemplates", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfListResponse)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("uiconf", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfListResponse)

    def getAvailableTypes(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("uiconf", "getAvailableTypes", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaUiConfTypeInfo)


class KalturaUploadService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def upload(self, fileData):
        kparams = KalturaParams()
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        self.client.queueServiceActionCall("upload", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getUploadedFileTokenByFileName(self, fileName):
        kparams = KalturaParams()
        kparams.put("fileName", fileName)
        self.client.queueServiceActionCall("upload", "getUploadedFileTokenByFileName", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadResponse)


class KalturaUploadTokenService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, uploadToken = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("uploadToken", uploadToken)
        self.client.queueServiceActionCall("uploadtoken", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadToken)

    def get(self, uploadTokenId):
        kparams = KalturaParams()
        kparams.put("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("uploadtoken", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadToken)

    def upload(self, uploadTokenId, fileData, resume = False, finalChunk = True, resumeAt = -1):
        kparams = KalturaParams()
        kparams.put("uploadTokenId", uploadTokenId)
        kfiles = KalturaFiles()
        kfiles.put("fileData", fileData)
        kparams.put("resume", resume)
        kparams.put("finalChunk", finalChunk)
        kparams.put("resumeAt", resumeAt)
        self.client.queueServiceActionCall("uploadtoken", "upload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadToken)

    def delete(self, uploadTokenId):
        kparams = KalturaParams()
        kparams.put("uploadTokenId", uploadTokenId)
        self.client.queueServiceActionCall("uploadtoken", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("uploadtoken", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUploadTokenListResponse)


class KalturaUserRoleService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, userRole):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("userRole", userRole)
        self.client.queueServiceActionCall("userrole", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def get(self, userRoleId):
        kparams = KalturaParams()
        kparams.put("userRoleId", userRoleId)
        self.client.queueServiceActionCall("userrole", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def update(self, userRoleId, userRole):
        kparams = KalturaParams()
        kparams.put("userRoleId", userRoleId)
        kparams.addObjectIfNotNone("userRole", userRole)
        self.client.queueServiceActionCall("userrole", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def delete(self, userRoleId):
        kparams = KalturaParams()
        kparams.put("userRoleId", userRoleId)
        self.client.queueServiceActionCall("userrole", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("userrole", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRoleListResponse)

    def clone(self, userRoleId):
        kparams = KalturaParams()
        kparams.put("userRoleId", userRoleId)
        self.client.queueServiceActionCall("userrole", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRole)


class KalturaUserService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, user):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("user", user)
        self.client.queueServiceActionCall("user", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def update(self, userId, user):
        kparams = KalturaParams()
        kparams.put("userId", userId)
        kparams.addObjectIfNotNone("user", user)
        self.client.queueServiceActionCall("user", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def get(self, userId):
        kparams = KalturaParams()
        kparams.put("userId", userId)
        self.client.queueServiceActionCall("user", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def getByLoginId(self, loginId):
        kparams = KalturaParams()
        kparams.put("loginId", loginId)
        self.client.queueServiceActionCall("user", "getByLoginId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def delete(self, userId):
        kparams = KalturaParams()
        kparams.put("userId", userId)
        self.client.queueServiceActionCall("user", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("user", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserListResponse)

    def notifyBan(self, userId):
        kparams = KalturaParams()
        kparams.put("userId", userId)
        self.client.queueServiceActionCall("user", "notifyBan", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def login(self, partnerId, userId, password, expiry = 86400, privileges = "*"):
        kparams = KalturaParams()
        kparams.put("partnerId", partnerId)
        kparams.put("userId", userId)
        kparams.put("password", password)
        kparams.put("expiry", expiry)
        kparams.put("privileges", privileges)
        self.client.queueServiceActionCall("user", "login", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def loginByLoginId(self, loginId, password, partnerId = "", expiry = 86400, privileges = "*"):
        kparams = KalturaParams()
        kparams.put("loginId", loginId)
        kparams.put("password", password)
        kparams.put("partnerId", partnerId)
        kparams.put("expiry", expiry)
        kparams.put("privileges", privileges)
        self.client.queueServiceActionCall("user", "loginByLoginId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateLoginData(self, oldLoginId, password, newLoginId = "", newPassword = "", newFirstName = "", newLastName = ""):
        kparams = KalturaParams()
        kparams.put("oldLoginId", oldLoginId)
        kparams.put("password", password)
        kparams.put("newLoginId", newLoginId)
        kparams.put("newPassword", newPassword)
        kparams.put("newFirstName", newFirstName)
        kparams.put("newLastName", newLastName)
        self.client.queueServiceActionCall("user", "updateLoginData", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def resetPassword(self, email):
        kparams = KalturaParams()
        kparams.put("email", email)
        self.client.queueServiceActionCall("user", "resetPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def setInitialPassword(self, hashKey, newPassword):
        kparams = KalturaParams()
        kparams.put("hashKey", hashKey)
        kparams.put("newPassword", newPassword)
        self.client.queueServiceActionCall("user", "setInitialPassword", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def enableLogin(self, userId, loginId, password = ""):
        kparams = KalturaParams()
        kparams.put("userId", userId)
        kparams.put("loginId", loginId)
        kparams.put("password", password)
        self.client.queueServiceActionCall("user", "enableLogin", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)

    def disableLogin(self, userId = "", loginId = ""):
        kparams = KalturaParams()
        kparams.put("userId", userId)
        kparams.put("loginId", loginId)
        self.client.queueServiceActionCall("user", "disableLogin", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUser)


class KalturaWidgetService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, widget):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("widget", widget)
        self.client.queueServiceActionCall("widget", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def update(self, id, widget):
        kparams = KalturaParams()
        kparams.put("id", id)
        kparams.addObjectIfNotNone("widget", widget)
        self.client.queueServiceActionCall("widget", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def get(self, id):
        kparams = KalturaParams()
        kparams.put("id", id)
        self.client.queueServiceActionCall("widget", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def clone(self, widget):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("widget", widget)
        self.client.queueServiceActionCall("widget", "clone", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidget)

    def list(self, filter = None, pager = None):
        kparams = KalturaParams()
        kparams.addObjectIfNotNone("filter", filter)
        kparams.addObjectIfNotNone("pager", pager)
        self.client.queueServiceActionCall("widget", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaWidgetListResponse)


class KalturaXInternalService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def xAddBulkDownload(self, entryIds, flavorParamsId = ""):
        kparams = KalturaParams()
        kparams.put("entryIds", entryIds)
        kparams.put("flavorParamsId", flavorParamsId)
        self.client.queueServiceActionCall("xinternal", "xAddBulkDownload", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaCoreClient(KalturaClientPlugin):
    # KalturaCoreClient
    instance = None

    def __init__(self, client):
        KalturaClientPlugin.__init__(self, client)

    # @return KalturaCoreClient
    @staticmethod
    def get(client):
        if KalturaCoreClient.instance == None:
            KalturaCoreClient.instance = KalturaCoreClient(client)
        return KalturaCoreClient.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'accessControl': KalturaAccessControlService,
            'adminUser': KalturaAdminUserService,
            'baseEntry': KalturaBaseEntryService,
            'bulkUpload': KalturaBulkUploadService,
            'category': KalturaCategoryService,
            'conversionProfile': KalturaConversionProfileService,
            'data': KalturaDataService,
            'EmailIngestionProfile': KalturaEmailIngestionProfileService,
            'flavorAsset': KalturaFlavorAssetService,
            'flavorParams': KalturaFlavorParamsService,
            'liveStream': KalturaLiveStreamService,
            'media': KalturaMediaService,
            'mixing': KalturaMixingService,
            'notification': KalturaNotificationService,
            'partner': KalturaPartnerService,
            'permissionItem': KalturaPermissionItemService,
            'permission': KalturaPermissionService,
            'playlist': KalturaPlaylistService,
            'report': KalturaReportService,
            'search': KalturaSearchService,
            'session': KalturaSessionService,
            'stats': KalturaStatsService,
            'syndicationFeed': KalturaSyndicationFeedService,
            'system': KalturaSystemService,
            'thumbAsset': KalturaThumbAssetService,
            'thumbParams': KalturaThumbParamsService,
            'uiConf': KalturaUiConfService,
            'upload': KalturaUploadService,
            'uploadToken': KalturaUploadTokenService,
            'userRole': KalturaUserRoleService,
            'user': KalturaUserService,
            'widget': KalturaWidgetService,
            'xInternal': KalturaXInternalService,
        }

    def getEnums(self):
        return {
            'KalturaAccessControlOrderBy': KalturaAccessControlOrderBy,
            'KalturaAdminUserOrderBy': KalturaAdminUserOrderBy,
            'KalturaApiActionPermissionItemOrderBy': KalturaApiActionPermissionItemOrderBy,
            'KalturaApiParameterPermissionItemAction': KalturaApiParameterPermissionItemAction,
            'KalturaApiParameterPermissionItemOrderBy': KalturaApiParameterPermissionItemOrderBy,
            'KalturaAssetOrderBy': KalturaAssetOrderBy,
            'KalturaAssetParamsOrderBy': KalturaAssetParamsOrderBy,
            'KalturaAssetParamsOutputOrderBy': KalturaAssetParamsOutputOrderBy,
            'KalturaAssetType': KalturaAssetType,
            'KalturaAudioCodec': KalturaAudioCodec,
            'KalturaBaseEntryOrderBy': KalturaBaseEntryOrderBy,
            'KalturaBaseJobOrderBy': KalturaBaseJobOrderBy,
            'KalturaBaseSyndicationFeedOrderBy': KalturaBaseSyndicationFeedOrderBy,
            'KalturaBatchJobErrorTypes': KalturaBatchJobErrorTypes,
            'KalturaBatchJobOrderBy': KalturaBatchJobOrderBy,
            'KalturaBatchJobStatus': KalturaBatchJobStatus,
            'KalturaBatchJobType': KalturaBatchJobType,
            'KalturaBitRateMode': KalturaBitRateMode,
            'KalturaCategoryOrderBy': KalturaCategoryOrderBy,
            'KalturaCommercialUseType': KalturaCommercialUseType,
            'KalturaContainerFormat': KalturaContainerFormat,
            'KalturaControlPanelCommandOrderBy': KalturaControlPanelCommandOrderBy,
            'KalturaControlPanelCommandStatus': KalturaControlPanelCommandStatus,
            'KalturaControlPanelCommandTargetType': KalturaControlPanelCommandTargetType,
            'KalturaControlPanelCommandType': KalturaControlPanelCommandType,
            'KalturaConversionEngineType': KalturaConversionEngineType,
            'KalturaConversionProfileOrderBy': KalturaConversionProfileOrderBy,
            'KalturaCountryRestrictionType': KalturaCountryRestrictionType,
            'KalturaDataEntryOrderBy': KalturaDataEntryOrderBy,
            'KalturaDirectoryRestrictionType': KalturaDirectoryRestrictionType,
            'KalturaDurationType': KalturaDurationType,
            'KalturaEditorType': KalturaEditorType,
            'KalturaEmailIngestionProfileStatus': KalturaEmailIngestionProfileStatus,
            'KalturaEntryModerationStatus': KalturaEntryModerationStatus,
            'KalturaEntryStatus': KalturaEntryStatus,
            'KalturaEntryType': KalturaEntryType,
            'KalturaFileSyncObjectType': KalturaFileSyncObjectType,
            'KalturaFlavorAssetOrderBy': KalturaFlavorAssetOrderBy,
            'KalturaFlavorAssetStatus': KalturaFlavorAssetStatus,
            'KalturaFlavorParamsOrderBy': KalturaFlavorParamsOrderBy,
            'KalturaFlavorParamsOutputOrderBy': KalturaFlavorParamsOutputOrderBy,
            'KalturaGender': KalturaGender,
            'KalturaGenericSyndicationFeedOrderBy': KalturaGenericSyndicationFeedOrderBy,
            'KalturaGenericXsltSyndicationFeedOrderBy': KalturaGenericXsltSyndicationFeedOrderBy,
            'KalturaGoogleSyndicationFeedAdultValues': KalturaGoogleSyndicationFeedAdultValues,
            'KalturaGoogleVideoSyndicationFeedOrderBy': KalturaGoogleVideoSyndicationFeedOrderBy,
            'KalturaITunesSyndicationFeedAdultValues': KalturaITunesSyndicationFeedAdultValues,
            'KalturaITunesSyndicationFeedCategories': KalturaITunesSyndicationFeedCategories,
            'KalturaITunesSyndicationFeedOrderBy': KalturaITunesSyndicationFeedOrderBy,
            'KalturaIpAddressRestrictionType': KalturaIpAddressRestrictionType,
            'KalturaLicenseType': KalturaLicenseType,
            'KalturaLiveStreamAdminEntryOrderBy': KalturaLiveStreamAdminEntryOrderBy,
            'KalturaLiveStreamEntryOrderBy': KalturaLiveStreamEntryOrderBy,
            'KalturaMailJobOrderBy': KalturaMailJobOrderBy,
            'KalturaMediaEntryOrderBy': KalturaMediaEntryOrderBy,
            'KalturaMediaFlavorParamsOrderBy': KalturaMediaFlavorParamsOrderBy,
            'KalturaMediaFlavorParamsOutputOrderBy': KalturaMediaFlavorParamsOutputOrderBy,
            'KalturaMediaInfoOrderBy': KalturaMediaInfoOrderBy,
            'KalturaMediaType': KalturaMediaType,
            'KalturaMixEntryOrderBy': KalturaMixEntryOrderBy,
            'KalturaModerationFlagStatus': KalturaModerationFlagStatus,
            'KalturaModerationFlagType': KalturaModerationFlagType,
            'KalturaModerationObjectType': KalturaModerationObjectType,
            'KalturaNotificationOrderBy': KalturaNotificationOrderBy,
            'KalturaNotificationType': KalturaNotificationType,
            'KalturaNullableBoolean': KalturaNullableBoolean,
            'KalturaPartnerOrderBy': KalturaPartnerOrderBy,
            'KalturaPartnerStatus': KalturaPartnerStatus,
            'KalturaPartnerType': KalturaPartnerType,
            'KalturaPermissionItemOrderBy': KalturaPermissionItemOrderBy,
            'KalturaPermissionItemType': KalturaPermissionItemType,
            'KalturaPermissionName': KalturaPermissionName,
            'KalturaPermissionOrderBy': KalturaPermissionOrderBy,
            'KalturaPermissionStatus': KalturaPermissionStatus,
            'KalturaPermissionType': KalturaPermissionType,
            'KalturaPlayableEntryOrderBy': KalturaPlayableEntryOrderBy,
            'KalturaPlaylistOrderBy': KalturaPlaylistOrderBy,
            'KalturaPlaylistType': KalturaPlaylistType,
            'KalturaReportType': KalturaReportType,
            'KalturaSearchConditionComparison': KalturaSearchConditionComparison,
            'KalturaSearchOperatorType': KalturaSearchOperatorType,
            'KalturaSearchProviderType': KalturaSearchProviderType,
            'KalturaSessionType': KalturaSessionType,
            'KalturaSiteRestrictionType': KalturaSiteRestrictionType,
            'KalturaSourceType': KalturaSourceType,
            'KalturaStatsEventType': KalturaStatsEventType,
            'KalturaStatsKmcEventType': KalturaStatsKmcEventType,
            'KalturaSyndicationFeedStatus': KalturaSyndicationFeedStatus,
            'KalturaSyndicationFeedType': KalturaSyndicationFeedType,
            'KalturaThumbAssetOrderBy': KalturaThumbAssetOrderBy,
            'KalturaThumbCropType': KalturaThumbCropType,
            'KalturaThumbParamsOrderBy': KalturaThumbParamsOrderBy,
            'KalturaThumbParamsOutputOrderBy': KalturaThumbParamsOutputOrderBy,
            'KalturaTubeMogulSyndicationFeedCategories': KalturaTubeMogulSyndicationFeedCategories,
            'KalturaTubeMogulSyndicationFeedOrderBy': KalturaTubeMogulSyndicationFeedOrderBy,
            'KalturaUiConfCreationMode': KalturaUiConfCreationMode,
            'KalturaUiConfObjType': KalturaUiConfObjType,
            'KalturaUiConfOrderBy': KalturaUiConfOrderBy,
            'KalturaUploadErrorCode': KalturaUploadErrorCode,
            'KalturaUploadTokenOrderBy': KalturaUploadTokenOrderBy,
            'KalturaUploadTokenStatus': KalturaUploadTokenStatus,
            'KalturaUserOrderBy': KalturaUserOrderBy,
            'KalturaUserRoleOrderBy': KalturaUserRoleOrderBy,
            'KalturaUserRoleStatus': KalturaUserRoleStatus,
            'KalturaUserStatus': KalturaUserStatus,
            'KalturaVideoCodec': KalturaVideoCodec,
            'KalturaWidgetOrderBy': KalturaWidgetOrderBy,
            'KalturaWidgetSecurityType': KalturaWidgetSecurityType,
            'KalturaYahooSyndicationFeedAdultValues': KalturaYahooSyndicationFeedAdultValues,
            'KalturaYahooSyndicationFeedCategories': KalturaYahooSyndicationFeedCategories,
            'KalturaYahooSyndicationFeedOrderBy': KalturaYahooSyndicationFeedOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaBaseRestriction': KalturaBaseRestriction,
            'KalturaAccessControl': KalturaAccessControl,
            'KalturaSearchItem': KalturaSearchItem,
            'KalturaFilter': KalturaFilter,
            'KalturaAccessControlBaseFilter': KalturaAccessControlBaseFilter,
            'KalturaAccessControlFilter': KalturaAccessControlFilter,
            'KalturaFilterPager': KalturaFilterPager,
            'KalturaAccessControlListResponse': KalturaAccessControlListResponse,
            'KalturaUser': KalturaUser,
            'KalturaDynamicEnum': KalturaDynamicEnum,
            'KalturaBaseEntry': KalturaBaseEntry,
            'KalturaBaseEntryBaseFilter': KalturaBaseEntryBaseFilter,
            'KalturaBaseEntryFilter': KalturaBaseEntryFilter,
            'KalturaBaseEntryListResponse': KalturaBaseEntryListResponse,
            'KalturaModerationFlag': KalturaModerationFlag,
            'KalturaModerationFlagListResponse': KalturaModerationFlagListResponse,
            'KalturaEntryContextDataParams': KalturaEntryContextDataParams,
            'KalturaEntryContextDataResult': KalturaEntryContextDataResult,
            'KalturaBulkUploadPluginData': KalturaBulkUploadPluginData,
            'KalturaBulkUploadResult': KalturaBulkUploadResult,
            'KalturaBulkUpload': KalturaBulkUpload,
            'KalturaBulkUploadListResponse': KalturaBulkUploadListResponse,
            'KalturaCategory': KalturaCategory,
            'KalturaCategoryBaseFilter': KalturaCategoryBaseFilter,
            'KalturaCategoryFilter': KalturaCategoryFilter,
            'KalturaCategoryListResponse': KalturaCategoryListResponse,
            'KalturaCropDimensions': KalturaCropDimensions,
            'KalturaConversionProfile': KalturaConversionProfile,
            'KalturaConversionProfileBaseFilter': KalturaConversionProfileBaseFilter,
            'KalturaConversionProfileFilter': KalturaConversionProfileFilter,
            'KalturaConversionProfileListResponse': KalturaConversionProfileListResponse,
            'KalturaDataEntry': KalturaDataEntry,
            'KalturaDataEntryBaseFilter': KalturaDataEntryBaseFilter,
            'KalturaDataEntryFilter': KalturaDataEntryFilter,
            'KalturaDataListResponse': KalturaDataListResponse,
            'KalturaConversionAttribute': KalturaConversionAttribute,
            'KalturaEmailIngestionProfile': KalturaEmailIngestionProfile,
            'KalturaPlayableEntry': KalturaPlayableEntry,
            'KalturaMediaEntry': KalturaMediaEntry,
            'KalturaAsset': KalturaAsset,
            'KalturaFlavorAsset': KalturaFlavorAsset,
            'KalturaAssetBaseFilter': KalturaAssetBaseFilter,
            'KalturaAssetFilter': KalturaAssetFilter,
            'KalturaFlavorAssetListResponse': KalturaFlavorAssetListResponse,
            'KalturaString': KalturaString,
            'KalturaAssetParams': KalturaAssetParams,
            'KalturaFlavorParams': KalturaFlavorParams,
            'KalturaFlavorAssetWithParams': KalturaFlavorAssetWithParams,
            'KalturaAssetParamsBaseFilter': KalturaAssetParamsBaseFilter,
            'KalturaAssetParamsFilter': KalturaAssetParamsFilter,
            'KalturaFlavorParamsBaseFilter': KalturaFlavorParamsBaseFilter,
            'KalturaFlavorParamsFilter': KalturaFlavorParamsFilter,
            'KalturaFlavorParamsListResponse': KalturaFlavorParamsListResponse,
            'KalturaLiveStreamBitrate': KalturaLiveStreamBitrate,
            'KalturaLiveStreamEntry': KalturaLiveStreamEntry,
            'KalturaLiveStreamAdminEntry': KalturaLiveStreamAdminEntry,
            'KalturaPlayableEntryBaseFilter': KalturaPlayableEntryBaseFilter,
            'KalturaPlayableEntryFilter': KalturaPlayableEntryFilter,
            'KalturaMediaEntryBaseFilter': KalturaMediaEntryBaseFilter,
            'KalturaMediaEntryFilter': KalturaMediaEntryFilter,
            'KalturaLiveStreamEntryBaseFilter': KalturaLiveStreamEntryBaseFilter,
            'KalturaLiveStreamEntryFilter': KalturaLiveStreamEntryFilter,
            'KalturaLiveStreamListResponse': KalturaLiveStreamListResponse,
            'KalturaSearch': KalturaSearch,
            'KalturaSearchResult': KalturaSearchResult,
            'KalturaMediaListResponse': KalturaMediaListResponse,
            'KalturaMixEntry': KalturaMixEntry,
            'KalturaMixEntryBaseFilter': KalturaMixEntryBaseFilter,
            'KalturaMixEntryFilter': KalturaMixEntryFilter,
            'KalturaMixListResponse': KalturaMixListResponse,
            'KalturaClientNotification': KalturaClientNotification,
            'KalturaKeyValue': KalturaKeyValue,
            'KalturaPartner': KalturaPartner,
            'KalturaPartnerUsage': KalturaPartnerUsage,
            'KalturaPermissionItem': KalturaPermissionItem,
            'KalturaPermissionItemBaseFilter': KalturaPermissionItemBaseFilter,
            'KalturaPermissionItemFilter': KalturaPermissionItemFilter,
            'KalturaPermissionItemListResponse': KalturaPermissionItemListResponse,
            'KalturaPermission': KalturaPermission,
            'KalturaPermissionBaseFilter': KalturaPermissionBaseFilter,
            'KalturaPermissionFilter': KalturaPermissionFilter,
            'KalturaPermissionListResponse': KalturaPermissionListResponse,
            'KalturaMediaEntryFilterForPlaylist': KalturaMediaEntryFilterForPlaylist,
            'KalturaPlaylist': KalturaPlaylist,
            'KalturaPlaylistBaseFilter': KalturaPlaylistBaseFilter,
            'KalturaPlaylistFilter': KalturaPlaylistFilter,
            'KalturaPlaylistListResponse': KalturaPlaylistListResponse,
            'KalturaReportInputFilter': KalturaReportInputFilter,
            'KalturaReportGraph': KalturaReportGraph,
            'KalturaReportTotal': KalturaReportTotal,
            'KalturaReportTable': KalturaReportTable,
            'KalturaSearchResultResponse': KalturaSearchResultResponse,
            'KalturaSearchAuthData': KalturaSearchAuthData,
            'KalturaStartWidgetSessionResponse': KalturaStartWidgetSessionResponse,
            'KalturaStatsEvent': KalturaStatsEvent,
            'KalturaStatsKmcEvent': KalturaStatsKmcEvent,
            'KalturaCEError': KalturaCEError,
            'KalturaBaseSyndicationFeed': KalturaBaseSyndicationFeed,
            'KalturaBaseSyndicationFeedBaseFilter': KalturaBaseSyndicationFeedBaseFilter,
            'KalturaBaseSyndicationFeedFilter': KalturaBaseSyndicationFeedFilter,
            'KalturaBaseSyndicationFeedListResponse': KalturaBaseSyndicationFeedListResponse,
            'KalturaSyndicationFeedEntryCount': KalturaSyndicationFeedEntryCount,
            'KalturaThumbAsset': KalturaThumbAsset,
            'KalturaThumbParams': KalturaThumbParams,
            'KalturaThumbAssetListResponse': KalturaThumbAssetListResponse,
            'KalturaThumbParamsBaseFilter': KalturaThumbParamsBaseFilter,
            'KalturaThumbParamsFilter': KalturaThumbParamsFilter,
            'KalturaThumbParamsListResponse': KalturaThumbParamsListResponse,
            'KalturaUiConf': KalturaUiConf,
            'KalturaUiConfBaseFilter': KalturaUiConfBaseFilter,
            'KalturaUiConfFilter': KalturaUiConfFilter,
            'KalturaUiConfListResponse': KalturaUiConfListResponse,
            'KalturaUiConfTypeInfo': KalturaUiConfTypeInfo,
            'KalturaUploadResponse': KalturaUploadResponse,
            'KalturaUploadToken': KalturaUploadToken,
            'KalturaUploadTokenBaseFilter': KalturaUploadTokenBaseFilter,
            'KalturaUploadTokenFilter': KalturaUploadTokenFilter,
            'KalturaUploadTokenListResponse': KalturaUploadTokenListResponse,
            'KalturaUserRole': KalturaUserRole,
            'KalturaUserRoleBaseFilter': KalturaUserRoleBaseFilter,
            'KalturaUserRoleFilter': KalturaUserRoleFilter,
            'KalturaUserRoleListResponse': KalturaUserRoleListResponse,
            'KalturaUserBaseFilter': KalturaUserBaseFilter,
            'KalturaUserFilter': KalturaUserFilter,
            'KalturaUserListResponse': KalturaUserListResponse,
            'KalturaWidget': KalturaWidget,
            'KalturaWidgetBaseFilter': KalturaWidgetBaseFilter,
            'KalturaWidgetFilter': KalturaWidgetFilter,
            'KalturaWidgetListResponse': KalturaWidgetListResponse,
            'KalturaPartnerBaseFilter': KalturaPartnerBaseFilter,
            'KalturaPartnerFilter': KalturaPartnerFilter,
            'KalturaPartnerListResponse': KalturaPartnerListResponse,
            'KalturaFlavorParamsOutputBaseFilter': KalturaFlavorParamsOutputBaseFilter,
            'KalturaFlavorParamsOutputFilter': KalturaFlavorParamsOutputFilter,
            'KalturaFlavorParamsOutput': KalturaFlavorParamsOutput,
            'KalturaThumbParamsOutputBaseFilter': KalturaThumbParamsOutputBaseFilter,
            'KalturaThumbParamsOutputFilter': KalturaThumbParamsOutputFilter,
            'KalturaThumbParamsOutput': KalturaThumbParamsOutput,
            'KalturaMediaInfoBaseFilter': KalturaMediaInfoBaseFilter,
            'KalturaMediaInfoFilter': KalturaMediaInfoFilter,
            'KalturaMediaInfo': KalturaMediaInfo,
            'KalturaCountryRestriction': KalturaCountryRestriction,
            'KalturaDirectoryRestriction': KalturaDirectoryRestriction,
            'KalturaIpAddressRestriction': KalturaIpAddressRestriction,
            'KalturaSessionRestriction': KalturaSessionRestriction,
            'KalturaPreviewRestriction': KalturaPreviewRestriction,
            'KalturaSiteRestriction': KalturaSiteRestriction,
            'KalturaSearchCondition': KalturaSearchCondition,
            'KalturaSearchComparableCondition': KalturaSearchComparableCondition,
            'KalturaSearchOperator': KalturaSearchOperator,
            'KalturaBaseJobBaseFilter': KalturaBaseJobBaseFilter,
            'KalturaBaseJobFilter': KalturaBaseJobFilter,
            'KalturaBatchJobBaseFilter': KalturaBatchJobBaseFilter,
            'KalturaControlPanelCommandBaseFilter': KalturaControlPanelCommandBaseFilter,
            'KalturaMailJobBaseFilter': KalturaMailJobBaseFilter,
            'KalturaNotificationBaseFilter': KalturaNotificationBaseFilter,
            'KalturaBatchJobFilter': KalturaBatchJobFilter,
            'KalturaControlPanelCommandFilter': KalturaControlPanelCommandFilter,
            'KalturaMailJobFilter': KalturaMailJobFilter,
            'KalturaNotificationFilter': KalturaNotificationFilter,
            'KalturaBatchJobFilterExt': KalturaBatchJobFilterExt,
            'KalturaAssetParamsOutputBaseFilter': KalturaAssetParamsOutputBaseFilter,
            'KalturaFlavorAssetBaseFilter': KalturaFlavorAssetBaseFilter,
            'KalturaMediaFlavorParamsBaseFilter': KalturaMediaFlavorParamsBaseFilter,
            'KalturaMediaFlavorParamsOutputBaseFilter': KalturaMediaFlavorParamsOutputBaseFilter,
            'KalturaThumbAssetBaseFilter': KalturaThumbAssetBaseFilter,
            'KalturaAssetParamsOutputFilter': KalturaAssetParamsOutputFilter,
            'KalturaFlavorAssetFilter': KalturaFlavorAssetFilter,
            'KalturaMediaFlavorParamsFilter': KalturaMediaFlavorParamsFilter,
            'KalturaMediaFlavorParamsOutputFilter': KalturaMediaFlavorParamsOutputFilter,
            'KalturaThumbAssetFilter': KalturaThumbAssetFilter,
            'KalturaLiveStreamAdminEntryBaseFilter': KalturaLiveStreamAdminEntryBaseFilter,
            'KalturaLiveStreamAdminEntryFilter': KalturaLiveStreamAdminEntryFilter,
            'KalturaAdminUserBaseFilter': KalturaAdminUserBaseFilter,
            'KalturaAdminUserFilter': KalturaAdminUserFilter,
            'KalturaGoogleVideoSyndicationFeedBaseFilter': KalturaGoogleVideoSyndicationFeedBaseFilter,
            'KalturaGoogleVideoSyndicationFeedFilter': KalturaGoogleVideoSyndicationFeedFilter,
            'KalturaITunesSyndicationFeedBaseFilter': KalturaITunesSyndicationFeedBaseFilter,
            'KalturaITunesSyndicationFeedFilter': KalturaITunesSyndicationFeedFilter,
            'KalturaTubeMogulSyndicationFeedBaseFilter': KalturaTubeMogulSyndicationFeedBaseFilter,
            'KalturaTubeMogulSyndicationFeedFilter': KalturaTubeMogulSyndicationFeedFilter,
            'KalturaYahooSyndicationFeedBaseFilter': KalturaYahooSyndicationFeedBaseFilter,
            'KalturaYahooSyndicationFeedFilter': KalturaYahooSyndicationFeedFilter,
            'KalturaApiActionPermissionItemBaseFilter': KalturaApiActionPermissionItemBaseFilter,
            'KalturaApiParameterPermissionItemBaseFilter': KalturaApiParameterPermissionItemBaseFilter,
            'KalturaApiActionPermissionItemFilter': KalturaApiActionPermissionItemFilter,
            'KalturaApiParameterPermissionItemFilter': KalturaApiParameterPermissionItemFilter,
            'KalturaGenericSyndicationFeedBaseFilter': KalturaGenericSyndicationFeedBaseFilter,
            'KalturaGenericSyndicationFeedFilter': KalturaGenericSyndicationFeedFilter,
            'KalturaGenericXsltSyndicationFeedBaseFilter': KalturaGenericXsltSyndicationFeedBaseFilter,
            'KalturaGenericXsltSyndicationFeedFilter': KalturaGenericXsltSyndicationFeedFilter,
            'KalturaAssetParamsOutput': KalturaAssetParamsOutput,
            'KalturaMediaFlavorParamsOutput': KalturaMediaFlavorParamsOutput,
            'KalturaMediaFlavorParams': KalturaMediaFlavorParams,
            'KalturaApiActionPermissionItem': KalturaApiActionPermissionItem,
            'KalturaApiParameterPermissionItem': KalturaApiParameterPermissionItem,
            'KalturaGenericSyndicationFeed': KalturaGenericSyndicationFeed,
            'KalturaGenericXsltSyndicationFeed': KalturaGenericXsltSyndicationFeed,
            'KalturaGoogleVideoSyndicationFeed': KalturaGoogleVideoSyndicationFeed,
            'KalturaITunesSyndicationFeed': KalturaITunesSyndicationFeed,
            'KalturaTubeMogulSyndicationFeed': KalturaTubeMogulSyndicationFeed,
            'KalturaYahooSyndicationFeed': KalturaYahooSyndicationFeed,
        }

    # @return string
    def getName(self):
        return ''

