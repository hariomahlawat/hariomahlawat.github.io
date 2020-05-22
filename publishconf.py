#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://hariomahlawat.github.io'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
HTTPS = True
DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
def deploy():
    """Push to GitHub pages"""
    env.msg = "Build site"
    clean()
    preview()
    local("ghp-import -m '{msg}' -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))