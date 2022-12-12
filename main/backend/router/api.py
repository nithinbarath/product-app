import logging
from flask import Flask

from endpoint.flask_test import simple_page
logger = logging.getLogger(__name__)


app = Flask(__name__)

app.register_blueprint(simple_page)

origins= [
    'http://localhost:3000'
]

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=9559)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )

