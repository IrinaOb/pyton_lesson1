# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и строки и
# сохраните в переменные, затем выведите на экран
name = input('Как тебя зовут? ')
print('Привет,', name)
age = int(input('Сколько тебе лет? '))
ave_life = 71
rest = ave_life-age
print(f'По статистике, {name} ,тебе осталось жить', rest)
play = input('Хочешь поиграть? ')
if play=='да':
    print('Здорово! Начнем с загадок')
    riddle1 = input('На раскрашенных страницах Много праздников хранится? ')
    if riddle1=='календарь':
        print('так держать! Веселео поиграли')
    else: print('Подумай еще')
elif play=='нет':
    print('Жаль( Пока')
# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк
user_time_sec = int(input('Введите время в секундах, '))
hours = user_time_sec // 3680
minutes = user_time_sec % 3680 // 60
seconds = user_time_sec % 3680 % 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
n = int(input('Введите число '))
nn = n*n
nnn = n*n*n
result = n + nn + nnn
print(f'{n} + {nn} + {nnn} =', result)
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.
value = (input('Введите целое положительное число '))
length = len(value)
max_element = 0
i = 0
while i < length:
    current_element = int(value[i])
    if current_element > max_element:
        max_element = current_element
    i += 1
print(max_element)

value = int(input('Введите целое положительное число '))
max_element = 0
while value != 0:
    last_element = value % 10
    value = value//10
    if last_element > max_element:
        max_element = last_element
print(max_element)

value = (input('Введите целое положительное число '))
value = list(value)
print(max(value))

# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input('Введите значение выручки '))
costs = int(input('Введите издержки фирмы '))
if revenue > costs:
    print('Фирма работает с прибылью')
else:
    print('Фирма работает в убыток')
if revenue > costs:
    profit = (revenue - costs)
    cost_effect = (profit/revenue)*100
    print(f'Рентабельность фирмы составляет, {cost_effect} %')
    empl_count = int(input('Сколько сотрудников работает в фирме? '))
    profit_empl = profit/empl_count
    print('прибыль фирмы в расчете на одного сотрудника', profit_empl)
#
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
# увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число
# — номер дня.
a = int(input('В первый день спортсмен пробежал км '))
b = int(input('Желаемый результат в км '))

days = 1
while a < b:
    a *= 1.1
    days += 1
print(f'Спортсмен достигнет результата в {b} км за {days} дней')