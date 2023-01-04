import pika, json
from sqlalchemy.orm import Session
from models.product import Product as ProductModels
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from application import get_db_session, db_session
from alchemy_mock.mocking import UnifiedAlchemyMagicMock
params = pika.URLParameters('amqps://cbfwwtrw:AiIgxiQ3RDuevDyU2paTX457_tk0gDE_@puffin.rmq2.cloudamqp.com/cbfwwtrw')

connection = pika.BlockingConnection(params)

channel = connection.channel() 

channel.queue_declare(queue='main')

def add_product(session: Session, data):
    product = ProductModels(id=data['id'], title=data['title'], image=data['image'])
    db_session.add(product)
    db_session.commit()



def callback(self,ch, method, properties, body):
    print('Received in main', properties.content_type)
    data = json.loads(body)
    print(data)
    self.session = UnifiedAlchemyMagicMock()
    # session: Session = Depends(get_db_session)
    if properties.content_type == 'product created':
        print('okay')
        # add_product(session=self.session, data=data)
        product = ProductModels(id=data['id'], title=data['title'], image=data['image'])
        self.session.add(product)
        self.session.commit()



channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)


print('started Consuming')

channel.start_consuming()

channel.close()