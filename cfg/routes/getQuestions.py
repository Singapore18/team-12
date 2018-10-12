import logging

from flask import request, jsonify;

from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

@app.route('/questions', methods=['GET'])
def evaluate():
    data = request.get_json();
    result = [
        {
            id: 1,
            text: "string",
            category: 1,
            isScale: boolean,
            # scale: int,
            # reversed: boolean,
            options: ["string1", "string2", "string3", "string4"]
        }
        # {
        #     id: int,
        #     text: string,
        #     category: int,
        #     isScale: boolean,
        #     scale: int,
        #     reversed: boolean,
        #     options: [string, string, string, string],
        # }
    ]
    return jsonify(result);
