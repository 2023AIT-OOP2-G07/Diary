from diaries.DiarySample import DiarySample # ↓のリストには、メンバーの各日記が格納されます。
from diaries.IwashiroDiary import IwashiroDiary
from diaries.TajimaDiary import TajimaDiary
diaries = [
  DiarySample(),
  IwashiroDiary(),
  TajimaDiary()
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
