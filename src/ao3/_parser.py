from bs4 import BeautifulSoup, NavigableString


class AO3Soup(BeautifulSoup):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            *args,
            **kwargs,
        )

    def fetch_token(
        self,
    ) -> str:
        token = self.find(
            name="input",
            attrs={
                "name": "authenticity_token",
            },
        )
        return token.attrs["value"]  # type: ignore
