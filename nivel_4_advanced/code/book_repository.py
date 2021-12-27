from nivel_4_advanced.code.book import Book


class BookRepository:
    books = [
        Book(author="Michael Gerber", title="The E Myth", release_year=2018),
        Book(author="J.K. Rowling", title="Harry Potter", release_year=1998),
        Book(author="Ken Robinson", title="Creative schools", release_year=2015),
        Book(author="Ken Robinson", title="The Element", release_year=2013),
        Book(author="J.K. Rowling", title="Fantastic Beasts", release_year=2017),
        Book(author="David Eagleman", title="Incognito", release_year=2013),
        Book(author="Daniel J. Siegel", title="Mindsight", release_year=2015),
    ]

    def get_all(self):
        return self.books

    def _get_all_by_condition(self, condition):
        return [book for book in self.books if condition(book)]

    def get_all_by_author(self, author):
        return self._get_all_by_condition(lambda book: book.author == author)

    def get_all_after_year(self, year):
        return self._get_all_by_condition(lambda book: book.release_year > year)

    def get_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise Exception("Title not found")
