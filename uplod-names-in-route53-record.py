import json
import boto3

s3 = boto3.client('s3')
route53 = boto3.client('route53')

def upload_to_s3(folder, filename, bucket_name, key):
    """Upload a file to a folder in an Amazon S3 bucket."""
    key = folder + '/' + key
    s3.put_object(filename, bucket_name, key)
    
def get_route53_hosted_zones(next_zone=None):
    """Recursively returns a list of hosted zones in Amazon Route 53."""
    if(next_zone):
        response = route53.list_hosted_zones_by_name(
            DNSName=next_zone[0],
            HostedZoneId=next_zone[1]
        )
    else:
        response = route53.list_hosted_zones_by_name()
    hosted_zones = response['HostedZones']
    # if response is truncated, call function again with next zone name/id
    if(response['IsTruncated']):
        hosted_zones += get_route53_hosted_zones(
            (response['NextDNSName'],
            response['NextHostedZoneId'])
        )
    return hosted_zones

def get_route53_zone_records(zone_id, next_record=None):
    """Recursively returns a list of records of a hosted zone in Route 53."""
    if(next_record):
        response = route53.list_resource_record_sets(
            HostedZoneId=zone_id,
            StartRecordName=next_record[0],
            StartRecordType=next_record[1]
        )
    else:
        response = route53.list_resource_record_sets(HostedZoneId=zone_id)
    zone_records = response['ResourceRecordSets']
    # if response is truncated, call function again with next record name/id
    if(response['IsTruncated']):
        zone_records += get_route53_zone_records(
            zone_id,
            (response['NextRecordName'],
            response['NextRecordType'])
        )
    return zone_records
    
def lambda_handler(event, context):
	# S3 Bucket
	bucket ='marvel-s3-route53-dns-backup-march2023-test'

	recordToUpload = {}
    # Set Test File
	fileName = 'route53-sample-data' + '.json'
	
	# Route53
	"""Recursively returns a list of records
	of a hosted zone in Route 53.
	Example:
		Hoseted Zone Name: marvel-universe-test-zone
	    HostedZoneId: Z0123AABBCCXXYYZZ"""
	
	zone_records = get_route53_zone_records(zone_id='Z0123AABBCCXXYYZZ')
    # 	print(zone_records)
	for item in zone_records:
	    recordToUpload['Name'] = item['Name']
	
    # Deploy File to S3 Bucket
	uploadByteStream = bytes(json.dumps(recordToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Success! New file add to' + bucket)
