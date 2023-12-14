from diaries.DiarySample import DiarySample # ↓のリストには、メンバーの各日記が格納されます。
from diaries.IwashiroDiary import IwashiroDiary
from diaries.TajimaDiary import TajimaDiary
from diaries.matsuuraakaneDiary import matsuuraakaneDiary
from diaries.chokaiDiary import chokaiDiary
from diaries.FujitaDiary import FujitaDiary
diaries = [
  DiarySample(),
  IwashiroDiary(),
  TajimaDiary(),
  matsuuraakaneDiary(),
  chokaiDiary(),
  FujitaDiary()
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
