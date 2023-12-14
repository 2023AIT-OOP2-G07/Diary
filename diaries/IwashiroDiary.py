from diaries.AbstractDiary import AbstractDiary
class IwashiroDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "夜ご飯は鍋にする"
    def get_author(self):
        return "岩城大和"