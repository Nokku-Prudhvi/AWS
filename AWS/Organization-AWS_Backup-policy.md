Using this new feature of AWS Backup service, we can manage all backup-plans and rules centrally from master account.
Child accounts wont have permissions to modify these backup-plans.
Backup plan and rule(one rule for one backup plan) need to be created in master account.
In all child accounts , backup-vault need to be created with same name as provided in the rule.This vault stores all the backups.
copying of backup with other regions is possible.
This aws-backup supports - ec2,ebs,rds-cluster,instance,dynamo,redis.
The backup plans/rules have no cost, however backups stored have cost.
