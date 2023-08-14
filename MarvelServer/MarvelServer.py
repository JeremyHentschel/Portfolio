import flask
from flask import request
import mariadb  # pip install mariadb
import sys

app = flask.Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="marvel_crisis_protocol",
        autocommit=True
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cursor = conn.cursor()


@app.route('/', methods=['GET'])
def hello():
    print("It's Marvel Baby!")
    return "It's Marvel Baby!"


@app.route('/characters', methods=['GET'])
def all_characters():

    cursor.execute("SELECT id, name,threat,health, affiliation FROM characters")

    characters_list = []

    for (a, b, c, d, e) in cursor:
        print(f'ID: {a}, Name: {b}, Threat: {c}, Health: {d}, Affiliation: {e}')
        characters_list.append({"id": a, "name": b, "threat": c, "health": d, "affiliation": e})

    return characters_list


@app.route('/characters/<id>', methods=['GET'])
def get_character(id):

    cursor.execute(
        "SELECT id, name, threat, health, affiliation FROM characters WHERE id = %s", (id,))

    row = cursor.fetchone()
    character_list = []

    if row is not None:
        return {"id": row[0], "name": row[1], "threat": row[2], "health": row[3], "affiliation": row[4]}
    else:
        return "Unable to find a character with id = " + id, 404


@app.route('/characters', methods=['POST'])
def new_character():

    new_character = request.json

    cursor.execute("INSERT INTO characters (name, threat, health, affiliation) VALUES (%s, %s, %s, %s)",
                   (new_character['name'], new_character['threat'], new_character['health'], new_character['affiliation']))

    print(new_character['name'], "has joined the Brotherhood!")

    return new_character['name'] + " has joined the Brotherhood!", 201


@app.route('/characters/bulk', methods=['POST'])
def new_character_bulk():

    new_character = request.json
    new_character_list = []
    name_list = []

    for x in new_character:
        temptuple = x["name"], x["threat"], x["health"], x["affiliation"]
        new_character_list.append(temptuple)
        name_list.append(x["name"])

    result_list = []

    for x in name_list:
        result_list.append(f"{x} has joined the Brotherhood!")
        print(f"User has added {x} to the Brotherhood!")

    cursor.executemany(
        "INSERT INTO characters (name, threat, health, affiliation) VALUES (%s, %s, %s, %s)", new_character_list)

    return result_list, 201


@app.route('/characters/query', methods=['GET'])
def query():
    print(request.args)

    query_id = request.args.get('id', None)
    query_name = request.args.get('name', None)
    query_threat = request.args.get('threat', None)
    query_health = request.args.get('health', None)
    query_affiliation = request.args.get('affiliation', None)

    if not (query_id or query_name or query_threat or query_health or query_affiliation):
        return "You have to include one of the search paramters", 400
    
    sql = "SELECT id, name, threat, health, affiliation FROM characters WHERE "

    where_statement = []
    where = []

    if query_id:
        where_statement.append("id = %s")
        where.append(query_id)
    if query_name:
        where_statement.append("name = %s")
        where.append(query_name)
    if query_threat:
        where_statement.append("threat = %s")
        where.append(query_threat)
    if query_health:
        where_statement.append("health = %s")
        where.append(query_health)
    if query_affiliation:
        where_statement.append("affiliation LIKE concat('%', %s, '%')")
        where.append(query_affiliation)

    sql += ' AND '.join(where_statement)
    
    cursor.execute(sql, where)

    character_list = []

    for a, b, c, d, e in cursor:
        character_list.append({"id": a, "name": b, "threat": c, "health": d, "affiliation": e})

    return character_list


@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    cursor.execute(
        "SELECT id, name FROM characters WHERE id= %s", (id,))
    row = cursor.fetchone()

    if row is not None:
        cursor.execute("DELETE FROM characters WHERE id = %s", (id,))
        return "User has removed " + row[1] + " from the Brotherhood!"
    else:
        return "Unable to find a character with id" + id, 404


@app.route('/characters/<id>', methods=['PUT'])
def update_character(id):

    updated_character = request.json

    cursor.execute(
        "SELECT id, name, threat, health, affiliation FROM characters WHERE id = %s", (id,))
    row = cursor.fetchone()

    if row is not None:
        print("User updated the character with id " + id)
        cursor.execute("UPDATE characters SET name = %s, threat = %s, health = %s, affiliation = %s WHERE id = %s",
            (updated_character["name"] or row[1], updated_character["threat"] or row[2], updated_character["health"] or row[3], updated_character["affiliation"] or row[4], id))
        return "Successfully updated the character with id " + id, 200
    else:
        return "Unable to find a character with id " + id, 404


app.run(host="0.0.0.0", port=5111)

conn.close()
