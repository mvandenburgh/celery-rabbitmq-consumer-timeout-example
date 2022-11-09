from celery import Celery

app = Celery(
    "proj",
    broker="amqp://localhost:5672",
    include=["proj.tasks"],
)

if __name__ == "__main__":
    app.start()
