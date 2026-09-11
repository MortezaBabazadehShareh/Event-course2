# this works with producer2.py, along with the notification_consumer.py to show the fanout exchange

import asyncio
from pydantic import BaseModel, PositiveInt
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue, RabbitExchange, ExchangeType

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)

order_events = RabbitExchange("order_events", type=ExchangeType.FANOUT, durable=True)
payment_queue = RabbitQueue("payment_queue", durable=True)


class Order(BaseModel):
    order_id: PositiveInt
    item: str


@broker.subscriber(payment_queue, order_events)
async def charge(order: Order) -> None:
    print(f"[payment] charging card for order {order.order_id}")


if __name__ == "__main__":
    asyncio.run(app.run())