from sorting.comparisons.comparison import sort_by_title, sort_by_year
from sorting.comparisons.movies import movies

# Expected test output of test #1
expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]


# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];


def test_by_year():
    actual = [movie['title'] for movie in sort_by_year(movies)]
    global expected1
    assert actual == expected1


def test_by_title():
    actual = [movie['title'] for movie in sort_by_title(movies)]
    global expected2
    assert actual == expected2


