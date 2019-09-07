import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('ducks.png', 'rb')
print(s3.Bucket('storagepennapps19').put_object(Key='ducks', Body=data))
