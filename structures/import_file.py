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
        print("Exception on normalize point: {} {}".format(type(e), e))
        raise e


def clamp(x):
    return max(0, min(x, 255))


def rbg_to_hex(color):
    try:
        return "#{0:02x}{1:02x}{2:02x}".format(clamp(color['r']), clamp(color['g']), clamp(color['b']))
    except Exception as e:
        print("Exception on rbg_to_hex: {} {}".format(type(e), e))
        raise e


def import_json(filename, window):
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            figure = data.get("figura")
            for r in figure.get("reta"):
                color = rbg_to_hex(color=r['cor'])
                LineGraph(
                    p1=normalize_point(point=r['p1'], window=window, color=color),
                    p2=normalize_point(point=r['p2'], window=window, color=color),
                    color=color
                ).draw(window=window, action=True)

            for r in figure.get("retangulo"):
                color = rbg_to_hex(color=r['cor'])
                RectangleGraph(
                    p1=normalize_point(point=r['p1'], window=window, color=color),
                    p2=normalize_point(point=r['p2'], window=window, color=color),
                    color=color
                ).draw(window=window, action=True)

            for polygon in figure.get("poligono"):
                color = rbg_to_hex(color=polygon['cor'])
                poligono = PolygonGraph(color=color)
                for p in polygon["ponto"]:
                    poligono.push(normalize_point(point=p, window=window, color=color))
                poligono.draw(window=window, multiple_points=True)

            for c in figure.get("circulo"):
                color = rbg_to_hex(color=c['cor'])
                center = normalize_point(point=c['ponto'], window=window, color=color)
                radius = c['raio'] * ((window.canvas_width + window.height) / 2)
                circle = CircleGraph(center=center, radius=radius, color=color)
                circle.draw(window=window, action=True)

        return False
    except Exception as e:
        print("Exception on import json: {} {}".format(type(e), e))
        raise e
