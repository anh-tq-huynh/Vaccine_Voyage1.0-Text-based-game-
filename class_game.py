from class_country import Country
from class_game_movement import GameMovement
from mysql.connector import cursor
from databaseconnection import connection
import random

#inherit functions
class Game(GameMovement):
    def __init__(self,disease_name,points = 300):
        self.disease_name = disease_name
        self.points = points
        self.country_list = []
        self.current_level = 1
        self.correct_guess = []
        self.level_over = "No"
        self.game_over = "No"
        super().__init__(self.current_level)

    #generate 7 countries for the game + create a class for it through Country()
    def ingredient_country(self):
        sql = f"select name from countries where name != 'No country' order by rand() limit 7 "
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            level = 1
            for row in result:
                self.country_list.append(Country(row[0],level,self.retrieve_hints(row[0],level)))
                level += 1
        return self.country_list

    def retrieve_hints(self,name,level):
        # SQL query to retrieve 6 hints correlating to the selected country, randomly ordered
        hint_list = []
        sql_hint = (
            f"select hints.description from hints inner join countries on countries.country_id = hints.country_id where countries.name = '{name}' and  hints.level = '{level}' order by rand();")
        # create a cursor_hint to collect countries
        cursor_hint = connection.cursor()
        cursor_hint.execute(sql_hint)
        result_hint = cursor_hint.fetchall()

        if cursor_hint.rowcount > 0:
            for hint_row in result_hint:
                hint_list.append(hint_row[0])
        return hint_list
        """
        for answer in self.country_list:
            sql_fact = f"select fun_fact from countries where name = '{answer}' "
            cursor_fact = connection.cursor()
            cursor_fact.execute(sql_fact)
            result_fact = cursor.fetchall()
            if cursor_fact.rowcount > 0:
                for row in result_fact:
                    fact = row[0]
                    country = super((answer,self.country_list.index(answer) + 1,fact))
        """

    def answer_is_correct(self,guess_input):
        if guess_input == self.country_list[self.current_level - 1].name:
            self.current_level += 1
            self.correct_guess.append(guess_input)
            self.points += self.point_per_level()
            print(f'Points: {self.points}')
            print(f'Correct guess: {self.correct_guess}')
            print("Your guess is correct - Congratulations, let's go!")
            self.level_over = "Yes"
            return self.points
        else:
            if self.points >= 0:
                print("Your guess is incorrect, try again!")
                self.points -= self.point_per_level()
                print(f'Points: {self.points}')
            else:
                self.game_over = "Yes"
            return self.points, self.game_over

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
        if self.points >= 0:
            self.points -= self.point_per_level()*1.5
            print('Points: ', self.points)
            sql = f"select name from countries where name != '{self.country_list[self.current_level - 1]}';"
            listed_countries = []
            multiple_options = [self.country_list[self.current_level - 1].name]
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
        else:
            self.game_over = "Yes"
            return self.game_over

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


    def is_lost(self):
        if self.points >= 0:
            self.game_over = "No"
            return self.game_over
        else:
            self.game_over = "Yes"
            return self.game_over

    def insert_session(self):
        sql_session = f"insert into disease(disease_name, visited_countries,level) values '{self.disease_name}','{self.correct_guess}', '{self.current_level}');"
        cursor_session = connection.cursor()
        cursor_session.execute(sql_session)
        return

    def new_hint(self, hint_list,current_hint_no):
        if self.points >=0:
            super().new_hint(hint_list, current_hint_no)

            self.points -= self.point_per_level()
            print(f'Points: {self.points}')
        else:
            self.points -= self.point_per_level()
            self.game_over = "Yes"
        return self.points, self.game_over


    def guess (self):
        super().guess()

    def quit (self):
        super().quit()


    def decision (self,action, hint_list,current_hint_no):
        if action == "NEW HINT":
            self.new_hint(hint_list,current_hint_no)
        elif action == "GUESS":
            guess_input = super().guess()
            self.answer_is_correct(guess_input)
        elif action == "QUIT":
            self.quit()


