from random import randint
import requests
import datetime
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.hp = randint(50, 200)
        self.power = randint(5, 50)
        self.img = self.get_img()
        self.name = self.get_name()
        self.last_feed_time = datetime.now()
        self.next_feed_time = self.last_feed_time
        Pokemon.pokemons[pokemon_trainer] = self
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
        здоровье твоего покемона: {self.hp}
        сила твоего покемона: {self.power}
        следующее время кормления: {self.next_feed_time}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if self.hp > 0:
            if isinstance(enemy, Wizard):
                chance = randint(1,5)
                if chance == 1:
                    return "Покемон-волшебник применил щит в сражении"
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"""Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}
                Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}"""
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        else:
            return "Здоровье вашего покемона не позволяет вам участвовать в сражениях"
        
    # def korm(self):
    #     lek = randint(1,10)
    #     self.hp += lek
    #     return f"Вы покормили своего покемона, теперь его здоровье: {self.hp}"
    
    def feed(self, feed_interval = 20, hp_increase = 10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        self.next_feed_time = current_time + delta_time
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.next_feed_time}"
class Wizard(Pokemon):
    def info(self):
        return "У тебя покемон-волшебник \n\n" + super().info()
    def feed(self, feed_interval = 10, hp_increase = 10):
        return super().feed(feed_interval, hp_increase)

class Fighter(Pokemon):
    def attack(self, enemy):
        if self.hp > 0:
            super_power = randint(5,15)
            self.power += super_power
            result = super().attack(enemy)
            self.power -= super_power
            return result + f"\nБоец применил супер-аттаку силой:{super_power}"
        else:
            return "Здоровье вашего покемона не позволяет вам участвовать в сражениях"
    def info(self):
        return "У тебя покемон-боец\n\n" + super().info()
    def feed(self, feed_interval = 20, hp_increase = 20):
        return super().feed(feed_interval, hp_increase)
       
        



