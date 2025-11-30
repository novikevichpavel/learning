
# 1. Создать словарь, используя ключи со значениями разных типов
# 2. Конвертировать словарь в JSON
# 3. Результирующий JSON вывести в терминал
# 4. Вывести в терминал тип результируещего значения

import json

test_dict = {
    "id": 1234,
    "name": "Anthony",
    "surname": "Soprano",
    "age": 34,
    "role": {
        "family": "Soprano",
        "isDon": True
    }
}

dict_to_json = json.dumps(test_dict, indent=1)

print(dict_to_json)
print(type(dict_to_json))
