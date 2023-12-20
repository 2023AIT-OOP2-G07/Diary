from diaries.DiarySample import DiarySample  # ↓のリストには、メンバーの各日記が格納されます。
from diaries.IwashiroDiary import IwashiroDiary
from diaries.TajimaDiary import TajimaDiary
from diaries.matsuuraakaneDiary import matsuuraakaneDiary
from diaries.chokaiDiary import ChokaiDiary
from diaries.FujitaDiary import FujitaDiary
from diaries.KonishishutoDiary import shuDiary
from diaries.Nakayama900Diary import Nakayama900Diary

diaries = [
    DiarySample(),
    IwashiroDiary(),
    TajimaDiary(),
    matsuuraakaneDiary(),
    ChokaiDiary(),
    FujitaDiary(),
    shuDiary(),
    Nakayama900Diary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
