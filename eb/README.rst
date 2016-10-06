Notes:

* I had to add AmazonEC2ContainerRegistryReadOnly policy to
aws-elasticbeanstalk-ec2-role to have this working. Otherwise I was missing
ecr:GetAuthorizationToken permission.