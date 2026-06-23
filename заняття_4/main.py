import matplotlib.pyplot as plt

months = ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер']
sales = [120, 150, 180, 130, 200, 170]

plt.figure(figsize=(8, 5))

plt.bar(months, sales)

plt.title('Продажі по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Продажі')

plt.show()