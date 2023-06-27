print("""TrollSlayer 0.3 [14.5.2023] by Danil Pistoletov
github.com/DanilPistoletov""")
while 1:
    print("""Команды:
    1 - DeanonIP [0.9]
    2 - Проверка номера
    3 - Supportik Classic [1.9]
    4 - Supportik Mini [0.2]""")
    cmd = input("Что выберешь, семпай?\n")
    if cmd == "1":
        def checkports(ip):
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.09)
            try:
                connect = sock.connect((ip, i))
                print("Найден открытый порт:", i)
                sock.close()
            except:
                pass

        def coords(ip):
            try:
                for i in ip:
                    if i in "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя":
                        import socket
                        ip = socket.gethostbyname(ip)
                        break
                import geocoder
                coord = geocoder.ipinfo(ip)
                print("Координаты IP-адреса:", coord.latlng)
                print("Примерное местоположение IP:", coord.city)
            except:
                pass

        def who(ip):
            import whois
            print(whois.whois(ip))

        def who2(ip):
            try:
                for i in ip:
                    if i in "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщьыъэюя":
                        import socket
                        ip = socket.gethostbyname(ip)
                        break
            except:
                pass
            import requests
            infoList1 = requests.get("https://ipinfo.io/" + ip + "/json")
            infoList = infoList1.json()
            try:
                print("IP: ", infoList["ip"])
                print("Город: ", infoList["city"])
                print("Регион: ", infoList["region"])
                print("Страна: ", infoList["country"])
                print("Организация: ", infoList["org"])
                print("Координаты: ", infoList["loc"])
                print("Индекс: ", infoList["postal"])
                print("Часовой пояс: ", infoList["timezone"])
                print("Хост: ", infoList["hostname"])
            except:
                pass

        test = 0
        while 1:
            ip = input("Напиши мне IP либо домен и я добуду информацию :з\n")
            for i in ip:
                if i in ".":
                    test = 1
                    break
            if test == 0:
                pass
            elif test == 0:
                print("Неправильный IP/домен, не играйся со мной >:(")
                ip = "127.0.0.1"
            ports = [7, 20, 21, 22, 23, 25, 53, 69, 79, 80, 81, 88, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087,
                     2222, 3128, 3306, 5432, 8080, 8083]
            for i in ports:
                checkports(ip)
            coords(ip)
            print("Whois №1:\n")
            who(ip)
            print("Whois №2:\n")
            who2(ip)
            ip = input("Готов ли ты к следующей проверке?\n")

    if cmd == "2":
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
            try:
                import phonenumbers
                from phonenumbers import timezone, carrier, geocoder
                phone1 = phonenumbers.parse("+" + phone)
                print("Существует ли данный телефон:", phonenumbers.is_valid_number(phone1))
                print("Может ли существовать данный телефон:", phonenumbers.is_possible_number(phone1))
                print("Временная зона:", phonenumbers.timezone.time_zones_for_number(phone1))
                print("Оператор:", carrier.name_for_number(phone1, 'ru'))
                print("Страна:", geocoder.description_for_number(phone1, 'ru'))
            except:
                print("Произошла ошибка")

        phone = input("Введите номер телефона без знака +\n")
        print("Способ первый:")
        one(phone)
        print("\nСпособ второй:")
        two(phone)

    if cmd == "3":
        import socket

        def getip():
            import urllib.request
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            print(external_ip)


        def getdhcp():
            print(socket.gethostbyname(socket.gethostname()))


        def gethelp():
            print("""
            Соблюдайте регистр команд и всё будет хорошо
            help / помощь - список команд и пояснение к ним
            getip / мойайпи - получение внешнего адреса компьютера
            getdhcp / получитьdhcp - получение вашего DHCP
            getpcname / имякомпа - получение имени вашего компьютера
            getdomainip / айписайта [ДОМЕН] - получение IP сайта (без http/https)
            sitestatus / статуссайта [ДОМЕН] - проверка статуса сайта (без http/https)
            getmac / получитьмак - получить MAC-адрес
            getmacnum / получитьмакцифры- получить MAC-адрес в виде числа
            scanportsonip / проверитьпортыайпи - проверить популярные открытые порты по IP
            scanportsondomain / проверитьпортыдомен - проверить популярные открытые порты по домену (без http/https)
            rangeportsdomain / диапазонпортовдомен - проверить открытые порты по домену (без http/https)
            rangeportsip / диапазонпортовайпи - проверить открытые порты по айпи
            getcoords / моикоординаты - узнать координаты по своему IP-адресу
            coordsbyip / координатыайпи - узнать координаты по указанному IP-адресу
            citybyip / городпоайпи - узнать город по IP-адресу
            genpass / сделатьпароль - генерирует пароль (английский алфавит + цифры)
            genpassv2 / сложныйпароль - генерирует пароль (английский и русский алфавиты + цифры + символ)
            linklocation / путьссылки - узнать куда ведёт ссылка (без http/https)
            pseudocrypt / псевдошифр - шифрование русских маленьких букв
            cryptoff / шифрвыкл - дешифрование псевдошифра
            """)

        def getpcname():
            try:
                print(socket.getfqdn())
            except:
                print("Произошла ошибка")

        def getlocalip():
            try:
                host = socket.getaddrinfo(socket.gethostname(), None)
                ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
                print(ipv4_addresses)
            except:
                print("Произошла ошибка")

        def getdomainip(x):
            try:
                print(socket.gethostbyname(x))
            except:
                print("Произошла ошибка")

        def sitestatus(x):
            import requests
            import urllib.request
            from urllib.error import URLError
            try:
                urllib.request.urlopen("https://" + x)
                print("Сайт доступен")
                status = requests.get('https://' + x)
                print("Код сайта: ", status.status_code)
            except URLError:
                print("Сайт недоступен")

        def getmac():
            from uuid import getnode
            import re
            print(':'.join(re.findall('..', '%012x' % getnode())))

        def getmacnum():
            from uuid import getnode
            print(getnode())

        def scanports(ip):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.09)
            try:
                connect = sock.connect((ip, i))
                print("Порт ", i, " открыт")
                sock.close()
            except:
                print("Произошла ошибка")


        def genpass():
            import random
            variable = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
            length = int(input("Введите длину пароля\n"))
            password = ""
            for i in range(length):
                password += random.choice(variable)
            print(password)

        def genpassv2():
            import random
            variable = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*/~"
            length = int(input("Введите длину пароля\n"))
            password = ""
            for i in range(length):
                password += random.choice(variable)
            print(password)

        def scanportsv2(ip):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.09)
            try:
                connect = sock.connect((ip, i))
                print("Порт ", i, " открыт")
                sock.close()
            except:
                print("Произошла ошибка")

        def linklocation(link):
            import requests
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
            r = requests.get(link, headers=headers)
            for i, each in enumerate(r.history, 1):
                print(f'{i} {each.status_code} {each.url}')

        def pseudocrypt(str):
            text = str
            text = text.replace("а", "0")
            text = text.replace("б", "9")
            text = text.replace("в", "8")
            text = text.replace("г", "7")
            text = text.replace("д", "6")
            text = text.replace("е", "5")
            text = text.replace("ё", "4")
            text = text.replace("ж", "3")
            text = text.replace("з", "2")
            text = text.replace("и", "1")
            text = text.replace("й", "!")
            text = text.replace("к", "@")
            text = text.replace("л", "#")
            text = text.replace("м", "$")
            text = text.replace("н", "%")
            text = text.replace("о", "^")
            text = text.replace("п", "&")
            text = text.replace("р", "*")
            text = text.replace("с", "(")
            text = text.replace("т", ")")
            text = text.replace("у", "-")
            text = text.replace("ф", "_")
            text = text.replace("х", "+")
            text = text.replace("ц", "=")
            text = text.replace("ч", "№")
            text = text.replace("ш", ";")
            text = text.replace("щ", ":")
            text = text.replace("ь", "?")
            text = text.replace("ы", "~")
            text = text.replace("ъ", "`")
            text = text.replace("э", "<")
            text = text.replace("ю", ">")
            text = text.replace("я", ",")
            print(text)

        def pseudocryptoff(str):
            text = str
            text = text.replace("0", "а")
            text = text.replace("9", "б")
            text = text.replace("8", "в")
            text = text.replace("7", "г")
            text = text.replace("6", "д")
            text = text.replace("5", "е")
            text = text.replace("4", "ё")
            text = text.replace("3", "ж")
            text = text.replace("2", "з")
            text = text.replace("1", "и")
            text = text.replace("!", "й")
            text = text.replace("@", "к")
            text = text.replace("#", "л")
            text = text.replace("$", "м")
            text = text.replace("%", "н")
            text = text.replace("^", "о")
            text = text.replace("&", "п")
            text = text.replace("*", "р")
            text = text.replace("(", "с")
            text = text.replace(")", "т")
            text = text.replace("-", "у")
            text = text.replace("_", "ф")
            text = text.replace("+", "х")
            text = text.replace("=", "ц")
            text = text.replace("№", "ч")
            text = text.replace(";", "ш")
            text = text.replace(":", "щ")
            text = text.replace("?", "ь")
            text = text.replace("~", "ы")
            text = text.replace("`", "ъ")
            text = text.replace("<", "э")
            text = text.replace(">", "ю")
            text = text.replace(",", "я")
            print(text)

        while 1:
            command = input()
            if command == "getip" or command == "мойайпи":
                getip()
            elif command == "getdhcp" or command == "получитьdhcp":
                getdhcp()
            elif command == "help" or command == "помощь":
                gethelp()
            elif command == "getpcname" or command == "имякомпа":
                print(socket.getfqdn())
            elif command == "getlocalip":
                getlocalip()
            elif "getdomainip" in command:
                domain = command[12:]
                getdomainip(domain)
            elif "айписайта" in command:
                domain1 = command[10:]
                getdomainip(domain1)
            elif "sitestatus" in command:
                siteforcheck = command[11:]
                sitestatus(siteforcheck)
            elif "статуссайта" in command:
                siteforcheck1 = command[12:]
                sitestatus(siteforcheck1)
            elif command == "getmac" or command == "получитьмак":
                getmac()
            elif command == "getmacnum" or command == "получитьмакцифры":
                getmacnum()
            elif "rangeportsip" in command:
                na4alo = int(input("Введите начальный порт\n"))
                predel = int(input("Введите последний порт\n"))
                for i in range(na4alo, predel):
                    scanports(command[13:])
            elif "диапазонпортовайпи" in command:
                na4alo1 = int(input("Введите начальный порт\n"))
                predel1 = int(input("Введите последний порт\n"))
                for i in range(na4alo1, predel1):
                    scanports(command[19:])
            elif "rangeportsdomain" in command:
                na4alo2 = int(input("Введите начальный порт\n"))
                predel2 = int(input("Введите последний порт\n"))
                for i in range(na4alo2, predel2):
                    scanports(socket.gethostbyname(command[17:]))
            elif "диапазонпортовдомен" in command:
                na4alo3 = int(input("Введите начальный порт\n"))
                predel3 = int(input("Введите последний порт\n"))
                for i in range(na4alo3, predel3):
                    scanports(socket.gethostbyname(command[20:]))
            elif "проверитьпортыдомен" in command:
                ports = [7, 20, 21, 22, 23, 25, 53, 69, 79, 80, 81, 88, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222,
                         3128, 3306, 5432, 8080, 8083]
                for i in ports:
                    scanportsv2(socket.gethostbyname(command[20:]))
            elif "scanportsondomain" in command:
                ports = [7, 20, 21, 22, 23, 25, 53, 69, 79, 80, 81, 88, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222,
                         3128, 3306, 5432, 8080, 8083]
                for i in ports:
                    scanportsv2(socket.gethostbyname(command[19:]))
            elif "проверитьпортыайпи" in command:
                ports = [7, 20, 21, 22, 23, 25, 53, 69, 79, 80, 81, 88, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222,
                         3128, 3306, 5432, 8080, 8083]
                for i in ports:
                    scanportsv2(command[19:])
            elif "scanportsonip" in command:
                ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 79, 81, 88, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222,
                         3128, 3306, 5432, 8080, 8083]
                for i in ports:
                    scanportsv2(command[14:])
            elif command == "genpass" or command == "сделатьпароль":
                genpass()
            elif command == "getcoords" or command == "моикоординаты":
                import geocoder
                g = geocoder.ipinfo("me")
                print(g.latlng)
            elif "coordsbyip" in command:
                import geocoder
                g1 = geocoder.ipinfo(command[11:])
                print(g1.latlng)
            elif "координатыайпи" in command:
                import geocoder
                g2 = geocoder.ipinfo(command[15:])
                print(g2.latlng)
            elif "citybyip" in command:
                import geocoder
                g3 = geocoder.ipinfo(command[9:])
                print(g3.city)
            elif "городпоайпи" in command:
                import geocoder
                g4 = geocoder.ipinfo(command[12:])
                print(g4.city)
            elif command == "genpassv2" or command == "сложныйпароль":
                genpassv2()
            elif "linklocation" in command:
                linklocation("https://" + command[13:])
            elif "путьссылки" in command:
                linklocation("https://" + command[11:])
            elif "pseudocrypt" in command:
                pseudocrypt(command[12:])
            elif "псевдошифр" in command:
                pseudocrypt(command[11:])
            elif "cryptoff" in command:
                pseudocryptoff(command[9:])
            elif "шифрвыкл" in command:
                pseudocryptoff(command[9:])
            else:
                print("Неверная команда. Вы можете ввести \"помощь\" для просмотра всех команд")
    elif cmd == "4":
        def ip():
            import urllib.request
            external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            print(external_ip)


        def dhcp():
            print(socket.gethostbyname(socket.gethostname()))

        def pcname():
            try:
                print(socket.getfqdn())
            except:
                print("Произошла ошибка")

        def mac():
            from uuid import getnode
            import re
            print(':'.join(re.findall('..', '%012x' % getnode())))

        def macnum():
            from uuid import getnode
            print(getnode())

        print("""Команды:
        pcname - имя компьютера
        ip - получение IP
        dhcp - получение DHCP
        mac - получение MAC-адреса
        macnum - получение MAC-адреса в цифрах
        """)
        cmd = input("Что выберешь?")
        if cmd == "pcname":
            pcname()
        elif cmd == "ip":
            ip()
        elif cmd == "dhcp":
            dhcp()
        elif cmd == "mac":
            mac()
        elif cmd == "macnum":
            macnum()
    else:
        print("Не понимаю тебя, семпай :с")