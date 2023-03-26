import datetime


# NOTE: MODE_CONFIG only applies to ranking crawler
MODE_CONFIG = {
    # start date
    "START_DATE": datetime.date(2024, 3, 3),
    # date range: [start, start + range - 1]
    "RANGE": 2,

    # which ranking list
    "RANKING_MODES": [
        "daily", "weekly", "monthly",
        "male", "female", "daily_ai",
        "daily_r18", "weekly_r18",
        "male_r18", "female_r18", "daily_r18_ai"
    ],
    "MODE": "daily",  # choose from the above

    # illustration, manga, or both
    "CONTENT_MODES": [
        "all",  # download both illustrations & mangas
        "illust", "manga"
    ],
    "CONTENT_MODE": "all",  # choose from the above

    # download top x in each ranking
    #   suggested x be a multiple of 50
    "N_ARTWORK": 50
}

OUTPUT_CONFIG = {
    # verbose / simplified output
    "VERBOSE": False,
    "PRINT_ERROR": False
}

NETWORK_CONFIG = {
    # proxy setting
    #   you should customize your proxy setting accordingly
    #   default is for clash
    "PROXY": {"https": "127.0.0.1:33210"},

    # common request header
    "HEADER": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    }
}

USER_CONFIG = {
    # user id
    #   access your pixiv user profile to find this
    #   e.g. https://www.pixiv.net/users/49934750
    "USER_ID": "49934750",

    "COOKIE": "first_visit_datetime_pc=2023-12-09%2021%3A31%3A13; p_ab_id=0; p_ab_id_2=6; p_ab_d_id=244589072; yuid_b=NlCVUYk; c_type=19; privacy_policy_notification=0; a_type=0; b_type=0; _im_uid.3929=i.faCjMkcZRMy-qpbmCiOz_Q; cf_clearance=FwwWUlQfsjH0sIBtCEpHI_lRlLvW59p3zYeo_NG91Jo-1711181204-1.0.1.1-LPM7V63ZbWaJ3F8aDCkNlmqSNOoqQWrggADlb2mhih2sKniiVIbo7b1YksS.x.KCnKhwmcLlKVO7Fw7bb.i1GA; _im_vid=01HSN5J6EFEXFJ1VK6CGXP5FHM; _gid=GA1.2.107121573.1711181220; cc1=2024-03-24%2013%3A00%3A20; PHPSESSID=49934750_2wzMUHKnZMeVnpK6sDpjZY9EM7whRnfi; device_token=6e4a37243c98bad1be237f5dc03264e8; privacy_policy_agreement=6; _ga_MZ1NL4PHH0=GS1.1.1711252826.4.0.1711252828.0.0.0; login_ever=yes; _gcl_au=1.1.578930438.1711252829; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __cf_bm=pbxOWLqZokaxjnRhp7vdrzYmGMfRuOPqnXBkBumso6w-1711258808-1.0.1.1-Fzcmr54jiXWhWvcKCcdH3Y3MhEpff1ukUY_fledPLz4hIlieuSHK0NbbWoAXffWdodlJ2UfDVwRTRpEJgckhvw_1B30iFdggArIXiAYEiXU; _gat_UA-1830249-3=1; _ga=GA1.1.565933053.1702125080; _ga_75BBYNYN9J=GS1.1.1711258813.7.0.1711258813.0.0.0"
}


DOWNLOAD_CONFIG = {
    # image save path
    #   NOTE: DO NOT miss "/"
    "STORE_PATH": "images/",

    # abort request / download
    #   after 10 unsuccessful attempts
    "N_TIMES": 10,

    # need tag ?
    "WITH_TAG": True,

    # waiting time (s) after failure
    "FAIL_DELAY": 1,

    # max parallel thread number
    "N_THREAD": 8,
    # waiting time (s) after thread start
    "THREAD_DELAY": 1,
}
