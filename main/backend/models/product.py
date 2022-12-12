# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import UniqueConstraint


# from router.api import app

# db = SQLAlchemy(app)

# class Product(db.Model):
#     id = db.Column


from sqlalchemy import Column , Integer , String, UniqueConstraint
from application import Base



class Product(Base):

    __tablename__ = "product"

    id = Column ( Integer , primary_key = True , index = True )
    title = Column(String)
    image = Column(String)

class ProductUser(Base):

    __tablename__ = "productuser"

    id = Column ( Integer , primary_key = True , index = True )
    user_id = Column(Integer)
    product_id = Column(Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')
    

