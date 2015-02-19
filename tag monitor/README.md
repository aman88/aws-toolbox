Usage
==========
1. Install and configure Python and Boto (See: https://github.com/boto/boto)
2. Create a SNS topic in AWS and copy the ARN into the config file
3. Subscribe with a email address to the SNS topic
4. Create a user in IAM and put the key and secret in the config file
5. Copy config.sample to config.py
6. Change the Region and Endpoint for AWS in the config.py file
7. Install the script in the cron