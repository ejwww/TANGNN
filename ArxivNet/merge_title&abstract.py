import json


# 此函数将递归地修改嵌套字典中的数据
def modify_entry(entry):
    if 'title' in entry and 'abstract' in entry:
        entry['title-abstract'] = f"{entry['title']}: {entry['abstract']}"
    if 'citing_title' in entry and 'citing_abstract' in entry:
        entry['citing_title-abstract'] = f"{entry['citing_title']}: {entry['citing_abstract']}"

    # 对于字典中的嵌套字典，递归调用此函数
    for key, value in entry.items():
        if isinstance(value, dict):
            modify_entry(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    modify_entry(item)


# 此函数接收 JSON 文件路径，读取数据，并递归地修改每条记录
def modify_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if isinstance(data, dict):
        modify_entry(data)
    elif isinstance(data, list):
        for item in data:
            modify_entry(item)

    return data


# 请替换为您的 JSON 文件路径
json_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_sentiment.json'

# 修改 JSON 数据
modified_json_data = modify_json_data(json_file_path)

# 请替换为您希望保存输出文件的路径
output_json_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_merged_title&abstract.json'
with open(output_json_file_path, 'w', encoding='utf-8') as file:
    json.dump(modified_json_data, file, indent=4, ensure_ascii=False)
