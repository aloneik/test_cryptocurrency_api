import asyncio
import json

from unittest.mock import Mock
from contextlib import asynccontextmanager
from .. import bitfinex_api


def test_parse_api_response():
    async def text_mock():
        return '{"1": "value"}'
    mock = Mock()
    mock.text.return_value = text_mock()

    loop = asyncio.get_event_loop()
    # Call API
    result = loop.run_until_complete(bitfinex_api.parse_api_response(mock))

    assert result == {"1": "value"}


def test_parse_api_response_1():
    async def text_mock():
        return '{"error": "test"}'
    mock = Mock()
    mock.text.return_value = text_mock()

    loop = asyncio.get_event_loop()
    # Call API
    try:
        _ = loop.run_until_complete(bitfinex_api.parse_api_response(mock))
    except bitfinex_api.APIError as exception:
        assert str(exception) == "test"
