##
# @author : Remi Dupuy : IT Student
# Create a basic queue and send a message

import pika
import os


amqp_url='amqp://tijjoigp:0uzZbSC8N5fxxkHsgXKaB5CcE4eKjKWf@lark.rmq.cloudamqp.com/tijjoigp'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='presentation')


username = 'remiDupuy'

#Publish datas
channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body=username)


print(" [x] Sent "+username)
connection.close()