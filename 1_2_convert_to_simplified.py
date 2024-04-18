import opencc


def convert_traditional_to_simplified(input_file, output_file):
    # 初始化OpenCC转换器
    converter = opencc.OpenCC('t2s.json')  # t2s.json 是繁体转简体的配置文件

    # 打开输入和输出文件
    with open(input_file, 'r', encoding='utf-8') as f_in, \
            open(output_file, 'w', encoding='utf-8') as f_out:
        # 逐行读取并转换
        for line in f_in:
            simplified_line = converter.convert(line)
            f_out.write(simplified_line)

        # 使用函数进行转换


input_file = 'wiki.zh.txt'  # 假设你的繁体中文语料文件名为 wiki.zh.txt
output_file = 'wiki.zh.simp.txt'  # 转换后的简体中文文件名
convert_traditional_to_simplified(input_file, output_file)
