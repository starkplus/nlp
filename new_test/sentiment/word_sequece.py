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
        # """
        # 把单个句子保存在dict中
        # sentence：文本中的句子
        # """
        for word in sentence:
            self.count[word]=self.count.get(word,0) + 1
    def build_vocab(self,min=5,max=None,max_feature=None):
        # """
        # 构建词汇表
        # min为单词最小出现次数
        # max为单词最大出现次数
        # max_feature一共保留多少个词语
        # min和max单词转换向量的时候防止出现只出现一次也转换
        # 见证性考虑？
        # """
        if min is not None:
            self.count={word:value for word,value in self.count.items() if value>min}
        if max is not None:
            self.count={word:value for word,value in self.count.items() if value<max}
        if max_feature is not None:
            temp = sorted(self.count.items(),key=lambda x:x[-1],reverse=True)[max_feature]
            self.count =dict[temp]
        for word in self.count:
            self.dict[word]=len(self.dict)
        #反转字典？感觉没啥用
        self.inverse_dict =dict(zip(self.dict.values(),self.dict.keys()))
    def transform(self,sentence,max_len=None):
        # """
        # 把句子转换序列：单词-编号
        # 为了处理把长句子截断，短句子填充
        # 因为神经网络模型的输入中必须是长度相同的参数
        # """
        if max_len is not None:
            if max_len<len(sentence):
                sentence=sentence+[self.PAD_TAG]*(max_len-len(sentence))
            if max_len>len(sentence):
                sentence=sentence[:max_len]
        return [self.dict.get(word,self.UNK) for word in sentence]
    def inverse_transform(self,indices):
        # """
        # 实现从序列转化为单词
        # :param indices:[1,2,3,4...]
        # :return: [word1,word2,word3...]
        # """
        return [self.inverse_dict.get(idx) for idx in indices]
    def __len__(self):
        return len(self.dict)
    

 
# 测试整体 ：  

# if __name__=='__main__':

#     ws=Word2Sequence()
#     ws.fit(['我shi','是','谁'])

#     ws.fit(['a','s','ws'])

#     ws.fit(['a','s','ws'])

#     ws.build_vocab(min=0)

#     print(ws.dict)



# # 创建两个实例s
# word_sequence1 = Word2Sequence()
# word_sequence2 = Word2Sequence()

# # 修改第一个实例的字典
# word_sequence1.dict["NEW_WORD"] = 2

# # 查看两个实例的字典
# print(word_sequence1.dict)  # 输出: {'UNK': 0, 'PAD': 1, 'NEW_WORD': 2}
# print(word_sequence2.dict)  # 输出: {'UNK': 0, 'PAD': 1}
