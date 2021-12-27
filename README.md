# TDD Tema
Tema pentru modulul Software testing and TDD

Nivel 1.

a) Scrieti o functie care sa returneze numarul de elemente dintr-o lista egale cu un element dat. Functia primeste doi parametri: lista in care se cauta si elementul care se cauta.

Optional: Daca elementul nu este gasit sa se arunce exceptie

e.g. 

 

```python
get_no_of_equals([1,2,3,4,5,3,4,2,7,4], 4) = 3
```

b) Sa se testeze functia

Optional: Sa se testeze folosind pytest.raises partea cu exceptie intr-o a doua functie de test

Nivel 2

a) Sa se scrie o clasa Book care sa contina atributele author, title si release_year (anul aparitiei).

b) Sa se faca getteri si setteri pentru aceasta clasa

c) Sa se implementeze functiile __str__ si __eq__ (egalitatea consta in egalitate tuturor atributelor)

Nivel 3

a) Sa se scrie o clasa BookRepository in care sa se puna o lista de Book data mai jos

```python
books = [
	Book(author="Michael Gerber", title="The E Myth", release_year=2018),
	Book(author="J.K. Rowling", title="Harry Potter", release_year=1998),
	Book(author="Ken Robinson", title="Creative schools", release_year=2015),
	Book(author="Ken Robinson", title="The Element", release_year=2013),
	Book(author="J.K. Rowling", title="Fantastic Beasts", release_year=2017),
	Book(author="David Eagleman", title="Incognito", release_year=2013),
	Book(author="Daniel J. Siegel", title="Mindsight", release_year=2015)
]
```

In aceasta clasa va trebui sa scrieti mai multe metode:

b) get_all() care returneaza toate cartile

c) get_all_by_author(author) care returneaza toate cartile autorului dat

d) get_all_after_year(release_year) care returneaza toate cartile lansate dupa anul dat ca parametru

e) Scrieti teste pentru toate functiile implementate folosind pytest

Nivel 4

f) Asigurati-va ca aveti 100% coverage folosind libraria coverage

e.g.

coverage run —source=”.” -m pytest

coverage report `nume_fisier`

g) Scrieti functia get_by_title(title) in BookRepository care returneaza o cartea care are titlul dat.

Data nu este gasita o carte cu acel title aruncati exceptie (raise Exception)

h) Scrieti 2 teste pentru functia get_by_title, dintre care unul  sa foloseasca pytest.raises
