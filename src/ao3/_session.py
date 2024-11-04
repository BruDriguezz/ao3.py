from typing import Generic, TypeVar

from asyncio import get_event_loop, run
from aiohttp import ClientSession
from bs4 import BeautifulSoup

from ao3._parser import AO3Soup

UserT = TypeVar(name="UserT")  # Veeeery temporary. To be substituted by `User`!


class Session(Generic[UserT]):
    def __init__(
        self,
    ) -> None:
        self._session = ClientSession(
            base_url="https://archiveofourown.org/",
            loop=get_event_loop(),
            raise_for_status=True,
        )  # TODO: This will become a centralized requester API soon-ish.

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

    def _soupify(
        self,
        text: str,
    ) -> BeautifulSoup:
        return AO3Soup(
            text, "lxml"
        )  # TODO: Implement custom soup for standardized parsing methods, soon... | Half-done? I still have to elaborate on it.

    async def fetch_page(
        self,
        target: str,
    ) -> BeautifulSoup:  # TODO: This implementation is delayed until the custom `BeautifulSoup` is implemented.
        result = await self._fetch_raw_data(target=target)
        if result:
            return self._soupify(text=result)

        # TODO: Consider if I'd like to implement an exception for this...


# TODO: Elaborate on this class later; it will require some careful thinking regarding how to manage user operations.
# I'll draw out a UML model to fully flesh out the planned software structure and flow soon.
class UserSession(Session):
    def __init__(
        self,
        username: str,
        password: str,
    ) -> None:
        super().__init__()
        self._token = None
        self._user = None
        self._username = username
        self._password = password

    @property
    def user(
        self,
    ) -> ...:  # TODO:  Returns `User`
        ...

    @property
    def token(
        self,
    ) -> str:  # Returns ´str`, perhaps? Consider if we'd like a custom `Token` object.
        return self._token

    async def login(
        self,
    ) -> bool:
        async with self._session.post(
            url="/users/login",
            data={
                "user[login]": self._username,
                "user[password]": self._password,
            },
        ) as result:
            match result.status:
                case 200:
                    text = self._soupify(await result.text())
                    self._token = text.fetch_token()
                    self._session.headers.update(
                        {
                            "x-requested-with": "XMLHttpRequest",
                            "x-csrf-token": self._token,
                        }
                    )

                    return True
                case _:
                    return False  # TODO: Implement an exception for this... :)

    async def refresh_token(self) -> None: ...
