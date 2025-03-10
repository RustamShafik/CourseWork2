import json
import requests
from abc import ABC, abstractmethod

class Parser(ABC):
    '''Создаем абстрактный класс для работы с API сервиса с вакансиями'''

    @abstractmethod
    '''Создаем абстрактный метод для получения вакансий по ключевому слову'''
    def load_vacancies(self, keyword):
        pass

class HH(Parser):
    '''Подключается к API HH и получает вакансии по ключевому слову'''

    def load_vacancies(self, keyword):
        '''Функция получает вакансии по ключевому слову'''
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword}
        response = requests.get(url, params=params)
        data = response.json()
        return data
