FROM rabbitmq:3-management


RUN rabbitmq-plugins enable --offline rabbitmq_management
#RUN rabbitmqctl set_disk_free_limit 300MB

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y wget
RUN wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.7.8/bin/rabbitmqadmin
RUN chmod 777 rabbitmqadmin
RUN cp rabbitmqadmin /usr/local/bin/



EXPOSE 15672
EXPOSE 5672


#CMD sleep(5000)