
---


## severity_predictor.py


```python
"""
severity_predictor.py
Train a baseline severity classifier and save the trained model + vectorizer.
Usage:
python severity_predictor.py --data data/github_issues.csv --out model.joblib
"""
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os




def load_data(path):
df = pd.read_csv(path)
# minimal validation
assert 'issue_text' in df.columns and 'severity' in df.columns, 'CSV must have issue_text and severity columns'
df = df.dropna(subset=['issue_text','severity'])
return df




def train(df):
X = df['issue_text'].astype(str)
y = df['severity'].astype(str)


vec = TfidfVectorizer(stop_words='english', max_df=0.9, min_df=2)
Xv = vec.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(Xv, y, test_size=0.2, random_state=42)


clf = LogisticRegression(max_iter=300)
clf.fit(X_train, y_train)


preds = clf.predict(X_test)
print('Evaluation:')
print(classification_report(y_test, preds))


return vec, clf




def save_model(vec, clf, out_path):
os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
joblib.dump({'vectorizer': vec, 'model': clf}, out_path)
print('Saved model to', out_path)


save_model(vec, clf, args.out)
