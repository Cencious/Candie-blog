import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kakan:Abiathar2022@localhost/blog'

