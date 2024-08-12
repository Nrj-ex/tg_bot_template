from datetime import datetime
from telegram import User as TG_user
from database.database_class import Database


class Storage:
    def __init__(self, database: Database):
        self.database = database
        self.__check_struct_db__()

    def __check_struct_db__(self) -> None:
        # Таблица пользователей
        request = ("CREATE TABLE if not exists users(id integer PRIMARY KEY, name text, "
                   "username text, full_name text, link text, role text, joining_date timestamp)")

        self.database.create_table(request)

    def __get_user_data__(self, user_id: int) -> tuple:
        request = """SELECT id, username FROM users WHERE id = ?"""
        response = self.database.select_fetchone(request, (user_id,))
        return response

    def __get_user_id_by_username__(self, username: str) -> tuple:
        request = """SELECT id FROM users WHERE username = ?"""
        response = self.database.select_fetchone(request, (username,))
        return response

    def __add_new_user__(self, user: TG_user, role: str) -> None:
        """
        Args:
            user: add user in database

        Returns:
            None
        """
        request = "INSERT INTO users(id, name, username, full_name, link, role, joining_date) " \
                  "VALUES(?, ?, ?, ?, ?, ?, ?)"
        values = (
            user.id, user.name, user.username,
            user.full_name, user.link, role, datetime.now()
        )
        self.database.insert(request, values)

    def add_user(self, user: TG_user, role: str = 'user') -> None:
        """
        Args:
            user: объект телеграм пользователя
            role: роль пользователя

        Returns: None
        """
        # добавление пользователя в бд
        user_data = self.__get_user_data__(user_id=user.id)

        if not user_data:
            self.__add_new_user__(user=user, role=role)


if __name__ == "__main__":
    pass
