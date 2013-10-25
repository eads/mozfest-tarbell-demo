# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "mozfest"

# Descriptive title of project
TITLE = "MozFest 2013 quotes"

# Google spreadsheet key
#SPREADSHEET_KEY = "None"

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    # "mytarget": "s3://mys3url.bucket.url/some/path"
    "staging": "s3://projects.beta.coolorg.net/mozfest/",
    "production": "s3://projects.coolorg.net/mozfest/",
}

# Repository this project is based on (used for updates)
TEMPLATE_REPO_URL = "https://github.com/newsapps/tarbell-template"

# Default template variables
DEFAULT_CONTEXT = {
    'data': [   {   'column1': u'row1, column1',
                    'column2': u'row1, column2'},
                {   'column1': u'row2, column1',
                    'column2': u'row2, column2'}],
    'google_analytics_id': None,
    'headline': u'Test headline',
    'keyed_data': {   'key1': {   'column1': u'key1, column1',
                                  'column2': u'key1, column2',
                                  'key': u'key1'},
                      'key2': {   'column1': u'key2, column1',
                                  'column2': u'key2, column2',
                                  'key': u'key2'}},
    'name': 'mozfest',
    'opengraph_description': None,
    'opengraph_image': None,
    'title': 'MozFest 2013 quotes',
    'twitter_description': None
}