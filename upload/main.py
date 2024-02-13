import functions_framework

from urllib.request import urlopen
from google.cloud import storage

client = storage.Client()

@functions_framework.http
def upload(request):

    filedata = urlopen('https://data.police.uk/data/archive/latest.zip')
    datatoupload = filedata.read()

    bucket = client.get_bucket('demovanessa')
    blob = bucket.blob("latest.zip")
    blob.upload_from_string(datatoupload)

    return blob.public_url
