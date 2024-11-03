from typing import Generic, TypeVar

from asyncio import get_event_loop
from aiohttp import ClientSession
from bs4 import BeautifulSoup


UserT = TypeVar(name="UserT")  # Veeeery temporary. To be substituted by `User`!


class Session(Generic[UserT]):
    def __init__(
        self,
    ) -> None:
        self._token = None
        self._user = None  # TODO: Implement a `User` object to represent AO3 users.
        self._session = ClientSession(
            base_url="https://archiveofourown.org/",
            loop=get_event_loop(),
            raise_for_status=True,
        )

    @property
    def user(
        self,
    ) -> ...:  # TODO:  Returns `User`
        ...

    @property
    def token(
        self,
    ) -> ...:  # Returns ´str`, perhaps? Consider if we'd like a custom `Token` object.
        ...

    async def _fetch_raw_data(
        self,
        target: str,
    ) -> str | None:
        async with self._session.get(url=target) as result:
            match result.status:
                case 200:
                    return str(result.content)
                case _:
                    return None  # TODO: Elaborate on this later...

    async def _soupify(
        self,
        text: str,
    ) -> BeautifulSoup:
        return BeautifulSoup(
            text, "lxml"
        )  # TODO: Implement custom soup for standardized parsing methods, soon...

    async def fetch_page(
        self,
        target: str,
    ) -> ...:  # TODO: This implementation is delayed until the custom `BeautifulSoup` is implemented.
        ...
