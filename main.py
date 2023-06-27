from datetime import datetime, timedelta


def get_period(next_week_start:bool) -> dict[int,datetime]:
    next_days = []
    curent_date = datetime.now()
    
    if next_week_start:
        # we will use next day for begining of list (start_period + 1 day), that's why use 4 
        start_period = curent_date + timedelta(days=4-curent_date.weekday())
    else:
        # we will use tomorrow for begining of list (curent_date + 1 day)
        start_period = curent_date

    count = 1

    while count <= 7:
        start_period += timedelta(1)
        next_days.append((start_period.weekday(), start_period))
        count += 1

    return dict(next_days)


def get_datetime_date(date: datetime|str) -> datetime:
    if isinstance(date, str):
        if date.find("-") == 4:
            return datetime.strptime(date, "%Y-%m-%d")
        elif date.find("-") == 2:
            return datetime.strptime(date, "%d-%m-%Y")
        elif date.find(".") == 4:
            return datetime.strptime(date, "%Y.%m.%d")
        elif date.find(".") == 2:
            return datetime.strptime(date, "%d.%m.%Y")
        elif date.find("/") == 4:
            return datetime.strptime(date, "%Y/%m/%d")
        elif date.find("/") == 2:
            return datetime.strptime(date, "%d/%m/%Y")
        else:
            return datetime(1, 1, 1)
    else:
        return date
    

def get_birthdays_per_week(users: list[dict[str,datetime|str]], next_week_start:bool=False) -> None:
    weekdays = get_period(next_week_start)
    
    moove_users_lst = []
    
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
        
        if weekday_int == 0:
            users_lst.extend(moove_users_lst)
        
        if len(users_lst):
            weekday_str = weekday_datetime.strftime("%A")
            users_str = ", ".join(users_lst)
            print(f"{weekday_str}: {users_str}")



if __name__ == "__main__":
    # test dict
    users = [{"name": "Oleksii Hladkov", "birthday": datetime(1989, 12, 11)},
            {"name": "Luke Skywalker", "birthday": datetime(1977, 6, 29)},
            {"name": "Leia Organa", "birthday": datetime(1977, 6, 29)},
            {"name": "Han Solo", "birthday": datetime(1977, 6, 30)},
            {"name": "Chewbacca", "birthday": "1977-7-1"},
            {"name": "Wilhuff Tarkin", "birthday": datetime(1977, 7, 2)},
            {"name": "Grido", "birthday": "1977-7-3"},
            {"name": "Obi-Wan Kenobi", "birthday": "1977-7-4"},
            {"name": "Darth Vader", "birthday": "1977-7-5"},
            {"name": "R2-D2", "birthday": "1977-7-5"}]
    
    # week type switcher
    next_week_start = False
    # next_week_start = True
    
    get_birthdays_per_week(users, next_week_start)