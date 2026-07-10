"""
Визуализация inorder-обхода — схема с портами + стек + история.
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


def visualize(values):
    root = build_tree(values)
    if not root:
        print(f"  {RED}Пустое дерево → []{RESET}\n")
        return
    
    result = []
    stack = []
    current = root
    done_nodes = set()
    step = 0
    history = []  # последние 4 действия
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def wait():
        key = input(f"\n{YELLOW}Enter — дальше, q — выход{RESET} ")
        if key.lower() == 'q':
            sys.exit(0)
    
    def draw_node(val, left_val, right_val, state):
        """Узел с портами."""
        if state == 'cur':
            c = YELLOW
            l = f"{c} L {RESET}"
            v = f"{c}[{val}]{RESET}"
            r = f"{c} R {RESET}"
        elif state == 'stack':
            c = CYAN
            l = f"{c} L {RESET}"
            v = f"{c} {val} {RESET}"
            r = f"{c} R {RESET}"
        elif state == 'done':
            c = GREEN
            l = f"{c} L {RESET}"
            v = f"{c} {val} {RESET}"
            r = f"{c} R {RESET}"
        else:
            l = " L "
            v = f" {val} "
            r = " R "
        
        left_label = f"{left_val}" if left_val is not None else "·"
        right_label = f"{right_val}" if right_val is not None else "·"
        
        print(f"  ┌───┬───┬───┐     left={left_label}  right={right_label}")
        print(f"  │{l}│{v}│{r}│")
        print(f"  └───┴───┴───┘")
    
    def show():
        # Фаза
        if current:
            print(f"  {BOLD}Фаза:{RESET} {YELLOW}▼ СПУСК (push){RESET} — идём влево, кладём в стек")
        else:
            print(f"  {BOLD}Фаза:{RESET} {GREEN}▲ ПОДЪЁМ (pop){RESET} — достаём из стека, идём вправо")
        print()
        
        # Текущий узел
        if current:
            left_val = current.left.val if current.left else None
            right_val = current.right.val if current.right else None
            print(f"  {BOLD}cur:{RESET}")
            draw_node(current.val, left_val, right_val, 'cur')
        else:
            print(f"  {BOLD}cur:{RESET} {RED}None{RESET} — левее некуда, сейчас будет pop")
        print()
        
        # Стек с нумерацией
        print(f"  {BOLD}Стек ({len(stack)} шт.):{RESET}")
        if stack:
            for i, node in enumerate(reversed(stack)):
                num = len(stack) - i
                arrow = " ← верх" if i == 0 else ""
                print(f"  #{num}  {CYAN}[L={node.left.val if node.left else '·'}]→({node.val})→[R={node.right.val if node.right else '·'}]{RESET}{arrow}")
        else:
            print(f"  (пуст)")
        print()
        
        # Результат
        if result:
            print(f"  {BOLD}Результат:{RESET} {GREEN}{' → '.join(map(str, result))}{RESET}  ({len(result)} шт.)")
        else:
            print(f"  {BOLD}Результат:{RESET} —")
        print()
        
        # История
        if history:
            print(f"  {BOLD}История:{RESET}")
            for h in history:
                print(f"    {h}")
        print()
    
    clear()
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}Inorder Traversal: левый → корень → правый{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    print(f"  {YELLOW}[x]{RESET} cur  |  {CYAN}x{RESET} стек  |  {GREEN}x{RESET} готово")
    print()
    
    history.append(f"{YELLOW}●{RESET} Начало: cur = root ({root.val})")
    show()
    wait()
    
    while current or stack:
        step += 1
        
        if current:
            action = f"Шаг {step}: {YELLOW}▼ push {current.val}{RESET} в стек, cur = cur.left"
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            action = f"Шаг {step}: {GREEN}▲ pop {current.val}{RESET} → результат, cur = cur.right"
            result.append(current.val)
            done_nodes.add(current)
            current = current.right
        
        history.append(action)
        if len(history) > 4:
            history.pop(0)
        
        clear()
        print(f"{CYAN}{'='*60}{RESET}")
        print(f"{action}")
        print(f"{CYAN}{'='*60}{RESET}\n")
        show()
        wait()
    
    clear()
    print(f"{GREEN}{'='*60}{RESET}")
    print(f"{BOLD}Готово!{RESET}")
    print(f"{GREEN}{'='*60}{RESET}\n")
    print(f"  {BOLD}Результат:{RESET} {GREEN}{' → '.join(map(str, result))}{RESET}")
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
