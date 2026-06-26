import contextlib
from types import SimpleNamespace
from typing import Any, cast

import pytest
from pytest_mock import MockerFixture

from tarifia.dummy.tasks import dummy_task
from tarifia.redis import Redis
from tarifia.worker import RedisMiddleware


@pytest.mark.asyncio
async def test_dummy_task_uses_database_and_redis(
    redis: Redis, mocker: MockerFixture
) -> None:
    execute = mocker.AsyncMock()
    session = SimpleNamespace(execute=execute)

    @contextlib.asynccontextmanager
    async def sessionmaker() -> Any:
        yield session

    mocker.patch("tarifia.dummy.tasks.AsyncSessionMaker", sessionmaker)
    mocker.patch.object(RedisMiddleware, "get", return_value=redis)

    await dummy_task(redis_key="dummy:test")

    execute.assert_awaited_once()
    value = cast(str | bytes | None, await redis.get("dummy:test"))
    if isinstance(value, bytes):
        value = value.decode()
    assert value == "1"
