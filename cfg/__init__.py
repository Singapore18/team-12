from flask import Flask
app = Flask(__name__)
import cfg.routes.square # sample
import cfg.routes.getQuestions
# import cfg.routes.updateQuestions
