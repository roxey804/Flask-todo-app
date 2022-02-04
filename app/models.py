from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)  # Optional field
    priority = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Str representation of the model (as its desc)"""
        return '<Todo %r>' % self.description

#Q Why no init method here?