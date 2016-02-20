import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
daemon = False
pidfile='gunicorn_pid'
accesslog='gunicorn_access.log'
errorlog='gunicorn_error.log'
