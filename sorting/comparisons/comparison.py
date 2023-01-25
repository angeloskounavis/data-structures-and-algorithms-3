def sort_by_year(object):
    return sorted(sorted(object, key=lambda x: title_cleaner(x['title']), reverse=True), key=lambda x: x['year'], reverse=True)


def title_cleaner(title):
    leading_words = ['A ', 'An ', 'The ']
    for word in leading_words:
        if title.startswith(word):
            return (title[len(word):]).lower().strip()
    return title.lower()


def sort_by_title(object):
    return sorted(object, key=lambda x: title_cleaner(x['title']))

