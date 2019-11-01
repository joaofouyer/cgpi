import json
from primitives.point_graph import PointGraph
from primitives.line_graph import LineGraph
from primitives.rectangle_graph import RectangleGraph
from primitives.polygon_graph import PolygonGraph
from primitives.circle_graph import CircleGraph


def hex_to_rgb(color):
    try:
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        return {"r": rgb[0], "g": rgb[1], "b": rgb[2]}

    except Exception as e:
        print("Exception on hex to rbg: {} {}".format(type(e), e))
        raise e


def normalize(x, size):
    try:
        return x / size
    except Exception as e:
        print("Exception on normalize point: {} {}".format(type(e), e))
        raise e


def point_to_json(point, width, height):
    try:
        return {"x": normalize(x=point.x, size=width), "y": normalize(x=point.y, size=height)}
    except Exception as e:
        print("Exception on point to json: {} {}".format(type(e), e))
        raise e


def export_json(window):
    try:
        dict = {
            "figura": {
                "reta": [],
                "circulo": [],
                "retangulo": [],
                "poligono": []
            }
        }
        for f in window.actions.actions_stack:
            print(type(f))
            color = hex_to_rgb(f.color)
            if isinstance(f, RectangleGraph):
                p1 = point_to_json(point=f.p1, width=window.canvas_width, height=window.height)
                p2 = point_to_json(point=f.p2, width=window.canvas_width, height=window.height)
                dict['figura']['retangulo'].append({"p1": p1, "p2": p2, "color": color})
            elif isinstance(f, PolygonGraph):
                pass
            elif isinstance(f, CircleGraph):
                pass
            elif isinstance(f, LineGraph):
                p1 = point_to_json(point=f.p1, width=window.canvas_width, height=window.height)
                p2 = point_to_json(point=f.p2, width=window.canvas_width, height=window.height)
                dict['figura']['reta'].append({"p1": p1, "p2": p2, "color": color})
            else:
                print("Figura não suportada!")
        with open('export.json', 'w') as exportfile:
            json.dump(dict, exportfile)
    except Exception as e:
        print("Exception on export_json: {} {}".format(type(e), e))
        raise e
