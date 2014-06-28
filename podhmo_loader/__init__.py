#:coding=utf-8:

from django.conf import settings
from django.conf.urls import url


def load_from_text_file():
    pattern_list = []
    with open(settings.URL_TEXT_FILE) as url_settings:
        for line in url_settings.readlines():
            name, view, regex = line.split()
            pattern_list.append(url(
                regex=regex.lstrip('/'),
                view=view,
                name=name,
            ))
    return pattern_list
