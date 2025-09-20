import os, hmac, hashlib, subprocess
from flask import Blueprint, request
from dotenv import load_dotenv

# load the .env that sits in /home/dailafing/.env
load_dotenv(os.path.expanduser("~/.env"))

blueprint = Blueprint("deployhook", __name__)
SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "").encode()

@blueprint.route("/github-webhook", methods=["POST"])
def github_webhook():
    sig_header = request.headers.get("X-Hub-Signature-256", "")
    calc = hmac.new(SECRET, request.data, hashlib.sha256).hexdigest()

    # DEBUG — remove after test
    print("▶ header =", sig_header[7:])
    print("▶ local  =", calc)

    if not sig_header.startswith("sha256="):
        return "Missing signature", 403
    if not hmac.compare_digest(sig_header[7:], calc):
        return "Invalid signature", 403

