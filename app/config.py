# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')

    # App Config - the minimal footprint
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')

    # STRIPE_SECRET_KEY      = os.getenv('STRIPE_SECRET_KEY'     , None )
    STRIPE_SECRET_KEY = "sk_test_51IHLB1FJDtbGk6LsIPcWHbEqgAI2En7QiXXXLBTjT7jrZIoBEh0biUOnH1gx2ah5zDpjZROrgIqvgddVG3sip6kF002QU3zk9A"
    # STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None )
    STRIPE_PUBLISHABLE_KEY = "pk_test_51IHLB1FJDtbGk6LsbIXVJZusF1FOBy4X0MllyO43eMGF6ctpOOb4omDX0xAsGBzjbmfKpV62G26ROQUpt2LeytrZ00wrZbK1uu"
    SERVER_ADDRESS         = os.getenv('SERVER_ADDRESS', 'http://localhost:5000/')

    STRIPE_IS_ACTIVE = False
    if STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY:
        STRIPE_IS_ACTIVE = True
