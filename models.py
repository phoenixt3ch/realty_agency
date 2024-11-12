from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Agent(db.Model):
    __tablename__ = 'Agents'
    agent_id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(50), nullable=False)
    agent_phone = db.Column(db.String(50), nullable=False)
    agent_email = db.Column(db.String(50))