DATA = [
    {
        'name':'Lorena',
        'age': 56,
        'organization': 'Python O',
        'position': 'Language Maker',
        'language': 'python'
    },
        {
        'name':'Martin',
        'age': 25,
        'organization': 'Python O',
        'position': 'Language Maker',
        'language': 'java'
    },
        {
        'name':'Raul',
        'age': 69,
        'organization': 'Platzi',
        'position': 'Language Maker',
        'language': 'c++'
    },
        {
        'name':'Hector',
        'age': 45,
        'organization': 'Intel',
        'position': 'Language Maker',
        'language': 'java'
    },
        {
        'name':'Maria',
        'age': 56,
        'organization': 'Platzi',
        'position': 'Language Maker',
        'language': 'python'
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 45, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 68}, DATA))

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()