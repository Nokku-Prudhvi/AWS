https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html

https://www.amazonaws.cn/en/ec2/faqs/

old-article:
https://aws.amazon.com/blogs/aws/new-hibernate-your-ec2-instances/


Same as EC2-stop instances in cost-wise (EBS-vulem and EIP cost)

### Advantage over EC2-stopped:
- Ec2 Hibernation stores RAM in root-EBS-volume and stops the instance.So if instance starts again no need to boot-up operating system.You can verify this scenario by
'uptime' command which gives info on os-boot-time
- The most interesting use cases for hibernation revolve around long-running processes and 
services that take a lot of time to initialize before they are ready to accept traffic where this would not be a concern

### Limitations:
- No, you cannot enable hibernation on an existing instance (running or stopped). This needs to be enabled during instance launch.
- Hibernation is currently supported across C3, C4, C5, I3, M3, M4, M5, M5a, M5ad, R3, R4, R5, R5a, R5ad, T2, T3, and T3a instances running Amazon Linux, Amazon Linux 2, 
Ubuntu, and Windows
- we cant keep an instance hibernated for more than 60 days
