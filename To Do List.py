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

def add_task():
    try:
        total_tasks = int(input("Masukkan jumlah tugas yang ingin ditambahkan (angka saja): "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka saja.\n")
        return
    with open ("to_do_list.txt", "a", encoding="utf-8") as file:
        for i in range(total_tasks):
            task = input(f"Masukkan tugas {i + 1}: ")
            file.write(f"{task} [ ]\n")

def update_task():
    show_task()
    print("1. Tandai tugas sebagai selesai")
    print("2. Menghapus tanda pada tugas sebagai belum selesai")
    while True:
        try:
            update_choice = int(input("Pilih opsi pembaruan (angka saja): "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka saja.\n")

    if update_choice == 1:
        mark_task_as_completed()
    elif update_choice == 2:
        unmark_task_as_completed()
    else:
        print("Pilihan tidak valid.\n")

def mark_task_as_completed(): 
    while True:
        try:
            task_number = int(input("Masukkan nomor tugas yang ingin ditandai sebagai selesai (angka saja): "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka saja.\n")
            return

    with open ("to_do_list.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[\u2713]")
        with open ("to_do_list.txt", "w", encoding="utf-8") as file:
            file.writelines(tasks)
        print("Tugas berhasil ditandai sebagai selesai.\n")
    else:
        print("Nomor tugas tidak ditemukan.\n")

def unmark_task_as_completed():
    while True:
        try:
            task_number = int(input("Masukkan nomor tugas yang ingin dihapus tandanya sebagai belum selesai (angka saja): "))
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka saja.\n")

    with open ("to_do_list.txt", "r", encoding="utf-8") as file:
        tasks = file.readlines()
    
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[\u2713]", "[ ]")
        with open ("to_do_list.txt", "w", encoding="utf-8") as file:
            file.writelines(tasks)
        print("Tanda tugas berhasil dihapus, sekarang menjadi belum selesai.\n")
    else:
        print("Nomor tugas tidak ditemukan.\n")

update_task()