class MainController:
    def __init__(self, rocket_controller, site_controller, launch_controller):
        self.rocket_controller = rocket_controller
        self.site_controller = site_controller
        self.launch_controller = launch_controller

    def run(self):
        while True:
            print("\n--- Rocket Launch Management ---")
            print("1. Add Rocket")
            print("2. Add Launch Site")
            print("3. Add Launch")
            print("4. List Rockets")
            print("5. List Launch Sites")
            print("6. List Launches")
            print("0. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                self.rocket_controller.add_rocket()
            elif choice == "2":
                self.site_controller.add_launch_site()
            elif choice == "3":
                self.launch_controller.add_launch()
            elif choice == "4":
                self.rocket_controller.list_rockets()
            elif choice == "5":
                self.site_controller.list_launch_sites()
            elif choice == "6":
                self.launch_controller.list_launches()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
