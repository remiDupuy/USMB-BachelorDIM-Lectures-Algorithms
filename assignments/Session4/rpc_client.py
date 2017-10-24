import os
import uuid
import msgpack
import msgpack_numpy as m
import numpy
import pika
import cv2

amqp_url='amqp://tijjoigp:0uzZbSC8N5fxxkHsgXKaB5CcE4eKjKWf@lark.rmq.cloudamqp.com/tijjoigp'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params)

channel = connection.channel()
result = channel.queue_declare(exclusive=True)
callback_queue = result.method.queue

corr_id = str(uuid.uuid4())
messageBody = cv2.imread('../Session1/cat.jpg', 1)
messageBody = cv2.bitwise_not(messageBody)
#messageJson = {'type': 0, 'value': 'Test'}
encoded_message = m.packb(messageBody, default = m.encode)
##
# Publish message in queue
channel.basic_publish(exchange='',
                       routing_key='rpc_queue',
                       properties=pika.BasicProperties(
                             reply_to = callback_queue,
                             correlation_id = corr_id
                       ),
                       body=encoded_message)


#print(" [x] Sent "+encoded_message)


##
# Get response from server side and close connection if gets datas
response=None
def on_response(ch, method, props, body):
    # Check if it's our message
    if corr_id != props.correlation_id:
        raise Exception()

    global response
    response=str(body)
    print(m.unpackb(response, object_hook = m.decode))

print('Starting to wait on the response queue')
channel.basic_consume(on_response, no_ack=True,
                      queue=callback_queue)
while response is None: # wait for an answer
    connection.process_data_events()
connection.close()
