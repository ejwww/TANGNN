import json
import torch
from transformers import AutoTokenizer, AutoModel

def load_specter_model():
    # 加载SPECTER模型和分词器
    tokenizer = AutoTokenizer.from_pretrained("C:\\Users\\admin\\PycharmProjects\\pythonProject\\specter")
    model = AutoModel.from_pretrained("C:\\Users\\admin\\PycharmProjects\\pythonProject\\specter")
    return tokenizer, model

def convert_text_to_vector(text, tokenizer, model):
    # 将文本转换为向量
    inputs = tokenizer([text], padding=True, truncation=True, return_tensors="pt", max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).tolist()  # 转换为列表以便JSON序列化

def process_json_file(input_json, output_json):
    # 加载模型
    tokenizer, model = load_specter_model()

    try:
        # 读取JSON文件
        with open(input_json, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("JSON file does not contain a list of entries.")

        # 为每篇论文及其引文生成摘要向量
        for entry in data:
            abstract = entry.get("abstract", "")
            entry["abstract_vector"] = ' '.join(map(str, convert_text_to_vector(abstract, tokenizer, model)))

            if "citing_papers" in entry:
                for citing_paper in entry["citing_papers"]:
                    citing_abstract = citing_paper.get("citing_abstract", "")
                    citing_paper["citing_abstract_vector"] = ' '.join(map(str, convert_text_to_vector(citing_abstract, tokenizer, model)))

        # 将更新后的数据写入新的JSON文件
        with open(output_json, 'w', encoding='utf-8') as out_file:
            json.dump(data, out_file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")

# 调用函数
process_json_file('C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data_citing.json', 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data_vevtors.json')
