config = {

    # AWS credentials for the IAM user (alternatively can be set up as environment variables)
    'aws_access_key': '*****************',
    'aws_secret_key': '*****************',

    # EC2 info about your server's region
    'ec2_region_name': 'us-east-1',
    'ec2_region_endpoint': 'ec2.us-east-1.amazonaws.com',

    # ARN of the SNS topic (optional)
    'arn': 'arn:aws:sns:us-east-1:*****************,:Tag_Checker'
}
