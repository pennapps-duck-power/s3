Handle object upload/download to/from s3 bucket, as a cloud lambda function.

To build, run `make`, then upload the generated `s3.zip` to aws lambda function named "store".

There are two tests on function "store". Test "PUTURL" will put some ducks in the bucket. Successful run will create new file "ducks_puturl.png" in the bucket. Test "GET" will get and return "test.json" file in the bucket as a string.
