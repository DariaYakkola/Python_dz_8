def search(book: list[str], info: str) -> list[str]:
    result = [contact for contact in book if info in contact]
    while len(result) != 1:
        info = input('Уточните данные контакта: ')
        result = [contact for contact in book if info in contact]
    return result


def delete() -> None:
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_find = input('Введите данные контакта: ')
    contact_to_find = search(data, contact_to_find)
    data.remove(contact_to_find)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def change() -> None:
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_find = input('Введите данные контакта: ')
    contact_to_find = search(data, contact_to_find)
    fio = input('Введите новое ФИО: ')
    phone_num = input('Введите новый номер телефона: ')
    data[data.index(contact_to_find)] = f'{fio} | {phone_num}'
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))