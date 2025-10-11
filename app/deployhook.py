"""
GitHub webhook handler for automatic deployment.
Validates webhook signatures and triggers deployment updates.
"""
import os, hmac, hashlib, subprocess
from flask import Blueprint, request, Response
from dotenv import load_dotenv

# load the .env that sits in /home/dailafing/.env
load_dotenv(os.path.expanduser("~/.env"))

blueprint = Blueprint("deployhook", __name__)
SECRET = os.getenv("GITHUB_WEBHOOK_SECRET", "").encode()

@blueprint.route("/github-webhook", methods=["POST"])
def github_webhook():
    """Handle GitHub webhook for automatic deployment with signature validation."""
    # Get signature from request headers
    sig_header = request.headers.get("X-Hub-Signature-256", "")
    
    # Calculate expected signature using HMAC-SHA256
    calc = hmac.new(SECRET, request.data, hashlib.sha256).hexdigest()

    # Validate signature format and content
    if not sig_header.startswith("sha256="):
        return "Missing signature", 403
    if not hmac.compare_digest(sig_header[7:], calc):
        return "Invalid signature", 403

    # Signature validation successful - proceed with deployment
    # Pull latest code from GitHub repository
    subprocess.call(["git", "-C", "/home/dailafing/FlaskHotel", "pull"])
    
    # Touch WSGI file to trigger application reload
    subprocess.call(["touch", "/var/www/dailafing_pythonanywhere_com_wsgi.py"])

    return Response("Deployed", status=200)