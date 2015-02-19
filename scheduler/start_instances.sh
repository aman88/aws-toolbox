/usr/local/ec2/ec2-api-tools-1.7.2.2/bin/ec2-start-instances <instance-id-1> <instance-id-2> <instance-id-3>
sleep 90
/usr/local/ec2/ec2-api-tools-1.7.2.2/bin/ec2-associate-address -i <instance-id-1> -a eipalloc-********
/usr/local/ec2/ec2-api-tools-1.7.2.2/bin/ec2-associate-address -i <instance-id-2> -a eipalloc-********
/usr/local/ec2/ec2-api-tools-1.7.2.2/bin/ec2-associate-address -i <instance-id-3> -a eipalloc-********
