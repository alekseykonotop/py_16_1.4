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

def get_name_person(doc_number):
    """Функция спрашивает номер документа и
    выводит имя человека, которому он принадлежит.
    """

    # print('Функция находится в разработке.')
    # doc_number = input_doc_number()
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


def get_shelf_number(doc_number):
    """Функция получает номер документа и
    возвращает номер полки, на которой он находится.
    """

    # print('Функция находится в разработке.')  # Удалить
    # doc_number = input_doc_number()
    for shelf_number, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            return shelf_number
            # print('Документ номер "{0}" хранится на {1} полке.'.format(doc_number, shelf_number))

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
def get_index(number, data_array, key_dict=0):
    """Функция вернет индекс элемента итеррируемого

    объекта data_array, если этот элемент, который
    представляет из себя словарь, содержит в себе
    ключ key_dict со сначением number.
    """
    if key_dict != 0:
        for i, doc in enumerate(data_array):
            if doc[key_dict] == number:
                return i
    elif key_dict == 0:
        for i, doc_numb in enumerate(data_array):
            if doc_numb == number:
                return i


#  Для фукнции del_doc исправить код, чтобы для определения номера полки хранения документа использовалась уже
#  написанная фукнция get_shelf_number(doc_number), в которую надо только передать номер документа.
def del_doc():
    """Функция спросит номер документа и
    удалит его из каталога и из перечня полок.
    """

    global documents
    doc_number = input_doc_number()
    ind = get_index(doc_number, documents, 'number')
    documents.pop(ind)  # Удалили документ из общего списка
    print('Обновленный список документов:', documents)

    # Удалим документ с полки
    for number_shelf, doc_numbers in directories.items():
        if doc_number in doc_numbers:
            break
    print('Полка {0}, документы на полке {1}'.format(number_shelf, doc_numbers))
    ind_2 = get_index(doc_number, directories[number_shelf])
    del directories[number_shelf][ind_2]
    print('directories после удаления: ', directories)






# del_doc()

def input_shelf_number():
    sh_number = input('Введите номер полки: ')
    return sh_number

def move_doc():
    """Функция спросит номер документа и
    целевую полку и переместит его с текущей
    полки на целевую.
    """
# 1. нужна функция, которая узнает на какой полке находится документ
# 2. Если полко, на которой находится документ не совпадает с полкой которую указал пользователь, то программа удалит документ с прежней полки
# 3  Добавит документ в указанную пользователем полку

    print('Функция находится в разработке.')
    doc_number = input_doc_number()  # Получили номер документа
    shelf_number = input_shelf_number()




def add_new_shelf():
    """Функция спросит номер новой полки и
    добавит ее в перечень.
    """

    global directories
    shelf_number = get_shelf_number()
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
        m - переместить документ на другую полку;
        as - добавить новую полку хранения;
        q - выход из программы:""")
    return input('Введите желаемое действие: ').lower()


def run():
    while True:
        your_input = input_choice()
        print('Вы выбрали: {0}'.format(your_input))  #  Отладочный принт, удалить
        if your_input == 'p':
            doc_number = input_doc_number()
            get_name_person(doc_number)  #  Поиск имени по номеру документа
        elif your_input == 'l':
            get_all_doc_list()  # Показать список всех документов
        elif your_input == 's':
            doc_number = input_doc_number()
            print('Документ хранится на полке {0}'.format(get_shelf_number(doc_number)))  # Узнать номер полки хранения по номеру документа
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

          
run()