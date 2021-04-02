import os
from django.conf import settings
from jnius import autoclass

cp = os.path.abspath(os.path.join(
    settings.BASE_DIR, '/Back-End/jar/', 'tika-app-1.20.jar'))
os.environ['CLASSPATH'] = cp

Tika = autoclass('org.apache.tika.Tika')
Metadata = autoclass('org.apache.tika.metadata.Metadata')
FileInputStream = autoclass('java.io.FileInputStream')


def parse_to_string(filename):
    tika=Tika()
    meta=Metadata()
    text=tika.parseToString(FileInputStream(filename),meta)
    return text