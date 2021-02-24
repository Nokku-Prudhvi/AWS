Changing Public accessibilty to private accessibility:
- it will modify Rds for 1-2 minutes but the change wont cause any downtime

Downgrading RDS instance:
- Select the cluster you want to downgrade.
- Without changing writer, modify the reader instance first to other instance-type.
- After reader downgraded, go to actions and click on failover.
- After sometime reader becomes writer.
- If you want to do the same for both instances you can repeat as above, otherwise delete newly became reader to make cluster single-az
