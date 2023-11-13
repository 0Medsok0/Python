import telebot # для токена
from telebot import types # для кнопок

token = '--TOKEN--'
bot = telebot.TeleBot(token)


histori_pizza_facts = []


@bot.message_handler(commands=['start']) # Приветсвтвие
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👨‍🍳 Start")
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Привет! Я помогу тебе с заказом!', reply_markup=markup)

@bot.message_handler(content_types=['text']) # Основная функция после приветсвия
def get_message(message):
# На нажатие кнопки Start выводит следующие кнопки..
    if message.text == '👨‍🍳 Start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Создание новых кнопок
        btn1 = types.KeyboardButton('Меню')
        markup.add(btn1) # добавляем кнопки в бота
        bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup) #ответ бота


    elif message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('Роллы 🍣')
        btn3 = types.KeyboardButton('Салаты 🥗')
        btn4 = types.KeyboardButton('Горячие блюда 🍲')
        btn5 = types.KeyboardButton('Десерты 🍰')
        btn6 = types.KeyboardButton('Напитки 🫖')
        btn7 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup)

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup)
# тут кнопки для стека пицца
    elif message.text == 'Пицца 🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Маргарита🍕')
        btn2 = types.KeyboardButton('Четыре сезона🍕')
        btn3 = types.KeyboardButton('Корбанара🍕')
        btn4 = types.KeyboardButton('Маринара🍕')
        btn5 = types.KeyboardButton('Капричоза🍕')
        btn6 = types.KeyboardButton('Четыре сыра🍕')
        btn7 = types.KeyboardButton('Крудо🍕')
        btn8 = types.KeyboardButton('Неаполетано🍕')
        btn9 = types.KeyboardButton('По-апулийски🍕')
        btn10 = types.KeyboardButton('Монтанара🍕')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)  # добавляем кнопки в бота
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n⬇ Выберите подраздел',reply_markup=markup)            ##
# тут описание кнопок для стека пицца
    elif message.text == 'Маргарита🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%86%D1%86%D0%B0#/media/%D0%A4%D0%B0%D0%B9%D0%BB:Eq_it-na_pizza-margherita_sep2005_sml.jpg')
        bot.send_message(message.from_user.id, 'Маргарита🍕\nСостав: Тесто для пиццы 270 - 300 г\nСоус томатный 100 - 130 г\nСыр Моцарелла для пиццы 150 - 180 г\nПомидоры 1 шт.\nБазилик зелёный 8-10 листиков\nМасло оливковое')
    elif message.text == 'Четыре сезона🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор', reply_markup=markup,parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Pizza_Quattro_Stagioni.jpg/1280px-Pizza_Quattro_Stagioni.jpg')
        bot.send_message(message.from_user.id,'Четыре сезона🍕\nСостав: \n\tЗима  Начинка — \nгрибы(150гр),яйца'
                                              '\n\t Весна: Начинка — \n1 вариант: морепродукты (150 гр.) с травами. \n2 вариант без морепродуктов: 150 гр. свежих или консервированных артишоков,оливки,маслины (150 гр),\n\t Лето Начинка — \n мясная (150 -200 гр). нежирная ветчина, салями, куриная грудка, свежий перец,\n\t Осень  Начинка — \nпомидоры и Моцарелла (150 гр)/черри (10-12 шт)')
    elif message.text == 'Корбанара🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://papitospizza.ru/wa-data/public/shop/products/39/00/39/images/278/278.320@2x.jpg')
        bot.send_message(message.from_user.id, 'Корбанара🍕\nСостав: Основа для пиццы 1 шт,Моцарелла 150 Г,сыр пармезан,70 г,яйца 3 шт,бекон 125 г,томатный соус 3 ст. л.,оливковое масло 2 ст. л.')
    elif message.text == 'Маринара🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://pizzarini.info/wp-content/uploads/2018/06/0230.jpg')
        bot.send_message(message.from_user.id, 'Маринара🍕\nСостав: Тecтo для пиццы 400 г,Пoмидopы caмыe cпeлыe 4-5 шт,Чecнoк 3-4 зубчикa, oливкoвoe мacлo 3-4 cт. л.,Зeлeный бaзилик 2-3 вeтoчки,coль, opeгaнo, cуxиe тpaвы, caxap')
    elif message.text == 'Капричоза🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Pizza_capricciosa.jpg/1280px-Pizza_capricciosa.jpg')
        bot.send_message(message.from_user.id, 'Капричоза🍕\nСостав: приготовленная из сыра моцарелла, запеченной ветчины, грибов, артишоков и помидоров.')
    elif message.text == 'Четыре сыра🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Pizza_quattro_formaggi_at_restaurant%2C_Chalk_Farm_Road%2C_London.jpg/1280px-Pizza_quattro_formaggi_at_restaurant%2C_Chalk_Farm_Road%2C_London.jpg')
        bot.send_message(message.from_user.id, 'Четыре сыра🍕\nСостав: покрытая комбинацией из четырёх видов сыра, обычно расплавленных вместе, с томатным соусом (росса, красный) или без него (бьянка, белый)')
    elif message.text == 'Крудо🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.good-cook.ru/articles/2019/08/04-1-picca-crudo-kulinarnoe-issledovanie.jpg')
        bot.send_message(message.from_user.id, 'Крудо🍕\nСостав: 50 граммов сыра маскарпоне,180-200 граммов сыра моцарелла,100 граммов пармской ветчины; ложка оливкового масла.')
    elif message.text == 'Неаполетано🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.gastronom.ru/binfiles/images/20190429/bc86546a.jpg')
        bot.send_message(message.from_user.id, 'Неаполетано🍕\nСостав:  60 г маслин каламата,30 г анчоусов в масле,40 г каперсов,5–6 зубчиков чеснока,сушеный орегано,листья базилика')
    elif message.text == 'По-апулийски🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://thumb.tildacdn.com/tild3239-3034-4132-a633-623437373333/-/format/webp/P10923-1914321.jpg')
        bot.send_message(message.from_user.id, 'По-апулийски🍕\nСостав: 250 г белого репчатого лука,1 ч. л. свежего орегано,100 г тертого пекорино,4 ст. л. оливкового масла,соль, свежемолотый черный перец')
    elif message.text == 'Монтанара🍕':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Пицца 🍕')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://mac-pizza.by/wp-content/uploads/2017/04/montanara-scaled-e1581418466128.jpg')
        bot.send_message(message.from_user.id, 'Монтанара🍕\nСостав:  ветчина в/р, жареная куриная грудинка, орегано, соус карри, сыр, томатный соус, чесночное масло')
# тут кнопки для стека роллы
    elif message.text == 'Роллы 🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Томаго Суши Ролл🍣')
        btn2 = types.KeyboardButton('Цезарь суши ролл🍣')
        btn3 = types.KeyboardButton('Таки Суши Ролл🍣')
        btn4 = types.KeyboardButton('Чукка Суши Ролл🍣')
        btn5 = types.KeyboardButton('Суши Ролл Калифорния с крабом🍣')
        btn6 = types.KeyboardButton('Калифорния Хот Ролл🍣')
        btn7 = types.KeyboardButton('Америка Хот Суши Рол🍣')
        btn8 = types.KeyboardButton('Бонито Суши Ролл🍣')
        btn9 = types.KeyboardButton('Унаги Маки Суши Ролл🍣')
        btn10 = types.KeyboardButton('Мидори Хот Суши Рол🍣')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)  # добавляем кнопки в бота
        bot.send_message(message.from_user.id, 'Твой раздел: Пицца 🍕\n \n⬇ Выберите подраздел',reply_markup=markup)
# тут описание кнопок для стека роллы
    elif message.text == 'Томаго Суши Ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/tamaqo-min.jpg')
        bot.send_message(message.from_user.id, 'Томаго Суши Ролл🍣\nСостав: Рис, нори, огурец, крем сыр, японский омлет, специальный соус с икрой, куриное филе. Входит: 1 соевый соус, 1 имбирь')
    elif message.text == 'Цезарь суши ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/sezar-roll-1500x950.jpg')
        bot.send_message(message.from_user.id, 'Цезарь суши ролл🍣\nСостав: Рис, нори, куриный соус, лист салата, томаты. входит: 1 соевый соус, 1 имбирь')
    elif message.text == 'Таки Суши Ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/taki-roll.jpg')
        bot.send_message(message.from_user.id, 'Таки Суши Ролл🍣\nСостав: Рис, нори, огурец, авокадо, тобико, крем сыр, рыба унаги, копченый лосось. Входит: 1 соевый соус, 1 имбирь.')
    elif message.text == 'Чукка Суши Ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/cuka-roll-retush.jpg')
        bot.send_message(message.from_user.id, 'Чукка Суши Ролл🍣\nСостав: Рис, нори, огурец, крем сыр, водоросли чукка, ореховый соус, копченый лосось. Входит: 1 соевый соус, 1 имбирь')
    elif message.text == 'Суши Ролл Калифорния с крабом🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/california-crab-roll.jpg')
        bot.send_message(message.from_user.id, 'Суши Ролл Калифорния с крабом🍣\nСостав: Рис, нори, огурец, тобико, японский майонез, крабовые палочки. Входит: 1 соевый соус, 1 имбирь')
    elif message.text == 'Калифорния Хот Ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/roll-kaliforniya-khot.jpg')
        bot.send_message(message.from_user.id, 'Калифорния Хот Ролл🍣\nСостав: Рис, нори, крем сыр, огурцы, панировочные сухари, крабовые палочки, тобико. Входит: 1 соевый соус, 1 имбирь.')
    elif message.text == 'Америка Хот Суши Рол🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/amerika-hot-roll.jpg')
        bot.send_message(message.from_user.id, 'Америка Хот Суши Рол🍣\nСостав:  рис, индейка холодного копчения, японский омлет, огурцы, перец, панировочные сухари')
    elif message.text == 'Бонито Суши Ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/bonito-roll.jpg')
        bot.send_message(message.from_user.id, 'Бонито Суши Ролл🍣\nСостав:  Рис, нори, огурец, японский майонез, стружка тунца, семга в соусе терияки. Входит: 1 соевый соус, 1 имбирь.')
    elif message.text == 'Унаги Маки Суши Ролл🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/maki-with-smoked-eel.jpg')
        bot.send_message(message.from_user.id, 'Унаги Маки Суши Ролл🍣\nСостав:  Рис, нори, огурец, кунжут, унаги рыба. Входит: 1 соевый соус, 1 имбирь')
    elif message.text == 'Мидори Хот Суши Рол🍣':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Роллы 🍣')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Роллы 🍣\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.bakenroll.az/ru/image/midori-goryachiy-roll-s-krevetkami.jpg')
        bot.send_message(message.from_user.id, 'Мидори Хот Суши Рол🍣\nСостав:  Рис, нори, крем сыр, огурцы, панировочные сухари, креветки. Входит: 1 соевый соус, 1 имбирь')
# тут кнопки для стека салаты
    elif message.text == 'Салаты 🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Зеленый салат🥗')
        btn2 = types.KeyboardButton('Салат из цукини🥗')
        btn3 = types.KeyboardButton('Нисуаз🥗')
        btn4 = types.KeyboardButton('Салат из шампиньонов с кукурузой🥗')
        btn5 = types.KeyboardButton('Греческий🥗')
        btn6 = types.KeyboardButton('Салат с копченой горбушей🥗')
        btn7 = types.KeyboardButton('Салат из фасоли по-тоскански🥗')
        btn8 = types.KeyboardButton('Салат средиземноморский🥗')
        btn9 = types.KeyboardButton('Салат со спаржей и заправкой из маракуйи🥗')
        btn10 = types.KeyboardButton('Салат с пармской ветчиной и апельсинами🥗')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)  # добавляем кнопки в бота
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n⬇ Выберите подраздел',reply_markup=markup)
# тут описание кнопок для стека салаты
    elif message.text == 'Зеленый салат🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/the-village.ru/post_image-image/4lRCP_6jx0wg6YErjaTWQQ.png')
        bot.send_message(message.from_user.id, 'Зеленый салат🥗\nСостав:  салат романо — 30 ГР.,свежий шпинат — 30 ГР.,бок-чой (китайская листовая капуста)— 30 ГР.,цветная капуста — 60 ГР.бобы эдамаме — 20 ГР.ростки гороха — 15 ГР.трюфельное масло — 5 ГР.имбирно-чесночная заправка — 15 ГР.')
    elif message.text == 'Салат из цукини🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/the-village.ru/post_image-image/QE8o7HNgfngBgO_O6V3t9A.jpg')
        bot.send_message(message.from_user.id, 'Салат из цукини🥗\nСостав:  листья салата (романо, айсберг, латук) — 40 ГР.цукини — 100 ГР.заправка сливочный винегрет — 40 ГР.различные семена'
                                               '(кунжут, лен, тыквенные семечки) — 15 ГР.зерна граната — 20 ГР.творожный сыр — 40 ГР.заправка «сливочный винегрет»:жирные сливки — 10 ГР.яблочный уксус — 10 ГР.растительное масло — 10 ГР.красный лук — 10 ГР')
    elif message.text == 'Нисуаз🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/f5/5b/65/f55b65b1f5e121f3cba641d28a8e2b92/728x485_1_8185a6e7991c997a6fc5a1792900a375@1200x800_0xd42ee42a_8767714101435583686.jpeg')
        bot.send_message(message.from_user.id, 'Нисуаз🥗\nСостав: Тунец Блю Фин — 100 гр,микс листьев салатов — 15 гр,1 яйцо,'
                                               '1 средний картофель,зеленый лук,бобы кенийские отварные — 1/3 стакана,1 крупный сладкий помидор,'
                                               '1 столовая ложка соуса песто,таджикских оливки ,перец болгарский,соль,перец,паприка,кумин')
    elif message.text == 'Салат из шампиньонов с кукурузой🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/wp-content/uploads/b905dfd6.jpg')
        bot.send_message(message.from_user.id, 'Салат из шампиньонов с кукурузой🥗: Шампиньоны целые – 400 г,'
                                               'кукуруза сладкая – 400 г,белая сладкая луковица — 1 шт.,'
                                               'куриные яйца – 4 шт.,растительное масло – 40 мл,майонез – 2 ст.л.')
    elif message.text == 'Греческий🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/wp-content/uploads/b8dbdce8.jpg')
        bot.send_message(message.from_user.id, 'Греческий🥗\nСостав:  огурцы – 2 шт. среднего размера,красный болгарский перец – 1 шт.,'
                                               'желтый болгарский перец – 1 шт.,помидоры черри — 200 г,красная луковица – 1 шт.,фета – 220 голивки сорта каламата — 100 г,чеснок – 2,'
                                               ' зубчика,сухой орегано — 1 ч.л.,горчица,красный винный уксус,морская соль,черный перец крупного помола — 1/2 ч.л.,оливковое масло – 120 мл')
    elif message.text == 'Салат с копченой горбушей🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/wp-content/uploads/b4c768fb.jpg')
        bot.send_message(message.from_user.id, 'Салат с копченой горбушей🥗\nСостав:  филе крупной горбуши гор./копч – 1 шт.,'
                                               'очень мелкий картофель – 0,5 кг,красная луковица большая – 1 шт.,яйца куриные – 4 шт.,каперсы – 3 ст.л.,икра красная – 1 ст.л.,'
                                               'оливковое масло – 1 ст.л.,горчица – 1 ст.л.,майонез – 1 ст.л.,веточка укропа для украшения')
    elif message.text == 'Салат из фасоли по-тоскански🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/wp-content/uploads/00087042.jpg')
        bot.send_message(message.from_user.id, 'Салат из фасоли по-тоскански🥗\nСостав:  зеленая фасоль – 300 г,консервированная белая фасоль – 350 г,'
                                               'консервированный тунец в собств. соку – 300 г,помидоры черри — 200 г,'
                                               'зеленый листовой салат – 1 кочан,пучок листьев салата,красная луковица – 1 шт.красный винный уксус – 50 мл,'
                                               'консервированные каперсы — 2ст. л.,белый хлеб — 2 кусочка,чеснок – 2 зубчика')
    elif message.text == 'Салат средиземноморский🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/wp-content/uploads/bdb4f9ff.jpg')
        bot.send_message(message.from_user.id, 'Салат средиземноморский🥗\nСостав: 1 шт. зеленое яблоко,2 свежих огурца,1 ст. л. сока лимонного,1 авокадо,2 куриных яйца,200 г крабового мяса,50 г красной икры,соль,80 г майонеза,зубчик чеснока')
    elif message.text == 'Салат со спаржей и заправкой из маракуйи🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/the-village.ru/post_image-image/W7KAybgNWOql6Ei8iV_kyw.png')
        bot.send_message(message.from_user.id, 'Салат со спаржей и заправкой из маракуйи🥗\nСостав:  свежая спаржа — 20 ГР.,фенхель — 20 ГР.,редис — 20 ГР.,огурец — 30 ГР.,микс салата — 20 ГР.,микс проростков зелени (горох, щавель, кресс-салат) — 10 ГР.,'
                                               'кинза — 2 ГР.,щавель — 10 ГР.,зеленое яблоко — 20 ГР.,отварная киноа — 15 ГР.,заправка маракуйя — 20 ГР.,гуакамоле,авокадо — 1 ШТ.,сок лимона — 10 ГР.,соль — 2 ГР.,оливковое масло — 20 ГР.')
    elif message.text == 'Салат с пармской ветчиной и апельсинами🥗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Салаты 🥗')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Салаты 🥗\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://ramsaygordon.ru/images/wp-content/uploads/00061785.jpg')
        bot.send_message(message.from_user.id, 'Салат с пармской ветчиной и апельсинами🥗\nСостав:  200 г смеси из салатных листьев,150 г нарезки пармской ветчины,100 г помидоров черри,1 крупный апельсин')

# тут кнопки для стека Горячие блюда
    elif message.text == 'Горячие блюда 🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Шницель из телятины на кости🍲')
        btn2 = types.KeyboardButton('Караси, жаренные в сметане🍲')
        btn3 = types.KeyboardButton('Спагетти с мясным рагу🍲')
        btn4 = types.KeyboardButton('Хашлама по-армянски🍲')
        btn5 = types.KeyboardButton('Мидии с чоризо и томатами🍲')
        btn6 = types.KeyboardButton('Куриное бедро в орехово-горчичном маринаде🍲')
        btn7 = types.KeyboardButton('Жаровня со свининой в сливочно-грибном соусе🍲')
        btn8 = types.KeyboardButton('Мухаммара🍲')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)  # добавляем кнопки в бота
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n⬇ Выберите подраздел', reply_markup=markup)
# тут описание кнопок для стека Горячие блюда
    elif message.text == 'Шницель из телятины на кости🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/97c/800_contemporary_shnitselbb3.jpg')
        bot.send_message(message.from_user.id, 'Шницель из телятины на кости🍲: Состав:\nТелятина на кости, от 500 г,Куриное яйцо, 1 шт.,Молоко, 200 мл,Панировочные сухари 80 г,Салат кейл')
    elif message.text == 'Караси, жаренные в сметане🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/0d0/zhivago_karasi_zharennye_v_smetanec4c.jpg')
        bot.send_message(message.from_user.id, 'Караси, жаренные в сметане🍲: Состав:\n Филе карася, 180 г,Пшеничная мука, 1,5 ч. л.,Репчатый лук, 0,5 шт.,Сметана, 3 ст. л.Сливки жирные,'
                                               ' 5 ст. л.,Укроп, 2 веточки,Рыбный бульон, 3 ст. л.,растительное масло для жаркиСоль и перец по вкусу')
    elif message.text == 'Спагетти с мясным рагу🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/b1b/spagetti441.jpg')
        bot.send_message(message.from_user.id, 'Спагетти с мясным рагу🍲: Состав:\n Говяжий фарш, 350 г,Телятина, 350 г,'
                                               'Шалфей, 1 г,Тимьян, 1 г,Розмарин, 1 г,Лук репчатый, 10 г,'
                                               'Морковь, 6 г,Чеснок, 1 г,Стебель сельдерея 4 г,'
                                               'Томаты мутти,100 гПерец, 1 г,Помидоры черри, 15 г,'
                                               'Бульон куриный 15 мл,Спагетти 30 г,Пармезан, 5 гСвежий базилик, 1 г')
    elif message.text == 'Хашлама по-армянски🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/296/2669.jpg')
        bot.send_message(message.from_user.id, 'Хашлама по-армянски🍲: Состав:\n Баранина, 1кг,Перец болгарский, 3 шт.,Помидоры, 3 шт.,Лук репчатый,  1 шт.,Зелень петрушки, 50 г,Зелень укропа,'
                                               ' 50 г,Зелень красного базилика 50 г,Лавровый лист 1 шт.,Перец черный горошек,  5-6 шт.')
    elif message.text == 'Мидии с чоризо и томатами🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/8ca/molto_buono_20_midii_s_chorizo_mind6f.jpg')
        bot.send_message(message.from_user.id, 'Мидии с чоризо и томатами🍲: Состав:\n олубые мидии, 6 шт.,'
                                               'Чеснок, 2 зубчика,Лук красный, 20 г,Чоризо колбаса, 20 г,Томаты 100 г,'
                                               'Белая фасоль консервированная 30 г,Коньяк,10 мл,Тархун 10 г,'
                                               'Рыбный бульон 100 г,Багет для подачи')
    elif message.text == 'Куриное бедро в орехово-горчичном маринаде🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/aec/varenichnaya_1_kurinoe_bedro_v_orehovo_gorchichnom_marinadee5b.jpg')
        bot.send_message(message.from_user.id, 'Куриное бедро в орехово-горчичном маринаде🍲: Состав:\n Куриное бедро,'
                                               ' 800 г,Отварной картофель, 400 г,Кабачок, 4 шт.\nдля маринада:Горчица, 40 г,Зерновая горчица, 40 г,Масло оливковое, 60 г,Мед, 20 г,'
                                               'Паста арахисовая, 60 г,Соевый соус, 20 г,Паприка копченая, 4 г,Тимьян, 4 г,Чеснок, 4 г')
    elif message.text == 'Жаровня со свининой в сливочно-грибном соусе🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/900/so_svininoi_v_slivochno_gribnom_souse_395r_3_435079.jpg')
        bot.send_message(message.from_user.id, 'Жаровня со свининой в сливочно-грибном соусе🍲: Состав:\n Свинина (вырезка), 100 г,Лук репчатый, 50 г,Шампиньоны, 50 г,'
                                               'Растительное масло, 30 мл,Сливки (22 %), 130 мл,Сметана, 50 г,Картофель,150 г,Корнишоны, 15 г,Маринованные черри, 15 г,Петрушка, 3 г,Лук фри, 6 г')
    elif message.text == 'Мухаммара🍲':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Горячие блюда 🍲')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Горячие блюда 🍲\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://www.restoran.ru/upload/editor/f07/img_20190130_wa0001188.jpg')
        bot.send_message(message.from_user.id, 'Мухаммара🍲: Состав:\n Острый сушеный перец, 150 г,Кунжутная паста, 100 г,Гранатовый соус наршараб, 40 мл,Грецкий орех, 100 г,'
                                               'Сухарики, 40 г,Оливковое масло, 15 мл,Запеченный болгарский перец красный, 200 г,Лук репчатый, 20 гЗира, 5 г,Кориандр, 5 г')

# тут кнопки для стека Десерты
    elif message.text == 'Десерты 🍰':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Чизкейк из мацони🍰')
        btn2 = types.KeyboardButton('Королевская ватрушка с кокосовым сахаром🍰')
        btn3 = types.KeyboardButton('Малиново-фисташковый трайфл🍰')
        btn4 = types.KeyboardButton('Морковный кекс🍰')
        markup.add(btn1, btn2, btn3, btn4)  # добавляем кнопки в бота
        bot.send_message(message.from_user.id, 'Твой раздел: Десерты 🍰\n \n⬇ Выберите подраздел', reply_markup=markup)
# тут описание кнопок для стека Десерты
    elif message.text == 'Чизкейк из мацони🍰':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Десерты 🍰')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Десерты 🍰\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://eda.ru/img/eda/620x-/s1.eda.ru/StaticContent/Photos/110816122019/201124130122/p_O.jpg')
        bot.send_message(message.from_user.id, 'Чизкейк из мацони🍰: Состав:\n Сливки 35%-ные,Мацони'
                                               ',Желатин1,5 чайных ложек,Белый шоколад75'
                                               ' г,Яичный белок60 г,Сахар6,5 столовых ложек,Сливочное масло75, гМед75 г,Куриное яйцо3,5 штуки,Пшеничная мука9,5 столовых ложек,'
                                               'Разрыхлитель1,5 чайных ложек,Лимонная цедра,Сгущенное молоко4 столовые ложки,Вода1,5 столовых ложек')
    elif message.text == 'Королевская ватрушка с кокосовым сахаром🍰':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Десерты 🍰')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Десерты 🍰\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://eda.ru/img/eda/620x-/s1.eda.ru/StaticContent/Photos/110816122019/201124130146/p_O.jpg')
        bot.send_message(message.from_user.id, 'Королевская ватрушка с кокосовым сахаром🍰: Состав:\n Рисовая мука,450 г,Миндальная мука 20 г,Топленое масло 180 г,Кокосовый сахар 50 г,'
                                               'Лимонный сок 10 мл,Топленый творог 350 г Куриное яйцо 1 штука Сироп из топинамбура 20 мл')
    elif message.text == 'Малиново-фисташковый трайфл🍰':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Десерты 🍰')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Десерты 🍰\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://eda.ru/img/eda/620x-/s1.eda.ru/StaticContent/Photos/150618164615/201124130203/p_O.jpg')
        bot.send_message(message.from_user.id, 'Малиново-фисташковый трайфл🍰: Состав:\n Сахарная пудра0,1 г,Сыр маскарпоне50 г,'
                                               'Сливки 33%-ные50 мл,Яичный желток25 г,Вода 22 мл,Фисташки 5 г,Рисовая мука 10 г,'
                                               'Миндальная мука 10 г,Сливочное масло 10 г,Малина замороженная 30 г,Сахар 10 г,Пектин1 г')
    elif message.text == 'Морковный кекс🍰':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Десерты 🍰')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Десерты 🍰\n \n👨‍🍳 Отличный выбор',reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id, 'https://eda.ru/img/eda/620x-/s1.eda.ru/StaticContent/Photos/150618164615/201124130219/p_O.jpg')
        bot.send_message(message.from_user.id, 'Морковный кекс🍰: Состав:\n Куриное яйцо 4 штуки,Пшеничная мука 300 г,Миндальная мука 120 г,'
                                               'Разрыхлитель 14 г,Растительное масло 210 мл,Морковь 330 г,Цедра апельсина 3 штуки,Вода 75 мл,'
                                               'Мандариновый сок 90 мл,Мандарины 100 г,Лимонный сок 30 мл,Сахар 790 г,Пектин 4 г,Листья мяты4 г')
        
# тут кнопки для стека Напитки
    elif message.text == 'Напитки 🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Безалкогольные напитки🫖')
        btn2 = types.KeyboardButton('Свежевыжатый сок🫖')
        btn3 = types.KeyboardButton('Лимонад🫖')
        btn4 = types.KeyboardButton('Молочные коктейли🫖')
        btn5 = types.KeyboardButton('Кофе🫖')
        btn6 = types.KeyboardButton('Чай в чайнике🫖')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)  # добавляем кнопки в бота
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n⬇ Выберите подраздел', reply_markup=markup)
# тут описание кнопок для стека Напитки
    elif message.text == 'Безалкогольные напитки🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Напитки 🫖')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n👨‍🍳 Отличный выбор', reply_markup=markup,
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Безалкогольные напитки🫖:Жемчужина Байкала,Боржоми,Нарзан,Кока-Кола,Швепс-Тоник,Соки в ассортименте')
    elif message.text == 'Свежевыжатый сок🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Напитки 🫖')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n👨‍🍳 Отличный выбор', reply_markup=markup,
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Свежевыжатый сок🫖:Апельсиновый,Яблочный,Морковный,Яблочно-морковный')
    elif message.text == 'Лимонад🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Напитки 🫖')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n👨‍🍳 Отличный выбор', reply_markup=markup,
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Лимонад🫖:Лимонад Манго-Маракуйя,Тархун,Фиалковый лимонад,Лимонад Киви - Лайм,Лимонад Клубника - Лаванда')
    elif message.text == 'Молочные коктейли🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Напитки 🫖')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n👨‍🍳 Отличный выбор', reply_markup=markup,
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Молочные коктейли🫖:Ванильный Молочный Коктейль,'
                                               'Шоколадный Молочный Коктейль,'
                                               'Клубничный Молочный Коктейль,Безалкогольные коктейли,'
                                               'Безалкогольный Мохито,Клубничный безалкогольный Мохито')
    elif message.text == 'Кофе🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Напитки 🫖')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n👨‍🍳 Отличный выбор', reply_markup=markup,
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Кофе🫖:Ристретто,Эспрессо,Двойной эспрессо,Американо,Каппучино,Латте,'
                                               'Кофе Гляссе,Эспрессо с ванильным мороженым,Какао с маршмэллоу')
    elif message.text == 'Чай в чайнике🫖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Напитки 🫖')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Твой раздел: Напитки 🫖\n \n👨‍🍳 Отличный выбор', reply_markup=markup,
                         parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Чай в чайнике🫖: \nЧай чёрный в чайнике: Ассам,Цейлон,Чёрный байховый с чабрецом,Эрл Грей,Юньнань Пуэр'
                                               '\nЧай зелёный в чайнике: Сенча,Серебрянный жасмин,Молочный Улун'
                                               '\nЧай фруктовый в чайнике: Чай имбирно-лимонный:Имбирь, лимон, мед;'
                                               'Чай облепиховый:Облепиха, сок лимона, острый перчик чили, корица, анис;Чай '
                                               '«Пино Колада»:Гибискус, яблоко, шиповник, кусочки ананаса, аромат персика и маракуйи;'
                                               'Марокканский ЧайЧай Сенча: корица, ванильный сахар, мята;'
                                               'Чай Малина-Имбирь:Пюре малины, имбиря, лимонный сок')

bot.infinity_polling(none_stop=True, interval = 0) #обязательная для работы бота часть
