"""
Визуализация перевода римского числа в целое.
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


def visualize(s):
    """Пошаговая визуализация обхода справа налево."""
    
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev = 0
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Римское число: {s}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Идём {BOLD}справа налево{RESET}")
    print(f"  Если cur < prev — {RED}вычитаем{RESET}, иначе — {GREEN}складываем{RESET}")
    print()
    wait()
    
    for i in range(len(s) - 1, -1, -1):
        step += 1
        ch = s[i]
        cur = values[ch]
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        # Показываем строку с подсветкой текущего символа
        print(f"  ", end="")
        for j, c in enumerate(s):
            if j == i:
                print(f"{YELLOW}[{c}]{RESET}", end="")
            else:
                print(f" {c} ", end="")
        print()
        
        # Указатель
        print(f"  " + " " * (i * 3 + 1) + f"{YELLOW}▲{RESET}")
        print()
        
        print(f"  Символ: {YELLOW}{ch}{RESET} = {values[ch]}")
        print(f"  prev = {prev}")
        
        old_total = total
        if cur < prev:
            total -= cur
            action = f"{RED}cur < prev → вычитаем{RESET}"
            print(f"  {action}")
            print(f"  total = {old_total} - {cur} = {GREEN}{total}{RESET}")
        else:
            total += cur
            action = f"{GREEN}cur ≥ prev → складываем{RESET}"
            print(f"  {action}")
            print(f"  total = {old_total} + {cur} = {GREEN}{total}{RESET}")
        
        prev = cur
        print(f"  Новый prev = {cur}")
        print()
        wait()
    
    # Финал
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  {s} = {GREEN}{total}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = ["III", "LVIII", "MCMXCIV", "IV", "XL"]
    
    for s in examples:
        print(f"\n{CYAN}{s}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(s)
        print()