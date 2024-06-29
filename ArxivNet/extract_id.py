import json

def extract_data_from_jsonl(file_path):
    extracted_data = []

    with open(file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)

            # 提取所需字段
            paper_id = entry.get('paper_id', '')
            title = entry.get('metadata', {}).get('title', '')
            abstract = entry.get('metadata', {}).get('abstract', '')

            # 初始化列表来存储arxiv_ids和numbers，以及它们的对应关系
            arxiv_ids = []
            numbers = []
            arxiv_id_to_number_map = {}

            for number, bib_entry in entry.get('bib_entries', {}).items():
                ids = bib_entry.get('ids', {})
                arxiv_id = ids.get('arxiv_id', '')
                if arxiv_id:
                    arxiv_ids.append(arxiv_id)
                    numbers.append(number)
                    arxiv_id_to_number_map[arxiv_id] = number

            # 如果有arxiv_id，则保存相关信息
            if arxiv_ids:
                extracted_data.append({
                    'paper_id': paper_id,
                    'title': title,
                    'abstract': abstract,
                    'arxiv_ids': arxiv_ids,  # 单独存储arxiv_ids
                    'numbers': numbers,  # 单独存储numbers
                    'arxiv_id_to_number': arxiv_id_to_number_map  # 存储arxiv_id与number的对应关系
                })

    return extracted_data

def save_data_to_json(output_file, data):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 使用示例
file_path = "G:\\2\\unarXive_230324\\00\\arXiv_src_0006_001.jsonl"                   #输入存储数据集的路径
output_file = "C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data.json"#输出保存文件的路径

extracted_data = extract_data_from_jsonl(file_path)
save_data_to_json(output_file, extracted_data)
