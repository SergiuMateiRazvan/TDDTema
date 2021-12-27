import pytest

from nivel_3.code.book_repository import BookRepository


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
