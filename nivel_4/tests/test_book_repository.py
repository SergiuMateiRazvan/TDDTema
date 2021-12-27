import pytest

from nivel_4.code.book import Book
from nivel_4.code.book_repository import BookRepository


class TestBookRepository:
    def test_get_all(self):
        repo = BookRepository()
        assert repo.get_all() == repo.books

    @pytest.mark.parametrize(
        "author, expected",
        [("J.K. Rowling", 2), ("Michael Gerber", 1), ("No author", 0)],
    )
    def test_get_all_by_author(self, author, expected):
        repo = BookRepository()
        assert len(repo.get_all_by_author(author)) == expected

    @pytest.mark.parametrize(
        "year, expected", [(2018, 0), (2000, 6), (1990, 7), (2013, 4)]
    )
    def test_get_all_after_year(self, year, expected):
        repo = BookRepository()
        assert len(repo.get_all_after_year(year)) == expected

    @pytest.mark.parametrize(
        "title, expected",
        [
            (
                "Harry Potter",
                Book(author="J.K. Rowling", title="Harry Potter", release_year=1998),
            ),
            (
                "The Element",
                Book(author="Ken Robinson", title="The Element", release_year=2013),
            ),
        ],
    )
    def test_get_by_title(self, title, expected):
        repo = BookRepository()
        assert repo.get_by_title(title) == expected

    def test_get_by_title_not_found(self):
        repo = BookRepository()
        with pytest.raises(Exception):
            repo.get_by_title("Not a good title")
