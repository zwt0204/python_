# -*- encoding: utf-8 -*-
"""
@File    : BloomFilter.py
@Time    : 2019/12/30 19:51
@Author  : zwt
@git   : https://github.com/Sssmeb/BloomFilter/blob/master/BloomFilter.py
@Software: PyCharm
"""
import math
import copy
import bitarray
import mmh3
import time
import datetime


class BloomFilter(object):

    def __init__(self, data_size, error_rate=0.001):
        """
        :param data_size: 所需存放数据的数量
        :param error_rate:  可接受的误报率，默认0.001
        通过这两个参数来确定需要多少个哈希函数以及位数组的大小
         bf = BloomFilter(data_size=100000, error_rate=0.001)
         bf.add("test")
        True
         "test" in bf
        True
        """

        if not data_size > 0:
            raise ValueError("Capacity must be > 0")
        if not (0 < error_rate < 1):
            raise ValueError("Error_Rate must be between 0 and 1.")

        self.data_size = data_size
        self.error_rate = error_rate

        bit_num, hash_num = self._adjust_param(data_size, error_rate)
        self._bit_array = bitarray.bitarray(bit_num)
        self._bit_array.setall(0)
        self._bit_num = bit_num
        self._hash_num = hash_num

        # 将哈希种子固定为 1 - hash_num （预留持久化过滤的可能）
        self._hash_seed = [i for i in range(1, hash_num+1)]

        # 已存数据量
        self._data_count = 0

    def add(self, key):
        """
        :param key: 要添加的数据
        :return:
         bf = BloomFilter(data_size=100000, error_rate=0.001)
        bf.add("test")
        True
        """
        for time in range(self._hash_num):
            key_hashed_idx = mmh3.hash(key, self._hash_seed[time]) % self._bit_num
            self._bit_array[key_hashed_idx] = 1

        self._data_count += 1
        return True

    def is_exists(self, key):
        """
        :param key:
        :return:
        判断该值是否存在
        有任意一位为0 则肯定不存在
        """
        for time in range(self._hash_num):
            key_hashed_idx = mmh3.hash(key, self._hash_seed[time]) % self._bit_num
            if not self._bit_array[key_hashed_idx]:
                return False
        return True

    def copy(self):
        """
        :return: 返回一个完全相同的布隆过滤器实例
        复制一份布隆过滤器的实例
        """
        new_filter = BloomFilter(self.data_size, self.error_rate)
        return self._copy_param(new_filter)

    def _copy_param(self, filter):
        filter._bit_array = copy.deepcopy(self._bit_array)
        filter._bit_num = self._bit_num
        filter._hash_num = self._hash_num
        filter._hash_seed = copy.deepcopy(self._hash_seed)
        filter._data_count = self._data_count
        return filter

    def _adjust_param(self, data_size, error_rate):
        """
        :param data_size:
        :param error_rate:
        :return:
        通过数据量和期望的误报率 计算出 位数组大小 和 哈希函数的数量
        k为哈希函数个数    m为位数组大小
        n为数据量          p为误报率
        m = - (nlnp)/(ln2)^2
        k = (m/n) ln2
        """
        p = error_rate
        n = data_size
        m = - (n * (math.log(p, math.e)) / (math.log(2, math.e))**2)
        k = m / n * math.log(2, math.e)

        return int(m), int(k)

    def __len__(self):
        """"
        返回现有数据容量
        """
        return self._data_count

    def __contains__(self, key):
        """
        用于实现 in 判断
        bf = BloomFilter(data_size=100000, error_rate=0.001)
        bf.add("test")
        True
        "test" in bf
        True
        """
        return self.is_exists(key)


def time_now():
    t = datetime.datetime.now().microsecond
    return t


if __name__ == '__main__':
    bf = BloomFilter(100000000, 0.00001)
    print(bf._bit_num, bf._hash_num)

    for i in range(10000000):
        bf.add(str(i))

    b = ['100', '1000']
    start = time.clock()
    for i in b:
        if bf.is_exists(i):
            print('%s exist' % i)
        else:
            print('%s not exist' % i)
    elapsed = (time.clock() - start)
    print("Time used:", elapsed)
    print('bf had load data: ', len(bf))

    t1 = time_now()
    for i in b:
        if bf.is_exists(i):
            print('%s exist' % i)
        else:
            print('%s not exist' % i)
    t2 = time_now()

    strTime = 'funtion time use:%dms' % ((t2 - t1) / 1000)
    print(strTime)