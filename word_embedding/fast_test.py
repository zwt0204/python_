# -*- encoding: utf-8 -*-
"""
@File    : fast_test.py
@Time    : 2020/7/1 11:26
@Author  : zwt
@git   : https://github.com/salestock/fastText.py
@Software: PyCharm
"""
import fasttext

model = fasttext.train_unsupervised('../data/test.txt', model='skipgram')
model.save_model('../data/test.bin')
print(model.words)
print(model['words'])

# fasttext.load_model()
