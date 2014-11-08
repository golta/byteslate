from flask import render_template, session, redirect, url_for, request, jsonify
from . import api
from flask.ext.login import login_user, logout_user, login_required
from ..models import Contest
import bson

POST_PER_PAGE = 16

@api.route('/contest/<page>', methods=['GET'])
def get_contest_by_page(page):
    limit_start = (int(page)-1) * POST_PER_PAGE
    limit_end = limit_start + POST_PER_PAGE
    contests = Contest.query.all()[limit_start:limit_end]
    return jsonify({'contests' : [bson.loads(contest.to_json()) for contest in contests] })

@api.route('/contest/', methods=['GET'])
def get_contest():
	contests = Contest.query.all()
	return jsonify({'contests' : [bson.loads(contest.to_json()) for contest in contests] })