"""
Визуализация построения BST из отсортированного массива.
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def draw_tree(node, highlight=None, prefix="", is_left=True):
    if node is None:
        return
    if node.right:
        draw_tree(node.right, highlight, prefix + ("│   " if is_left else "    "), False)
    branch = "└── " if is_left else "┌── "
    if node == highlight:
        print(f"  {prefix}{branch}{YELLOW}{node.val}{RESET}")
    else:
        print(f"  {prefix}{branch}{node.val}")
    if node.left:
        draw_tree(node.left, highlight, prefix + ("    " if is_left else "│   "), True)


def visualize(nums):
    """Пошаговая визуализация построения BST."""
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def build(root, nums, left, right, depth):
        """Рекурсивное построение с визуализацией."""
        nonlocal step
        
        if left > right:
            return None
        
        mid = (left + right) // 2
        step += 1
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: создаём узел{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        # Показываем массив с выделением
        print(f"  {BOLD}Массив:{RESET}")
        print(f"  ", end="")
        for i, val in enumerate(nums):
            if i == mid:
                print(f"{YELLOW}[{val}]{RESET}", end=" ")
            elif left <= i <= right:
                print(f"{val}", end=" ")
            else:
                print(f"{RED}{val}{RESET}", end=" ")
        print()
        print(f"  ", end="")
        for i, _ in enumerate(nums):
            if i == left:
                print(f" L ", end="")
            elif i == right:
                print(f" R ", end="")
            elif i == mid:
                print(f" M ", end="")
            else:
                print(f"   ", end="")
        print()
        print()
        
        print(f"  {BOLD}Диапазон:{RESET} [{left}, {right}]")
        print(f"  {BOLD}Середина:{RESET} mid = ({left} + {right}) // 2 = {mid}")
        print(f"  {BOLD}Корень:{RESET} nums[{mid}] = {YELLOW}{nums[mid]}{RESET}")
        print()
        
        # Создаём узел
        node = TreeNode(nums[mid])
        
        # Показываем дерево на текущий момент
        if root is None:
            root = node
        
        print(f"  {BOLD}Дерево сейчас:{RESET}")
        draw_tree(root)
        print()
        
        print(f"  {BOLD}Действие:{RESET}")
        print(f"  Узел {YELLOW}{nums[mid]}{RESET} создан (глубина {depth})")
        print()
        
        # Переменные
        print(f"  ┌────────────┬──────────────────────┐")
        print(f"  │ Переменная │ Значение             │")
        print(f"  ├────────────┼──────────────────────┤")
        print(f"  │ left       │ {left:<20} │")
        print(f"  │ right      │ {right:<20} │")
        print(f"  │ mid        │ {mid:<20} │")
        print(f"  │ значение   │ {nums[mid]:<20} │")
        print(f"  │ глубина    │ {depth:<20} │")
        print(f"  └────────────┴──────────────────────┘")
        print()
        
        wait()
        
        # Левое поддерево
        if mid - 1 >= left:
            print(f"  {CYAN}→ строим ЛЕВОЕ поддерево: [{left}, {mid-1}]{RESET}")
            print()
            wait()
            node.left = build(root, nums, left, mid - 1, depth + 1)
        else:
            step += 1
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}: левое поддерево — пусто{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            print(f"  Диапазон [{left}, {mid-1}] = [{left}, {left - 1}] — пустой")
            print(f"  {RED}left > right → None{RESET}")
            print()
            draw_tree(root)
            print()
            wait()
        
        # Правое поддерево
        if mid + 1 <= right:
            print(f"  {CYAN}→ строим ПРАВОЕ поддерево: [{mid+1}, {right}]{RESET}")
            print()
            wait()
            node.right = build(root, nums, mid + 1, right, depth + 1)
        else:
            step += 1
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}: правое поддерево — пусто{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            print(f"  Диапазон [{mid+1}, {right}] = [{right+1}, {right}] — пустой")
            print(f"  {RED}left > right → None{RESET}")
            print()
            draw_tree(root)
            print()
            wait()
        
        return node
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Sorted Array → BST{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Исходный массив: {nums}")
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  1. Корень = середина массива")
    print(f"  2. Левое поддерево = левая половина")
    print(f"  3. Правое поддерево = правая половина")
    print(f"  4. Повторить для каждой половины")
    print()
    print(f"  {YELLOW}[x]{RESET} — выбранный элемент")
    print(f"  {RED}x{RESET} — вне текущего диапазона")
    print(f"  L=левая граница, M=середина, R=правая граница")
    print()
    wait()
    
    step = 0
    root = None
    root = build(root, nums, 0, len(nums) - 1, 1)
    
    # Финал
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Готово!{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    print(f"  Массив: {nums}")
    print()
    draw_tree(root)
    print()
    print(f"  Дерево сбалансировано: высота левого и правого")
    print(f"  поддеревьев отличается не более чем на 1.")
    print()


if __name__ == "__main__":
    examples = [
        [-10, -3, 0, 5, 9],
        [1, 2, 3, 4, 5, 6, 7],
    ]
    
    for nums in examples:
        print(f"\n{CYAN}{nums}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(nums)
        print()
