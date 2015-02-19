Requires EC2 API Tools


crontab
=======
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO="<email>"
30 20 * * * /bin/bash -c /path/to/stop_instances.sh >> /home/ubuntu/cron.log 2>&1
30 8 * * * /bin/bash -c /path/to/start_instances.sh >> /home/ubuntu/cron.log 2>&1


.bashrc (in the account running the cron)
=========================================
export JAVA_HOME="/usr/lib/jvm/java-7-openjdk-amd64/jre"
export EC2_HOME=/usr/local/ec2/ec2-api-tools-1.7.2.2
export AWS_ACCESS_KEY=A**************A
export AWS_SECRET_KEY=A*********************A
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/ec2/ec2-api-tools-1.7.2.2/bin
