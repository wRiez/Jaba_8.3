DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_query(query):
    name, question = query.split(', ', 1)

    if name == 'анфиса':
        return process_anfisa(question)


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_friends_count(count)} друзей.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print(process_query('анфиса, сколько у меня друзей?'))
print(process_query('анфиса, кто все мои друзья?'))
print(process_query('анфиса, где все мои друзья?'))
print(process_query('анфиса, кто виноват?'))
print(process_query('соня, ты где?'))