"""
Визуализация подъёма по лестнице — все возможные пути.
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


def generate_paths(n):
    """Генерирует все пути для ступеньки n."""
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    
    # Берём шаг 1 от n-1 + шаг 2 от n-2
    paths = []
    for path in generate_paths(n - 1):
        paths.append(path + [1])
    for path in generate_paths(n - 2):
        paths.append(path + [2])
    return paths


def visualize(n):
    """Пошаговая визуализация всех путей."""
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Climbing Stairs: n = {n}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    print(f"  Задача: подняться на {n} ступенек.")
    print(f"  Шаги: +1 или +2 ступеньки за раз.")
    print(f"  Сколько ВСЕХ путей? Покажем каждый.\n")
    print(f"  {BOLD}Идея:{RESET}")
    print(f"  На ступеньку {n} можно попасть:")
    print(f"    • с {n-1} → добавляем шаг +1 ко всем путям до {n-1}")
    print(f"    • с {n-2} → добавляем шаг +2 ко всем путям до {n-2}")
    print()
    wait()
    
    # Собираем пути для каждой ступеньки от 1 до n
    all_paths = {0: [[]], 1: [[1]]}
    
    for i in range(2, n + 1):
        # Строим пути для ступеньки i
        paths_i = []
        for path in all_paths[i - 1]:
            paths_i.append(path + [1])
        for path in all_paths[i - 2]:
            paths_i.append(path + [2])
        all_paths[i] = paths_i
        
        clear()
        print(f"{CYAN}{'='*60}{RESET}")
        print(f"{BOLD}Шаг {i - 1}: ступенька {i}{RESET}")
        print(f"{CYAN}{'='*60}{RESET}\n")
        
        # Показываем пути для i-1 и i-2
        print(f"  Пути до ступеньки {i-1} ({len(all_paths[i-1])} шт.):")
        for p in all_paths[i - 1]:
            steps_str = "+".join(map(str, p))
            print(f"    {GREEN}{steps_str}{RESET}", end="")
            print(f"  → {YELLOW}+1{RESET} = {steps_str}+1")
        print()
        
        print(f"  Пути до ступеньки {i-2} ({len(all_paths[i-2])} шт.):")
        for p in all_paths[i - 2]:
            steps_str = "+".join(map(str, p))
            print(f"    {GREEN}{steps_str}{RESET}", end="")
            print(f"  → {YELLOW}+2{RESET} = {steps_str}+2")
        print()
        
        # Все пути для ступеньки i
        print(f"  {BOLD}Все пути до ступеньки {i} ({len(paths_i)} шт.):{RESET}")
        for p in paths_i:
            steps_str = "+".join(map(str, p))
            total = sum(p)
            print(f"    {CYAN}{steps_str}{RESET} = {total}")
        print()
        
        # Формула
        print(f"  {BOLD}Формула:{RESET}")
        print(f"  ways({i}) = ways({i-1}) + ways({i-2})")
        print(f"            = {len(all_paths[i-1])} + {len(all_paths[i-2])}")
        print(f"            = {GREEN}{len(paths_i)}{RESET}")
        print()
        
        wait()
    
    # Финал
    clear()
    all_final = all_paths[n]
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}")
    print(f"  n = {n}")
    print(f"  Всего путей: {GREEN}{len(all_final)}{RESET}")
    print()
    print(f"  Все пути:")
    for p in all_final:
        steps_str = "+".join(map(str, p))
        print(f"    {GREEN}{steps_str}{RESET} = {sum(p)}")
    print(f"{GREEN}{'='*60}{RESET}\n")


if __name__ == "__main__":
    examples = [2, 3, 4, 5]
    
    for n in examples:
        print(f"\n{CYAN}n = {n}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(n)
        print()