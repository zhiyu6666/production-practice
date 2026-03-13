# -*- coding: utf-8 -*-
"""
Программа для расчета выполнения сменного задания
и записи результатов в файл.
"""

def main():
    print("=== Расчет выполнения сменного задания ===")
    # Ввод данных
    product = input("Введите название продукта: ")
    plan = float(input("Введите плановое задание (тонн): "))
    fact = float(input("Введите фактически произведено (тонн): "))
    
    # Расчет процента выполнения
    percent = (fact / plan) * 100 if plan != 0 else 0
    result = "выполнен" if fact >= plan else "не выполнен"
    
    # Вывод на экран
    print(f"\nПродукт: {product}")
    print(f"План: {plan} т, Факт: {fact} т")
    print(f"Выполнение: {percent:.1f}%")
    print(f"План {result}!")
    
    # Запись в файл
    with open("shift_results.txt", "a", encoding="utf-8") as f:
        f.write(f"{product}\t{plan}\t{fact}\t{percent:.1f}\t{result}\n")
    
    print("\nРезультат сохранен в файл shift_results.txt")

if __name__ == "__main__":
    main()