class Todo:
    menu = {'1': 'Добавить дело', '2': 'Список дел', '3': 'Найти дело', '4': 'Выполнить дело',
            '5': 'Повторить дело', '6': 'Выйти'}
 
    def __init__(self):
        self.todo_items = []  # Список дел
 
    def add_todo(self, items):
        self.todo_items.append(items)
 
    def list(self):
        print('Список дел:')
        for item in self.todo_items:
            print(str(item.num) + '. ' + item.todo + ' (Выполнено)' * int(item.is_done))
        print()
 
    def find(self, find_str):
        return ((item.num, item.todo) for item in self.todo_items if item.todo.find(find_str) != -1)
 
    def run(self):
 
        while True:
            print('Меню:')
            for num, val in Todo.menu.items():
                print(num + '. ' + val, end='\n')
            command = input()
            if command == '1':
                self.add_todo(TodoItem(input('Какре дело? ')))
                print('Новое дело добавлено')
            elif command == '2':
                self.list()
            elif command == '3':
                find = self.find(input('Введите ключевое слово? '))
                for num, val in find:
                    print(str(num) + '. ' + val)
            elif command == '4':
                num = int(input('Номер дела для выполнения: '))
                for item in self.todo_items:
                    if item.num == num:
                        item.check()
                        print(f'Дело {num} выполнено')
                        break
                else:
                    print(f'Дело {num} не найдено')
 
            elif command == '5':
                num = int(input('Номер дела для повторения: '))
                for item in self.todo_items:
                    if item.num == num:
                        item.uncheck()
                        print(f'Дело {num} повторено')
                        break
                else:
                    print(f'Дело {num} не найдено')
 
            elif command == '6':
                print('Программа завершена')
                break
 
 
class TodoItem:
    couner_do = 0
 
    def __init__(self, new_do):
        self.is_done = False
        TodoItem.couner_do += 1
        self.num = TodoItem.couner_do
        self.todo = new_do
 
    def check(self):
        self.is_done = True
 
    def uncheck(self):
        self.is_done = False
 
 
if __name__ == '__main__':
    todo_1 = Todo()
    todo_1.run()