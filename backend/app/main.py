from flask import Flask, request, jsonify
from flask_cors import CORS
from extract import Extract

extract_instance = Extract()
app = Flask(__name__)


@app.route("/extract", methods=["POST", "GET"])
def make_requests():
    """
    Handle POST and GET requests for text extraction.

    For POST requests, extract text from the uploaded image and return the result.
    For GET requests, return the previously extracted text from the database.

    :return: Extracted text or response message.
    :rtype: str
    """
    if request.method == "POST":
        uploaded_image = request.files["image"]
        return jsonify(extract_instance.extract_text(uploaded_image)), 200
    elif request.method == "GET":
        return jsonify(extract_instance.get_text()), 200


CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
