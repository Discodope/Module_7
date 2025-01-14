team1_num = 5

team2_num = 6

score_1 = 40

score_2 = 42

team1_time = 1552.512

team2_time = 2153.31451

tasks_total = 82

time_avg = 45.2

challenge_result = []

print(" В команде Мастера кода участников: 5 ! ")
print(" Итого сегодня в командах участников: 5 и 6 !")

# format()

print(" Команда Волшебники данных решила задач: {} !".format(score_2))
print(" Волшебники данных решили задачи за {} с !".format(team1_time))

# f

print(f" Команды решили {score_1} и {score_2} задач.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = ["Результат битвы: победа команды Мастера кода!"]
    print(challenge_result)

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = ["Результат битвы: победа команды Волшебники Данных!"]
    print(challenge_result)

else:
    print(" Ничья! ")
