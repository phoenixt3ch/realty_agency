from flask import Flask, render_template, redirect, url_for
from config import Config
from models import db, Agent
from forms import AgentForm

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

if __name__ == '__main__':
    app.run(debug=True)