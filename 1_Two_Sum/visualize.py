"""
Визуализация Two Sum.
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


def visualize(nums, target):
    """Пошаговая визуализация поиска двух индексов."""
    
    seen = {}
    found = None
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Two Sum: nums={nums}, target={target}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    
    for i, num in enumerate(nums):
        need = target - num
        
        # Показываем массив с текущей позицией
        print(f"  {BOLD}Шаг {i}:{RESET}  ", end="")
        for j, n in enumerate(nums):
            if j == i:
                print(f"{YELLOW}[{n}]{RESET}", end=" ")
            elif found and j in found:
                print(f"{GREEN}{n}{RESET}", end=" ")
            else:
                print(f"{n}", end=" ")
        print()
        
        # # Указатель
        # print(f"        " + " " * i * 2 + f"{YELLOW}▲{RESET}")
        
        # Детали
        print(f"  num={YELLOW}{num}{RESET},  нужно {CYAN}{need}{RESET}")
        
        if need in seen:
            j = seen[need]
            found = (j, i)
            print(f"  {GREEN}Нашли!{RESET} seen[{need}]={j}  →  nums[{j}]+nums[{i}] = {nums[j]}+{num} = {target}")
            print(f"  {GREEN}Ответ: [{j}, {i}]{RESET}\n")
            return
        
        seen[num] = i
        print(f"  seen[{num}] = {i}")
        print(f"  Словарь: {dict(sorted(seen.items()))}")
        print()
        wait()
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Two Sum: nums={nums}, target={target}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
    
    print(f"  {RED}Пара не найдена{RESET}\n")


if __name__ == "__main__":
    examples = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    
    for nums, target in examples:
        print(f"\n{CYAN}nums={nums}, target={target}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums, target)
        print()