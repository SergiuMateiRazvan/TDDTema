class Book:
    def __init__(self, author, title, release_year):
        self.__author = author
        self.__title = title
        self.__release_year = release_year

    def get_author(self):
        return self.__author

    def set_author(self, value):
        self.__author = value

    def get_title(self):
        return self.__title

    def set_title(self, value):
        self.__title = value

    def get_release_year(self):
        return self.__release_year

    def set_release_year(self, value):
        self.__release_year = value

    def __eq__(self, other):
        return (
            self.__author == other.__author and self.__title == other.__title,
            self.__release_year == other.__release_year,
        )

    def __str__(self):
        return f"Author: {self.__author}; Title: {self.__title}; Release Year: {self.__release_year};"
