from flask import Flask, render_template, request, jsonify
import logging
import os

app = Flask(__name__)

# Basic logging for SRE monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory task store (for practice; replace with Redis/DB for prod)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append({'id': len(tasks) + 1, 'task': task, 'completed': False})
            logger.info(f"Added task: {task}")
    return render_template('index.html', tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({'status': 'ready'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
