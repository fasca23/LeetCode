"""
Визуализация зигзаг-преобразования с полной сеткой и переменными.
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
    """Пошаговая визуализация зигзага с сеткой и переменными."""
    
    if numRows == 1 or numRows >= len(s):
        print(f"  {YELLOW}Особый случай — строка не меняется{RESET}")
        print(f"  Результат: {GREEN}{s}{RESET}\n")
        return
    
    # Сетка: список списков, сначала всё None
    grid = [[None for _ in range(len(s))] for _ in range(numRows)]
    row, col = 0, 0
    step = 1
    
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
    
    def draw_grid(current_col, max_col):
        """Рисует сетку до колонки max_col включительно."""
        for r in range(numRows):
            print(f"     ", end="")
            for c in range(max_col + 1):
                val = grid[r][c]
                if val is None:
                    print(" · ", end="")
                elif c == current_col:
                    print(f"{YELLOW}[{val}]{RESET}", end="")
                else:
                    print(f" {GREEN}{val}{RESET} ", end="")
            # Накопленная строка
            line = ''.join(grid[r][c] for c in range(max_col + 1) if grid[r][c] is not None)
            print(f"  →  {GREEN}{line!r}{RESET}")
    
    rows = [''] * numRows
    cur_row = 0
    cur_step = 1
    
    clear()
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Zigzag: {s!r}, строк = {numRows}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    print(f"  Начальное состояние:")
    print(f"    rows = {['']*numRows}")
    print(f"    row  = {cur_row}")
    print(f"    step = {cur_step} ({'▼ вниз' if cur_step == 1 else '▲ вверх'})")
    print()
    wait()
    
    for step_num, ch in enumerate(s):
        clear()
        print(f"{CYAN}{'='*60}{RESET}")
        print(f"{BOLD}Шаг {step_num + 1}/{len(s)}: символ {YELLOW}{ch!r}{RESET}")
        print(f"{CYAN}{'='*60}{RESET}\n")
        
        print(f"  {BOLD}Сетка:{RESET}")
        print()
        draw_grid(step_num, step_num)
        print()
        
        # Переменные ДО
        print(f"  {BOLD}Переменные ДО:{RESET}")
        print(f"    row  = {cur_row}")
        print(f"    step = {cur_step} ({'▼ вниз' if cur_step == 1 else '▲ вверх'})")
        print(f"    rows = {rows}")
        print()
        
        # Действие
        rows[cur_row] += ch
        print(f"  {BOLD}Действие:{RESET}")
        print(f"    {YELLOW}{ch!r}{RESET} → rows[{cur_row}]")
        print(f"    rows[{cur_row}] = {rows[cur_row]!r}")
        print()
        
        # Меняем направление
        if cur_row == 0:
            cur_step = 1
            print(f"    row == 0 (верх) → step = {GREEN}1 (▼ вниз){RESET}")
        elif cur_row == numRows - 1:
            cur_step = -1
            print(f"    row == {numRows - 1} (низ) → step = {RED}-1 (▲ вверх){RESET}")
        else:
            print(f"    row == {cur_row} (середина) → step не меняется")
        
        cur_row += cur_step
        print(f"    row = {cur_row - cur_step} + ({cur_step}) = {GREEN}{cur_row}{RESET}")
        print()
        
        # Переменные ПОСЛЕ
        print(f"  {BOLD}Переменные ПОСЛЕ:{RESET}")
        print(f"    row  = {cur_row}")
        print(f"    step = {cur_step} ({'▼ вниз' if cur_step == 1 else '▲ вверх'})")
        print(f"    rows = {rows}")
        print()
        wait()
    
    # Финал — полная сетка
    clear()
    result = ''.join(rows)
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Финальная сетка:{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    draw_grid(-1, len(s) - 1)
    print()
    print(f"  {BOLD}Читаем построчно:{RESET}")
    for r in range(numRows):
        print(f"    Строка {r}: {GREEN}{rows[r]!r}{RESET}")
    print(f"\n  {BOLD}Результат:{RESET} {GREEN}{result!r}{RESET}")
    print(f"{GREEN}{'='*60}{RESET}\n")


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