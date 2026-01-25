# =============================================================================
# Air Conditioner System - PYTHON SERIAL INTERFACE
# =============================================================================
# This program provides a serial communication interface between a PC and
# two microcontroller-based Air Conditioner System board.
#
# Air Conditioner System:
# - Reads ambient temperature
# - Reads user-defined desired temperature
# - Reads fan speed (rps)
# - Allows the user to update the desired temperature
#
# Author: Serkan SEVMEZ

import serial
import time

# =============================================================================
# SETTINGS
# =============================================================================
PORT_AC = 'COM10'  
BAUD_RATE = 9600  


# =============================================================================
# API CLASSES
# =============================================================================

class HomeAutomationSystemConnection:
    def __init__(self, port_name):
        self.ser = None
        self.comPort = port_name
        self.baudRate = BAUD_RATE

    def open(self):
        try:
            self.ser = serial.Serial(self.comPort, self.baudRate, timeout=2)
            print(f"[CONNECTION] {self.comPort} opened.")
            return True
        except Exception as e:
            print(f"[ERROR] {self.comPort} could not be opened: {e}")
            return False

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"[CONNECTION] {self.comPort} closed.")

    def send_byte(self, byte_val):
        if self.ser and self.ser.is_open:
            self.ser.write(bytes([byte_val]))
            time.sleep(0.05)

    def read_byte(self):
        if self.ser and self.ser.is_open:
            val = self.ser.read(1)
            if val:
                return int.from_bytes(val, byteorder='big')
        return 0


class AirConditionerSystemConnection(HomeAutomationSystemConnection):
    def __init__(self, port):
        super().__init__(port)
        self.desiredTemperature = 0.0
        self.ambientTemperature = 0.0
        self.fanSpeed = 0

    def update(self):
        # 1. Ambient Temperature
        self.send_byte(0x04)
        amb_int = self.read_byte()
        self.send_byte(0x03)
        amb_frac = self.read_byte()
        self.ambientTemperature = float(f"{amb_int}.{amb_frac}")

        # 2. Desired Temperature
        self.send_byte(0x02)
        des_int = self.read_byte()
        self.send_byte(0x01)
        des_frac = self.read_byte()
        self.desiredTemperature = float(f"{des_int}.{des_frac}")

        # 3. Fan Speed
        self.send_byte(0x05)
        self.fanSpeed = self.read_byte()

    def setDesiredTemp(self, temp):
        str_temp = f"{temp:.1f}"
        parts = str_temp.split('.')
        val_int = int(parts[0])
        val_frac = int(parts[1])
        if val_int > 63: val_int = 63
        if val_frac > 9: val_frac = 9

        self.send_byte(0xC0 | val_int)
        time.sleep(0.05)
        self.send_byte(0x80 | val_frac)
        return True

    def getAmbientTemp(self):
        return self.ambientTemperature

    def getDesiredTemp(self):
        return self.desiredTemperature

    def getFanSpeed(self):
        return self.fanSpeed


# =============================================================================
# APPLICATION MENU
# =============================================================================

def main_menu():
    print("Sistem Başlatılıyor...")
    ac_system = AirConditionerSystemConnection(PORT_AC)

    try:
        ac_system.open()
    except:
        pass

    while True:
        print("\n" + "=" * 40)
        print("      AIR CONDITIONER SYSTEM")
        print("=" * 40)
        print("1. Show Values")
        print("2. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            air_conditioner_menu(ac_system)
        elif choice == '2':
            ac_system.close()
            break
        else:
            print("Invalid choice!")


def air_conditioner_menu(system):
    while True:
        system.update()
        print("\n" + "-" * 40)
        print("   AIR CONDITIONER MENU")
        print("-" * 40)
        print(f"Home Ambient Temperature: {system.getAmbientTemp()} °C")
        print(f"Home Desired Temperature: {system.getDesiredTemp()} °C")
        print(f"Fan Speed: {system.getFanSpeed()} rps")
        print(f"Connection Port: COM10")
        print(f"Connection Baudrate: 9600")
        print("-" * 40)
        print("1. Enter the desired temperature")
        print("2. Return")

        choice = input("Choice: ")
        if choice == '1':
            try:
                val = float(input("Enter Desired Temp: "))
                system.setDesiredTemp(val)
            except ValueError:
                print("Error: Please enter a number.")
        elif choice == '2':
            break
        time.sleep(0.5)


if __name__ == "__main__":
    main_menu()
