def create_to_do_list():
    with open ("to_do_list.txt", "w", encoding="utf-8") as file:
        pass
    print("Catatan To Do List berhasil dibuat.\n")

def show_task():
    with open ("to_do_list.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    if tasks:
        print("Daftar Tugas:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task.strip()}")
        print()
    else:
        print("Belum ada tugas yang ditambahkan.\n")