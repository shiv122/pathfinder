import random
import flask
import json
from flask import request, jsonify, render_template
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/path', methods=['GET'])
def index():
    return render_template('./index.html')


@app.route('/route', methods=['POST'])
def route():
    data = request.stream.read()
    start_x = int(json.loads(data)[1][0]['start_x'])
    start_y = int(json.loads(data)[1][0]['start_y'])
    end_x = int(json.loads(data)[1][0]['end_x'])
    end_y = int(json.loads(data)[1][0]['end_y'])
    grid = Grid(matrix=create_matrix(json.loads(data)[0]))

    start = grid.node(start_x, start_y)
    end = grid.node(end_x, end_y)
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    print(grid.grid_str(path=path, start=start, end=end))
    return json.dumps(path)


@app.route('/', methods=['POST'])
def home():
    data = request.stream.read()
    start_x = int(json.loads(data)[1]['start_x'])
    start_y = int(json.loads(data)[1]['start_y'])
    end_x = int(json.loads(data)[1]['end_x'])
    end_y = int(json.loads(data)[1]['end_y'])

    # start = (start_x, start_y)
    # end = (end_x, end_y)

    # path = astar(), start, end)

    # return json.dumps(create_matrix(json.loads(data)[0]))
    grid = Grid(matrix=create_matrix(json.loads(data)[0]))

    start = grid.node(start_x, start_y)
    end = grid.node(end_x, end_y)
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, grid)
    print(grid.grid_str(path=path, start=start, end=end))
    return json.dumps(path)


def create_matrix(data):
    matrix = []
    new_matrix = []
    for i in range(len(data)):
        matrix.append([])
        new_matrix.append([])
        for j in range(len(data[i])):
            matrix[i].append(data[i][j])
            val = 0 if data[i][j]['occupied'] == 1 else 1
            new_matrix[i].append(val)
    return new_matrix


app.run()
