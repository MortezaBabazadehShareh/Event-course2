import asyncio
from faststream.rabbit import RabbitBroker, RabbitExchange, ExchangeType

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
order_events = RabbitExchange("order_events", type=ExchangeType.FANOUT, durable=True)


async def main() -> None:
    async with broker:
        for order_id in range(1, 10):
            await broker.publish(
                {"order_id": order_id, "item": "keyboard"},
                exchange=order_events,
            )
            print(f"[producer] published order {order_id}")
            await asyncio.sleep(1.5)

if __name__ == "__main__":
    asyncio.run(main())