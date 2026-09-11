import asyncio
from faststream import FastStream
from faststream.rabbit import RabbitBroker

# Connect to localhost since we mapped container port 5672 -> host port 5672
BROKER_URL = "amqp://guest:guest@localhost:5672/"

broker = RabbitBroker(BROKER_URL)
app = FastStream(broker)


@broker.subscriber("no-compose-queue")
async def handle_msg(msg: str):
    print(f" Received: {msg}")


@app.after_startup
async def send_initial_message():
    await asyncio.sleep(1)
    await broker.publish(
        "Hello from manual setup without Docker Compose!",
        queue="no-compose-queue",
    )
    print(" Sent message successfully.")