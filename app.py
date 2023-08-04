from flask import Flask, render_template, jsonify
from data import read_data



app = Flask(__name__)

data = [
    {
        "id": 1,
        "name": "Northern fur seal",
        "race": "Latin American Indian",
        "age": "27366",
        "genre": "Male",
        "location": "6 Shasta Lane"
    },
    {
        "id": 2,
        "name": "White-winged tern",
        "race": "Ute",
        "age": "596",
        "genre": "Female",
        "location": "02130 Kensington Point"
    },
    {
        "id": 3,
        "name": "Brown and yellow marshbird",
        "race": "Chilean",
        "age": "665",
        "genre": "Male",
        "location": "697 Northview Way"
    },
    {
        "id": 4,
        "name": "Common zebra",
        "race": "Malaysian",
        "age": "35458",
        "genre": "Female",
        "location": "375 Comanche Alley"
    },
    {
        "id": 5,
        "name": "Grey lourie",
        "race": "Apache",
        "age": "8624",
        "genre": "Female",
        "location": "8 Maple Point"
    },
    {
        "id": 6,
        "name": "Crane, sarus",
        "race": "Menominee",
        "age": "571",
        "genre": "Female",
        "location": "51958 Mosinee Crossing"
    },
    {
        "id": 7,
        "name": "Hornbill, leadbeateri's ground",
        "race": "Cuban",
        "age": "7",
        "genre": "Female",
        "location": "8 Chive Hill"
    },
    {
        "id": 8,
        "name": "Brown capuchin",
        "race": "Cuban",
        "age": "242",
        "genre": "Female",
        "location": "47554 Summer Ridge Place"
    },
    {
        "id": 9,
        "name": "Stork, european",
        "race": "Venezuelan",
        "age": "778",
        "genre": "Male",
        "location": "65304 Merrick Court"
    },
    {
        "id": 10,
        "name": "African pied wagtail",
        "race": "Native Hawaiian",
        "age": "1556",
        "genre": "Female",
        "location": "5254 Prairieview Junction"
    },
    {
        "id": 11,
        "name": "Gecko, ring-tailed",
        "race": "Ottawa",
        "age": "105",
        "genre": "Female",
        "location": "188 Mcguire Terrace"
    },
    {
        "id": 12,
        "name": "Common pheasant",
        "race": "Laotian",
        "age": "8",
        "genre": "Female",
        "location": "953 Kropf Avenue"
    },
    {
        "id": 13,
        "name": "Gray rhea",
        "race": "Chinese",
        "age": "0",
        "genre": "Male",
        "location": "43 Brown Avenue"
    },
    {
        "id": 14,
        "name": "Gazelle, grant's",
        "race": "Sri Lankan",
        "age": "1",
        "genre": "Female",
        "location": "83082 Lindbergh Terrace"
    },
    {
        "id": 15,
        "name": "Caiman, spectacled",
        "race": "White",
        "age": "835",
        "genre": "Female",
        "location": "12540 Fulton Circle"
    },
    {
        "id": 16,
        "name": "Polar bear",
        "race": "Laotian",
        "age": "00",
        "genre": "Male",
        "location": "6 Mandrake Circle"
    },
    {
        "id": 17,
        "name": "Barasingha deer",
        "race": "Aleut",
        "age": "48",
        "genre": "Female",
        "location": "05933 Hazelcrest Center"
    },
    {
        "id": 18,
        "name": "Squirrel, pine",
        "race": "Paraguayan",
        "age": "5",
        "genre": "Female",
        "location": "86161 Crest Line Way"
    },
    {
        "id": 19,
        "name": "Uinta ground squirrel",
        "race": "Creek",
        "age": "06421",
        "genre": "Female",
        "location": "798 Maryland Lane"
    },
    {
        "id": 20,
        "name": "Indian mynah",
        "race": "Vietnamese",
        "age": "2268",
        "genre": "Male",
        "location": "2423 Shelley Junction"
    }
]

company_name = "Estoy desde Replit"

@app.route("/")
def hello_world():
    return render_template('index.html', data=data, company =company_name )

@app.route("/api/pets")
def pet_list():
    return jsonify(data)


if (__name__) == "__main__":
    app.run(port=3001, debug=True)
