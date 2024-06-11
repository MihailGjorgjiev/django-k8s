from waitress import serve
from django_k8s.wsgi import application

if __name__ == '__main__':
    serve(application, port='8000')