from datetime import date

from app import db


class Habit(db.Model):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    target_per_day = db.Column(db.Integer, nullable=False, default=1)

    completions = db.relationship(
        "Completion",
        backref="habit",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def today_count(self):
        today = date.today()
        return Completion.query.filter_by(
            habit_id=self.id,
            completed_date=today
        ).count()


class Completion(db.Model):
    __tablename__ = "completions"

    id = db.Column(db.Integer, primary_key=True)

    habit_id = db.Column(
        db.Integer,
        db.ForeignKey("habits.id"),
        nullable=False
    )

    completed_date = db.Column(
        db.Date,
        nullable=False,
        default=date.today
    )