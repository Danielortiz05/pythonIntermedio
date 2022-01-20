def run ():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Daniel", "lastname": "Ortiz"}


    super_list = [
        {"firstname": "Daniel", "lastname": "Ortiz"},
        {"firstname": "Miguel", "lastname": "Duran"},
        {"firstname": "Pepe", "lastname": "Rodriguez"},
        {"firstname": "Pepa", "lastname": "Hernandez"},
        {"firstname": "Susana", "lastname": "Martinez"},
    ]


    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "float_nums": [1.1, 4.5, 6.43],
    }


    for key, value in super_dict.items():
        print(key, "-", value)


    for i in super_list:
        print(i["firstname"], i["lastname"])


if __name__ == '__main__':
    run()