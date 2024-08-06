# Переводчик 
from translate import Translator


def translate_text():
    """ Переводит текст введеный пользователем """
    url = 'https://snipp.ru/handbk/iso-639-1'
    print('На данный момент переводчик работает на 145 языках')
    text = input('Введите слово: ')

    lang = [
        'aa','ab','af','am','an','ar','as','ay','az','ba','be',
         'bg','bh','bi','bn','bo','br','ca','co','cs','cy','da',
         'de','dz','el','en','eo','es','et','eu','fa','fi','fj',
         'fo','fr','fy','ga','gd','gl','gn','gu','gv','ha','he',
         'hi','hr','ht','hu','hy','ia','id','ie','ii','ik','io',
         'is','it','iu','ja','jv','ka','kk','kl','km','kn','ko',
         'ks','ku','ky','la','li','ln','lo','lt','lv','mg','mi',
         'mk','ml','mn','mo','mr','ms','mt','my','na','ne','nl',
         'no','oc','om','or' ,'pa','pl','ps','pt','qu','rm',"rn",
         'ro','ru','rw','sa',"sd","sg",'sh','si','sk','sl','sm',
         'sn','so','sq','sr','ss','st','su','sv', 'sw','ta','te',
         'tg','th','ti','tk','tl','tn','to','tr','ts','tt','tw',
         'ug','uk','ur','uz','vi','vo','wa','wo','xh','yi','yo',
         'zh','zh','zu'
         ]

    question = input("На какой язык хотите перевети? ")
    if question not in lang:
        print(f"Чтобы правильно ввести язык ознакомьтесь с кодами языков : {url}")

    lang = question
    translator= Translator(to_lang='')
    translation = translator.translate("This is a pen.")
    if question not in lang:
        print("Попробуйте выбрать язык еще раз")
    else:
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        print(translation)

translate_text()


"""
aa	Афарский
ab	Абхазский
af	Африкаанс
am	Амхарский
an	Арагонский
ar	Арабский

as	Ассамский
ay	Аймарский
az	Азербайджанский
ba	Башкирский
be	Белорусский
bg	Болгарский

bh	Бихарский
bi	Бислама
bn	Бенгальский
bo	Тибетский
br	Бретонский
ca	Каталонский

co	Корсиканский
cs	Чешский
cy	Валлийский (Уэльский)
da	Датский
de	Немецкий
dz	Бхутани
el	Греческий
en	Английский
eo	Эсперанто
es	Испанский
et	Эстонский
eu	Баскский
fa	Фарси
fi	Финский
fj	Фиджи
fo	Фарерский
fr	Французский
fy	Фризский
ga	Ирландский
gd	Гэльский (Шотландский )
gl	Галисийский
gn	Гуарани
gu	Гуджарати
gv	Гэльский (язык жителей острова Мэн)
ha	Хауса
he, iw	Еврейский
hi	Хинди
hr	Хорватский
ht	Гаитянский Креольский
hu	Венгерский
hy	Армянский
ia	Интерлингва
id, in	Индонезийский
ie	Интерлингва
ii	Сычуань И
ik	Инупиак
io	Идо
is	Исландский
it	Итальянский
iu	Инуктитут
ja	Японский
jv	Яванский
ka	Грузинский
kk	Казахский
kl	Гренландский
km	Камбоджийский
kn	Каннада
ko	Корейский
ks	Кашмирский (Кашмири)
ku	Курдский
ky	Киргизский
la	Латинский
li	Лимбургский (Лимбургер)
ln	Лингала
lo	Лаосский
lt	Литовский
lv	Латвийский (Латышский )
mg	Малагасийский
mi	Маорийский
mk	Македонский
ml	Малаялам
mn	Монгольский
mo	Молдавский
mr	Маратхский
ms	Малайский
mt	Мальтийский
my	Бирманский
na	Науруанский
ne	Непальский
nl	Нидерландский
no	Норвежский
oc	Окситанский
om	Оромо (Афан, Галла)
or	Ория
pa	Пенджабский (Панджабский)
pl	Польский
ps	Пушту (Пушто)
pt	Португальский
qu	Кечуа
rm	Ретороманский
rn	Кирунди (Рунди)
ro	Румынский
ru	Русский
rw	Киняруанда (Руанда)
sa	Санскритский
sd	Синдхи
sg	Сангро
sh	Сербо-Хорватский
si	Сингальский (Сингалезский)
sk	Словацкий
sl	Словенский
sm	Самоанский
sn	Шона
so	Сомалийский
sq	Албанский
sr	Сербский
ss	Свати
st	Северный сото
su	Сунданский
sv	Шведский
sw	Суахили
ta	Тамильский
te	Телугу
tg	Таджикский
th	Тайский
ti	Тигринья
tk	Туркменский
tl	Тагальский
tn	Тсвана (Сетсвана)
to	Тонга (Тонганский)
tr	Турецкий
ts	Тсонга
tt	Татарский
tw	Чви (Тви)
ug	Уйгурский
uk	Украинский
ur	Урду
uz	Узбекский
vi	Вьетнамский
vo	Волапюк
wa	Валлон
wo	Волоф
xh	Коса
yi, ji	Идиш
yo	Йоруба
zh	Китайский (Упрощенный)
zh	Китайский (Традиционный)
zu	Зулусский
"""