def one(phone):
    import requests
    try:
        infoPhone1 = requests.get("https://htmlweb.ru/geo/api.php?json&telcod=" + phone)
        infoPhone = infoPhone1.json()
        print("Номер:", "+" + phone)
        print("Страна:", infoPhone["country"]["name"])
        print("Регион:", infoPhone["region"]["name"])
        print("Округ:", infoPhone["region"]["okrug"])
        print("Оператор:", infoPhone["0"]["oper"])
        print("Часть света:", infoPhone["country"]["location"])
    except:
        print("Произошла ошибка")

def two(phone):
    import phonenumbers
    from phonenumbers import timezone, carrier, geocoder
    phone1 = phonenumbers.parse("+" + phone)
    print("Существует ли данный телефон:", phonenumbers.is_valid_number(phone1))
    print("Может ли существовать данный телефон:", phonenumbers.is_possible_number(phone1))
    print("Временная зона:", phonenumbers.timezone.time_zones_for_number(phone1))
    print("Оператор:", carrier.name_for_number(phone1, 'ru'))
    print("Страна:", geocoder.description_for_number(phone1, 'ru'))

phone = input("Введите номер телефона без знака +\n")
print("Способ первый:")
one(phone)
print("\nСпособ второй:")
two(phone)