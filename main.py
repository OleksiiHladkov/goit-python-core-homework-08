from datetime import datetime, timedelta


def get_next_seven_days() -> dict[int,datetime]:
    next_days = []
    current_date = datetime.now()

    count = 1

    while count <= 7:
        current_date = current_date + timedelta(1)
        next_days.append((current_date.weekday(), current_date))
        count += 1

    return dict(next_days)

def get_datetime_date(date: datetime|str) -> datetime:
    if isinstance(date, str):
        args = date.split("-")
        year = int(args[0])
        month = int(args[1])
        day = int(args[2])
        return datetime(year, month, day)
    else:
        return date

def get_birthdays_per_week(users: list[dict[str,datetime|str]]) -> None:
    weekdays = get_next_seven_days()
    
    moove_users_lst = []
    is_already_moove = False
    
    for weekday_int, weekday_datetime in weekdays.items():
        users_lst = []
        
        for user_data in users:
            user_name = user_data.get("name")
            user_birthday = get_datetime_date(user_data.get("birthday"))
            
            if user_birthday.month == weekday_datetime.month and user_birthday.day == weekday_datetime.day:
                if weekday_int in (5, 6):
                    moove_users_lst.append(user_name)
                else:
                    users_lst.append(user_name)
            elif weekday_int == 0 and not is_already_moove:
                is_already_moove = True
                users_lst.extend(moove_users_lst)
        
        if len(users_lst):
            weekday_str = weekday_datetime.strftime("%A")
            users_str = ", ".join(users_lst)
            print(f"{weekday_str}: {users_str}")



if __name__ == "__main__":
    users = [{"name": "Oleksii Hladkov", "birthday": datetime(1989, 12, 11)},
            {"name": "Luke Skywalker", "birthday": datetime(1977, 6, 28)},
            {"name": "Leia Organa", "birthday": datetime(1977, 6, 28)},
            {"name": "Han Solo", "birthday": datetime(1977, 6, 29)},
            {"name": "Chewbacca", "birthday": "1977-6-30"},
            {"name": "Wilhuff Tarkin", "birthday": datetime(1977, 7, 1)}]
    
    get_birthdays_per_week(users)