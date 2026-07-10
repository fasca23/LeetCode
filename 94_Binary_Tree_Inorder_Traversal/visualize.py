"""
Визуализация inorder-обхода — таблица с деревом.
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


def collect_all_nodes(root):
    nodes = []
    def dfs(node):
        if node is None:
            return
        nodes.append(node)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return nodes


def visible_len(s):
    """Длина строки без ANSI-кодов."""
    import re
    return len(re.sub(r'\033\[[0-9;]*m', '', s))


def pad_right(s, width):
    """Дополняет справа пробелами до видимой ширины."""
    need = width - visible_len(s)
    return s + ' ' * max(0, need)


def visualize(values):
    root = build_tree(values)
    if not root:
        print(f"  {RED}Пустое дерево → []{RESET}\n")
        return
    
    all_nodes = collect_all_nodes(root)
    node_index = {node: i + 1 for i, node in enumerate(all_nodes)}
    
    result = []
    stack = []
    current = root
    done_nodes = set()
    step = 0
    history = []
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def get_status(node):
        if node == current:
            return f"{YELLOW}[cur]{RESET}"
        if node in done_nodes:
            return f"{GREEN}✓{RESET}"
        if node in stack:
            pos = stack.index(node) + 1
            return f"{CYAN}#{pos}{RESET}"
        return "·"
    
    def show():
        # Фаза
        if current:
            print(f"  {YELLOW}▼ СПУСК{RESET}")
        else:
            print(f"  {GREEN}▲ ПОДЪЁМ{RESET}")
        print()
        
        # Таблица: # | Узел | Дети | Ст
        print(f"  #  Узел  Дети      Стек")
        print(f"  ────────────────────────")
        
        for node in all_nodes:
            num = str(node_index[node])
            val = str(node.val)
            left_val = str(node.left.val) if node.left else "·"
            right_val = str(node.right.val) if node.right else "·"
            kids = f"L:{left_val} R:{right_val}"
            status = get_status(node)
            
            print(f"  {num:<2} {val:<4} {kids:<10} {status}")
        
        print(f"  ────────────────────────")
        
        # Стек
        if stack:
            stack_vals = " → ".join([f"{CYAN}{n.val}{RESET}" for n in stack])
            print(f"  Стек:      {stack_vals}")
        else:
            print(f"  Стек:      пуст")
        
        # Результат
        if result:
            res_vals = " → ".join([f"{GREEN}{v}{RESET}" for v in result])
            print(f"  Результат: {res_vals}")
        else:
            print(f"  Результат: —")
        
        print()
        
        # История
        if history:
            print(f"  История:")
            for h in history:
                print(f"    {h}")
            print()
    
    clear()
    print(f"{CYAN}  Inorder: левый → корень → правый{RESET}")
    print(f"  {YELLOW}[cur]{RESET} — cur  |  {CYAN}#N{RESET} — стек  |  {GREEN}✓{RESET} — готово  |  · — ждёт")
    print()
    
    history.append(f"Начало: cur = root ({root.val})")
    show()
    wait()
    
    while current or stack:
        step += 1
        
        if current:
            action = f"▼ push {current.val}, cur = cur.left"
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            action = f"▲ pop {current.val} → результат, cur = cur.right"
            result.append(current.val)
            done_nodes.add(current)
            current = current.right
        
        history.append(f"Шаг {step}: {action}")
        if len(history) > 4:
            history.pop(0)
        
        clear()
        print(f"{CYAN}  Шаг {step}: {action}{RESET}")
        print()
        show()
        wait()
    
    # Финал
    clear()
    print(f"{GREEN}  Готово!{RESET}")
    print()
    print(f"  #  Узел  Дети        Ст")
    print(f"  ────────────────────────")
    for node in all_nodes:
        num = str(node_index[node])
        val = str(node.val)
        left_val = str(node.left.val) if node.left else "·"
        right_val = str(node.right.val) if node.right else "·"
        kids = f"L:{left_val} R:{right_val}"
        print(f"  {num:<2} {val:<4} {kids:<10} {GREEN}✓{RESET}")
    print(f"  ────────────────────────")
    res_vals = " → ".join([f"{GREEN}{v}{RESET}" for v in result])
    print(f"  Результат: {res_vals}")
    print()


if __name__ == "__main__":
    examples = [
        [1, None, 2, 3],
        [1, 2, 3, 4, 5],
        [5, 3, 8, 2, 4, 7, 9, 1, None, None, None, 6],
    ]
    
    for values in examples:
        print(f"\n{CYAN}Дерево: {values}{RESET}")
        input(f"{YELLOW}Enter для запуска{RESET} ")
        visualize(values)
        print()