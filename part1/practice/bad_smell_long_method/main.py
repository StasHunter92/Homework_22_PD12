# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(file: str) -> list[dict]:
    list_of_users = [user.split(';') for user in file.split('\n')]
    dict_with_users = [{'name': name, 'age': age} for name, age in list_of_users]
    return dict_with_users


def _sort(data: list[dict]) -> list[dict]:
    sorted_data = sorted(data, key=lambda user: int(user['age']))
    return sorted_data


def _filter(data: list[dict]) -> list[dict]:
    filtered_data = [user for user in data if int(user['age']) > 10]
    return filtered_data


def get_users_list():
    users = _read(csv)
    users = _sort(users)
    users = _filter(users)
    return users


if __name__ == '__main__':
    print(get_users_list())
