from __future__ import annotations

from typing import Type, Union, Optional
from ao3.models.works import AO3Work
from ao3.client import Session, UserSession


SessType = Union[Type[Session], Type[UserSession]]


class User:
    def __init__(
        self,
        username: str,
        id: Optional[int] = None,
        user_id: Optional[int] = None,
        session: Optional[SessType] = None,
        is_authenticated: bool = False,
        bio: Optional[str] = None,
        joined_at: Optional[str] = None,
        works: Optional[list[AO3Work]] = None,
        history: Optional[list[AO3Work]] = None,
        bookmarks: Optional[list[AO3Work]] = None,
        pseudonyms: Optional[list[str]] = None,
        series: Optional[list[str]] = None,
        collections: Optional[list[str]] = None,
    ) -> None:
        self.name = username
        self.id = id
        self.user_id = user_id
        self.url = f"https://archiveofourown.org/users/{username}/"
        self._session = session
        self._is_authenticated = is_authenticated
        self.bio = bio
        self.joined_at = joined_at
        self.works = works if works is not None else []
        self.history = history if history is not None else []
        self.bookmarks = bookmarks if bookmarks is not None else []
        self.pseudonyms = pseudonyms if pseudonyms is not None else []
        self.series = series if series is not None else []
        self.collections = collections if collections is not None else []

    def __repr__(self) -> str:
        return f"<User(name={self.name}, id={self.id})>"

    # TODO: Implement the rest of the methods.
    # There's a fair bit of work to be done here, but I'll try tackling the
    # methods definition first, and then move on to the implementation.
