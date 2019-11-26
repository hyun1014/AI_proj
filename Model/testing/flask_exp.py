# flask 관련.

from flask import Flask, request
from pymongo import MongoClient
import settings
# import main_model
from flask_cors import CORS, cross_origin
from bson import ObjectId


app = Flask(__name__)
cors = CORS(app, resources={r"/app/*": {"origins": "*"}})
client = MongoClient(settings.db_url)
diaries = client.database.diaries


@app.route('/Get_Diary', methods=['POST'])
def Get_Diary():
    """
    param_id = request.json.get('_id')
    paramContents = request.json.get('Contents')
    print("param_id: ", param_id)
    print("paramContents:" , paramContents)
    result = main_model.calculate_sentiment_single_siary(paramContents)

    diaries.update_one({'_id': ObjectId(param_id)}, { '$set': {'Sentiment_Analysis': result}})
    """
    print("sibural")
    return "done"


if __name__ == '__main__':
    app.run()
