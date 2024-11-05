from __future__ import annotations

from typing import Optional
from ao3.models.users import User
from typing import Optional


class AO3Work:
    """
    Represents a work on AO3 (Archive of Our Own).

    Attributes
    ----------
    title : str
        The title of the work.
    url : str
        The URL of the work.
    id : Optional[int]
        The ID of the work.
    author : User | str
        The author of the work. Defaults to "Orphaned".
    summary : Optional[str]
        A summary of the work.
    rating : Optional[str]
        The rating of the work.
    language : str
        The language of the work. Defaults to "N/A".
    chapters : str
        The number of chapters in the work. Defaults to "0/?".
    word_count : Optional[int]
        The word count of the work. Defaults to 0.
    tags : set[str]
        The tags associated with the work.
    warnings : set[str]
        The warnings associated with the work.
    categories : set[str]
        The categories of the work.
    fandoms : set[str]
        The fandoms associated with the work.
    relationships : set[tuple[str]]
        The relationships in the work.
    characters : set[str]
        The characters in the work.
    comments : int
        The number of comments on the work.
    hits : int
        The number of hits on the work.
    bookmarks : int
        The number of bookmarks on the work.
    published_at : Optional[str]
        The publication date of the work. Defaults to "N/A".
    updated_at : Optional[str]
        The last update date of the work. Defaults to "N/A".
    is_complete : bool
        Whether the work is complete. Defaults to False.
    """

    def __init__(
        self,
        title: str,
        url: str,
        id: Optional[int] = None,
        author: User | str = "Orphaned",
        summary: Optional[str] = None,
        rating: Optional[str] = None,
        language: str = "N/A",
        chapters: str = "0/?",
        word_count: Optional[int] = 0,
        tags: Optional[set[str]] = None,
        warnings: Optional[set[str]] = None,
        categories: Optional[set[str]] = None,
        fandoms: Optional[set[str]] = None,
        relationships: Optional[set[tuple[str]]] = None,
        characters: Optional[set[str]] = None,
        comments: int = 0,
        hits: int = 0,
        bookmarks: int = 0,
        published_at: Optional[str] = "N/A",
        updated_at: Optional[str] = "N/A",
        is_complete: bool = False,
    ) -> None:
        self.title = title
        self.url = url
        self.id = id
        self.author = author
        self.summary = summary
        self.rating = rating
        self.language = language
        self.chapters = chapters
        self.word_count = word_count
        self.tags = tags if tags is not None else set()
        self.warnings = warnings if warnings is not None else set()
        self.categories = categories if categories is not None else set()
        self.fandoms = fandoms if fandoms is not None else set()
        self.relationships = relationships if relationships is not None else set()
        self.characters = characters if characters is not None else set()
        self.comments = comments
        self.hits = hits
        self.bookmarks = bookmarks
        self.published_at = published_at
        self.updated_at = updated_at
        self.is_complete = is_complete

    def __repr__(self) -> str:
        return f"<AO3Work(title={self.title}, id={self.id})>"

    # TODO: Implement the rest of the methods.
    # There's a fair bit of work to be done here, but I'll try tackling the
    # methods definition first, and then move on to the implementation.
