from database import create_database, add_box, get_all_boxes, \
    get_one_box, get_container, add_box_to_container, seed_data, get_all_containers,\
    get_all_freight, get_config
from tabulate import tabulate


def retrieve_numeric_input(value):
    """
    error checking for numerical value
    :param value: box details input
    :return: value for box
    """
    input_ok = False
    n = None
    while not input_ok:
        n = input(f"\n Enter {value} ")
        try:
            n = float(n)
            input_ok = True
        except ValueError:
            print("Please provide a numeric input")

    return n


def add_box_menu():
    """
    adding the box's name, height, width, length
    :return: None
    """
    box_name = input("\nEnter name dor the box: ")
    box_height = retrieve_numeric_input(value="the box height in meters")
    box_width = retrieve_numeric_input(value="the box width in meters")
    box_length = retrieve_numeric_input(value="the box length in meters")

    add_box(connection, (box_name, box_height, box_width, box_length))


def display_boxes():
    """
    display the boxes
    :return: boxes
    """
    boxes = get_all_boxes(connection)
    if len(boxes) == 0:
        print("\nPlease add a a box!")
    print("\n" + tabulate(boxes,
                          headers=['box_id', 'box_name', 'height', 'width', 'length'],
                          tablefmt='psql') + "\n"
          )


def load_box_menu():
    """
    taking container details and checking with the box space and showing messages to the user
    """
    # ask the box name
    n = input("Enter the box name: ")
    # validation weather box exists
    box = get_one_box(connection, by_name=n)
    if not box:
        print(f"\nThere is not box named {n}! \n")
    else:
        box_dims = box.height * box.width * box.height
        container_id = input("Enter the container ID to load the box to: ")
        container = get_container(connection, container_id)
        if container is None or (container.occupied_volume + box_dims <= float(config.get("MAX_CONTAINER_STORAGE")),):
            # insert and add the box to freight
            add_box_to_container(connection, box.id, container_id)
            print(f"Box {box.name} added to Container {container_id}")

        else:
            print(f"Container {container_id} does not have enough space for box {box.id}")




def display_containers():
    """ Print container details """
    containers = get_all_containers(connection)
    print("\n" + tabulate(containers, headers=["container_id", "occupied_volume"], tablefmt="fancy_grid") + "\n")



def display_summary():
    """
    Summary of the complete transaction

    """
    freight = get_all_freight(connection)
    containers = get_all_containers(connection) or ()

    num_containers = len(containers)

    if not num_containers:
        print("\nThere is no contracted freight currently!\n")

    contracted_volume = sum([c.occupied_volume for c in containers])
    revenue = round(contracted_volume * float(config.get("CUBIC_METER_CHARGEOUT")), 2)

    cost = num_containers * float(config.get("COST_PER_CONTAINER"))

    print(f"Contracted {len(freight)} in {len(containers)} container.")
    print(f"The total contracted volume is {contracted_volume} meters!")
    print(f"Estimated total cost of this freight is: ${cost}")
    print(f"Estimated P/L: ${revenue - cost}\n")





# creating an interface for freight manager
def main_menu():
    print("Welcome to Transport Manager!")
    n = "no_op"
    while n.upper() != 'X':
        print("""
            1. Add a box type
            2. Show all box types
            3. Load box to container
            4. Show container 
            5. Summary Report 
            X. Close\n
        """)
        n = input("Your Choices: ")
        if n == "1":
            print("Adding the box!")
            add_box_menu()
        elif n == "2":
            print("Displaying the boxes!")
            display_boxes()
        elif n == "3":
            print("Loading box menue.. .")
            load_box_menu()
        elif n == "4":
            print("display all containers")
            display_containers()
        elif n == "5":
            print("Complete Summery\n")
            display_summary()


    print("\nThank You and Goodbye!")


if __name__ == "__main__":
    # created the database and tables
    connection = create_database(filename='delivery_manager.db')
    # inserting boxes data
    seed_data(connection)
    config = get_config(connection)

    # main function
    main_menu()
