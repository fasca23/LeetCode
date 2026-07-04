"""
Визуализация поиска квадратного корня бинарным поиском.
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


def visualize(x):
    """Пошаговая визуализация бинарного поиска sqrt."""
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Sqrt({x}){RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Ищем наибольшее целое число, чей квадрат ≤ {x}.")
    print(f"  Метод: бинарный поиск в диапазоне [0, {x}].")
    print()
    
    if x < 2:
        print(f"  {GREEN}Особый случай: x < 2 → ответ = {x}{RESET}\n")
        return
    
    left, right = 1, x
    step = 0
    
    wait()
    
    while left <= right:
        step += 1
        mid = (left + right) // 2
        square = mid * mid
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        # Диапазон
        print(f"  Диапазон: [{left}, {right}]")
        print(f"  mid = ({left} + {right}) // 2 = {YELLOW}{mid}{RESET}")
        print()
        
        # Сравнение квадратов
        print(f"  {mid}² = {square}")
        print(f"  {square} vs {x}: ", end="")
        
        if square == x:
            print(f"{GREEN}равно!{RESET}")
            print(f"  {GREEN}Ответ: {mid}{RESET}")
            print()
            return
        
        elif square < x:
            print(f"{YELLOW}{square} < {x} → ищем справа{RESET}")
            print(f"  left = mid + 1 = {mid} + 1 = {mid + 1}")
            left = mid + 1
        
        else:
            print(f"{RED}{square} > {x} → ищем слева{RESET}")
            print(f"  right = mid - 1 = {mid} - 1 = {mid - 1}")
            right = mid - 1
        
        print()
        print(f"  Новый диапазон: [{left}, {right}]")
        print()
        wait()
    
    # Цикл закончился — left > right
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  Диапазон: [{left}, {right}] — left > right, поиск окончен")
    print(f"  right = {right} — последнее число с квадратом ≤ {x}")
    print(f"  {right}² = {right * right} ≤ {x}")
    if (right + 1) * (right + 1) <= x:
        print(f"  {(right + 1)}² = {(right + 1) * (right + 1)} > {x}")
    print()
    print(f"  {BOLD}Ответ:{RESET} {GREEN}{right}{RESET}")
    print(f"  Проверка: {right}² = {right * right} ≤ {x}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [4, 8, 10, 16, 25, 2]
    
    for x in examples:
        print(f"\n{CYAN}x = {x}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(x)
        print()
