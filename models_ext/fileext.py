# -*- coding: utf-8 -*-

import os

from TimeConvert import TimeConvert as tc


def upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/file/<ym>/<stamp>.<ext>
    return 'file/{ym}/{stamp}{ext}'.format(
        ym=tc.local_string(format='%Y%m'),
        stamp=tc.local_timestamp(ms=True),
        ext=os.path.splitext(filename)[1].lower(),
    )
