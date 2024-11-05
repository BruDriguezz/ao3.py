from typing import Generic, TypeVar

from requests import Session as ClientSession
from bs4 import BeautifulSoup
from ao3._parser import AO3Soup
from ao3.models.users import User

UserT = TypeVar(name="UserT")  # Veeeery temporary. To be substituted by `User`!


class Session(Generic[UserT]):
    def __init__(
        self,
    ) -> None:
        self._session = ClientSession()
        self._session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
            }
        )

    def _soupify(
        self,
        text: str,
    ) -> BeautifulSoup:
        return AO3Soup(text, "lxml")

    def fetch_page(
        self,
        target: str,
    ) -> BeautifulSoup:
        with self._session.get(target) as result:
            return self._soupify(result.text)

    def post_to_page(
        self,
        target: str,
        data: dict,
    ) -> ...:
        with self._session.post(
            url=target,
            data=data,
        ) as result:
            return self._soupify(result.text)

    def __del__(
        self,
    ) -> None:
        self._session.close()


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
    ) -> str:
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
                    self._user = User(self._username, self, is_authenticated=True)
                case _:
                    return False  # TODO: Implement an exception for this...

    def refresh_token(self) -> None:
        if self._token:
            result = self.fetch_page(
                "https://archiveofourown.org/users/{self._username}/"
            )
            self._token = result.fetch_token()
            self._session.headers.update(
                {
                    "x-requested-with": "XMLHttpRequest",
                    "x-csrf-token": self._token,
                }
            )
