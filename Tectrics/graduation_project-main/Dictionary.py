def item_to_dict(item):
    return {
        "partno": item.partno,
        "name": item.name,
        "typeof": item.typeof,
        "dimensions": {
            "width": item.width,
            "height": item.height,
            "depth": item.depth
        },
        "weight": item.weight,
        "level": item.level,
        "loadbear": item.loadbear,
        "updown": item.updown,
        "color": item.color,
        "rotation_type": item.rotation_type,
        "position": item.position
    }

def bin_to_dict(bin):
    return {
        "partno": bin.partno,
        "dimensions": {
            "width": bin.width,
            "height": bin.height,
            "depth": bin.depth
        },
        "max_weight": bin.max_weight,
        "items": [item_to_dict(item) for item in bin.items]
    }
