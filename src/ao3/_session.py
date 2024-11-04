from typing import Generic, TypeVar

from requests import Session as ClientSession
from bs4 import BeautifulSoup

from ao3._parser import AO3Soup

UserT = TypeVar(name="UserT")  # Veeeery temporary. To be substituted by `User`!


class Session(Generic[UserT]):
    def __init__(
        self,
    ) -> None:
        self._session = ClientSession()
        self._session.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'    
            }
        )  # TODO: This will become a centralized requester API soon-ish.

    def _fetch_raw_data(
        self,
        target: str,
    ) -> str | None:
        with self._session.get(
            url=target,
        ) as result:
            match result.status_code:
                case 200:
                    return result.text
                case _:
                    return None  # TODO: Elaborate on this later...

    def _soupify(
        self,
        text: str,
    ) -> BeautifulSoup:
        return AO3Soup(
            text, "lxml"
        )  # TODO: Implement custom soup for standardized parsing methods, soon... | Half-done? I still have to elaborate on it.

    def fetch_page(
        self,
        target: str,
    ) -> BeautifulSoup:  # TODO: This implementation is delayed until the custom `BeautifulSoup` is implemented.
        result = self._fetch_raw_data(target=target)
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

    def login(
        self,
    ) -> bool:
        with self._session.post(
            url="https://archiveofourown.org/users/login",
            data={
                "user[login]": self._username,
                "user[password]": self._password,
            },
        ) as result:
            match result.status_code:
                case 200:
                    self._token = self._soupify(result.text).fetch_token()
                    self._session.headers.update(
                        {
                            "x-requested-with": "XMLHttpRequest",
                            "x-csrf-token": self._token,
                        }
                    )
                case _:
                    return False  # TODO: Implement an exception for this... :)

    def refresh_token(self) -> None: ...
