# 208. Implement Trie
"""
a, ant, cat, and

              {a, c} 
           /         \ 
     {n, "#":True}    {a}
     /               /
  {t, d}          {t}
 /     \         /       
{"#":True}  {"#": True}

"""
class Trie:
    def __init__(self):
        self.dic = {}

    def insert(self, word):
        cur = self.dic # set pointer to the trie root
        for w in word:
            if w not in cur:
                cur[w] = {} # create the sub dict
            cur = cur[w]
        cur["#"] = True

    def search(self, word): # --> boolean
        cur = self.dic
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return cur["#"]==True

    def startWith(self, word): # --> boolean
        cur = self.dic
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        return True            


# 14	Longest Common Prefix	42.8%	Easy

# 588	Design In-Memory File System48.1%	Hard	
    

# 1268	Search Suggestions System	65.2%	Medium	
# 1166	Design File System 62.8%	Medium	
# 642	Design Search Autocomplete System 48.9%	Hard	
# 139	Word Break	46.8%	Medium	
# 140	Word Break II	48.0%	Hard	
# 212	Word Search II