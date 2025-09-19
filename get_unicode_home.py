# coding=utf-8
# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from posix_or_nt import posix_or_nt
from read_unicode_environment_variables_dictionary import read_unicode_environment_variables_dictionary
from typing import Text


def get_unicode_home():
    # type: () -> Text
    unicode_environment_variables_dictionary = read_unicode_environment_variables_dictionary()
    if posix_or_nt() == 'nt':
        userprofile_or_none = unicode_environment_variables_dictionary.get(u'USERPROFILE', None)
        if userprofile_or_none is not None:
            return userprofile_or_none
        else:
            homedrive_or_none = unicode_environment_variables_dictionary.get(u'HOMEDRIVE', None)
            homepath_or_none = unicode_environment_variables_dictionary.get(u'HOMEPATH', None)
            if homedrive_or_none is not None and homepath_or_none is not None:
                return homedrive_or_none + homepath_or_none
            else:
                raise EnvironmentError('Cannot get NT home directory; tried reading the environment variables USERPROFILE and HOMEDRIVE+HOMEPATH, but they were not set.')
    else:
        home_or_none = unicode_environment_variables_dictionary.get(u'HOME', None)
        if home_or_none is not None:
            return home_or_none
        else:
            raise EnvironmentError('Cannot get POSIX home directory; tried reading the environment variable HOME, but it was not set.')
