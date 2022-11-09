from time import sleep

from .celery import app


@app.task(
    acks_late=True,
    bind=True,
)
def sleep_task(self, seconds: int):
    print(f"sleep_task({seconds}) (task id = {self.request.id})")
    for _ in range(seconds):
        sleep(1)
