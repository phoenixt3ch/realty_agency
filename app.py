from flask import Flask, render_template, redirect, url_for, request, jsonify
from config import Config
from models import db, Agent, Client, Realty
from forms import AgentForm, ClientForm, RealtyForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/agents', methods=['GET', 'POST'])
def agents():
    form = AgentForm()
    if form.validate_on_submit():
        agent = Agent(
            agent_name=form.agent_name.data,
            agent_phone=form.agent_phone.data,
            agent_email=form.agent_email.data
        )
        db.session.add(agent)
        db.session.commit()
        return redirect(url_for('agents'))

    agents = Agent.query.all()
    return render_template('agents.html', form=form, agents=agents)

@app.route('/update_agent/<int:id>', methods=['POST'])
def update_agent(id):
    agent = Agent.query.get_or_404(id)
    data = request.get_json()

    agent.agent_name = data.get('agent_name', agent.agent_name)
    agent.agent_phone = data.get('agent_phone', agent.agent_phone)
    agent.agent_email = data.get('agent_email', agent.agent_email)

    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/delete_agent/<int:id>', methods=['GET', 'POST'])
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('agents'))

@app.route('/clients', methods=['GET', 'POST'])
def clients():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            client_name=form.client_name.data,
            client_phone=form.client_phone.data,
            client_email=form.client_email.data
        )
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('clients'))

    clients = Client.query.all()
    return render_template('clients.html', form=form, clients=clients)

@app.route('/update_client/<int:id>', methods=['POST'])
def update_client(id):
    client = Client.query.get_or_404(id)
    data = request.get_json()

    client.client_name = data.get('client_name', client.client_name)
    client.client_phone = data.get('client_phone', client.client_phone)
    client.client_email = data.get('client_email', client.client_email)

    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/delete_client/<int:id>', methods=['GET', 'POST'])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('clients'))

@app.route('/realty', methods=['GET', 'POST'])
def realty():
    form = RealtyForm()
    if form.validate_on_submit():
        new_realty = Realty(
            realty_address=form.realty_address.data,
            realty_square=form.realty_square.data
        )
        db.session.add(new_realty)
        db.session.commit()
        return redirect(url_for('realty'))

    realties = Realty.query.all()
    return render_template('realty.html', form=form, realties=realties)


@app.route('/update_realty/<int:realty_id>', methods=['POST'])
def update_realty(realty_id):
    data = request.get_json()
    realty = Realty.query.get_or_404(realty_id)
    realty.realty_address = data['realty_address']
    realty.realty_square = int(data['realty_square'])

    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/delete_realty/<int:realty_id>', methods=['POST'])
def delete_realty(realty_id):
    realty = Realty.query.get_or_404(realty_id)
    db.session.delete(realty)
    db.session.commit()
    return redirect(url_for('realty'))

if __name__ == '__main__':
    app.run(debug=True)