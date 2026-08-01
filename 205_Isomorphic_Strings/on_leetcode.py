class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Два словаря для взаимно-однозначного отображения
        # s→t и t→s
        map_st = {}  # символ s → символ t
        map_ts = {}  # символ t → символ s
        
        for ch_s, ch_t in zip(s, t):
            # Проверяем прямое отображение s→t
            if ch_s in map_st and map_st[ch_s] != ch_t:
                # ch_s уже связан с ДРУГИМ символом t
                return False
            
            # Проверяем обратное отображение t→s
            if ch_t in map_ts and map_ts[ch_t] != ch_s:
                # ch_t уже связан с ДРУГИМ символом s
                return False
            
            # Сохраняем связи
            map_st[ch_s] = ch_t
            map_ts[ch_t] = ch_s
        
        return True
