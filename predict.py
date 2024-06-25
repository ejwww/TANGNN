import torch
from transformers import AutoTokenizer, AutoModel
from sentibert import SentiBert


class Predictor:
    def __init__(self, model_name='scibert', num_classes=3):
        # 初始化 tokenizer 和 base_model
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.base_model = AutoModel.from_pretrained(model_name)

        # 使用 SentiBert 模型，传入基模型和类别数
        self.model = SentiBert(base_model=self.base_model, num_classes=num_classes)

        # 加载训练好的模型权重
        model_path = "/Users/ejww/Desktop/experiment/DictSentiBERT-main/saved_models/scibert_sentibert_best.pth"  # 确保路径正确
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)

    def predict(self, texts):
        inputs = self.tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {key: val.to(self.device) for key, val in inputs.items()}

        # 模拟 attention_weights; 这需要根据您的具体应用适当生成
        attention_weights = torch.rand(inputs['input_ids'].shape[0], 1, 1, 1, device=self.device)
        inputs['attention_weights'] = attention_weights

        with torch.no_grad():
            predicts = self.model(inputs)
        sentiments = torch.argmax(predicts, dim=1).cpu().numpy().tolist()
        return sentiments


if __name__ == "__main__":
    predictor = Predictor(model_name='/Users/ejww/Desktop/experiment/DictSentiBERT-main/scibert', num_classes=3)
    sample_texts = ["Owing to its atomically thin structure and exceptional highmobilities,  graphene is potentially well suited to radiofrequency (RF) applications"]
    sentiments = predictor.predict(sample_texts)
    print(f"Sentiments: {sentiments}")
