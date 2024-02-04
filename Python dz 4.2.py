def get_humans_info(path):
    try:
        humans_list = []
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                human_id, name, age = line.strip().split(',')
                human_info = {"id": human_id, "name": name, "age": age}
                humans_list.append(human_info)
        return humans_list
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

humans_info = get_humans_info("path/to/humans_file.txt")
print(humans_info)