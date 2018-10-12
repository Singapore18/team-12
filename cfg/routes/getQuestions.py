import logging

from flask import request, jsonify;

from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

@app.route('/questions/<int:surveyId>', methods=['GET'])
def getQuestions(surveyId):
    print("surveyId:", surveyId)
    # data = request.get_json();
    # result = [
    #     {
    #         "id": 1,
    #         "text": "string",
    #         "category": 1,
    #         "isScale": False,
    #         # scale: int,
    #         # reversed: boolean,
    #         "options": ["string1", "string2", "string3", "string4"]
    #     }
    #     # {
    #     #     id: int,
    #     #     text: string,
    #     #     category: int,
    #     #     isScale: boolean,
    #     #     scale: int,
    #     #     reversed: boolean,
    #     #     options: [string, string, string, string],
    #     # }
    # ]
    query = "select * from halogen.question"
    factory = connection_manager.connection_manager()
    connection = factory.connection
    cursor = connection.cursor()
    print("test")
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
    except:
        raise
    finally:
        factory.close_all(cursor=cursor, connection=connection)
#     result = {
# 	"data": [
# 	{
# 		"surveyid": 2,
# 		"questionid": 1,
# 		"questiontext": "string",
# 		"category": 1,
# 		"isScale": 1,
# 		"scale": 7,
# 		"reversed": 0,
# 		"options": ["string", "string", "string", "string"]
# 	},
# 	{
# 		"surveyid": 2,
# 		"questionid": 1,
# 		"questiontext": "string",
# 		"category": 1,
# 		"isScale": 1,
# 		"scale": 7,
# 		"reversed": 0,
# 		"options": ["string", "string", "string", "string"]
# 	}
# ]
# }
    return jsonify(results);
