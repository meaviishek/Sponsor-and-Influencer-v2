from celery_app import make_celery
from app import app  

celery = make_celery(app)

if __name__ == '__main__':

    celery.start()
