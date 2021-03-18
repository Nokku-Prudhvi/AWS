## How to use spot instance
### Spot-fleet-request
- For showing demo in-order, we will see the spot-fleet-request over load balancer.
- we will install jenkins using user-data-script.
#### Shell-script:
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
    
 
### autoscaling-group using spot-fleet
