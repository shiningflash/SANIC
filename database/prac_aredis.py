import asyncio
from aredis import StrictRedisCluster

async def example():
    client = StrictRedisCluster(host='172.17.0.2', port=7001)
    await client.flushdb()
    await client.set('foo', 1)
    await client.lpush('a', 1)
    print(await client.cluster_slots())

    await client.rpoplpush('a', 'b')
    assert await client.rpop('b') == b'1'

loop = asyncio.get_event_loop()
loop.run_until_complete(example())