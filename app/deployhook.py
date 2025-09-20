import os, hmac, hashlib, subprocess
from flask import Blueprint, request
from dotenv import load_dotenv

# load the .env that sits in /home/dailafing/.env
load_dotenv(os.path.expanduser("~/.env"))

blueprint = Blueprint("deployhook", __name__)
SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "").encode()

@blueprint.route("/github-webhook", methods=["POST"])
def github_webhook():
    signature = request.headers.get("X-Hub-Signature-256", "")
    if not signature.startswith("sha256="):
        return "Missing signature", 403
    digest = hmac.new(SECRET, request.data, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature[7:], digest):
        return "Invalid signature", 403

    # pull latest code
    subprocess.call(["git", "-C", "/home/dailafing/FlaskHotel", "pull"])
    # reload the web app
    subprocess.call(["touch", "/var/www/dailafing_pythonanywhere_com_wsgi.py"])
    return "Deployed", 200
