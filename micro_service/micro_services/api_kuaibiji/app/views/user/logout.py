# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11
@desc:
"""

# import ipdb
from flask import request, session, current_app, abort
# from flask_login import current_user, login_user, logout_user, AnonymousUserMixin, UserMixin
from flask import Blueprint, render_template, current_app, g
import json
from rpc.notebook import NoteBookClient
from rpc.user import UserClient
from common.request_tool import send_failure, send_success, login_required
from database import redis_client

mod = Blueprint('user_logout', __name__)

@mod.route('/logout')
def logout():
    # session.clear()
    # logout_user()
    token = 'jwmi hello ranndeeerom id'
    redis_client.delete(token)
    return send_failure(msg='no user')
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    # args = request.args
    # user_id = args.get('user_id', '')
    # s = UserClient()
    # user = s.user_by_id(user_id)
    # user_data = user.get('data', '')
    # if not user_data:
    #     return send_failure(msg='no user')
