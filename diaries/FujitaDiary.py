from diaries.AbstractDiary import AbstractDiary

class FujitaDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-15"
    
    def get_summary(self):
        return "今日は爽やかな秋景色だった"
    
    def get_author(self):
        return "Fujita Rikiya"