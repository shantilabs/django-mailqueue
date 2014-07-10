from celery import Celery
from mailqueue import process, clean


app = Celery()


@app.task(name='mailqueue.process')
def process_mailqueue():
    process()


@app.task(name='mailqueue.clean')
def clean_mailqueue():
    clean()
