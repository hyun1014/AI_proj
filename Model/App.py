# flask 관련.
from flask import Flask, request, jsonify
import main_model
from flask_cors import CORS
import jpype


app = Flask(__name__)
cors = CORS(app, resources={r"/app/*": {"origins": "*"}})

@app.route('/Get_Diary', methods=['POST'])
def Get_Diary():
    jpype.attachThreadToJVM()
    param_id = request.json.get('_id')
    paramContents = request.json.get('Contents')
    print("param_id: ", param_id)
    print("paramContents:" , paramContents)
    result = main_model.calculate_sentiment_single_diary(paramContents)
    if result==1:
        print("분석 결과 긍정적인 감정입니다.")
    else:
        print("분석 결과 부정적인 감정입니다.")
    return jsonify({"result": result})


if __name__ == '__main__':
    print("Start")
    app.run()
