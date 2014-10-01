from flask import render_template, session, redirect, url_for, request, flash
from . import contest
from ..models import Contest, Arena
from .forms import ContestAddForm
from flask.ext.login import login_required
from app import db

@contest.route('/add', methods=['GET', 'POST'])
@login_required
def add_contest():
	form = ContestAddForm()
	form.arena.choices = [(g.id, g.title) for g in Arena.query.order_by('title') ]

	if form.validate_on_submit():
		contest = Contest(title=form.title.data)
		contest.description = form.description.data
		contest.url = form.url.data
		contest.arena_id = form.arena.data
		contest.start_time = form.start_time.data
		contest.end_time = form.end_time
		
		db.session.add(contest)
		db.session.commit()
		flash('New contest Added')
		return redirect(url_for('main.index'))
	return render_template('contest/new.html', form=form)
