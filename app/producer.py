import asyncio
from faststream.rabbit import RabbitBroker

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")


async def main() -> None:
    async with broker:
        #await broker.publish({"order_id": 85, "item": "keyboard"}, "orders")
        #print("[NEW producer] published an order event")
        for i in range(1, 11):
            event_payload = {"order_id": i, "item": f"keyboard_{i}"}
            await broker.publish(event_payload, "orders")
            print(f"[NEW producer] published order event {i}")
            
            # Optional: Add a brief delay between messages to simulate stream
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())