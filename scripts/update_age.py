from datetime import datetime, timezone, timedelta
import re

BIRTH = datetime(2003, 6, 30, 23, 59, tzinfo=timezone(timedelta(hours=-6)))

def calculate_age(birth, now):
    years = now.year - birth.year
    months = now.month - birth.month
    days = now.day - birth.day

    if days < 0:
        months -= 1
        prev_month = now.month - 1 if now.month > 1 else 12
        prev_year = now.year if now.month > 1 else now.year - 1
        days_in_prev = (datetime(prev_year, prev_month % 12 + 1, 1) - timedelta(days=1)).day
        days += days_in_prev

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

now = datetime.now(timezone(timedelta(hours=-6)))
years, months, days = calculate_age(BIRTH, now)
age_str = f"{years} years, {months} months, {days} days"

print(f"Age calculated: {age_str}")

with open("dark_mode.svg", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r'(id="tspan114"[^>]*>)([^<]+)',
    rf'\g<1>{age_str}',
    content
)

with open("dark_mode.svg", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SVG updated successfully!")
