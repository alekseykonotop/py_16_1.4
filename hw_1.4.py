# Каталог документов хранится в следующем виде:
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;


def input_doc_number():
    """Функция запрашивает номер документа и
    возвращает его в виде строки.
    """

    doc_num = input('Введите номер документа: ')
    return doc_num

def get_name_person():
    """Функция спрашивает номер документа и
    выводит имя человека, которому он принадлежит.
    """

    # print('Функция находится в разработке.')
    doc_number = input_doc_number()
    for doc in documents:
        if doc['number'] == doc_number:
            print('Владельцем документа под номером "{0}" является {1}.'.format(doc_number, doc['name']))


def get_all_doc_list():
    """Функция выводит список всех документов
    в формате passport "2207 876234" "Василий Гупкин".
    """

    print('Список всех документов:')
    for doc in documents:
        print('{0} "{1}" {2}'.format(doc['type'], doc['number'], doc['name']))


def get_shelf_number():
    """Функция спросит номер документа и
    выведет номер полки, на которой он находится.
    """

    # print('Функция находится в разработке.')  # Удалить
    doc_number = input_doc_number()
    for number_shelf, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            print('Документ номер "{0}" хранится на {1} полке.'.format(doc_number, number_shelf))

def add_new_doc():
    """Функция добавит новый документ в каталог и в
    перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором
    он будет храниться.
    """
    # print('Функция находится в разработке.')  # Удалить
    new_doc = input('Введите данные через запятую без пробеллов в порядке: номер, тип, имя владельца и номер полки хранения').split(',')
    documents.append(dict([("type", new_doc[1]), ('number', new_doc[0]), ('name', new_doc[2])]))
    print('Актульный список документов: ', documents)
    for number_shelf, doc_numbers in directories.items():
        if number_shelf == new_doc[3]:
            doc_numbers.append(new_doc[0])
    print('Актуальный список полок: ', directories)


# В функции del_doc и move_doc вынести в отдельную функцию получение индекса документа в списке documents для последующего удаления.
# Так же вынести в отд. функ. получение номера полки для последующего удаления документа с этой полки.
def del_doc():
    """Функция спросит номер документа и
    удалит его из каталога и из перечня полок.
    """

    print('Функция находится в разработке.')
    global documents
    doc_number = input_doc_number()
    # Удалим документ из общего списка
    ind = 0
    for i, doc in enumerate(documents):
        if doc['number'] == doc_number:
            ind = i
            break
    documents.pop(ind)  # Удалили документ из общего списка
    print('Обновленный список документов:', documents)

    # Удалим документ с полки
    for number_shelf, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            break
    print('Полка {0}, документы на полке {1}'.format(number_shelf, doc_numbers))
    for i, doc_numb in enumerate(directories[number_shelf]):
        if doc_numb == doc_number:
            print('Мы нашли нужный документ под номером: {0}'.format(i))
            break
    del directories[number_shelf][i]
    print('Теперь directories выглядит так: ', directories)






# del_doc()

def move_doc():
    """Функция спросит номер документа и
    целевую полку и переместит его с текущей
    полки на целевую.
    """

    print('Функция находится в разработке.')

def add_new_shelf():
    """Функция спросит номер новой полки и
    добавит ее в перечень.
    """

    global directories
    shelf_number = input('Введите номер новой полки: ')
    if shelf_number not in directories:
        directories[shelf_number] = []
        print('Добавлена новая полка. Актуальный список полок: {}'.format(directories))
    else:
        print('Полка с таким номером уже есть, задайте другой номер.')

# add_new_shelf()



def input_choice():
    print("""Возможные действия:
        p - узнать имя по номеру;
        l - отобразить список всех документов;
        s - узнать номер полки хранения;
        a - добавить новый документ;
        d - удалить документ;
        as - добавить новую полку хранения;
        q - выход из программы:""")
    return input('Введите желаемое действие: ').lower()


def run():
    while True:
        your_input = input_choice()
        print('Вы выбрали: {0}'.format(your_input))  #  Отладочный принт, удалить
        if your_input == 'p':
            get_name_person()  #  Поиск имени по номеру документа
        elif your_input == 'l':
            get_all_doc_list()  # Показать список всех документов
        elif your_input == 's':
            get_shelf_number()  # Узнать номер полки хранения по номеру документа
        elif your_input == 'a':
            add_new_doc()  # Добавление нового документа в каталог и перечень полок
        elif your_input == 'd':
            del_doc()  # Удаление документа из каталога и перечня полок
        elif your_input == 'm':
            move_doc()  # Перемещение документа на указанную полку
        elif your_input == 'as':
            add_new_shelf()  # Добавить новую полну хранения, спросив ее номер
        elif your_input == 'q':
            print('Программа завершена.')
            break

          
# run()