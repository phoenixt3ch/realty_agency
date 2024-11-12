from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Agent(db.Model):
    __tablename__ = 'Agents'
    agent_id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(50), nullable=False)
    agent_phone = db.Column(db.String(50), nullable=False)
    agent_email = db.Column(db.String(50))

class Client(db.Model):
    __tablename__ = 'Clients'
    client_id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(50), nullable=False)
    client_phone = db.Column(db.String(50), nullable=False)
    client_email = db.Column(db.String(50))

class Realty(db.Model):
    __tablename__ = 'Realty'
    realty_id = db.Column(db.Integer, primary_key=True)
    realty_address = db.Column(db.String(50), nullable=False)
    realty_square = db.Column(db.Float, nullable=False)

class Rent(db.Model):
    __tablename__ = 'Rent'
    rent_id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('Agents.agent_id'), nullable=False)
    realty_id = db.Column(db.Integer, db.ForeignKey('Realty.realty_id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Clients.client_id'), nullable=False)
    rent_beginning_date = db.Column(db.Date, nullable=False)
    rent_ending_date = db.Column(db.Date)
    rent_price = db.Column(db.Integer, nullable=False)

class Sale(db.Model):
    __tablename__ = 'Sales'
    sale_id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('Agents.agent_id'), nullable=False)
    realty_id = db.Column(db.Integer, db.ForeignKey('Realty.realty_id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Clients.client_id'), nullable=False)
    sale_date = db.Column(db.Date, nullable=False)
    sale_price = db.Column(db.Integer, nullable=False)