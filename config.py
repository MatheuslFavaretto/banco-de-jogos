import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+pymysql',
        usuario = 'root',
        senha = 'favaretto',
        servidor = 'localhost',
        database = 'jogoteca'
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'