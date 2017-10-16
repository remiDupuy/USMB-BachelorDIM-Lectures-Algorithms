##
# @author : Remi Dupuy : IT Student
# Retrieve message from queue

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

#initialize counter
counter = 0
def callback(ch, method, properties, body):
    global counter
    counter = counter+1
    print(" [x] Received {body} : [{counter}]".format(body=body, counter=counter))


channel.basic_consume(callback,
                      queue='presentation',
                      no_ack=True)


print(" [x] Waiting for messages. To exit press Ctrl+c")
channel.start_consuming()