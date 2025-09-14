def add_obj(lst, obj):
    lst.append(obj)


def remove_obj(lst, obj):
    if obj in lst:
        lst.remove(obj)
    else:
        print("Item unavailable")

def check_obj(lst, obj):
    if obj in lst:
        print(f'Availability: "{obj} is available"')
    else:
        print(f'{obj} is not available')

initial_menu = input("Enter menu items (space separated): ").split()

add_item = input("Enter item to add: ")
add_obj(initial_menu, add_item)

remove_item = input("Enter item to remove: ")
remove_obj(initial_menu, remove_item)

check_item = input("Enter item to check: ")
check_obj(initial_menu, check_item)

print("Updated menu:", initial_menu)
