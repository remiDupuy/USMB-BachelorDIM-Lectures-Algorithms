##
# @author : Remi Dupuy : IT Student
# Create a basic queue and send a message
import os
import pika


# Open connection with amqp
amqp_url='amqp://tijjoigp:0uzZbSC8N5fxxkHsgXKaB5CcE4eKjKWf@lark.rmq.cloudamqp.com/tijjoigp'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params)

channel = connection.channel()

# Create or retrieve rpc_queue queue
channel.queue_declare(queue='rpc_queue')

def on_request(ch, method, props, body):  # process and reply function
    response = body  # process the message
    ch.basic_publish(exchange='',  # reply
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=props.correlation_id),
                     body=str(response))
    print(" [x] Send back response to client")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # acknowledge


# wait for requests
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
channel.start_consuming()