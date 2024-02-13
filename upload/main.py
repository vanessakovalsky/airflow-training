import functions_framework

from urllib.request import urlopen
from google.cloud import storage

from datetime import datetime
from dateutil.relativedelta import relativedelta

client = storage.Client()

@functions_framework.http
def upload(request):

    last_month = datetime.now() - relativedelta(months=2)
    get_date = last_month.strftime("%Y")+'-'+last_month.strftime("%m")

    url_to_open = 'https://data.police.uk/data/archive/'+ get_date +'.zip'
    print(url_to_open)
    filedata = urlopen(url_to_open)
    datatoupload = filedata.read()

    bucket = client.get_bucket('demovanessa')
    blob = bucket.blob("latest.zip")
    blob.upload_from_string(datatoupload)

    return blob.public_url
