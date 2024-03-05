import json
import re

def load_numbers_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        numbers = []
        for entry in data:
            # 提取arxiv_id_to_number映射字典
            arxiv_id_to_number = entry.get('arxiv_id_to_number', {})
            # 遍历映射字典，添加所有number到列表中
            for number in arxiv_id_to_number.values():
                if number:
                    numbers.append(number)
        return numbers

def extract_sentences_from_jsonl(jsonl_file_path, numbers):
    extracted_data = {}
    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            entry = json.loads(line)
            paper_id = entry.get('paper_id', '')
            if 'body_text' in entry:
                for paragraph in entry['body_text']:
                    text = paragraph.get('text', '')
                    for number in numbers:
                        if '{{cite:' + number + '}}' in text:
                            sentence = extract_sentence(text, number)
                            if sentence:
                                # 检查是否已存在该号码段的句子，若存在则比较长度
                                key = (paper_id, number)
                                if key not in extracted_data or len(extracted_data[key]['sentence']) < len(sentence):
                                    extracted_data[key] = {
                                        'paper_id': paper_id,
                                        'cite_number': number,
                                        'sentence': sentence
                                    }
    return list(extracted_data.values())
def extract_sentence(text, number):
    pattern = r'([^.]*\{\{cite:' + re.escape(number) + r'\}\}[^.]*\.)'
    matches = re.findall(pattern, text)
    return ' '.join(matches)

# 输入文件路径
data_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data_vevtors.json'
jsonl_file_path = 'G:\\2\\unarXive_230324\\00\\arXiv_src_0006_001.jsonl'
output_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\output.json'

# 从 JSON 文件中加载号码段
numbers = load_numbers_from_json(data_file_path)
print("Loaded numbers:", numbers)  # 调试语句

# 从 JSONL 数据集中提取相关信息
extracted_data = extract_sentences_from_jsonl(jsonl_file_path, numbers)
print("Extracted data:", extracted_data)  # 调试语句


if not extracted_data:
    print("No data was extracted. Please check the input files and the logic.")

# 将提取到的信息保存到新的 JSON 文件
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(extracted_data, outfile, indent=4, ensure_ascii=False)
