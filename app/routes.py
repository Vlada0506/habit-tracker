from datetime import date, timedelta

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    abort
)

from app import db
from app.models import Habit, Completion

main = Blueprint("main", __name__)


@main.route("/")
def index():
    habits = Habit.query.order_by(Habit.id.desc()).all()
    return render_template("index.html", habits=habits)


@main.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        target_per_day = int(request.form["target_per_day"])

        habit = Habit(
            name=name,
            description=description,
            target_per_day=target_per_day
        )

        db.session.add(habit)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_habit.html")


@main.route("/habit/<int:id>")
def habit_detail(id):
    habit = Habit.query.get_or_404(id)

    history = []

    for i in range(6, -1, -1):
        day = date.today() - timedelta(days=i)

        count = Completion.query.filter_by(
            habit_id=id,
            completed_date=day
        ).count()

        history.append({
            "date": day,
            "count": count
        })

    return render_template(
        "habit_detail.html",
        habit=habit,
        history=history
    )


@main.route("/toggle/<int:id>")
def toggle(id):
    habit = Habit.query.get_or_404(id)

    completion = Completion(
        habit_id=habit.id,
        completed_date=date.today()
    )

    db.session.add(completion)
    db.session.commit()

    return redirect(url_for("main.index"))


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_habit(id):
    habit = Habit.query.get_or_404(id)

    if request.method == "POST":
        habit.name = request.form["name"]
        habit.description = request.form["description"]
        habit.target_per_day = int(request.form["target_per_day"])

        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template(
        "edit_habit.html",
        habit=habit
    )


@main.route("/delete/<int:id>")
def delete_habit(id):
    habit = Habit.query.get_or_404(id)

    db.session.delete(habit)
    db.session.commit()

    return redirect(url_for("main.index"))


@main.route("/search")
def search():
    query = request.args.get("q", "")

    results = []

    if query:
        results = Habit.query.filter(
            Habit.name.ilike(f"%{query}%")
        ).all()

    return render_template(
        "search.html",
        query=query,
        results=results
    )