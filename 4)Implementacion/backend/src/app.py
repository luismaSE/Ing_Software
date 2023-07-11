from main import create_app
import os

app = create_app()
app.app_context().push()
from main import mongo

if __name__ == '__main__':
    app.run(debug = True, port = 3000)