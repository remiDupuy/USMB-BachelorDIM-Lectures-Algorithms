##
# @author : Remi Dupuy : IT Student
# Create a basic queue and send a message

import pika
import os
import argparse

parser = argparse.ArgumentParser()
# Create both arguments
parser.add_argument('-concurrency', action='store_true', help='Publish a message in queue')

concurrency = parser.parse_args().concurrency

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
if concurrency:
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=username,
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))
    print('concurrency mode')
else:
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=username)


print(" [x] Sent "+username)
connection.close()