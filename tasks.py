from celery import Celery

app = Celery('tasks', 
             broker='pyamqp://guest@localhost//',
             backend='rpc://')

@app.task(name='tasks.add')
def add(x, y):
    return x + y 
