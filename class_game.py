from class_country import Country
from class_game_movement import GameMovement
from mysql.connector import cursor
from databaseconnection import connection
import random

class Game(Country, GameMovement):
    def __init__(self,disease_name,points = 300, movement = "",):
        self.disease_name = disease_name
        self.points = points
        GameMovement.__init__(self,movement)
        self.country_list = []
        self.current_level = 1
        self.correct_guess = []

    def ingredient_country(self):
        sql = f"select name from countries where name != 'No country' order by rand() limit 7 "
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                self.country_list.append(row[0])
        for answer in self.country_list:
            sql_fact = f"select fun_fact from countries where name = '{answer}' "
            cursor_fact = connection.cursor()
            cursor_fact.execute(sql_fact)
            result_fact = cursor.fetchall()
            if cursor_fact.rowcount > 0:
                for row in result_fact:
                    fact = row[0]
                    country = Country(answer,self.country_list.index(answer) + 1,fact)

    def answer_is_correct(self,guess_input):
        if guess_input == self.country_list.index(self.current_level - 1):
            self.current_level += 1
            self.correct_guess.append(guess_input)
            print("Your guess is correct - Congratulations, let's go!")
            return True
        else:
            print("Your guess is incorrect, try again!")
            return False

    def randomize_countries(self,list_of_choices):
        new_list = list_of_choices
        if len(new_list) > 4:
            random.shuffle(new_list)
            result = new_list[:3]
        if len(new_list) <= 4:
            random.shuffle(new_list)
            result = new_list
        return result

    def multiple_choice(self):
        sql = f"select name from countries where name != '{self.country_list[self.current_level - 1]}';"
        listed_countries = []
        multiple_options = [self.country_list[self.current_level - 1]]
        cursor_count = connection.cursor()
        cursor_count.execute(sql)
        result = cursor_count.fetchall()
        if cursor_count.rowcount > 0:
            for row in result:
                listed_countries.append(row[0])
        listed_countries1 = self.randomize_countries(listed_countries)
        for i in listed_countries1:
            multiple_options.append(i)
        print('The ingredient may be in one of these countries: ', self.randomize_countries(multiple_options))

    def point_per_level(self):
        sql_point = f"select hints.points from hints where hints.level = '{self.current_level}' limit 1;"
        # create a cursor_hint to calculate point countries
        cursor_point = connection.cursor()
        cursor_point.execute(sql_point)
        result_point = cursor_point.fetchall()
        point_level = 0
        if cursor_point.rowcount > 0:
            for point_row in result_point:
                point_level = point_row[0]
        return point_level

    def current_point(self):
        if self.answer_is_correct is True:
            self.points += self.point_per_level()
        else:
            self.points -= self.point_per_level()

    def insert_session(self):
        sql_session = f"insert into disease(disease_name, visited_countries,level) values ('{self.disease_name}',(select country_id from countries where name = '{visited_countries}'), '{current_level}');"
        cursor_session = connection.cursor()
        cursor_session.execute(sql_session)
        return