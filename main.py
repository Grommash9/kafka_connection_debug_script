from aiokafka import AIOKafkaProducer
import json
import asyncio


async def create_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers="http://127.0.0.1:41795",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    await producer.start()
    await producer.send("sad", {"da": "net"})


if __name__ == "__main__":
    asyncio.run(create_producer())
