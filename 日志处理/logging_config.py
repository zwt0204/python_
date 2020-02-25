# -*- encoding: utf-8 -*-
"""
@File    : logging_config.py
@Time    : 2020/2/25 13:20
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import logging
from logging import handlers

# https://www.cnblogs.com/nancyzhu/p/8551506.html


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        # %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        # %(pathname)s[line:%(lineno)d] 调用日志输出函数的模块的完整路径名，可能没有
        # %(levelname)s 文本形式的日志级别
        # %(message)s 用户输出的消息
        self.logger = logging.getLogger(filename)
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 屏幕上输出
        sh = logging.StreamHandler()
        # 设置屏幕输出格式
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')

        # th = handlers.RotatingFileHandler(filename, maxBytes=100*1024*1024, backupCount=10)

        # 实例化TimedRotatingFileHandler
        # backupCount是备份文件的个数，如果超过这个个数，就会自动删除
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨

        # 设置文件里写入的格式
        th.setFormatter(format_str)
        # 对象加到logger中
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('all.log', level='debug')
    log.logger.debug("debug")