# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/6 
@desc:
"""

from flask_script import Manager
from micro_services.user import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()