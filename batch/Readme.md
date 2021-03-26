

sudo yum install docker
 sudo systemctl start docker
[root@ip-172-31-16-102 docker]# docker build -t nokkuprudhvi/nokku-docker-hub-repo-aws-batch .

[root@ip-172-31-16-102 docker]# docker login --username nokkuprudhvi

[root@ip-172-31-16-102 docker]# docker push nokkuprudhvi/nokku-docker-hub-repo-aws-batch


Dockerfile:
FROM python
RUN pip3 install boto3
RUN mkdir /src
COPY . /src
CMD ["python","/src/load_data.py"]

load_data.py:
import boto3
session = boto3.session.Session(region_name= 'us-east-1')
dynamodb = session.resource('dynamodb')


table = dynamodb.Table("TestTable")

filler = "x" * 1000

i = 0
while (i < 10):
    j = 0
    while (j < 10):
        print (i, j)

        table.put_item(
            Item={
                'pk':i,
                'sk':j,
                'filler':{"S":filler}
            }
        )
        j += 1
    i += 1



