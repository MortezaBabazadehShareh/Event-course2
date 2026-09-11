#### this code is designed to show the topic based distribution of the messages, after round rubin and fanout, this one is the 
#### third strategy, we run it after running the notification consumer 5 and fraud consumer 5
import asyncio
from faststream.rabbit import RabbitBroker, RabbitExchange, ExchangeType

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
order_events = RabbitExchange("order_events_topic", type=ExchangeType.TOPIC, durable=True)


async def main() -> None:
    async with broker:
        orders = [
            {"order_id": 1, "item": "keyboard", "value_tier": "standard"},
            {"order_id": 2, "item": "laptop", "value_tier": "high_value"},
            {"order_id": 3, "item": "mouse", "value_tier": "standard"},
            {"order_id": 4, "item": "keyboard", "value_tier": "standard"},
            {"order_id": 5, "item": "mouse", "value_tier": "standard"},
            {"order_id": 6, "item": "mouse", "value_tier": "high_value"},
            {"order_id": 7, "item": "monitor", "value_tier": "standard"},
            {"order_id": 8, "item": "hard drive", "value_tier": "standard"},
            {"order_id": 9, "item": "printer", "value_tier": "high_value"},
            {"order_id": 10, "item": "printer", "value_tier": "standard"},
        ]
        for order in orders:
            routing_key = f"order.created.{order['value_tier']}"
            await broker.publish(order, exchange=order_events, routing_key=routing_key)
            print(f"[producer] published order {order['order_id']} with key '{routing_key}'")
            await asyncio.sleep(1.5)

if __name__ == "__main__":
    asyncio.run(main())