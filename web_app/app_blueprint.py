from flask import Blueprint, request, render_template
import requests

app_blueprint = Blueprint('app_blueprint', __name__)


@app_blueprint.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        print("Your name is " + first_name + last_name)
        json_data = {"first_name": first_name, "last_name": last_name}
        # post to call to an API
        response = requests.post("https://gom9hfuyfa.execute-api.ap-south-1.amazonaws.com/dev/res1",#"https://pp2qfncgdk.execute-api.ap-south-1.amazonaws.com/dev/flaskresource1",
                                 json={"body": json_data, "id":"7"})
        print("post call triggered")

        print(response)
        print(response.json())
        return render_template("display.html", data=json_data)
        """
        In this example, we're sending a POST request , but this time we're sending JSON data in the request body instead of form data.
        The json parameter automatically sets the appropriate Content-Type header for JSON data.
        """

    return render_template("index.html")


if __name__ == "__main__":
    app_blueprint.run(debug=True)
