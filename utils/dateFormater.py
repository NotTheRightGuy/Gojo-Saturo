from datetime import datetime


def dateFormater(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day = date_obj.strftime('%d')
    suffix = 'th' if 11 <= int(day) <= 13 else {
        1: 'st', 2: 'nd', 3: 'rd'}.get(int(day) % 10, 'th')
    month = date_obj.strftime('%B')
    year = date_obj.strftime('%Y')
    formatted_date = f"{day}{suffix} {month} {year}"
    return formatted_date
