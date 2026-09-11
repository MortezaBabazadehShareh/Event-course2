import asyncio
from pydantic import BaseModel, PositiveInt
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue, RabbitExchange, ExchangeType

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)

order_events = RabbitExchange("order_events_topic", type=ExchangeType.TOPIC, durable=True)
#notification_queue = RabbitQueue("notification_queue", durable=True)
notification_queue = RabbitQueue(
    "notification_queue",
    routing_key="order.created.*",
    durable=True,
)


class Order(BaseModel):
    order_id: PositiveInt
    item: str
    value_tier: str


#@broker.subscriber(notification_queue, order_events, routing_key="order.created.*")
#async def notify(order: Order) -> None:
 #   print(f"[notification] confirmation email for order {order.order_id} ({order.value_tier})")
@broker.subscriber(notification_queue, order_events)
async def notify(order: Order) -> None:
    print(f"[notification] confirmation email for order {order.order_id} ({order.value_tier})")


if __name__ == "__main__":
    asyncio.run(app.run())