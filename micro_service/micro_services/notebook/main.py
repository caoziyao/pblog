# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc: notebook 服务
"""
from .service import NotebookService


def main():
    s = NotebookService()
    s.run()


if __name__ == '__main__':
    main()