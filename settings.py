class Settings:
    """ Класс, в котором хранятся общие данные """
    TOKEN = 'Bearer keydGwz8zs6pfYQEo' # ключ доступа к таблице
    TABLE_NAME = 'FirstTable' # имя таблицы

    def get_url(self):
        """ Метод, возвращающий ссылку на таблицу """
        return f'https://api.airtable.com/v0/appDtMoTVRSTN916B/{self.TABLE_NAME}/'


settings = Settings()