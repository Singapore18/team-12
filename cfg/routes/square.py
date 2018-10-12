import logging

from flask import request, jsonify;

from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

@app.route('/square', methods=['POST'])
def evaluate():
    factory = connection_manager.connection_manager()
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input");
    result = inputValue * inputValue
    logging.info("My result :{}".format(result))
    return jsonify(result);
