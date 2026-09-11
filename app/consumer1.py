# it works with the file producer.py
import asyncio
from pydantic import BaseModel, PositiveInt
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)

orders_queue = RabbitQueue("orders", durable=True)


class Order(BaseModel):
    order_id: PositiveInt
    item: str


@broker.subscriber(orders_queue)
async def handle_order(order: Order) -> None:
    print(f"[consumer] received valid order: {order}")


if __name__ == "__main__":
    asyncio.run(app.run())