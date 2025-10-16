from flask import Flask
from prometheus_client import start_http_server, Summary, Counter
import time
import random

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Tempo de resposta da requisição')
REQUEST_COUNT = Counter('total_requests', 'Contagem total de requisições')

@app.route('/')
@REQUEST_TIME.time()
def index():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.1, 1.0))
    return "Simulador em execução com métricas Prometheus!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=8080)