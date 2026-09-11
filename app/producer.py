import asyncio
from faststream.rabbit import RabbitBroker

broker = RabbitBroker("amqp://guest:guest@localhost:5672/")


async def main() -> None:
    async with broker:
        #await broker.publish({"order_id": 85, "item": "keyboard"}, "orders")
        #print("[NEW producer] published an order event")
        for i in range(100, 112):
            j = i
            if(i == 105):
                j = "ABCDE"
            event_payload = {"order_id": j, "item": f"keyboard_{j}"}
            await broker.publish(event_payload, "orders")
            print(f"[NEW producer] published order event {i}")
            
            # Optional: Add a brief delay between messages to simulate stream
            await asyncio.sleep(1.5)

if __name__ == "__main__":
    asyncio.run(main())