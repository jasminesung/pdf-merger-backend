import flask

def convert_temp(request):
    base = request.args.get('base')
    temp = float(request.args.get('temp'))
    if base == 'celsius':
        result = temp * 9/5 + 32
    elif base == 'fahrenheit':
        result = (temp - 32) * 5/9
    return str(round(result, 2))
    