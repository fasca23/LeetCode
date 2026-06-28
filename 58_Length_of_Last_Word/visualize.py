"""
Визуализация поиска длины последнего слова.
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


def visualize(s):
    """Пошаговая визуализация обхода с конца."""
    
    i = len(s) - 1
    length = 0
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Length of Last Word{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Строка: {s!r}")
    print(f"  Длина: {len(s)}")
    print()
    
    # Показываем строку с индексами
    print(f"  Индексы:")
    print(f"  ", end="")
    for j in range(len(s)):
        print(f"{j % 10}", end="")
    print()
    print(f"  ", end="")
    for j, ch in enumerate(s):
        if j == i:
            print(f"{YELLOW}{ch}{RESET}", end="")
        else:
            print(f"{ch}", end="")
    print()
    print()
    print(f"  {BOLD}Фаза 1:{RESET} пропускаем пробелы в конце")
    print()
    wait()
    
    # Фаза 1: пропускаем пробелы
    while i >= 0 and s[i] == ' ':
        step += 1
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: пропускаем пробел{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        print(f"  ", end="")
        for j, ch in enumerate(s):
            if j == i:
                print(f"{RED}[{ch}]{RESET}", end="")
            else:
                print(f"{ch}", end="")
        print()
        print(f"  " + " " * i + f"{RED}▲ пробел — пропускаем{RESET}")
        print()
        print(f"  i = {i} → {i - 1}")
        print(f"  length = {length}")
        print()
        
        i -= 1
        wait()
    
    # Фаза 2: считаем буквы
    if i >= 0:
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Фаза 2: считаем буквы{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        print(f"  Начинаем считать с позиции {i}:")
        wait()
    
    while i >= 0 and s[i] != ' ':
        step += 1
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: буква {YELLOW}{s[i]!r}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        print(f"  ", end="")
        for j, ch in enumerate(s):
            if j == i:
                print(f"{GREEN}[{ch}]{RESET}", end="")
            elif j > i and s[j] != ' ':
                print(f"{GREEN}{ch}{RESET}", end="")
            else:
                print(f"{ch}", end="")
        print()
        print(f"  " + " " * i + f"{GREEN}▲ считаем{RESET}")
        print()
        
        length += 1
        print(f"  i = {i} → {i - 1}")
        print(f"  length = {GREEN}{length}{RESET}")
        print()
        
        i -= 1
        wait()
    
    # Финал
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    
    # Показываем последнее слово
    last_word_start = i + 1 if i >= 0 else 0
    last_word = s[last_word_start:].strip()
    
    print(f"  Строка:       {s!r}")
    print(f"  Последнее слово: {GREEN}{last_word!r}{RESET}")
    print(f"  Длина:        {GREEN}{length}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        "Hello World",
        " fly me to the moon ",
        "luffy is still joyboy",
        "   day   ",
    ]
    
    for s in examples:
        print(f"\n{CYAN}{s!r}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(s)
        print()
