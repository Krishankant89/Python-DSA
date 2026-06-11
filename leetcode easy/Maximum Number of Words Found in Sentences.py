class Solution:
    
    def mostWordsFound(self, sentences: List[str]) -> str:
        
        max_word_count = 1 + max(s.count(' ')for s in sentences)
     
        return max_word_count