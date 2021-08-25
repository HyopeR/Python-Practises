from flask import Blueprint, render_template

main_route = Blueprint('main', __name__, template_folder='../templates')


@main_route.route("/", methods=['GET'])
def main():
    return render_template('main.html')