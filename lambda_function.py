import boto3
import urllib

s3 = boto3.resource('s3')
bucket = s3.Bucket('storagepennapps19')

s3_client = boto3.client('s3')

def put(key, obj):
    bucket.put_object(Key=key, Body=obj)

def download_source(source):
    response = urllib.request.urlopen(source)
    data = response.read()
    return data

# op - 'puturl'
#   source - url to get object
#   key - to store object in bucket
# op - 'get'
#   key - stored object in bucket
def lambda_handler(event, context):
    op = event['op']
    payload = event['payload']
    if op == 'puturl': # put object from url
        source = payload['source']
        key = payload['key']
        data = download_source(source)
        put(key, data)
        return 'ok'
    if op == 'get': # get object from bucket
        key = payload['key']
        response = s3_client.get_object(Bucket='storagepennapps19', Key=key)
        data = response['Body'].read().decode()
        return data
