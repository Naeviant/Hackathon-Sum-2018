### TEXT FILE MANIPULATION

# Import JSON Module
import json

# Save Data to Text File
def save(data):
    with open("data.json", "w") as text:
        json.dump(data, text)

# Get Data from Text File
def get():
    with open("data.json", "r") as text:
        data = text.read()
        if data == "":
            return {}
        else:
            return json.loads(data)

def calculate():
    data = get()
    # TODO: DATA MUST BE RETURNED AS A LIST OF DICTIONARIES
    # [
    #   {
    #       "title": "Sample Event 1",
    #       "times": {
    #           "start": "09:00",
    #           "end": "11:00"
    #       },
    #       "icon": "flag",
    #       "not_interested": True,
    #       "website": "http://www.tameside.ac.uk/",
    #       "maps": "https://www.google.co.uk/maps/place/Tameside+College/@53.4878207,-2.0826059,17z/data=!3m1!4b1!4m5!3m4!1s0x487bb637cdf91f2d:0x1af8c219fb8f3cff!8m2!3d53.4878175!4d-2.0804172",
    #       "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut condimentum nibh dui, non euismod orci pulvinar et. Nam ultrices, tellus quis accumsan facilisis, magna mi porta dui, at consequat augue sem non velit. Duis sit amet nibh pulvinar, gravida sapien in, suscipit nisi. Phasellus finibus enim ligula, quis auctor nisi commodo vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    #   },
    #   {
    #       "title": "Sample Event 2",
    #       "times": {
    #           start: "11:00",
    #           end: "12:30"
    #       },
    #       "icon": "flag",
    #       "not_interested": True,
    #       "website": "https://www.cineworld.co.uk/cinemas/ashton-under-lyne",
    #       "maps": "https://www.google.co.uk/maps/place/Cineworld+Cinema/@53.4893095,-2.1127273,16z/data=!4m5!3m4!1s0x4871438d86e3ded7:0xf78aac6a83e0cb8b!8m2!3d53.4893095!4d-2.1100482",
    #       "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut condimentum nibh dui, non euismod orci pulvinar et. Nam ultrices, tellus quis accumsan facilisis, magna mi porta dui, at consequat augue sem non velit. Duis sit amet nibh pulvinar, gravida sapien in, suscipit nisi. Phasellus finibus enim ligula, quis auctor nisi commodo vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    #   },
    #   {
    #       "title": "Bus Link: 409",
    #       "times": {
    #           "start": "12:30",
    #           "end": "13:00"
    #       },
    #       "icon": "directions_bus",
    #       "not_interested": False,
    #       "website": None,
    #       "maps": "https://www.google.co.uk/maps/place/Ashton+Bus+Station+(Stand+M)/@53.4901108,-2.0959614,19.25z/data=!4m5!3m4!1s0x487bb65a965775dd:0x5db084ebf64fb44a!8m2!3d53.4902175!4d-2.0966734",
    #       "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut condimentum nibh dui, non euismod orci pulvinar et. Nam ultrices, tellus quis accumsan facilisis, magna mi porta dui, at consequat augue sem non velit. Duis sit amet nibh pulvinar, gravida sapien in, suscipit nisi. Phasellus finibus enim ligula, quis auctor nisi commodo vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    #   },
    #   {
    #       "title: "Sample Event 3",
    #       "times: {
    #           "start": "13:00",
    #           "end:" "15:00"
    #       },
    #       "icon": "free_breakfast",
    #       "not_interested": True,
    #       "website": "http://dogandpartridgeashton.co.uk/ourfood.html",
    #       "maps": "https://www.google.co.uk/maps/place/Dog+and+Partridge/@53.4984886,-2.1033156,17.5z/data=!4m5!3m4!1s0x487bb654f44f4869:0xf3b9c8d8d4c6960d!8m2!3d53.4993158!4d-2.1039992",
    #       "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut condimentum nibh dui, non euismod orci pulvinar et. Nam ultrices, tellus quis accumsan facilisis, magna mi porta dui, at consequat augue sem non velit. Duis sit amet nibh pulvinar, gravida sapien in, suscipit nisi. Phasellus finibus enim ligula, quis auctor nisi commodo vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    #   }
    # ]
    return []

### ===================================================================================================================================================================================== ###

### HTTP SERVER

# Import Flask Framework
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

# Configure Server
app = Flask(__name__)
CORS(app)

# Handle Post Requests for /exists
@app.route('/exists', methods=["POST"])
def exists():
    data = get()
    if data == {}:
        return jsonify({
            "status": 200,
            "message": "Success",
            "body": False
        })
    else:
        return jsonify({
            "status": 200,
            "message": "Success",
            "body": True
        })

# Handle Post Requests for /populate
@app.route('/populate', methods=["POST"])
def populate():
    data = get()
    if data == {}: 
        return jsonify({
            "status": 204,
            "message": "No Content",
            "body": None
        })
    else:
        return jsonify({
            "status": 200,
            "message": "Success",
            "body": data
        })

# Handle Post Requests for /submit
@app.route('/submit', methods=["POST"])
def submit():
    save(request.get_json(force=True))
    return jsonify({
        "status": 204,
        "message": "No Content",
        "body": None
    })

# Handle Post Requests for /plan
@app.route('/plan', methods=["POST"])
def plan():
    return jsonify({
        "status": 200,
        "message": "Success",
        "body": calculate()
    })

app.run(host='0.0.0.0')
