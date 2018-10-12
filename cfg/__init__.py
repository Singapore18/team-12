from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import cfg.routes.square # sample
import cfg.routes.getQuestions
import cfg.routes.updateQuestions
import cfg.routes.answerQuestions
import cfg.routes.scoreUser
