import logging

from flask import request, jsonify;

from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

@app.route('/reports/<int:surveyId>', methods=['GET'])
def getReports(surveyId):
    print("surveyId:", surveyId)
    data = request.get_json();
    result = {
	"data": [
	{
		"surveyid": 2,
		"questionid": 1,
		"questiontext": "string",
		"category": 1,
		"isScale": 1,
		"scale": 7,
		"reversed": 0,
		"options": ["string", "string", "string", "string"]
	},
	{
		"surveyid": 2,
		"questionid": 1,
		"questiontext": "string",
		"category": 1,
		"isScale": 1,
		"scale": 7,
		"reversed": 0,
		"options": ["string", "string", "string", "string"]
	}
]
}
    return jsonify(result);
