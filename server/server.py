import os
import json
import sqlite3

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from waitress import serve
from requests import get

app = Flask(__name__)
CORS(app)

DATABASE = "comments.db"
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE)

TA_NAME = ""
TA_ENDPOINT = f"https://{TA_NAME}.cognitiveservices.azure.com/"
TA_KEY = ""


def createComment(data):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    sql = f"INSERT INTO comments (name, comment) VALUES('{data['name']}', '{data['comment']}');"
    cursor.execute(sql)
    connection.commit()
    connection.close()


def getComments():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    sql = "SELECT id, name, comment FROM comments"
    cursor.execute(sql)
    comments = []
    for data in cursor:
        comments.append({"id": data[0], "name": data[1], "comment": data[2]})
    connection.close()
    return comments


def authenticate_client():
    ta_credential = AzureKeyCredential(TA_KEY)
    text_analytics_client = TextAnalyticsClient(
        endpoint=TA_ENDPOINT,
        credential=ta_credential
    )
    return text_analytics_client


def getSentiment(documents):
    client = authenticate_client()
    doc_response = client.analyze_sentiment(documents, language="de")
    # successful_responses = [doc for doc in response if not doc.is_error]
    return [{
        "id": doc.id,
        "sentiment": doc.sentiment,
        "confidence_scores": {"positive": doc.confidence_scores.positive, "neutral": doc.confidence_scores.neutral, "negative": doc.confidence_scores.negative},
        "text": d} for (d, doc) in zip(documents, doc_response)]


@app.route("/api/comments", methods=["GET", "PUT"])
def comments():
    if request.method == "PUT":
        data = json.loads(request.data)
        if (data['name'] != "" and data['comment'] != ""):
            createComment(data)
            return jsonify(result="done")
        return jsonify(result="error: empty data")
    else:
        return jsonify(getComments())


@app.route("/api/sentiment", methods=["POST"])
def sentiment():
    data = json.loads(request.data)
    return jsonify(getSentiment(data))


@app.route("/", defaults={"path": ""}, methods=["GET"])
@app.route("/<path:path>")
def index(path):
    print(path)
    return render_template("index.html")


@app.errorhandler(404)
def not_found(error):
    print(error)
    return render_template("index.html")


if __name__ == "__main__":
    serve(app, port=5000)
