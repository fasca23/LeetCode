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
        print(f"  {prefix}{branch}{YELLOW}[{node.val}]{RESET}")
    else:
        print(f"  {prefix}{branch}{node.val}")
    if node.left:
        draw_tree(node.left, highlight, prefix + ("    " if is_left else "│   "), True)


def visualize(nums):
    """Пошаговая визуализация построения BST."""
    
    step = 0
    root = None  # будет TreeNode или None
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def show_array(left, right, mid):
        print(f"  массив = [", end="")
        for i, val in enumerate(nums):
            if i > 0:
                print(", ", end="")
            if i == mid:
                print(f"{YELLOW}{val}{RESET}", end="")
            elif left <= i <= right:
                print(f"{val}", end="")
            else:
                print(f"{RED}{val}{RESET}", end="")
        print(f"]")
    
    def build(parent, nums, left, right, is_left_child):
        """parent — уже созданный родительский узел (или None для корня)"""
        nonlocal step, root
        
        if left > right:
            return None
        
        mid = (left + right) // 2
        step += 1
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: создаём узел{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        show_array(left, right, mid)
        print()
        
        print(f"  left        = {left}")
        print(f"  right       = {right}")
        print(f"  mid         = ({left} + {right}) // 2 = {mid}")
        print(f"  значение    = nums[{mid}] = {YELLOW}{nums[mid]}{RESET}")
        print()
        
        # Создаём узел и сразу прикрепляем к родителю
        node = TreeNode(nums[mid])
        
        if parent is None:
            root = node
            print(f"  Это корень: {YELLOW}{nums[mid]}{RESET}")
        else:
            side = "ЛЕВЫЙ" if is_left_child else "ПРАВЫЙ"
            print(f"  Прикрепляем как {CYAN}{side}{RESET} ребёнок к родителю {parent.val}")
            if is_left_child:
                parent.left = node
            else:
                parent.right = node
        
        print()
        print(f"  {BOLD}Дерево на текущий момент:{RESET}")
        if root:
            draw_tree(root, node)
        else:
            print(f"  (пусто)")
        print()
        wait()
        
        # Левое поддерево
        if mid - 1 >= left:
            node.left = build(node, nums, left, mid - 1, True)
        else:
            step += 1
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}: левое поддерево для {nums[mid]}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            print(f"  диапазон = [{left}, {mid-1}] — пустой")
            print(f"  left > right → left = {RED}None{RESET}")
            print()
            print(f"  {BOLD}Дерево на текущий момент:{RESET}")
            draw_tree(root)
            print()
            wait()
        
        # Правое поддерево
        if mid + 1 <= right:
            node.right = build(node, nums, mid + 1, right, False)
        else:
            step += 1
            clear()
            print(f"{CYAN}{'='*55}{RESET}")
            print(f"{BOLD}Шаг {step}: правое поддерево для {nums[mid]}{RESET}")
            print(f"{CYAN}{'='*55}{RESET}\n")
            print(f"  диапазон = [{mid+1}, {right}] — пустой")
            print(f"  left > right → right = {RED}None{RESET}")
            print()
            print(f"  {BOLD}Дерево на текущий момент:{RESET}")
            draw_tree(root)
            print()
            wait()
        
        return node
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Sorted Array → BST{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  массив = {nums}")
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  1. Берём середину диапазона")
    print(f"  2. Создаём узел, прикрепляем к родителю")
    print(f"  3. Левая половина → левое поддерево")
    print(f"  4. Правая половина → правое поддерево")
    print()
    print(f"  {YELLOW}[x]{RESET} — только что созданный узел")
    print(f"  {RED}x{RESET}   — вне текущего диапазона")
    print()
    wait()
    
    build(None, nums, 0, len(nums) - 1, False)
    
    # Финал
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Готово!{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    print(f"  массив = {nums}")
    print()
    draw_tree(root)
    print()
    print(f"  Дерево сбалансировано.")
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
