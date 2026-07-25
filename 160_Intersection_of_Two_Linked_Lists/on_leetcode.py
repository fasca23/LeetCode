class Solution:
    def getIntersectionNode(self, headA, headB):
        # Два указателя: pA идёт по A, pB по B
        pA = headA
        pB = headB
        
        # Идём пока указатели не встретятся
        # Если пересечение есть — встретятся на нём
        # Если нет — оба станут None одновременно
        while pA != pB:
            # pA: если дошли до конца A → переходим на B
            # Иначе идём дальше по A
            pA = pA.next if pA else headB
            
            # pB: если дошли до конца B → переходим на A
            # Иначе идём дальше по B
            pB = pB.next if pB else headA
        
        # pA == pB: либо узел пересечения, либо None
        return pA
