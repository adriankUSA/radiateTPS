from application import create_app  # Import create_app function

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
