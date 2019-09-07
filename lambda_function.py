import boto3
import urllib

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    source = event['source']
    key = event['key']
    response = urllib.request.urlopen(source)
    data = response.read()
    print(data)
    s3.Bucket('storagepennapps19').put_object(Key=key, Body=data)
