import logging
import datetime
from flask import request, jsonify;

from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

@app.route('/answerquestions', methods=['POST'])
def answerQuestions():
    factory = connection_manager.connection_manager()
    connection = factory.connection
    cursor = connection.cursor()
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("data");
    query = "INSERT into userresponse (responseanswer, starttime, endtime, questionid, userid) VALUES ({}, \"{}\", \"{}\", {}, {});"
    output = {}
    output['status'] = ""
    for qs in inputValue:
        # print(qs)
        try:
            cursor.execute(str.format(query, qs['choice'], datetime.datetime.now(), datetime.datetime.now(), qs['questionid'], qs['userid']))
            output['status'] = 'OK'
        except:
            output['status'] = 'ERROR'
        finally:
            # factory.close_all(cursor=cursor, connection=connection)
            pass
    logging.info("My result :{}".format(output))
    return jsonify(output);
