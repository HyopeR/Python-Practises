from flask import Flask
from src.helpers.mysql.mysql_service import ServiceMysql
from src.routes.authentication.authentication_route import authentication
from src.routes.main.main_route import main

app = Flask(__name__, template_folder='./src/templates')

mysql = ServiceMysql.get_instance(app)
print('APP', mysql)

app.register_blueprint(main)
app.register_blueprint(authentication)

if __name__ == "__main__":
    app.run(debug=True)
