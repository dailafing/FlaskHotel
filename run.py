"""
Application entry point for Flask Hotel.
Creates Flask application instance for both local development and production deployment.
"""
from app import create_app

# Create application instance
application = create_app()  # for WSGI (PythonAnywhere)
app = application            # for local use

if __name__ == "__main__":
    # Run development server with debug mode enabled
    app.run(debug=True)
