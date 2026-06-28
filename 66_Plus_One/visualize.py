"""
Визуализация прибавления единицы к числу в виде массива.
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


def visualize(digits):
    """Пошаговая визуализация сложения с единицей."""
    
    original = digits[:]
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_array(arr, current=None, message=""):
        """Показать массив с подсветкой текущей позиции."""
        print(f"  [", end="")
        for j, d in enumerate(arr):
            if j == current:
                print(f"{YELLOW}{d}{RESET}", end="")
            elif j > current and current is not None:
                print(f"{GREEN}{d}{RESET}", end="")
            else:
                print(f"{d}", end="")
            if j < len(arr) - 1:
                print(", ", end="")
        print(f"]  {message}")
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Plus One{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Число: {original}")
    print(f"  {BOLD}Прибавляем 1{RESET}")
    print()
    show_array(digits, -1, "(начало)")
    print()
    print(f"  Идём справа налево.")
    print(f"  Если цифра < 9 — увеличиваем и всё.")
    print(f"  Если 9 — превращаем в 0, переносим 1 дальше.")
    print()
    wait()
    
    for i in range(len(digits) - 1, -1, -1):
        step += 1
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: позиция {i}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        show_array(digits, i)
        print()
        print(f"  digits[{i}] = {YELLOW}{digits[i]}{RESET}")
        print()
        
        if digits[i] < 9:
            old = digits[i]
            digits[i] += 1
            print(f"  {GREEN}{old} < 9 → увеличиваем{RESET}")
            print(f"  digits[{i}] = {old} + 1 = {GREEN}{digits[i]}{RESET}")
            print()
            show_array(digits, i, "← результат")
            print()
            break
        else:
            print(f"  {RED}{digits[i]} == 9 → превращаем в 0, переносим 1{RESET}")
            digits[i] = 0
            print(f"  digits[{i}] = {RED}0{RESET}")
            print()
            show_array(digits, -1, "→ идём дальше")
            print()
            
            if i == 0:
                digits.insert(0, 1)
                print(f"  {GREEN}Все цифры были 9 → добавляем 1 в начало{RESET}")
                print()
                show_array(digits, -1, "← результат")
                print()
        
        wait()
    else:
        # Если цикл закончился без break (не должно при правильном вводе)
        pass
    
    # Финал
    print(f"\n  {BOLD}Исходное:{RESET}  {original}")
    print(f"  {BOLD}Результат:{RESET} {GREEN}{digits}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
        [9, 9, 9],
        [1, 9, 9],
    ]
    
    for digits in examples:
        print(f"\n{CYAN}{digits}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(digits[:])
        print()
