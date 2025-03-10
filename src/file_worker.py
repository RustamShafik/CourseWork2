
class FileWorker():
    '''Создаем класс для работы с вакансиями. В этом классе нужно
     определить атрибуты, такие как название вакансии, ссылка на вакансию,
     зарплата, краткое описание или требования и т. п. (всего не менее
     четырех атрибутов). Класс должен поддерживать методы сравнения
     вакансий между собой по зарплате и валидировать данные, которыми
     инициализируются его атрибуты.'''
    def __init__(self, name: str, url: str, salary: int, employer: str):
        '''Убедимся, что в аргументах переданы подходящие значения'''
        if not isinstance(name, str):
            raise ValueError('Название вакансии должно быть строкой.')
        if not isinstance(url, str):
            raise ValueError('Ссылка на вакансию должна быть строкой.')
        if not isinstance(salary, int):
            raise ValueError('Зарплата должна быть числом.')
        if not isinstance(employer, str):
            raise ValueError('Имя работодателя должно быть строкой.')

        self.name = name
        self.url = url
        self.salary = salary if salary else 0
        '''Если зарплата не указана, то используется значение 0'''
        self.employer = employer

    def __lt__(self, other):
        '''Магический метод, возвращающий True, если равенство верное'''
        return self.salary < other.salary

    def __gt__(self, other):
        '''Магический метод, возвращающий True, если равенство верное'''
        return self.salary > other.salary

    def __eq__(self, other):
        '''Магический метод, возвращающий True, если равенство верное'''
        return self.salary == other.salary
