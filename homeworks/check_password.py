# 1. Создатб функцию для проверки пароля
# 2. Пароль должен быть минимум 8 символов
# 3. Пароль состоит из: букв верх. регистра, букв ниж. регистра, цифры, спец. символы
# 4. Пароль должен быть введен через терминал


import re

def check_password(password):
    len_pattern = re.compile(r'\S{8,}')
    spec_symb_pattern = re.compile(r'^.*[!@#$%^&*]+.*$')    
    num_pattern = re.compile(r'^.*[0-9]+.*$')
    upper_pattern = re.compile(r'^.*[A-Z]+.*$')
    lower_pattern = re.compile(r'^.*[a-z]+.*$')

    if not re.fullmatch(len_pattern, password):
        return (False, print('Password must have minimum eight characters'))
    if not re.fullmatch(spec_symb_pattern, password):
        return (False, print('Password must have at least one special charcters'))
    if not re.fullmatch(num_pattern, password):
        return (False, print('Password must have at least one number'))
    if not re.fullmatch(upper_pattern, password):
        return (False, print('Password must have at least one upper case letter'))
    if not re.fullmatch(lower_pattern, password):
        return (False, print('Password must have at least one lower case letter'))
    
    return (True, print('Your password was accept'))
    
check_password(input('Enter your password: '))

    

    