# Python Celery - Simple Tasks

Prototype using Celery, an asynchronous task queue with RabbitMQ.

- Start a RabbitMQ server

- Create a Python environment

```
virtualenv venv
source ./venv/bin/activate
```

- Install dependencies

```
(venv) pip install -r requirements.txt
```

- Start Celery worker

```
(venv) celery -A tasks worker --loglevel=INFO
```

- Start Celery client

```
(venv) python client.py
```
