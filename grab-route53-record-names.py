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

    # Set Test File
	# fileName = 'route53-record-name-data' + '.json'
	
	# Display Raw Hosted Zone 
# 	hosted_zones = get_route53_hosted_zones()
# 	print(hosted_zones)
	
	# Route53
	"""Recursively returns a list of records
	of a hosted zone in Route 53.
	Example:
		Hoseted Zone Name: marvel-universe-test-zone
	    HostedZoneId: Z0123AABBCCXXYYZZ"""
	
	# zone_records = get_route53_zone_records(zone_id='Z0123AABBCCXXYYZZ')
zone_records = [{'Name': 'marvel-spf-testzone.', 'Type': 'NS', 'TTL': 172800, 'ResourceRecords': [{'Value': 'ns-12345.awsdns-00.co.uk.'}, {'Value': 'ns-0.awsdns-1234512345.com.'}, {'Value': 'ns-12345.awsdns-00.org.'}, {'Value': 'ns-12345.awsdns-00.net.'}]}, {'Name': 'marvel-spf-testzone.', 'Type': 'SOA', 'TTL': 900, 'ResourceRecords': [{'Value': 'ns-12345.awsdns-00.co.uk. awsdns-example.amazon.com. 1 7200 123 12345 67980'}]}, {'Name': '_spf.marvel-spf-testzone.', 'Type': 'TXT', 'TTL': 60, 'ResourceRecords': [{'Value': '"v=spf1 include:spf_1.marvel-spf-testzone ~all"'}]}, {'Name': 'spf_1.marvel-spf-testzone.', 'Type': 'TXT', 'TTL': 60, 'ResourceRecords': [{'Value': 'serverless example'}]}]

# print(zone_records)
# for item in zone_records:
#     print(item['Name'])
# This WOOORKKKSS
'''This WORKS!!!!'''
myList = []
    for item in zone_records:
        myList.append(item['Name'])
    print(myList)

    
for record in zone_records:
            csv_row = ['']
            # csv_row[0] = record['Name']
            # csv_row[1] = record['Type']
            # csv_row[2] = record['TTL']
            csv_row[0] = {key: value for (key, value) in record.items()}
            results = str(csv_row)+ '\n'
            # print(str(csv_row)+ '\n')
print(results)
# print({key: value for (key, value) in record.items()})
	# response = route53.list_hosted_zones_by_name()
 #   hosted_zones = response['HostedZones']
	
    # Deploy File to S3 Bucket
	# uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	# s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	# print('Success! New file add to' + bucket)
