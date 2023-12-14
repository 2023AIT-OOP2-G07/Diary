from diaries.DiarySample import DiarySample
from diaries.FujitaDiary import FujitaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), FujitaDiary()]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
