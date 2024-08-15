#coding utf-8?实际上我也不知道我是不是utf-8
#1.定义tokennize方法正则模块把各种符号！等替换掉
import re
import os
import pickle
from word_sequece import Word2Sequence



def tokenize(text):
    fileters = ['!', '"', '#', '$', '%', '&', '\(','\)', '\*','\+' ,',' ,'-','\.','/',':',';',
                '<','=','>','\?','@','\[','\\','\]','^','_','`','\{','\|','\}','~','\t','\n',
                '\x97','\x96','”','“']
    text = re.sub("<.*?>"," ",  text, flags=re.S)
    text = re.sub("|".join(fileters)," ", text, flags=re.S)
    return [i.strip() for i in text.split()]

if __name__=='__main__':
    ws = Word2Sequence()
    path='D:/AAAcode/Datassets/IMDB/aclImdb/train'
    print(path)
    #new_test/sentiment/aclImdb/train
    #D:/AAAcode/nlp/nlp/new_test/sentiment/aclImdb/train
    #由于放sentiment就无法git传上去，所以更改到本地
    #"D:\AAAcode\Datassets\IMDB\aclImdb"
    temp_data_path = [os.path.join(path,"pos"),os.path.join(path,"neg")]
    for data_path in temp_data_path:
        file_paths = [os.path.join(data_path,file_name) for file_name in os.listdir(data_path)]
        for file_path in file_paths[1:100]:
            sentence = tokenize(open(file_path,encoding='utf-8').read())
            ws.fit(sentence)
     
    ws.build_vocab(min=10)
    print(ws.dict)
    # 指定保存路径和文件名
    save_directory = 'D:/AAAcode/nlp/nlp/new_test/sentiment/'  # 替换为你的实际路径
    file_name = 'ws.pkl'
    full_path = os.path.join(save_directory, file_name)

    # 保存词汇表为PKL格式
    with open(full_path, 'wb') as f:
        pickle.dump(ws, f)

    print(f"Vocabulary has been saved as '{full_path}'.")
