Correct order of application：
extract_id.py -> extract_url.py -> abstract_convert.py -> extract_sentence.py -> merged.py -> sentiment_analysis.py -> merge_title&abstract.py -> merged_title&abstract_sentiment.py -> clean.py -> predict.py

# Project Workflow and Description

## Correct Order of Application
1. `extract_id.py` - Extract ID
2. `extract_url.py` - Extract URL
3. `abstract_convert.py` - Abstract Convert
4. `extract_sentence.py` - Extract Sentence
5. `merged.py` - Merge Data
6. `sentiment_analysis.py` - Sentiment Analysis
7. `merge_title&abstract.py` - Merge Title & Abstract
8. `merged_title&abstract_sentiment.py` - Merge Title & Abstract Sentiment
9. `clean.py` - Clean Data
10. `predict.py` - Predict

## Script Descriptions

### `extract_id.py`
Extracts IDs from the data.

### `clean.py`
This script cleans the dataset. It removes the three emotions previously processed by SciBERT and re-labels emotions using the DictSentiBERT model. 

#### Process Description:
1. **Load Pre-trained Model**: Load the pre-trained DictSentiBERT model.
2. **Tokenization**: Each sentence is processed through a tokenizer to convert the text into a format readable by the model.
3. **Sentiment Prediction**: The model predicts the probability distribution of emotion categories (negative, neutral, positive) using the softmax function.
4. **Labeling**: The category with the highest probability is selected as the emotional score, and this score is mapped to the corresponding emotional label (negative, neutral, or positive).
5. **Save Results**: Each sentence is labeled with this emotion label, and the labeled data is saved back to the JSON file, updating the specific sentiment labels for each citation.

### Partial Dataset
Partial datasets are shown in the `processed01` directory.

### Complete Dataset
The complete dataset can be accessed via the following link: 
[Complete Dataset](https://pan.baidu.com/s/1s0ZKq5pE8qMAfzGYw_Hj2g?pwd=8688) 
Extraction code: `8688`

