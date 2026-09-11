import asyncio
from pydantic import BaseModel, PositiveInt
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue, RabbitExchange, ExchangeType

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
app = FastStream(broker)

order_events = RabbitExchange("order_events_topic", type=ExchangeType.TOPIC, durable=True)
#fraud_queue = RabbitQueue("fraud_queue", durable=True)
fraud_queue = RabbitQueue(
    "fraud_queue",
    routing_key="order.created.high_value",
    durable=True,
)


class Order(BaseModel):
    order_id: PositiveInt
    item: str
    value_tier: str


#@broker.subscriber(fraud_queue, order_events, routing_key="order.created.high_value")
#async def flag_for_review(order: Order) -> None:
 #   print(f"[fraud] flagging order {order.order_id} for manual review")
@broker.subscriber(fraud_queue, order_events)
async def flag_for_review(order: Order) -> None:
    print(f"[fraud] flagging order {order.order_id} for manual review")

if __name__ == "__main__":
    asyncio.run(app.run())