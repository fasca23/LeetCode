"""
Визуализация построения строки треугольника Паскаля — пирамида чисел.
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


def visualize(rowIndex):
    """Пошаговая визуализация — пирамида Паскаля."""
    
    triangle = []
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def draw_pyramid(highlight_row=-1, highlight_j=None, highlight_j2=None):
        if not triangle:
            return
        
        max_row = triangle[-1]
        cell_w = 4
        max_width = len(max_row) * cell_w
        
        for i, row in enumerate(triangle):
            row_width = len(row) * cell_w
            padding = (max_width - row_width) // 2
            
            row_str = ""
            for k, val in enumerate(row):
                if k > 0:
                    row_str += " " * (cell_w - 3)
                
                if i == highlight_row and k == highlight_j:
                    row_str += f"{YELLOW}{val:^3}{RESET}"
                elif i == highlight_row and k == highlight_j2:
                    row_str += f"{CYAN}{val:^3}{RESET}"
                else:
                    row_str += f"{val:^3}"
            
            print(f"  {' ' * padding}{row_str}")
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Треугольник Паскаля: rowIndex = {rowIndex}{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  {YELLOW}жёлтый{RESET} — новое, {CYAN}голубой{RESET} — верхние")
    print()
    wait()
    
    # Ряд 0
    triangle.append([1])
    step += 1
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Шаг {step}: ряд 0{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    draw_pyramid()
    print()
    print(f"  i = 0")
    print(f"  row = [1]")
    print()
    wait()
    
    if rowIndex == 0:
        return
    
    row = [1]
    
    for i in range(1, rowIndex + 1):
        row.append(1)
        triangle.append(row[:])
        
        step += 1
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: ряд {i}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        draw_pyramid(i, 0, len(row) - 1)
        print()
        print(f"  i = {i}")
        print(f"  row = {row}")
        print()
        wait()
        
        for j in range(i - 1, 0, -1):
            step += 1
            left_val = row[j - 1]
            new_val = row[j] + left_val
            row[j] = new_val
            triangle[i] = row[:]
            
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            draw_pyramid(i, j, j - 1)
            print()
            print(f"  i = {i}")
            print(f"  j = {j}")
            print(f"  row = {row}")
            print()
            wait()
    
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Готово!{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    draw_pyramid()
    print()
    print(f"  Ответ: {GREEN}{row}{RESET}")
    print()


if __name__ == "__main__":
    rowIndex = 6
    print(f"\n{CYAN}rowIndex = {rowIndex}{RESET}")
    input(f"{YELLOW}Enter для запуска{RESET} ")
    visualize(rowIndex)
