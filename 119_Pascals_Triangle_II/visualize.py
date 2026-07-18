"""
Визуализация построения строки треугольника Паскаля.
Управление: Enter — шаг, q — выход.
"""

import os
import sys

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'


def visualize(rowIndex):
    """Пошаговая визуализация построения строки."""
    
    row = [1]
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def draw_row(row, highlight=None, highlight2=None):
        """Рисует строку с подсветкой элементов."""
        print(f"  [", end="")
        for k, val in enumerate(row):
            if k > 0:
                print(", ", end="")
            if k == highlight:
                print(f"{YELLOW}{val}{RESET}", end="")
            elif k == highlight2:
                print(f"{CYAN}{val}{RESET}", end="")
            else:
                print(f"{val}", end="")
        print(f"]")
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Pascal's Triangle II: rowIndex = {rowIndex}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Треугольник Паскаля (первые ряды):")
    print(f"    0: [1]")
    print(f"    1: [1, 1]")
    print(f"    2: [1, 2, 1]")
    print(f"    3: [1, 3, 3, 1]")
    print(f"    4: [1, 4, 6, 4, 1]")
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  Начинаем с [1]. Для каждого нового ряда:")
    print(f"  1. Добавляем 1 в конец")
    print(f"  2. Обновляем середину справа налево:")
    print(f"     row[j] = row[j] + row[j-1]")
    print()
    print(f"  {YELLOW}жёлтый{RESET} — текущий j")
    print(f"  {CYAN}голубой{RESET} — row[j-1] (верхний левый)")
    print()
    wait()
    
    # Ряд 0
    step += 1
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Шаг {step}: ряд 0{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Начальный ряд:")
    draw_row(row)
    print()
    print(f"  row = [1]")
    print()
    wait()
    
    if rowIndex == 0:
        print(f"  {GREEN}Готово: {row}{RESET}\n")
        return
    
    for i in range(1, rowIndex + 1):
        step += 1
        old_row = row[:]
        
        # Добавляем 1 в конец
        row.append(1)
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: ряд {i} — добавляем правую 1{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        print(f"  Предыдущий ряд: {old_row}")
        print(f"  Добавляем 1 в конец:")
        draw_row(row, len(row) - 1)
        print()
        print(f"  row.append(1) → {row}")
        print()
        wait()
        
        # Обновляем середину справа налево
        for j in range(i - 1, 0, -1):
            step += 1
            old_val = row[j]
            left_val = row[j - 1]
            new_val = old_val + left_val
            row[j] = new_val
            
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}: ряд {i} — обновляем j={j}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            
            draw_row(row, j, j - 1)
            print()
            print(f"  j = {j}")
            print(f"  row[{j}] = row[{j}] + row[{j-1}]")
            print(f"  {old_val} + {left_val} = {YELLOW}{new_val}{RESET}")
            print(f"  row = {row}")
            print()
            wait()
    
    # Финал
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Готово!{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    print(f"  rowIndex = {rowIndex}")
    print(f"  Результат: {GREEN}{row}{RESET}")
    print()


if __name__ == "__main__":
    examples = [0, 1, 2, 3, 4]
    
    for rowIndex in examples:
        print(f"\n{CYAN}rowIndex = {rowIndex}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(rowIndex)
        print()
