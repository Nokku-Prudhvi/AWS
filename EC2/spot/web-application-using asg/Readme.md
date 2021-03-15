### For installation of jenkins and building golden-image , you can refer AWS->EC2->Spot->CICD

## once check soure : https://github.com/awslabs/ec2-spot-labs/tree/master/workshops/ec2-spot-fleet-web-app


- After building golden ami, you can make use of autoscaling to launch web-application . Major advantage is you can fix the demand-instances and can use spot instances on top of them.
- Pls note that ther is no cost for using AWS autoscaling group service.
- use launch template instead of launch configuration because launch template can be modified into versions.
- Don't specify spot option in launch template so that you can get option of spot instances while creating autoscaling group.
- you can make use of user-data if you want to test this scenario

      #cloud-config
      repo_update: true
      repo_upgrade: all

      packages:
        - httpd
        - curl

      runcmd:
        - [ sh, -c, "amazon-linux-extras install -y epel" ]
        - [ sh, -c, "yum -y install stress-ng" ]
        - [ sh, -c, "echo hello world. My instance-id is $(curl -s http://169.254.169.254/latest/meta-data/instance-id). My instance-type is $(curl -s http://169.254.169.254/latest/meta-data/instance-type). > /var/www/html/index.html" ]
        - [ sh, -c, "systemctl enable httpd" ]
        - [ sh, -c, "systemctl start httpd" ]

- Its better that you can attach a load balancer to asg , so that you can get a chance to share the load across multiple instances and also has leverage to keep instances in private subnets.
- In load balancer make sure your cross-zone load balancing and draining is enabled.
- you can add scaling-policies based on cpu-utilization to keep the instances scale-up and down when neccessary.
- you can verify the spot-instance by instance parameter "Lifecycle". Its value is "spot" for spot instances and "normal" for other type of instances.

### source:
https://www.youtube.com/watch?v=9psCsCcbfFM&t=3s&ab_channel=AWSOnlineTechTalks
