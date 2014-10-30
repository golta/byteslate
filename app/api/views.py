from flask import render_template, session, redirect, url_for, request, jsonify
from . import api
from flask.ext.login import login_user, logout_user, login_required
from ..models import Contest
import bson

@api.route('/contest/<page>', methods=['GET'])
def get_contest(page):
    limit_start = (int(page)-1)*2
    limit_end = limit_start + 2
    contests = Contest.query.all()[limit_start:limit_end]
    return jsonify({'contests' : [bson.loads(contest.to_json()) for contest in contests] })