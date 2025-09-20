from app import create_app

application = create_app()  # for WSGI (PythonAnywhere)
app = application            # for local use

if __name__ == "__main__":
    app.run(debug=True)
