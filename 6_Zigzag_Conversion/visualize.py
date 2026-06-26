"""
Визуализация зигзаг-преобразования с полной сеткой.
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


def visualize(s, numRows):
    """Пошаговая визуализация зигзага с сеткой."""
    
    if numRows == 1 or numRows >= len(s):
        print(f"  {YELLOW}Особый случай — строка не меняется{RESET}")
        print(f"  Результат: {GREEN}{s}{RESET}\n")
        return
    
    # Сетка: список списков, сначала всё None
    grid = [[None for _ in range(len(s))] for _ in range(numRows)]
    row, col = 0, 0
    step = 1
    
    # Заполняем сетку
    for ch in s:
        grid[row][col] = ch
        
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        
        row += step
        col += 1
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def draw_grid(current_col=-2):
        """
        Рисует сетку.
        current_col == -1  → все зелёные (финал)
        current_col == -2  → все пустые (начало)
        current_col >= 0   → до current_col зелёные, текущий жёлтый
        """
        for r in range(numRows):
            print(f"  ", end="")
            for c in range(len(s)):
                ch = grid[r][c]
                if ch is None:
                    print(" ", end=" ")
                elif current_col == -1:
                    print(f"{GREEN}{ch}{RESET}", end=" ")
                elif c == current_col:
                    print(f"{YELLOW}{ch}{RESET}", end=" ")
                elif c < current_col:
                    print(f"{GREEN}{ch}{RESET}", end=" ")
                else:
                    print(" ", end=" ")
            print()
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Zigzag: {s!r}, строк = {numRows}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Пустая сетка ({numRows} строк × {len(s)} столбцов):")
    print()
    draw_grid(current_col=-2)  # все пустые
    print()
    wait()
    
    # Проходим по шагам
    for step_num, ch in enumerate(s):
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step_num + 1}/{len(s)}: символ {YELLOW}{ch!r}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        print(f"  Сетка:")
        print()
        draw_grid(current_col=step_num)
        print()
        wait()
    
    # Финал: полная сетка + результат
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Финальная сетка:{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    draw_grid(current_col=-1)  # все зелёные
    print()
    
    # Собираем результат построчно
    result_parts = []
    print(f"  {BOLD}Читаем построчно:{RESET}")
    for r in range(numRows):
        line = ''.join(ch for ch in grid[r] if ch is not None)
        result_parts.append(line)
        print(f"    Строка {r}: {GREEN}{line!r}{RESET}")
    
    result = ''.join(result_parts)
    print(f"\n  {BOLD}Результат:{RESET} {GREEN}{result!r}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("ABCD", 2),
    ]
    
    for s, numRows in examples:
        print(f"\n{CYAN}{s!r}, rows={numRows}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(s, numRows)
        print()