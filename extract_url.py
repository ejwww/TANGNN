import json
import requests
from xml.etree import ElementTree
import time

def get_arxiv_paper_info(arxiv_id):
    try:
        url = f'http://export.arxiv.org/api/query?id_list={arxiv_id}'
        response = requests.get(url)

        if response.status_code == 200:
            root = ElementTree.fromstring(response.content)
            entry = root.find('{http://www.w3.org/2005/Atom}entry')
            if entry is not None:
                title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
                return title, summary
    except requests.exceptions.ConnectionError:
        print(f"Connection error encountered. Retrying for arXiv ID: {arxiv_id} after 5 seconds.")
        time.sleep(5)  # 重试前暂停5秒
        return get_arxiv_paper_info(arxiv_id)  # 递归地重试
    except Exception as e:
        print(f"An error occurred: {e}")
    return None, None

def update_data_with_arxiv_info(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for entry in data:
        if 'arxiv_ids' in entry:
            entry['citing_papers'] = []  # 创建一个空列表来保存引用论文的信息
            for arxiv_id in entry['arxiv_ids']:
                citing_title, citing_abstract = get_arxiv_paper_info(arxiv_id)
                if citing_title and citing_abstract:
                    entry['citing_papers'].append({
                        'arxiv_id': arxiv_id,
                        'citing_title': citing_title,
                        'citing_abstract': citing_abstract
                    })

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data updated and saved to {output_file}")

# 使用示例
input_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data.json'
output_file_path = 'C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_data_citing.json'

update_data_with_arxiv_info(input_file_path, output_file_path)
