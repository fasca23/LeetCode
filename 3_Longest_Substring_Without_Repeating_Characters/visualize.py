"""
Визуализация поиска самой длинной подстроки без повторов.
Управление: Enter — шаг, q — выход.
"""

import os
import sys
from solution import Solution

# Цвета
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'


def visualize(s):
    """Пошаговая визуализация скользящего окна."""
    
    sol = Solution()
    last = {}
    left = 0
    max_len = 0
    best_start = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    
    # Заголовок
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Строка: {s!r}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    
    if not s:
        print(f"  {RED}Пустая строка → ответ 0{RESET}\n")
        return
    
    for right, ch in enumerate(s):
        # Показываем строку с окном
        print(f"  {BOLD}Окно:{RESET}  ", end="")
        for i, c in enumerate(s):
            if i < left:
                print(f"{c}", end="")
            elif i == left:
                print(f"{GREEN}[{c}", end="")
            elif i == right:
                print(f"{c}]{RESET}", end="")
            else:
                print(f"{c}", end="")
        if right < left:
            print(f"{GREEN}[]", end="")
            for i, c in enumerate(s):
                if i >= left:
                    print(f"{c}", end="")
            print(RESET, end="")
        print()
        
        # Указатели
        indent = " " * 9
        for i, c in enumerate(s):
            if i == left:
                print(f"{indent}{GREEN}L{RESET}", end="")
            elif i == right:
                print(f"{GREEN}R{RESET}", end="")
            else:
                print(" ", end="")
        print()
        
        # Детали шага
        print(f"\n  Шаг {right}: символ {YELLOW}{ch!r}{RESET}", end="")
        
        if ch in last and last[ch] >= left:
            old_left = left
            left = last[ch] + 1
            print(f"  →  {RED}повтор{RESET} на позиции {last[ch]}")
            print(f"      L: {old_left} → {left}")
        else:
            print(f"  →  {GREEN}новый{RESET}")
        
        last[ch] = right
        current = right - left + 1
        
        if current > max_len:
            max_len = current
            best_start = left
            print(f"      {GREEN}Новый максимум: {max_len}{RESET} ({s[best_start:best_start+max_len]!r})")
        else:
            print(f"      Длина окна: {current}, максимум: {max_len}")
        
        print(f"      Словарь: {dict(sorted(last.items()))}")
        print()
        wait()
        clear()
        print(f"{CYAN}{'='*60}{RESET}")
        print(f"{BOLD}Строка: {s!r}{RESET}")
        print(f"{CYAN}{'='*60}{RESET}\n")
    
    # Финал
    best = s[best_start:best_start + max_len]
    print(f"  {GREEN}{'='*60}{RESET}")
    print(f"  {BOLD}Ответ:{RESET} {GREEN}{max_len}{RESET}")
    print(f"  {BOLD}Подстрока:{RESET} {GREEN}{best!r}{RESET}")
    print(f"  {GREEN}{'='*60}{RESET}\n")


if __name__ == "__main__":
    examples = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "abca",
        "",
    ]
    
    for s in examples:
        print(f"\n{CYAN}Строка: {s!r}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(s)
        print()
