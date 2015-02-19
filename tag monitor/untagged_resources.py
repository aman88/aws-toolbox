#!/usr/bin/python

from boto.ec2.connection import EC2Connection
from boto.ec2.regioninfo import RegionInfo
import boto.sns
from config import config

# Message to return result via SNS
message = "The following instances do not have a \"Project\" tag.\n\n"

# Get settings from config.py
aws_access_key = config['aws_access_key']
aws_secret_key = config['aws_secret_key']
ec2_region_name = config['ec2_region_name']
ec2_region_endpoint = config['ec2_region_endpoint']
sns_arn = config.get('arn')

region = RegionInfo(name=ec2_region_name, endpoint=ec2_region_endpoint)

# Connect to AWS
if aws_access_key:
    conn = EC2Connection(aws_access_key, aws_secret_key, region=region)
else:
    conn = EC2Connection(region=region)

# Connect to SNS
if sns_arn:
    print 'Connecting to SNS'
    # non proxy:
    # using roles
    if aws_access_key:
        sns = boto.sns.connect_to_region(ec2_region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    else:
        sns = boto.sns.connect_to_region(ec2_region_name)

reservations = conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    if 'Project' not in (i.__dict__)['tags']:
        if 'Name' in (i.__dict__)['tags']:
            message += '\n%s (%s)' % (i,(i.__dict__)['tags']['Name'])
        else:
            message += '\n%s' % i
if sns_arn:
	sns.publish(sns_arn, message, 'AWS Untagged Instances')