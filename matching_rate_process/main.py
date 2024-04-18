import heapq
import pandas as pd
from gensim.models import Word2Vec
from keyword_extract import extract_keywords_from_filename

filepath1 = r"C:\Users\28578\Desktop\问卷语料集\居民交通出行方式调查问卷.txt"
filepath2 = r"C:\Users\28578\Desktop\问卷语料集\新闻信息类互联网产品调查.txt"
filepath3 = r"C:\Users\28578\Desktop\问卷语料集\毕业生就业情况调查.txt"
filepath4 = r"C:\Users\28578\Desktop\问卷语料集\创业优惠政策对大学生创业影响的调查问卷.txt"
filepath5 = r"C:\Users\28578\Desktop\问卷语料集\关于购房需求的调查问卷.txt"
model_path = r"D:\Python\Questionnaire DRL\word_embedding\word2vec\4_16wiki.zh.text.model"
userdata_file_path = r"C:\Users\28578\Desktop\ti.xlsx"
common_words = ['使用', '对', '的', '是', '在', '有', '和', '就', '不', '人', '定位', '偏好',
                '都', '一', '一个', '调查', '问卷', '问卷调查', '分析', '统计', '关于', '问题',
                '情况', '有关', '市场', '去', '表', '看法', '调研', '“', '”', '《', '》', '全面', '.txt',
                '方式', '你', '我', '类', '产品', '了', '或', '或者', '基于', '习惯', '满意度', '全国', '及', '及其',
                '趋势', '中', '时', '影响', '当代', '现代', '当今', '状况', '现象', '主题', '认知', '认识', '观念',
                '观点',
                '了解', '结果', '效果', '评估', '质量', '反馈']
word32_list = [
    '数学', '物理', '化学', '生物', '地理', '科学', '互联网','电脑',
    '医学', '心理', '外语', '法律', '历史', '政治', '经济', '阅读',
    '写作', '宗教', '舞蹈', '乐器', '艺术', '休闲', '竞技', '激情',
    '汽车', '精致', '购物', '戏剧', '社交', '宠物', '园艺', '户外'
]
df = pd.read_excel(userdata_file_path, header=None)
keywords = extract_keywords_from_filename(filepath3, common_words)
len_keyword = len(keywords)
model = Word2Vec.load(model_path)


def get_word_matched_degree(model_path, word32_list, keyword, similarity_threshold=0.25, top_n=3):
    # 初始化空优先队列 保存匹配度及其对应词语
    matched_degree_heap = []
    # 初始化空列表 保存相似度
    filtered_single_matched_degree = []

    # 遍历词语列表，计算每个词语与关键词的相似度
    for word in word32_list:
        try:
            init_similarity = model.wv.similarity(word, keyword)  # 初始相似度init_similarity
            # 相似度与喜好程度的乘积 归一化得到single_matched_degree匹配度
            single_matched_degree = init_similarity * preferences[interests.tolist().index(word)] / 5
            if init_similarity > similarity_threshold:  # 设定相似度阈值 过滤低相似度的词语
                rounded_single_matched_degree = round(single_matched_degree, 3)
                # 尝试添加到优先队列中
                if len(matched_degree_heap) < top_n:
                    heapq.heappush(matched_degree_heap, (-rounded_single_matched_degree, word))  # heapq最小堆
                else:
                    # 如优先队列已满，则比较当前匹配度与队列中最小匹配度
                    if rounded_single_matched_degree > -matched_degree_heap[0][0]:
                        heapq.heapreplace(matched_degree_heap, (-rounded_single_matched_degree, word))

        except KeyError:
            pass

    # 取出优先队列中的元素，并放入filtered_weighted_similarities列表中
    while matched_degree_heap:
        sim, word = heapq.heappop(matched_degree_heap)
        filtered_single_matched_degree.append((-sim, word))  # 取出时取反以恢复原始相似度值

    return filtered_single_matched_degree


degrees_list = []
t = 0
for i in range(1, 1004):
    interests = df.iloc[0, :].values  # 兴趣名称
    preferences = df.iloc[i, :].values  # 喜好程度
    interest_dict = dict(zip(interests, preferences))
    preferences = [float(pref) for pref in preferences]

    sum_degree = 0
    average_degree = 0

    for keyword in keywords:
        matched_degree_sum = 0  # 初始化加权相似度总和为0
        matched_words = get_word_matched_degree(model_path, word32_list, keyword)

        # 遍历匹配词及其相似度
        for degree, word in matched_words:
            if degree > 0.15:
                matched_degree_sum += degree

        sum_degree += matched_degree_sum
        average_degree = sum_degree / len_keyword

    # print(f"The user{i} final matched degree  is: {round(average_degree, 3)}")
    degrees_list.append(average_degree)
    if round(average_degree, 3) > 1:
        t += 1
print(t)
# 计算最大值、最小值、平均值和中位数
max_degree = max(degrees_list)
min_degree = min(degrees_list)
mean_degree = sum(degrees_list) / len(degrees_list)
median_degree = sorted(degrees_list)[len(degrees_list) // 2] if len(degrees_list) % 2 != 0 \
    else (sorted(degrees_list)[len(degrees_list) // 2 - 1] + sorted(degrees_list)[len(degrees_list) // 2]) / 2

# 输出结果
print(f"Max degree: {max_degree}")
print(f"Min degree: {min_degree}")
print(f"Mean degree: {mean_degree}")
print(f"Median degree: {median_degree}")

normalized_degrees_list = [round((degree - min_degree+0.04) / (max_degree - min_degree+0.08),3)for degree in degrees_list]
print("处理后")
# 打印归一化后的数据
# print(normalized_degrees_list)
max_degree = max(normalized_degrees_list)
min_degree = min(normalized_degrees_list)
mean_degree = sum(normalized_degrees_list) / len(normalized_degrees_list)
median_degree = sorted(normalized_degrees_list)[len(normalized_degrees_list) // 2] \
    if len(normalized_degrees_list) % 2 != 0 \
    else (sorted(normalized_degrees_list)[len(normalized_degrees_list) // 2 - 1]
          + sorted(normalized_degrees_list)[len(normalized_degrees_list) // 2]) / 2

# 输出结果
print(f"Max degree: {max_degree}")
print(f"Min degree: {min_degree}")
print(f"Mean degree: {mean_degree}")
print(f"Median degree: {median_degree}")
