import json
from primitives.point_graph import PointGraph
from primitives.line_graph import LineGraph
from primitives.rectangle_graph import RectangleGraph
from primitives.polygon_graph import PolygonGraph
from primitives.circle_graph import CircleGraph


def normalize_point(point, window, color):
    try:
        return PointGraph(
            x=round(point['x']*window.canvas_width),
            y=round(point['y']*window.height),
            window=window,
            color=color
        )
    except Exception as e:
        print("Exception on import_file:", e)
        return True


def import_json(filename, window):
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            figure = data.get("figura")
            for r in figure.get("reta"):
                color = "#000000"
                LineGraph(
                    p1=normalize_point(point=r['p1'], window=window, color=color),
                    p2=normalize_point(point=r['p2'], window=window, color=color),
                    color=color
                ).draw(window=window, action=False)

            for r in figure.get("retangulo"):
                color = "#000000"
                RectangleGraph(
                    p1=normalize_point(point=r['p1'], window=window, color=color),
                    p2=normalize_point(point=r['p2'], window=window, color=color),
                    color=color
                ).draw(window=window, action=False)

            for polygon in figure.get("poligono"):
                poligono = PolygonGraph()
                for p in polygon["ponto"]:
                    color = "#000000"
                    poligono.push(normalize_point(point=p, window=window, color=color))
                poligono.draw(window=window, multiple_points=True)

            for c in figure.get("circulo"):
                color = "#000000"
                center = normalize_point(point=c['ponto'], window=window, color=color)
                radius = c['raio'] * ((window.canvas_width + window.height) / 2)
                circle = CircleGraph(center=center, radius=radius)
                circle.draw(window=window, action=False)

        return False
    except Exception as e:
        print("Exception on import_file:", e)
        return True
