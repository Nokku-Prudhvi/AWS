#### As a prerequisite you need to have a jenkins running.you can refer to below files for installation:
AWS->SSM->Readme.md
AWS->SSM->run-command.md  // For installation

- There are two pugins using which we can spin spot instances and build our jobs. one is "Amazon EC2" and other is "EC2 Fleet"(new-one)(https://plugins.jenkins.io/ec2-fleet/). 
- we will be using "EC2 Fleet" plugin to spin spot instances for building jobs.you can use "Amazon Ec2" plugin also :https://www.youtube.com/watch?v=dAa3u39RYpM
- Go to Manage-pulgins and click on "download and install after restart" and restart accordingly
- you need to create a spot-fleet-request in your aws-account.
- While create a spot request , make sure you allow ssh access from jenkins to spot-instances.(you can allow jenkins-sg for 22-port in spot-sg)
- While creatiing a spot request  we need to add following user-data to allow the jenkins to install jenkins-agen in spot intance.

      #!/bin/bash -xe
      yum -y --security update
      yum -y update aws-cli
      yum -y groupinstall "Development Tools"
      yum -y remove java-1.7.0
      yum -y install java-1.8*

      
- you can configure AWS Credentials or leave set to none to use AWS EC2 Instance Role, but make sure that role/user have iam-permission-polies as follows:AmazonEC2SpotFleetTaggingRole,AmazonEC2ReadOnlyAccess.Optional permissions : ModifySpotFleetRequest,TerminateInstances, UpdateAutoScalingGroup , refer https://plugins.jenkins.io/ec2-fleet/
- you need to add new cloud by going to "Manage Jenkins" and "Configure-system"/"configure clouds".
- In the new-cloud add the ssh-keypair details and add a label to it(default it is ec2-fleet). This label is useful in running jenkins-jobs in spot-instances
- Check Maintain target capacity ((Default) If you configure the request type as maintain, EC2 Fleet places an asynchronous request for your desired capacity, and maintains capacity by automatically replenishing any interrupted Spot Instances.)
- After creating cloud, create a new-item of free-style-job.Configure it to "Restrict where this project can be run" in "General" section to the label ("ec2-fleet")
of the cloud.
- You can write shell commands like "hostname" and verify and run the shell-commands in the spot-instances.
- you can make use of Autoscaling group instead of spot-fleet request.The min capacity and max capaciy provided in the jenkins-cloud, is only for maintaing jenkins-nodes, they 
cant scale-up/down the number of instances. so to scale-up and down the spot instances created for CI/CD and also to use mixture of on-demand-instances for CI/CD you need to make use of Auto-scaling group.pls refer screenshot for creating jenkins-cloud and for creating spot-Autoscaling group refer to AWS->SPOT->ASG 



source: https://www.youtube.com/watch?v=8gGItacZjps&t=1s&ab_channel=AmazonWebServices
