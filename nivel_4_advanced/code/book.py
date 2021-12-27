class Book:
    def __init__(self, author, title, release_year):
        self.__author = author
        self.__title = title
        self.__release_year = release_year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, value):
        self.__release_year = value

    def __eq__(self, other):
        return (
            self.__author == other.__author and self.__title == other.__title,
            self.__release_year == other.__release_year,
        )

    def __str__(self):
        return f"Author: {self.__author}; Title: {self.__title}; Release Year: {self.__release_year};"
