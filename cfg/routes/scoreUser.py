import logging

from flask import request, jsonify;
import pandas as pd
from cfg import app;

from cfg.routes import connection_manager

logger = logging.getLogger(__name__)

def getScore(selection, reversed=False, max_score=7):
    if reversed:
        selection = max_score + 1 - selection

    return selection


@app.route('/scoreuser', methods=['POST'])
def scoreUser():
    factory = connection_manager.connection_manager()
    connection = factory.connection
    # cursor = connection.cursor()
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("data");
    query = "select * from userresponse JOIN question on question.idquestion=userresponse.questionid where userresponse.userid={}"
    output = {}
    output['status'] = ""
    output['catscores'] = {}
    try:
        df = pd.read_sql_query(query.format(inputValue), connection)
        # print(df.info())

        categories = df['category'].unique()
        for c in categories:
            if c != "Team Player":
                curr_df = df.loc[df['category'] == c]
                # print(curr_df)
                curr_df['score'] = curr_df.apply(lambda row: getScore(row['responseanswer'], row['reversed'], row['scale']), axis=1)
                output['catscores'][c] = curr_df['score'].mean()
        # try:
        #     print(inputValue)
        #     cursor.execute(query, int(inputValue))
        #     results = cursor.fetchall()
        #     print(results)
        #     output['status'] = 'OK'
        # except:
        #     raise
        #     output['status'] = 'ERROR'
        # finally:
            # factory.close_all(cursor=cursor, connection=connection)
            # pass
        output['status'] = 'OK'
    except:
        output['status'] = 'ERROR'
        
    logging.info("My result :{}".format(output))
    return jsonify(output);
