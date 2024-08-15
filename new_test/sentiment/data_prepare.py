import os 
import pickle
import torch
from torch.utils.data import Dataset,DataLoader
from word_save import tokenize
#set帮助读取，Loader帮助批量方式加载

path='D:/AAAcode/Datassets/IMDB/aclImdb'
ws=pickle.load(open('D:/AAAcode/nlp/nlp/new_test/sentiment/ws.pkl','rb')) 

class ImdbDataset(Dataset):
    def __init__(self,mode):#mode 数据集模式
        #套路：调用父类的方法初始化子类继承的属性
        super(ImdbDataset,self).__init__()
        if mode == 'train':
            text_path = [os.path.join(path,i) for i in ["train/neg","train/pos"]]
        else: 
            text_path = [os.path.join(path,i) for i in ["test/neg","test/pos"]]
        self.total_file_path=[]
        for i in text_path:
            self.total_file_path.extend([os.path.join(i,j) for j in os.listdir(i)])

    def __getitem__(self, idx):
        
        cur_path= self.total_file_path[idx]
        cur_filename=os.path.basename(cur_path)#?basename是已经有的库函数吗
        print(cur_path)
        #用于test打印的是哪个文件
        label = int(cur_filename.split("_")[-1].split(".")[0]) -1#处理标题获取label，转换为0~9
        text = tokenize(open(cur_path,encoding='utf-8').read().strip())
        return label,text
    def __len__(self):
        return len(self.total_file_path)

#def 

#测试datase
if __name__=='__main__':
    dataset=ImdbDataset(mode='train')
    
    print(dataset[1])