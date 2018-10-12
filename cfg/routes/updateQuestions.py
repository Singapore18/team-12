import logging

from flask import request, jsonify;

from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

@app.route('/updatequestions', methods=['POST'])
def updateQuestions():
    factory = connection_manager.connection_manager()
    connection = factory.connection
    cursor = connection.cursor()
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("data");
    query = "UPDATE question SET `category`=\"{}\", `reversed`={}, `questiontext`=\"{}\", `scale`={}, `isscale`={}, `options`=\"{}\" WHERE `idquestion`={};"
    output = {}
    output['status'] = ""
    for qs in inputValue:
        print(qs)
        try:
            print(str.format(query, qs['category'], qs['reversed'], qs['questiontext'], qs['scale'], qs['isscale'], qs['options'], qs['questionid']))
            cursor.execute(str.format(query, qs['category'], qs['reversed'], qs['questiontext'], qs['scale'], qs['isscale'], qs['options'], qs['questionid']))
            output['status'] = 'OK'
        except:
            output['status'] = 'ERROR'
        finally:
            factory.close_all(cursor=cursor, connection=connection)
    logging.info("My result :{}".format(output))
    return jsonify(output);
