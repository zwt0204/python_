# -*- encoding: utf-8 -*-
"""
@File    : fast_test.py
@Time    : 2020/7/1 11:26
@Author  : zwt
@git   : https://github.com/salestock/fastText.py
@Software: PyCharm
"""
import fasttext

# 吃 味精 怎么 了
# model = fasttext.train_unsupervised('../data/test.txt', model='skipgram')
# model.save_model('../data/test.bin')
# print(model.words)
# print(model['words'])

# fasttext.load_model()

# 吃 味精 怎么 了   __label__1
# model = fasttext.train_supervised('../data/train.txt')
# print(model.labels)
# model.save_model('../data/fasttext.model.bin')

# 吃 味精 怎么 了   __label__1
classifier = fasttext.load_model("../data/fasttext.model.bin")

result = classifier.test("../data/train.txt")
print("准确率:", result)
print("回归率:", result)
print(classifier.predict('吃 上 一口 ， 香滑 细嫩 ， 美味 可口'))


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


print_results(*result)
