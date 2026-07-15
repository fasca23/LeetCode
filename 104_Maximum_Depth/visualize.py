"""
Визуализация поиска максимальной глубины дерева (DFS со стеком).
Управление: Enter — шаг, q — выход.
"""

import os
import sys
from collections import deque

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


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


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


def visualize(values):
    root = build_tree(values)
    step = 0
    max_depth = 0
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Maximum Depth — DFS со стеком{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  Дерево: {values}")
    print()
    if root:
        draw_tree(root)
    print()
    print(f"  {BOLD}Алгоритм:{RESET}")
    print(f"  Стек хранит пары: (узел, глубина_этого_узла).")
    print(f"  pop → сравниваем depth с max_depth →")
    print(f"  → push детей с depth+1")
    print()
    print(f"  {BOLD}Переменные:{RESET}")
    print(f"  max_depth — максимальная глубина (ответ)")
    print(f"  stack    — список пар (узел, глубина)")
    print(f"  node     — текущий узел (из pop)")
    print(f"  depth    — глубина текущего узла")
    print()
    wait()
    
    if not root:
        print(f"  {RED}Пустое дерево → max_depth = 0{RESET}\n")
        return
    
    # Начальное состояние
    stack = [(root, 1)]
    
    clear()
    print(f"{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}Начальное состояние{RESET}")
    print(f"{CYAN}{'='*55}{RESET}\n")
    print(f"  max_depth = {RED}0{RESET}")
    print(f"  stack     = [({root.val}, 1)]")
    print()
    print(f"  Кладём корень ({root.val}, 1) в стек.")
    print(f"  Глубина корня = 1.")
    print()
    wait()
    
    while stack:
        step += 1
        node, depth = stack.pop()
        old_max = max_depth
        
        # Проверяем: новый максимум?
        is_new_max = depth > max_depth
        if is_new_max:
            max_depth = depth
        
        clear()
        print(f"{CYAN}{'='*55}{RESET}")
        print(f"{BOLD}Шаг {step}: pop из стека{RESET}")
        print(f"{CYAN}{'='*55}{RESET}\n")
        
        # Дерево
        draw_tree(root, node)
        print()
        
        # Таблица переменных
        print(f"  ┌────────────┬──────────────────────┐")
        print(f"  │ Переменная │ Значение             │")
        print(f"  ├────────────┼──────────────────────┤")
        print(f"  │ node       │ {YELLOW}{node.val}{RESET:<20} │")
        print(f"  │ depth      │ {depth:<20} │")
        print(f"  │ max_depth  │ {old_max} → {max_depth if is_new_max else old_max:<20} │")
        if is_new_max:
            print(f"  │            │ {GREEN}↑ новый максимум!{RESET}   │")
        print(f"  ├────────────┼──────────────────────┤")
        
        # Стек
        if stack:
            print(f"  │ stack      │ ({stack[-1][0].val}, {stack[-1][1]}) ← верх   │")
            for n, d in reversed(stack[1:]):
                print(f"  │            │ ({n.val}, {d})             │")
        else:
            print(f"  │ stack      │ (пуст)               │")
        print(f"  └────────────┴──────────────────────┘")
        print()
        
        # Действие
        print(f"  {BOLD}Действие:{RESET}")
        print(f"  pop → узел {YELLOW}{node.val}{RESET}, его глубина = {depth}")
        print(f"  Сравниваем: depth ({depth}) > max_depth ({old_max})?")
        print(f"  → {GREEN if is_new_max else RED}{is_new_max}{RESET}")
        if is_new_max:
            print(f"  → max_depth = {GREEN}{depth}{RESET}")
        print()
        
        # Дети
        children = []
        if node.left:
            children.append(("left", node.left))
        if node.right:
            children.append(("right", node.right))
        
        if children:
            print(f"  {BOLD}Добавляем детей:{RESET}")
            for side, child in children:
                print(f"  push ({child.val}, depth+1) = ({child.val}, {depth + 1})  ← {side}")
                stack.append((child, depth + 1))
        else:
            print(f"  {GREEN}Лист!{RESET} Детей нет → ничего не добавляем")
            print(f"  Глубина этого листа = {depth}")
        
        print()
        wait()
    
    # Финал
    clear()
    print(f"{GREEN}{'='*55}{RESET}")
    print(f"{BOLD}Результат{RESET}")
    print(f"{GREEN}{'='*55}{RESET}\n")
    draw_tree(root)
    print()
    print(f"  ┌────────────┬──────────────────────┐")
    print(f"  │ Переменная │ Значение             │")
    print(f"  ├────────────┼──────────────────────┤")
    print(f"  │ stack      │ (пуст)               │")
    print(f"  │ max_depth  │ {GREEN}{max_depth}{RESET:<20} │")
    print(f"  └────────────┴──────────────────────┘")
    print()
    print(f"  {BOLD}Максимальная глубина: {GREEN}{max_depth}{RESET}")
    print()


if __name__ == "__main__":
    examples = [
        [3, 9, 20, None, None, 15, 7],
        [1, None, 2],
        [1, 2, 3, 4, 5, 6, 7],
    ]
    
    for values in examples:
        print(f"\n{CYAN}{values}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(values)
        print()
