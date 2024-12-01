from databaseconnection import connection

#each class represents a level with 1 country, 7 hints contained in a list
class Country:
    def __init__(self,name,level,hint_list):
        self.name = name
        self.level = level
        self.hint_list = hint_list


    def print_fun_fact(self):
        print(self.fun_fact)
"""
    def retrieve_hints(self):
        # SQL query to retrieve 6 hints correlating to the selected country, randomly ordered
        sql_hint = (
            f"select hints.description from hints inner join countries on countries.country_id = hints.country_id where countries.name = '{self.name}' and  hints.level = '{self.level}' order by rand();")
        # create a cursor_hint to collect countries
        cursor_hint = connection.cursor()
        cursor_hint.execute(sql_hint)
        result_hint = cursor_hint.fetchall()

        if cursor_hint.rowcount > 0:
            for hint_row in result_hint:
                self.hint_list.append(hint_row[0])
        return self.hint_list
"""





