
### run command

We can use run command to execute scripts directly without logging in to the server.
### Note explore one document for creating ssl on ec2-server ssm

Example:
As an example we will see how to install jenkins using "yum" via shell script.
As you know here are many method to install jenkins via "yum" or "docker" etc
sources:
https://cloudaffaire.com/how-to-install-jenkins-in-aws-ec2-instance/
https://medium.com/@itsmattburgess/installing-jenkins-on-amazon-linux-16aaa02c369c

- you need to select Command document "AWS-RunShellScript"
- since there is limit in the characters output in the console, there is option to send output to s3 or cloudwatch
- If you opted from any of aws service, make sure your instance-role has permission-policy to send to either cloudwatch or s3.


### Shell-script:
#!/bin/bash -xe   #(optional)
sudo yum -y update
sudo yum -y install java-1.8.0 
sudo yum -y remove java-1.7.0-openjdk
# We need to add the Jenkins repository so that yum knows where to install Jenkins from
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins.io/redhat/jenkins.repo
# we’re adding the Jenkins GPG key to our trusted keys so that we’re able to install Jenkins, verifying that the files are being sourced from a trusted location.
sudo rpm --import http://pkg.jenkins.io/redhat/jenkins.io.key
sudo yum -y install jenkins 
sudo systemctl start jenkins
sudo systemctl status jenkins
sudo systemctl enable jenkins
#we can use chkconfig to add Jenkins to our startup services.
sudo chkconfig --add jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
