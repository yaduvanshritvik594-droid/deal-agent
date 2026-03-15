from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data

agents = [
    {'id': 1, 'name': 'Agent A'},
    {'id': 2, 'name': 'Agent B'},
]
deals = [
    {'id': 1, 'title': 'Deal 1', 'agent_id': 1},
    {'id': 2, 'title': 'Deal 2', 'agent_id': 2},
]

# Get all agents
@app.route('/agents', methods=['GET'])
def get_agents():
    return jsonify(agents)

# Get a specific agent
@app.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    agent = next((agent for agent in agents if agent['id'] == agent_id), None)
    return jsonify(agent) if agent else ('', 404)

# Create a new agent
@app.route('/agents', methods=['POST'])
def create_agent():
    new_agent = request.json
    agents.append(new_agent)
    return jsonify(new_agent), 201

# Get all deals
@app.route('/deals', methods=['GET'])
def get_deals():
    return jsonify(deals)

# Get a specific deal
@app.route('/deals/<int:deal_id>', methods=['GET'])
def get_deal(deal_id):
    deal = next((deal for deal in deals if deal['id'] == deal_id), None)
    return jsonify(deal) if deal else ('', 404)

# Create a new deal
@app.route('/deals', methods=['POST'])
def create_deal():
    new_deal = request.json
    deals.append(new_deal)
    return jsonify(new_deal), 201

if __name__ == '__main__':
    app.run(debug=True)