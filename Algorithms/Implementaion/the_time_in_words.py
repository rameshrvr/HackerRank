
hours = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty'
}

minute_arr = [15, 30, 45]
minute_hash = {15: 'quarter', 30: 'half', 45: 'quarter'}


def get_time_in_words(hour, minute):
    result = ''
    if minute == 0:
        return "{} o' clock".format(hours[hour])
    if minute in minute_arr:
        minute_str = minute_hash[minute]
    else:
        if minute == 1:
            minute_str = 'one minute'
        elif 30 < minute:
            minute_str = '{} minutes'.format(
                convert_number_to_words(60 - minute)
            )
        else:
            minute_str = '{} minutes'.format(
                convert_number_to_words(minute)
            )
    if 1 <= minute <= 30:
        result = '{0} {1} {2}'.format(
            minute_str, 'past', hours[hour]
        )
    else:
        result = '{0} {1} {2}'.format(
            minute_str, 'to', hours[hour + 1]
        )
    return result


def convert_number_to_words(number):
    if number < 20:
        return hours[number]
    else:
        return hours[number / 10 * 10] + ' ' + hours[number % 10]


input_hour = int(raw_input())
input_minute = int(raw_input())

print get_time_in_words(
    hour=input_hour, minute=input_minute
)
