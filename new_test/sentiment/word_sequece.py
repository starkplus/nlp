class Word2Sequence:#单词转换为序列，2同to
    UNK_TAG="UNK"
    PAD_TAG="PAD"

    UNK=0
    PAD=1
    def __init__(self):
        self.dict = {
            self.UNK_TAG:self.UNK,
            self.PAD_TAG:self.PAD
        }
        self.count={}#词频统计
    def fit(self,sentence):
        """
        把单个句子保存在dict中
        sentence：文本中的句子
        """
        
        pass
# 创建两个实例s
word_sequence1 = Word2Sequence()
word_sequence2 = Word2Sequence()

# 修改第一个实例的字典
word_sequence1.dict["NEW_WORD"] = 2

# 查看两个实例的字典
print(word_sequence1.dict)  # 输出: {'UNK': 0, 'PAD': 1, 'NEW_WORD': 2}
print(word_sequence2.dict)  # 输出: {'UNK': 0, 'PAD': 1}