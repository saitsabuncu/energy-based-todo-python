def show_menu():
    print("Enerji Bazlı Todo List")
    print("1- Görev Ekle")
    print("2- Görevleri Listele")
    print("3- Enerjime Göre Görev Göster")
    print("4- Görev Tamamla")
    print("5- Çıkış")
    
def add_task(tasks):
    title = input("Görev adı: ")
    energy = get_valid_energy()
    
    task = {
            "title": title,
            "energy": energy,
            "done": False
        }
    tasks.append(task)
    print("Görev eklendi.")

def list_tasks(tasks):
    if not tasks:
        print("Henüz görev yok.")
        return
    
    for i, task in enumerate(tasks):
        situation = "✓" if task["done"] else " "
        print(f"{i+1}. [{situation}] {task['title']} (Enerji {task['energy']})")
        
def show_by_energy(tasks):
    current_energy = get_valid_energy()
    found = False
    
    for task in tasks:
        if task["energy"] == current_energy and not task["done"]:
            print(f"- {task['title']}")
            found = True
    if not found:
        print("Bu enerji seviyesine uygun görev yok.")
            
def complete_task(tasks):
    no = int(input("Tamamlanan görev numarası: ")) - 1
    
    if 0 <= no < len(tasks):
        tasks[no]["done"] = True
        print("Görev tamamlandı.")
    else:
        print("Geçersiz numara.")
        
def daily_summary(tasks):
    print("Gün Özeti:")
    summary={1: 0, 2: 0, 3: 0}
    
    for task in tasks:
        if task["done"]:
           summary[task["energy"]] += 1
           
    for energy, piece in summary.items():
        print(f"Enerji {energy}: {piece} görev")

def get_valid_energy():
    while True:
        try:
            energy = int(input("Enerji seviyesi (1-3): "))
            if energy in (1, 2, 3):
                return energy
            else:
                print("Enerji seviyesi sadece 1, 2 veya 3 olabilir.")
        except ValueError:
            print("Lütfen sayı gir.")
tasks = []

while True:
    show_menu()
    vote = input("Seçimin: ")
    
    if vote == "1":
        add_task(tasks)
    elif vote == "2":
        list_tasks(tasks)
    elif vote == "3":
        show_by_energy(tasks)
    elif vote == "4":
        complete_task(tasks)
    elif vote == "5":
        daily_summary(tasks)
        break
    else:
        print("Geçersiz seçim.")
