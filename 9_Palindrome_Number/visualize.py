"""
Визуализация проверки числа на палиндром.
Управление: Enter — шаг, q — выход.
"""

import os
import sys
from solution import Solution

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'


def visualize(x):
    """Пошаговая визуализация переворота половины числа."""
    
    original = x
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*50}{RESET}")
    print(f"{BOLD}Palindrome Number: {original}{RESET}")
    print(f"{CYAN}{'='*50}{RESET}\n")
    
    # Проверка особых случаев
    if original < 0:
        print(f"  {RED}Отрицательное → false{RESET}\n")
        return
    
    if original % 10 == 0 and original != 0:
        print(f"  {RED}Оканчивается на 0 → false{RESET}\n")
        return
    
    rev = 0
    
    print(f"  {BOLD}Идея:{RESET} переворачиваем правую половину")
    print(f"  и сравниваем с левой.")
    print(f"  x={YELLOW}{x}{RESET}, rev={rev}")
    print()
    wait()
    
    while x > rev:
        step += 1
        clear()
        print(f"{CYAN}{'='*50}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*50}{RESET}\n")
        
        last_digit = x % 10
        old_rev = rev
        rev = rev * 10 + last_digit
        old_x = x
        x //= 10
        
        # Визуализация
        print(f"  {BOLD}До:{RESET}   x={YELLOW}{old_x}{RESET}, rev={old_rev}")
        print(f"  {BOLD}Действие:{RESET}")
        print(f"    • Последняя цифра x: {YELLOW}{old_x} % 10 = {GREEN}{last_digit}{RESET}")
        print(f"    • rev = {old_rev} * 10 + {last_digit} = {GREEN}{rev}{RESET}")
        print(f"    • x = {old_x} // 10 = {GREEN}{x}{RESET}")
        print(f"  {BOLD}После:{RESET} x={GREEN}{x}{RESET}, rev={GREEN}{rev}{RESET}")
        print(f"  Проверка: x ({x}) > rev ({rev})? {GREEN if x > rev else RED}{x > rev}{RESET}")
        print()
        wait()
    
    clear()
    print(f"{CYAN}{'='*50}{RESET}")
    print(f"{BOLD}Сравнение{RESET}")
    print(f"{CYAN}{'='*50}{RESET}\n")
    
    print(f"  x    = {YELLOW}{x}{RESET}")
    print(f"  rev  = {YELLOW}{rev}{RESET}")
    print()
    
    # Чётное: x == rev
    # Нечётное: x == rev // 10 (средняя цифра в rev)
    even = x == rev
    odd = x == rev // 10
    result = even or odd
    
    if even:
        print(f"  {GREEN}x == rev  →  {x} == {rev}  ✓{RESET}")
    elif odd:
        print(f"  {GREEN}x == rev // 10  →  {x} == {rev // 10}  ✓{RESET}")
    else:
        print(f"  {RED}{x} != {rev}  и  {x} != {rev // 10}  ✗{RESET}")
    
    print(f"\n  {BOLD}Ответ:{RESET} {GREEN if result else RED}{result}{RESET}")
    print()


if __name__ == "__main__":
    examples = [121, -121, 10, 1221, 12321]
    
    for x in examples:
        print(f"\n{CYAN}Число: {x}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(x)
        print()