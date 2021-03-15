### Sysytem Manager:
- Collection of capabilities for configuring and managing Ec2,on-premise servers,other aws resources.
- Shortens the time to detect and resolve operational problems in infrastructure
- Gives complete view of infra performance and configuration,simplifies resource and application management, and make it easy to operate and 
manage infra at scale.


### How it Works:
- Collects information from instances using SSM agent (present default in mazon-based instances and dont forget to attch IAM role to instances),
and using that SSM we can perform actions like Automations, RUn command,Patch manager,session manager. And also using SSM agent we can see the Insights
like Inventory,compliance,Built-in insights,cloudwatch dashboards


### How to make an ec2-instance System-mamnager-managed instance:
- create an ec2-instance .If you create instance using amazon-default-ami's, the no need to install ssm-agent.it is default present.
- create a role and attach to instance during creation.if you attach the role after creation of instance or if your instance is not showing in ssm-console , you may bneed to 
reboot the instance.
- Attach the following policy("AmazonEC2RoleforSSM") to the iam-role created for ec2 .
- If you want to add user-data for apache-server for testing purpoe, you can refer the awslabs-github-link as given below in the sources section.
### sources:
    https://www.udemy.com/course/ultimate-aws-certified-sysops-administrator-associate/learn/lecture/12710365#overview
    https://github.com/awslabs/ec2-spot-workshops/blob/master/workshops/ec2-auto-scaling-with-multiple-instance-types-and-purchase-options/user-data.txt



## Insights:
### Built-in-Insights:
shows detailed information about resources in your resource groups, such as cloudtrai logs, results of evaluations aganist AWS Config rules, and Trusted 
Advisor reports,insights show information about single,selected group group at a time

### Cloudwatch Dashboards:
customize home pages in cloudwatch console that you can use to monitor your resources in a single view, even those resources that are spread across
different regions. You can use cloudwatch dashboards to create customized views of the metrics


### Inventory Management:
Automates the process of collecting software inventory from managed instances.You can use Inventory managet to gather meteadat about apllications,
files,coomponents,patches,and more on your managed instances

### Configuration compliance
scans your fleet of managed instances for patch compliance and configuration inconsistencies.You can collect and aggregate data from Multiple accounts
and regions.By default, it displays compliance data about patch manager patching and state manager associations.You create custom compliance types.


## Actions:
### Automation:
Automates common maintenance and deployment tasks.



Questions?
- Does Private/public RDS is supported by System Manager?
- can we create cloudwatch dashboards and report  erros for lambdas in different regions(once refer above)
- 
