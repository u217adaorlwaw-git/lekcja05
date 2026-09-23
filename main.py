tasks = []
def task():
    i = 1
    whattodo = input("Co chciał byś zrobić(print, add, remove, edit) ")
    if whattodo == "print":
        print(tasks)
        task()
    elif whattodo == "add":
        add = input("Co dodać? ")
        tasks.append(add)
        print(f"Zadanie dodano {len(tasks)} zadań wsumie")
        task()
    elif whattodo == "remove":
        lenght = len(tasks)
        if lenght == 0:
            print("Brak zadań")
            task()
        else:
            getridof1 = input("Które zadanie powinno być usunięte? ")
            tasks.remove(getridof1)
            lenght = len(tasks)
            print(f"Zadanie usunięte", len(tasks), "zostało")
            task()
    elif whattodo == "edit":
        lenght1 = len(tasks)
        if lenght1 == 0:
            print("Brak zadań")
            task()
        else:
            edytuj = input("Co edytować? ")
            tasks.remove(edytuj)
            edytuj = input("Jakie powinno być nowe immie? ")
            tasks.append(edytuj)
            task()
    else:
        print("To nie jest komenda")
        task()
task()
