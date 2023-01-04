import pika, json

params = pika.URLParameters('amqps://cbfwwtrw:AiIgxiQ3RDuevDyU2paTX457_tk0gDE_@puffin.rmq2.cloudamqp.com/cbfwwtrw')

connection = pika.BlockingConnection(params) 

channel = connection.channel() 

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
