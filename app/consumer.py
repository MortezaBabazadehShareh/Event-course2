import asyncio
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)

orders_queue = RabbitQueue("orders", durable=True)


@broker.subscriber(orders_queue)
async def handle_order(message: dict) -> None:
    print(f"[consumer] received: {message}")


if __name__ == "__main__":
    asyncio.run(app.run())