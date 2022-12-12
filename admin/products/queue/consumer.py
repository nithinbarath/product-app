import pika

params = pika.URLParameters('amqps://cbfwwtrw:AiIgxiQ3RDuevDyU2paTX457_tk0gDE_@puffin.rmq2.cloudamqp.com/cbfwwtrw')

connection = pika.BlockingConnection(params)

channel = connection.channel() 

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

 
channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)


print('started Consuming')

channel.start_consuming()

channel.close()