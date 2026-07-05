"""
Визуализация удаления дубликатов из связного списка.
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


def visualize(arr):
    """Пошаговая визуализация удаления дубликатов."""
    
    from solution import Solution, to_linked, to_list
    
    head = to_linked(arr)
    current = head
    step = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_list(head, current=None):
        """Показать связный список с указателем current."""
        print(f"  ", end="")
        node = head
        while node:
            if node == current:
                print(f"{YELLOW}[{node.val}]{RESET}", end="")
            elif current and current.next and node == current.next and current.val == current.next.val:
                print(f"{RED}[{node.val}]{RESET}", end="")
            else:
                print(f"[{node.val}]", end="")
            
            if node.next:
                print(f" → ", end="")
            node = node.next
        print()
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Remove Duplicates{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Исходный список: {arr}")
    print()
    
    if not head:
        print(f"  {RED}Пустой список → ничего не делаем{RESET}\n")
        return
    
    show_list(head, current)
    print()
    print(f"  {BOLD}Алгоритм:{RESET} идём по списку.")
    print(f"  Если cur.val == next.val → пропускаем next.")
    print(f"  Иначе → переходим к next.")
    print()
    wait()
    
    while current and current.next:
        step += 1
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        show_list(head, current)
        print()
        
        print(f"  cur = {YELLOW}{current.val}{RESET},  next = {current.next.val}")
        print(f"  {current.val} == {current.next.val} ?  ", end="")
        
        if current.val == current.next.val:
            # Пропускаем дубликат
            skipped = current.next.val
            print(f"{RED}ДА → пропускаем {skipped}{RESET}")
            print(f"  cur.next = cur.next.next")
            current.next = current.next.next
            
            print(f"  Результат: ", end="")
            show_list(head, current)
        else:
            print(f"{GREEN}НЕТ → идём дальше{RESET}")
            current = current.next
            print(f"  cur = cur.next")
        
        print()
        wait()
    
    # Финал
    clear()
    result = to_list(head)
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"  Исходный: {arr}")
    print(f"  Результат: {GREEN}{result}{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")


if __name__ == "__main__":
    examples = [
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [1, 1, 1],
        [1, 2, 3],
    ]
    
    for arr in examples:
        print(f"\n{CYAN}{arr}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(arr)
        print()
