import datetime

price = {
    'общий_60':2000,
    'общий_90':3000,
    'спина':1300,

    'детский_7_10': 1000,
    'детский_11_14': 1400,
    'мфц': 1600,

    'лимфодренажный': 2200,
    'антицилюлитный': 2400,
    'массаж_рук': 1000,

    'массаж_ног': 1000,
    'швз': 1000,
    'массаж головы': 800,
}

today = datetime.date.today() # текущий день
day_next = datetime.date.today() + datetime.timedelta(days=1) # Получаем следующий день


current_month = today.month
current_year = today.year
days_in_month = 31
if current_month == 2:
    days_in_month = 28
elif current_month in [4, 6, 9, 11]:
    days_in_month = 30

list_income = [] 


for day in range(1, days_in_month + 1):
    date = datetime.date(current_year, current_month, day)
    types_of_massage = int(input('Введите кол-во клиетов: '))
    daily_income = 0
    for i in range(types_of_massage):
        massage_type = input('Введите вид массажа: ')
        massage_price = price.get(massage_type)
        if massage_price: 
            daily_income += massage_price * 33 / 100        
        else:
            print(f'Неизвестный вид массажа: {massage_type}')

    print("Ваш дневной зароботок", daily_income, "за", date)
    list_income.append(daily_income)
    
    
monthly_income = 0
monthly_income = sum(list_income)

print("Ваш месячный зароботок", monthly_income, "рублей за", current_month, "месяц")
