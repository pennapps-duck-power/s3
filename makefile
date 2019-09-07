all:
	zip -r s3.zip lib/python3.6/site-packages
	zip -g s3.zip lambda_function.py
