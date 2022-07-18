# -*- coding: utf-8 -*-

from celery import Celery
import time

# 如何让宿主机能ping通redis容器的ip
BROKER_URL = 'redis://:666666@127.0.0.1:6379/0'
BACKEND_URL = 'redis://:666666@127.0.0.1:6379/1'

app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


@app.task
def add(x, y):
    time.sleep(60)
    return x + y