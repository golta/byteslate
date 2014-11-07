from flask import render_template, session, redirect, url_for, request, flash
from . import contest
from ..models import Contest, Arena
from .forms import ContestAddForm
from flask.ext.login import login_required
from app import db
from datetime import datetime

@contest.route('/add', methods=['GET', 'POST'])
@login_required
def add_contest():
	form = ContestAddForm()
	form.arena.choices = [(g.id, g.title) for g in Arena.query.order_by('title') ]

	if form.validate_on_submit():
		contest = Contest(title=form.title.data)
		contest.description = form.description.data
		contest.content = form.content.data
		contest.url = form.url.data
		contest.arena_id = form.arena.data
		contest.start_time = form.start_time.data
		contest.end_time = form.start_time.data
		contest.isprized = form.prizes.data
		contest.ishiring = form.hiring.data
		db.session.add(contest)
		db.session.commit()
		flash('New contest Added')
		return redirect(url_for('main.index'))
	return render_template('contest/new.html', form=form)

@contest.route('/edit/<id>', methods=['GET', 'POST'] )
@login_required
def edit_contest(id):
	contest = Contest.query.get_or_404(id)
	form = ContestAddForm()
	form.arena.choices = [(g.id, g.title) for g in Arena.query.order_by('title') ]
	if form.validate_on_submit():
		contest.title = form.title.data
		contest.description = form.description.data
		contest.url = form.url.data
		contest.arena_id = form.arena.data
		contest.start_time = form.start_time.data
		contest.end_time = form.end_time.data

		db.session.add(contest)
		flash('Contest updated')
		return redirect(url_for('contest.edit_contest', id=contest.id) )
	form.title.data = contest.title
	form.description.data = contest.description
	form.url.data =	contest.url
	form.arena.data = contest.arena_id
	form.start_time.data = contest.start_time
	form.end_time.data = contest.end_time
	return render_template('contest/edit.html', form=form, contest=contest)

@contest.route('/delete/<id>', methods=['POST'])
@login_required
def delete_contest(id):
	contest = Contest.query.get_or_404(id)
	db.session.delete(contest)
	flash('Delete Successful')
	return redirect(url_for('main.index'))
