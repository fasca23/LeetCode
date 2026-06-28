"""
Визуализация поиска самого длинного общего префикса.
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


def visualize(strs):
    """Пошаговая визуализация вертикального сканирования."""
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Longest Common Prefix{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Строки: {strs}")
    print()
    
    if not strs:
        print(f"  {RED}Пустой массив → ''{RESET}\n")
        return
    
    prefix = ""
    first = strs[0]
    
    print(f"  {BOLD}Идея:{RESET} берём символы первой строки")
    print(f"  и проверяем что у всех остальных на той же позиции")
    print(f"  такой же символ.")
    print()
    wait()
    
    for i, ch in enumerate(first):
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {i + 1}: символ {YELLOW}{ch!r}{RESET} на позиции {i}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        # Показываем все строки с подсветкой позиции i
        print(f"  Проверяем позицию {i}:")
        print()
        all_match = True
        
        for j, s in enumerate(strs):
            print(f"    ", end="")
            for k, c in enumerate(s):
                if k == i:
                    if j == 0:
                        # Первая строка — эталон, жёлтый
                        print(f"{YELLOW}[{c}]{RESET}", end="")
                    else:
                        # Остальные — пока не проверили, белые
                        print(f"[{c}]", end="")
                elif k < i:
                    # Уже пройденные — зелёные (общий префикс)
                    print(f"{GREEN}{c}{RESET}", end="")
                else:
                    print(f"{c}", end="")
            
            if i >= len(s):
                print(f"  {RED}← строка кончилась!{RESET}")
                all_match = False
            elif j > 0 and s[i] != ch:
                print(f"  {RED}← {s[i]!r} ≠ {ch!r}{RESET}")
                all_match = False
            elif j > 0:
                print(f"  {GREEN}← ✓{RESET}")
            else:
                print(f"  {YELLOW}← эталон{RESET}")
        
        print()
        
        if not all_match:
            print(f"  {RED}Символы разошлись → префикс = {prefix!r}{RESET}")
            print()
            break
        
        prefix += ch
        print(f"  {GREEN}Все совпали → префикс = {prefix!r}{RESET}")
        print(f"  Идём дальше...")
        print()
        wait()
    else:
        # Цикл закончился без break — вся первая строка префикс
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"  {GREEN}Вся первая строка — общий префикс!{RESET}")
    
    print(f"  {BOLD}Результат:{RESET} {GREEN}{prefix!r}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["ab", "a"],
    ]
    
    for strs in examples:
        print(f"\n{CYAN}{strs}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(strs)
        print()
