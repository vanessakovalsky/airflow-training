from urllib.request import urlopen
from google.cloud import storage

client = storage.Client()


def upload():

    filedata = urlopen('https://data.police.uk/data/archive/latest.zip')
    datatoupload = filedata.read()

    bucket = client.get_bucket('demovanessa')
    blob = Blob("latest.zip", bucket)
    blob.upload_from_string(datatoupload)
