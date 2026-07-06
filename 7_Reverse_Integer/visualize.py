"""
Визуализация реверса целого числа.
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
    """Пошаговая визуализация реверса цифр."""
    
    INT_MAX = 2**31 - 1
    
    sign = -1 if x < 0 else 1
    original = x
    x = abs(x)
    rev = 0
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_number(num, highlight_last=False):
        """Показать число, последняя цифра зелёная."""
        s = str(num)
        if highlight_last and len(s) > 1:
            print(f"  {s[:-1]}{GREEN}{s[-1]}{RESET}")
        else:
            print(f"  {GREEN}{s}{RESET}" if highlight_last else f"  {s}")
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Reverse Integer: {original}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    
    if original == 0:
        print(f"  x = 0 → {GREEN}0{RESET}\n")
        return
    
    print(f"  Знак: {'−' if sign == -1 else '+'},  |x| = {x}")
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  Берём последнюю цифру, добавляем к rev.")
    print(f"  rev = rev * 10 + цифра")
    print(f"  x = x // 10")
    print()
    print(f"  Старт:  rev=0, x={x}")
    print()
    wait()
    
    while x != 0:
        step += 1
        digit = x % 10
        old_rev = rev
        old_x = x
        
        # Проверка переполнения
        overflow = old_rev > (INT_MAX - digit) // 10
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        # x с подсвеченной последней цифрой
        s = str(old_x)
        if len(s) > 1:
            print(f"  x = {s[:-1]}{YELLOW}{s[-1]}{RESET}", end="")
        else:
            print(f"  x = {YELLOW}{s}{RESET}", end="")
        print(f"    →  цифра = {YELLOW}{digit}{RESET}")
        print()
        
        print(f"  rev = {old_rev}  →  {old_rev} * 10 + {digit} = ", end="")
        
        if overflow:
            rev_new = old_rev * 10 + digit
            print(f"{RED}{rev_new} (ПЕРЕПОЛНЕНИЕ!){RESET}")
            print()
            print(f"  {RED}Выход за границы 32-битного int → возвращаем 0{RESET}")
            print()
            return
        
        x //= 10
        rev = old_rev * 10 + digit
        
        print(f"{GREEN}{rev}{RESET}")
        print()
        print(f"  x = {old_x} // 10 = {x}")
        print(f"  rev = {rev}")
        print()
        print(f"  Граница: {rev} ≤ {INT_MAX}? {GREEN if rev <= INT_MAX else RED}{rev <= INT_MAX}{RESET}")
        print()
        wait()
    
    # Финал
    result = sign * rev
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  Исходное: {original}")
    print(f"  Реверс:   {GREEN}{result}{RESET}")
    print(f"  Проверка: reverse({original}) = {result}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [123, -123, 120, 1534236469]
    
    for x in examples:
        print(f"\n{CYAN}x = {x}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(x)
        print()