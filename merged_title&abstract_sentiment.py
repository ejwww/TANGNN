import json
import numpy as np
from transformers import AutoTokenizer, AutoModel

# 加载 Specter 模型和分词器
tokenizer, model = AutoTokenizer.from_pretrained("C:\\Users\\admin\\PycharmProjects\\pythonProject\\specter"), AutoModel.from_pretrained("C:\\Users\\admin\\PycharmProjects\\pythonProject\\specter")

# 函数：将文本转换为向量
def text_to_vector(text, tokenizer, model):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt", max_length=512)
    outputs = model(**inputs)
    # 取最后一层隐藏状态的平均值作为文本的向量表示
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy().flatten()
    return embeddings.tolist()  # 确保向量是一维数组

# 函数：修改 JSON 文件并添加向量
def process_entry(entry, tokenizer, model):
    if 'title-abstract' in entry:
        entry['title-abstract-vector'] = text_to_vector(entry['title-abstract'], tokenizer, model)
    if 'citing_title-abstract' in entry:
        entry['citing_title-abstract-vector'] = text_to_vector(entry['citing_title-abstract'], tokenizer, model)

    # 递归处理嵌套结构
    for key, value in entry.items():
        if isinstance(value, dict):
            process_entry(value, tokenizer, model)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    process_entry(item, tokenizer, model)


# 函数：修改 JSON 文件并添加向量
def modify_json_with_vectors(file_path, tokenizer, model):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if isinstance(data, dict):
        process_entry(data, tokenizer, model)
    elif isinstance(data, list):
        for item in data:
            process_entry(item, tokenizer, model)

    return data

# 输入和输出文件的路径
input_json_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_merged_title&abstract.json'
output_json_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\final_sentiment.json'

# 处理 JSON 文件并添加向量
modified_json_data = modify_json_with_vectors(input_json_file_path, tokenizer, model)

def convert_vectors_to_single_line(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list) and all(isinstance(x, (int, float)) for x in value):
                # 把数组转换为一行字符串
                data[key] = json.dumps(value)[1:-1]  # 移除开始和结尾的中括号
            else:
                convert_vectors_to_single_line(value)
    elif isinstance(data, list):
        for item in data:
            convert_vectors_to_single_line(item)

convert_vectors_to_single_line(modified_json_data)

# 保存修改后的 JSON 数据
with open(output_json_file_path, 'w', encoding='utf-8') as file:
    json.dump(modified_json_data, file, indent=4, ensure_ascii=False)


