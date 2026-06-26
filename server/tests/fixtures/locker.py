import pytest_asyncio

from tarifia.locker import Locker
from tarifia.redis import Redis


@pytest_asyncio.fixture
async def locker(redis: Redis) -> Locker:
    return Locker(redis)
