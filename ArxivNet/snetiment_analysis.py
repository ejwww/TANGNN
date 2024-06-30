import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained("C:\\Users\\admin\\PycharmProjects\\pythonProject\\scibert")
model = AutoModelForSequenceClassification.from_pretrained("C:\\Users\\admin\\PycharmProjects\\pythonProject\\scibert")

def sentiment_analysis(sentence):
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    probs = softmax(outputs.logits, dim=1)
    sentiment_score = torch.argmax(probs, dim=1).item() - 1  # 转换为 -1, 0, 1
    return sentiment_score

emotion_mapping = {
    -1: "Negative",
    0: "Neutral",
    1: "Positive"
}

# 读取输入文件
with open('C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_merged.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 情感分析并添加结果
for entry in data:
    if 'numbers_to_sentence' in entry:
        for number, sentence in entry['numbers_to_sentence'].items():
            sentiment_score = sentiment_analysis(sentence)
            entry['numbers_to_sentence'][number] = f"{emotion_mapping[sentiment_score]}: {sentence}"

# 保存结果到新的 JSON 文件
with open('C:\\Users\\admin\\PycharmProjects\\pythonProject\\processed_sentiment.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)
