#!/usr/bin/python3
""" main
"""

if __name__ == '__main__':
    import sys
    from os import path

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from = __import__("6-load_from_json_file").load_from_json_file

    file = "add_item.json"
    exist_file = path.exists(file)
    if exist_file:
        pass
    else:
        save_to_json_file([], file)

    if len(sys.argv) == 1 and not exist_file:
        save_to_json_file([], file)
    elif len(sys.argv) < 2:
        pass
    else:
        data_as_obj = load_from(file)
        for i in range(1, len(sys.argv)):
            data_as_obj.append(sys.argv[i])
        save_to_json_file(data_as_obj, file)
