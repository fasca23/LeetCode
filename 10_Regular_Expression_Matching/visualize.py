"""
Визуализация сопоставления с регулярным выражением.
Side-by-side: строка + шаблон + DP-таблица.
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


def visualize(s, p):
    """Пошаговая визуализация с указателями и DP-таблицей."""
    
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_state(i, j):
        """Показать строку и шаблон с подсветкой позиций."""
        # Строка s
        print(f"  s = ", end="")
        for k, ch in enumerate(s):
            if k == i - 1 and i > 0:
                print(f"{YELLOW}[{ch}]{RESET}", end="")
            else:
                print(f" {ch} ", end="")
        if i == 0:
            print(f"{YELLOW}[ε]{RESET}", end="")  # пустая строка
        print()
        
        # Шаблон p
        print(f"  p = ", end="")
        for k, ch in enumerate(p):
            if k == j - 1 and j > 0:
                print(f"{YELLOW}[{ch}]{RESET}", end="")
            else:
                print(f" {ch} ", end="")
        if j == 0:
            print(f"{YELLOW}[ε]{RESET}", end="")
        print()
    
    def show_dp_table(cur_i, cur_j):
        """Показать компактную DP-таблицу с текущей ячейкой."""
        # Заголовок
        print(f"  ┌───┼" + "───" * (n + 1) + "┐")
        header = f"  │   │ ε"
        for ch in p:
            header += f" {ch} "
        print(header)
        print(f"  ├───┼" + "───" * (n + 1) + "┤")
        
        # Строки
        for i in range(m + 1):
            if i == 0:
                label = "ε"
            else:
                label = s[i-1]
            row = f"  │ {label} │"
            for j in range(n + 1):
                val = dp[i][j]
                if i == cur_i and j == cur_j:
                    row += f"{YELLOW}{'T' if val else 'F'}{RESET}  "
                elif val:
                    row += f"{GREEN}T{RESET}  "
                else:
                    row += f"·  "
            print(row)
        
        print(f"  └───┴" + "───" * (n + 1) + "┘")
    
    # Инициализация: пустая строка против шаблонов с *
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}RegExp Matching{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  . = любой символ    * = 0+ повторений")
    print()
    show_state(0, 0)
    print()
    print(f"  {BOLD}Начало:{RESET} пустая строка, пустой шаблон → {GREEN}True{RESET}")
    print()
    show_dp_table(0, 0)
    print()
    print(f"  Пустая строка совпадает с шаблонами: ", end="")
    matches = [f"{p[:j]!r}" for j in range(n+1) if dp[0][j]]
    print(", ".join(matches) if matches else "только ε")
    print()
    wait()
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}s[{i-1}]={s[i-1]!r} vs p[{j-1}]={p[j-1]!r}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            
            show_state(i, j)
            print()
            
            if p[j - 1] == '*':
                prev_ch = p[j - 2]
                
                # Вариант 1: ноль повторений
                zero = dp[i][j - 2]
                
                # Вариант 2: одно+ повторений
                one_plus = False
                if prev_ch == '.' or prev_ch == s[i - 1]:
                    one_plus = dp[i - 1][j]
                
                dp[i][j] = zero or one_plus
                
                print(f"  {BOLD}{YELLOW}*{RESET} — два варианта:")
                print(f"    1) 0 повторов: пропускаем [{prev_ch}]* → dp[{i}][{j-2}] = {GREEN if zero else RED}{zero}{RESET}")
                
                if prev_ch == '.' or prev_ch == s[i - 1]:
                    print(f"    2) 1+ повторов: {prev_ch!r} == {s[i-1]!r} → dp[{i-1}][{j}] = {GREEN if one_plus else RED}{one_plus}{RESET}")
                else:
                    print(f"    2) {prev_ch!r} ≠ {s[i-1]!r} → нельзя")
                
                print(f"  Итог: {GREEN if dp[i][j] else RED}{dp[i][j]}{RESET}")
                
            elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                print(f"  {BOLD}{p[j-1]!r} == {s[i-1]!r}{RESET} → dp[{i-1}][{j-1}] = {GREEN if dp[i][j] else RED}{dp[i][j]}{RESET}")
            else:
                dp[i][j] = False
                print(f"  {BOLD}{p[j-1]!r} ≠ {s[i-1]!r}{RESET} → {RED}False{RESET}")
            
            print()
            show_dp_table(i, j)
            print()
            wait()
    
    # Финал
    clear()
    result = dp[m][n]
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  s = {s!r}")
    print(f"  p = {p!r}")
    print(f"  Результат: {GREEN if result else RED}{result}{RESET}")
    print()
    show_dp_table(m, n)
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        ("aa", "a*"),
        ("ab", ".*"),
        ("aab", "c*a*b"),
        ("aa", "a"),
        ("mississippi", "mis*is*p*."),
    ]
    
    for s, p in examples:
        print(f"\n{CYAN}s={s!r}, p={p!r}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(s, p)
        print()
