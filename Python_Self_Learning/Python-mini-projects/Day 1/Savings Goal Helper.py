# Savings Goal Helper

import math, datetime as dt

Current_save= float(input("Please enter your current savings amount:"))
Target_save = float(input("Please enter your target savings amount:"))
Monthly_save = float(input("please enter your monthly savings amount:"))

Months = math.ceil(max(0,Target_save - Current_save)/Monthly_save)
Estimated_days = Months*30
today = dt.date.today()
est_date = today + dt.timedelta(days=Estimated_days)

print(f"You will reach your goal in {Months} months, around {est_date}")
