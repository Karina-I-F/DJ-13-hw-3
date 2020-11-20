from django import template
from datetime import datetime
import time

register = template.Library()


@register.filter
def format_date(value):
    dt_now = int(datetime.now().timestamp())
    dt_post = (dt_now - value)
    if dt_post < (60 * 10):
        return 'только что'
    elif (60 * 10) <= dt_post < (60 * 60):
        minutes = int(dt_post // 60)
        return f'{minutes} назад'
    elif (60 * 60) <= dt_post < (60 * 60 * 24):
        hours = int(dt_post // (60 * 60))
        if hours == 1 or hours == 21:
            return f'{hours} час назад'
        elif 2 <= hours <= 4 or 22 <= hours <= 23:
            return f'{hours} часа назад'
        else:
            return f'{hours} часов назад'
    else:
        return time.ctime(value)


# необходимо добавить фильтр для поля `score`
@register.filter
def score(value, arg):
    if value < -5:
        return 'плохой'
    elif -5 <= value <= 5:
        return 'нейтральный'
    elif value > 5:
        return 'огонь'


@register.filter
def format_num_comments(value):
    if 0 < value <= 50:
        return value
    elif value > 50:
        return '50+'
    else:
        return 'оставьте комментарий'
