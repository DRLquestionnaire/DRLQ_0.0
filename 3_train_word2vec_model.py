#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 使用gensim word2vec训练脚本获取词向量

# 导入必要的模块并设置忽略特定警告
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略gensim库的用户警告

# 日志记录和其他准备工作
import logging
import os.path
import sys
import multiprocessing

# 从gensim库导入处理Wiki数据的WikiCorpus类，以及Word2Vec模型和LineSentence工具
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    # 主程序逻辑开始，设置日志记录
    program = os.path.basename(sys.argv[0])  # 获取程序名称
    logger = logging.getLogger(program)  # 初始化日志记录器

    # 配置日志输出格式和级别
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))  # 记录程序启动日志

    # 定义输入输出文件路径
    fdir = 'D:/Python/Questionnaire DRL/word_embedding/word2vec/4_16'
    inp = r"D:\Python\Questionnaire DRL\word_embedding\word2vec\4_16\wiki_zh_word2vec\wiki.zh.simp.seg.txt"  # 输入语料路径
    outp1 = fdir + 'wiki.zh.text.model'  # 输出模型路径
    outp2 = fdir + 'wiki.zh.text.vector'  # 输出向量模型路径

    # 使用LineSentence处理输入文本，并训练Word2Vec模型
    # 参数说明：
    # size=400: 词向量的维度为300
    # window=5: 词与词之间的最大距离（即在一个句子中）为5
    # min_count=5: 忽略出现次数少于10次的词汇
    # workers=multiprocessing.cpu_count(): 使用所有可用的CPU核心进行训练
    model = Word2Vec(LineSentence(inp), vector_size=300, window=5, min_count=4, sg=0,
                     workers=multiprocessing.cpu_count())

    # 保存训练得到的模型和向量文件
    model.save(outp1)  # 保存Word2Vec模型
    model.wv.save_word2vec_format(outp2, binary=False)  # 保存词向量文件（非二进制格式）
