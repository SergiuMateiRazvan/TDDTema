from nivel_3.code.book import Book


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

    def get_all_by_author(self, author):
        books_by_author = []
        for book in self.books:
            if book.get_author() == author:
                books_by_author.append(book)
        return books_by_author

    def get_all_after_year(self, year):
        all_books_after_year = []
        for book in self.books:
            if book.get_release_year() > year:
                all_books_after_year.append(book)
        return all_books_after_year
