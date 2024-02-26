from Mode import Mode

# Created by ksprdv

print('Режимы:')
print('1. Получить текущий timestamp')
print('2. Получить timestamp по дате')
print('3. Добавить к текущему timestamp минуты')
print('4. Добавить к текущему timestamp часы')
print('5. Добавить к текущему timestamp недели')
print()

mode = int(input('Выберите режим >> '))
if mode == 1:
    Mode.GetDefaultTimestamp()
elif mode == 2:
    Mode.GetTimestampToDate()
elif mode == 3:
    Mode.AddMinuteToTimestamp()
elif mode == 4:
    Mode.AddHourToTimestamp()
elif mode == 5:
    Mode.AddWeekToTimestamp()

