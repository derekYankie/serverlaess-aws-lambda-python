import json
import boto3

s3 = boto3.client('s3')
route53 = boto3.client('route53')

def upload_to_s3(folder, filename, bucket_name, key):
    """Upload a file to a folder in an Amazon S3 bucket."""
    key = folder + '/' + key
    s3.put_object(filename, bucket_name, key)
    
    
def lambda_handler(event, context):
	# S3 Bucket
	bucket ='marvel-s3-route53-dns-backup-march2023-test'

	transactionToUpload = {}
	transactionToUpload['vehicleId'] = '1235EFG'
	transactionToUpload['class'] = 'Sports-Car'
	transactionToUpload['type'] = 'Mazda RX7'
	transactionToUpload['hp'] = 110
	transactionToUpload['customerId'] = 'CID-2048'
    # Set Test File
	fileName = 'vehicle-sample-data' + '.json'
	
    # Deploy File to S3 Bucket
	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Success! New file add to' + bucket)
