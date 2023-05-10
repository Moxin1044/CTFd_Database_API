import datetime
import json
import time

from flask import request, render_template, Blueprint, Markup, abort, redirect, url_for, send_from_directory
from CTFd.utils.decorators import admins_only, during_ctf_time_only, require_verified_emails, require_team, authed_only
from CTFd.models import db, Challenges, Users, Solves, Teams, Submissions, Tracking
from CTFd.utils.modes import get_mode_as_word, get_model
from CTFd.utils import get_config

from sqlalchemy import desc

pages = Blueprint("CTFd Database API", __name__, template_folder="templates")


def load_page(route, plugin_dir='.'):
    @pages.route(route, methods=['GET', 'POST'])
    @admins_only
    def view_db_home():
        return render_template("api_config_home.html")

    @pages.route("/moxin_api/user_number", methods=['GET', 'POST'])
    def user_number():
        # 返回用户数量
        return str(Users.query.count())

    @pages.route("/moxin_api/ip_number", methods=['GET', 'POST'])
    def ipnum():
        # 返回IP数量
        return str(Tracking.query.with_entities(Tracking.ip).distinct().count())

    @pages.route("/moxin_api/challenge_number", methods=['GET', 'POST'])
    def challengenum():
        # 返回题目数量
        return str(Challenges.query.count())

    @pages.route("/moxin_api/solve_number", methods=['GET', 'POST'])
    def solvenum():
        # 返回解答数量
        Model = get_model()
        return str(Solves.query.join(Model, Solves.account_id == Model.id).filter(Model.banned == False,Model.hidden == False).count())

    @pages.route("/moxin_api/new_user", methods=['GET', 'POST'])
    def new_user():
        user = db.session.query(Users).order_by(desc(Users.id)).first()
        return str(user)
    return pages