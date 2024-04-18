import jieba
import os
from gensim.models import Word2Vec

model_path = r"D:\Python\Questionnaire DRL\word_embedding\word2vec\4_16wiki.zh.text.model"
model = Word2Vec.load(model_path)


def extract_keywords_from_filename(filepath, common_words, num_keywords=4):
    filename = os.path.basename(filepath)
    pure_filename = os.path.splitext(filename)[0]   # 去后缀名
    seg_list = jieba.cut(pure_filename, cut_all=False)   # 分词
    words = list(seg_list) # 将分词结果转换为列表
    # 过滤常用词
    filtered_words = [word for word in words if word not in common_words and word in model.wv.key_to_index]
    # 选择剩下的词中长度最长的num_keywords个
    keywords = sorted(filtered_words, key=len, reverse=True)[:num_keywords]
    return keywords





