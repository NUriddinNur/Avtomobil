#_______________________________________ Aftomobil ____________________________________________________
import os
import time


class Car:
    def __init__(self, car, petrol, turn=False):
        self.car = car
        self.petrol = petrol
        self.turn = turn
        self.select_options()

    def select_options(self):
        if self.turn:
            print("\n>>> g'in - g'innnnn")
        else:
            print("\n>>> Turn off")
        self.show_car_option()
        input_options = input(">>> ").strip()
        options = ['1', '2', '3', '4', '5']

        while input_options not in options:
            self.clear_window()
            if self.turn:
                print("\n>>> Turn on")
            else:
                print("\n>>> Turn off")
            self.show_car_option()
            print("[1/2/3/4/5]")
            input_options = input(">>> ").strip()

        if input_options == '1':
            self.turn_on()
        elif input_options == '2':
            self.turn_off()
        elif input_options == '3':
            if not self.turn:
                self.clear_window()
                print("""\n\n\n\t\tMashinani o't oldirin""")
                time.sleep(1)
                self.clear_window()
                self.select_options()
            else:
                self.go_to()
        elif input_options == '4':
            self.fill_petrol()
        else:
            self.view_status()

    def turn_on(self):
        if self.petrol == 0:
            self.clear_window()
            print("\n\n\n\t\tYoqilg'i yo'q !!!")
            time.sleep(2)
            self.clear_window()
            self.select_options()
        else:
            self.clear_window()
            self.turn = True
            self.select_options()

    def turn_off(self):
        self.clear_window()
        self.turn = False
        self.select_options()

    def go_to(self):
        input_destance = input("Masofani kiriting >>> ").strip()
        while not input_destance.isnumeric():
            self.clear_window()
            self.show_car_option()
            input_destance = input("Masofani kiriting >>> ").strip()
        print(self.petrol - int(input_destance) // 10)
        if self.petrol == 0:
            self.turn = False
            print("Yoqilg'i tugadi >>>")
            self.select_options()

        elif self.petrol - int(input_destance) // 10 < 0:
            print("Yoqilg'i belgilangan masofaga yetmaydi >>>")
            self.__init__(self.car, self.petrol, self.turn)
        else:
            self.petrol -= int(input_destance) / 10

            self.clear_window()
            print("\n\n\n\t\tMasofa bosib o'tildi")
            time.sleep(2)
            self.clear_window()
            self.select_options()

            # print("Masofa bosib o'tildi")
            # self.__init__(self.car, self.petrol, self.turn)

    def fill_petrol(self):
        if self.petrol == 100:
            self.clear_window()
            print("\n\n\n\t\tYoqilg'i baki to'la")
            time.sleep(2)
            self.clear_window()
            self.select_options()
        input_fill_petrol = input("Yoqilg'i quyin >>> ").strip()
        while not input_fill_petrol.isnumeric():
            self.clear_window()
            self.show_car_option()
            input_fill_petrol = input("Yoqilg'i quyin >>> ").strip()
        if self.petrol + int(input_fill_petrol) > 100:
            self.clear_window()
            print(f"""\n\n\n\t\t{int(input_fill_petrol) + self.petrol - 100} Litr ortiqcha yoqilg'i quyyapsiz !!!""")
            time.sleep(2)
            self.clear_window()
            self.select_options()
        else:
            self.clear_window()
            self.petrol += int(input_fill_petrol)
            print("\n\n\n\t\tYoqilg'i quyildi !!!")
            time.sleep(2)
            self.clear_window()
            self.select_options()

    def view_status(self):
        self.clear_window()
        print(f"\n\n\n\t\tMashina: {self.car} Yoqilg'i: {self.petrol}")
        time.sleep(2)
        self.clear_window()
        self.select_options()
        # print(f"Mashina: {self.car} Yoqilg'i: {self.petrol}")

    # _________________________________________ Show function ___________________________________

    @staticmethod
    def show_car_option():
        print("""
                 Car

            1. Engine on
            2. Engine off
            3. Go to
            4. Fill petrol
            5. View status
        """)

    @staticmethod
    def clear_window():
        os.system("clear")


car1 = Car("Nexia", 100)
