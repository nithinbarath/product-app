import pika

params = pika.URLParameters('amqps://cbfwwtrw:AiIgxiQ3RDuevDyU2paTX457_tk0gDE_@puffin.rmq2.cloudamqp.com/cbfwwtrw')

connection = pika.BlockingConnection(params) 

channel = connection.channel() 

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
