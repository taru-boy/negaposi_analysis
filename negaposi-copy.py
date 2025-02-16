# 形態素解析をするためのjanomeをimport
from pprint import pprint

import pandas as pd
from janome.tokenizer import Tokenizer

# pandas

"""
データフレームを引数に受け取り、
ネガポジ分析をする関数
"""
# 極性辞書をPythonの辞書にしていく
# 日本語評価極性辞書のファイルの読み込み
with open("pn.csv.m3.120408.trim", "r", encoding="utf-8") as f:
    # 1行1行を読み込み、文字列からリスト化。リストの内包表記の形に
    lines = [line.strip().split("\t") for line in f.readlines()]

# リストからデータフレームの作成
posi_nega_df = pd.DataFrame(lines, columns=["word", "score", "expalin"])

# データフレームの2つの列から辞書の作成　zip関数を使う
np_dic = dict(zip(posi_nega_df["word"], posi_nega_df["score"]))

# 形態素解析をするために必要な記述を書いていく
tokenizer = Tokenizer()
# ツイート一つ一つを入れてあるデータフレームの列（本文の列）をsentensesと置く
df_tweet = pd.read_csv("tweet_data.csv")
sentences = df_tweet["本文"]
# p,n,e,?p?nを数えるための辞書を作成
result = {"p": 0, "n": 0, "e": 0, "?p?n": 0}
# ツイートを一つ一つ取り出す
for sentence in sentences:
    # 形態素解析をする部分
    for token in tokenizer.tokenize(sentence):
        # ツイートに含まれる単語を抜き出す
        word = token.surface
        # 辞書のキーとして単語があるかどうかの存在確認
        if word in np_dic:
            # 値(pかnかeか?p?nのどれか)をvalueという文字で置く
            value = np_dic[word]

# キーの存在確認

# p,n,e,?p?nの個数を数える

# 総和を求める

# ネガポジ度の平均（pの総数 / summary, nの総数 / summary）を数値でそれぞれ出力
# summaryが0の場合もあるので、try-exceptで例外処理

# ポジティブ度の平均

# ネガティブ度の平均

# summaryが0の場合
