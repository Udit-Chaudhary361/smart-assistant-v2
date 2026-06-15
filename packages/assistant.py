from packages.storage import load_data, save_data


def set_name(name):
    data = load_data()
    data["name"] = name
    save_data(data)


def add_note(note):
    data = load_data()
    data["notes"].append(note)
    save_data(data)


def view_notes():
    data = load_data()
    return data["notes"]



def add_task(task):
    data = load_data()
    data["tasks"].append(task)
    save_data(data)


def view_tasks():
    data = load_data()
    return data["tasks"]