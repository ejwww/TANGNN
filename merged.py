import json

# 加载 JSON 数据
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 保存 JSON 数据
def save_json_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 将 sentences 添加到相应的 numbers 中
def add_sentences_to_numbers(sentences_file_path, numbers_file_path, output_file_path):
    # 加载文件数据
    sentences_data = load_json_data(sentences_file_path)
    numbers_data = load_json_data(numbers_file_path)

    # 创建一个 dict，映射 cite_number 到 sentence
    cite_number_to_sentence = {entry['cite_number']: entry['sentence'] for entry in sentences_data}

    # 遍历 numbers 数据，添加 sentences
    for entry in numbers_data:
        # 对于每个 paper_id，创建一个新的 key-value 对
        paper_id = entry['paper_id']
        numbers_to_sentence = {}
        for number in entry['numbers']:
            # 只有当 cite_number 在 sentences 文件中时才添加
            if number in cite_number_to_sentence:
                numbers_to_sentence[number] = cite_number_to_sentence[number]
        # 只有当 numbers_to_sentence 不为空时才添加到 entry 中
        if numbers_to_sentence:
            entry['numbers_to_sentence'] = numbers_to_sentence

    # 保存更新后的 JSON 数据
    save_json_data(numbers_data, output_file_path)

# 定义文件路径
sentences_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\output.json'  # 第一个 JSON 文件的路径
numbers_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data_vevtors.json'  # 第二个 JSON 文件的路径
output_file_path = 'C:\\Users\\admin\PycharmProjects\\pythonProject\\processed_merged.json'  # 输出文件的路径

# 执行函数
add_sentences_to_numbers(sentences_file_path, numbers_file_path, output_file_path)
