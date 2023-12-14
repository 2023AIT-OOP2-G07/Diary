from diaries.DiarySample import DiarySample # ↓のリストには、メンバーの各日記が格納されます。
from diaries.IwashiroDiary import IwashiroDiary # ↓のリストには、メンバーの各日記が格納されます。
diaries = [
        DiarySample(),
        IwashiroDiary(),
        ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()