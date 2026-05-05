# ============================================================
# SISTEMA DE CONTROL DE DISPOSITIVOS INTELIGENTES- EJERCISIO 5 
# Fase 3 - Modelos de herencia y polimorfismo y gestion de metodos 
# Curso: Programación - UNAD
# Autor: William Beltrán
# ============================================================

# ============================================
# NATIONAL OPEN AND DISTANCE UNIVERSITY (UNAD)
# COURSE: PROGRAMMING
# ACTIVITY: PHASE 3 - OOP
# STUDENT: [YOUR NAME]
# ============================================

# This program implements a Smart Device Control System using
# Object-Oriented Programming (OOP) principles.
#
# Concepts applied:
# - Inheritance
# - Polymorphism
# - Method Overloading (simulated with optional parameters)
# - Encapsulation
#
# A graphical user interface (GUI) is also implemented using Tkinter,
# allowing user interaction with the system.

import tkinter as tk

# ============================================
# BASE CLASS (ENCAPSULATION)
# ============================================

class Device:
    def __init__(self, name):
        self._name = name
        self._state = False

    def turn_on(self):
        self._state = True
        return f"{self._name} turned ON"

    def turn_off(self):
        self._state = False
        return f"{self._name} turned OFF"

    def status(self):
        return f"{self._name}: {'ON' if self._state else 'OFF'}"

    def get_name(self):
        return self._name


# ============================================
# CHILD CLASSES
# ============================================

class SmartBulb(Device):

    def turn_on(self):
        self._state = True
        return f"{self._name} light is ON"

    def turn_off(self):
        self._state = False
        return f"{self._name} light is OFF"

    def status(self):
        return f"Bulb {self._name}: {'ON' if self._state else 'OFF'}"

    #  SOBRECARGA REAL (VARIOS ESCENARIOS)
    def configure(self, mode, intensity=None, time=None):
        if intensity is None and time is None:
            return f"{self._name} set to mode: {mode}"
        elif time is None:
            return f"{self._name} set to mode: {mode}, intensity: {intensity}"
        else:
            return f"{self._name} set to mode: {mode}, intensity: {intensity}, time: {time}"


class SmartCurtain(Device):

    def turn_on(self):
        self._state = True
        return f"{self._name} curtain OPEN"

    def turn_off(self):
        self._state = False
        return f"{self._name} curtain CLOSED"

    def status(self):
        return f"Curtain {self._name}: {'OPEN' if self._state else 'CLOSED'}"

    def configure(self, mode, intensity=None, time=None):
        if intensity is None and time is None:
            return f"{self._name} mode: {mode}"
        elif time is None:
            return f"{self._name} mode: {mode}, opening: {intensity}%"
        else:
            return f"{self._name} mode: {mode}, opening: {intensity}%, time: {time}"


class SmartThermostat(Device):

    def turn_on(self):
        self._state = True
        return f"{self._name} thermostat ON"

    def turn_off(self):
        self._state = False
        return f"{self._name} thermostat OFF"

    def status(self):
        return f"Thermostat {self._name}: {'ON' if self._state else 'OFF'}"

    def configure(self, mode, intensity=None, time=None):
        if intensity is None and time is None:
            return f"{self._name} mode: {mode}"
        elif time is None:
            return f"{self._name} mode: {mode}, temperature: {intensity}°C"
        else:
            return f"{self._name} mode: {mode}, temperature: {intensity}°C, time: {time}"


# ============================================
# CONTROL CENTER
# ============================================

class ControlCenter:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_on_all(self):
        return [d.turn_on() for d in self.devices]

    def turn_off_all(self):
        return [d.turn_off() for d in self.devices]

    def get_status(self):
        return [d.status() for d in self.devices]

    #  CONFIGURACIÓN INDIVIDUAL (REQUERIMIENTO DEL ANEXO)
    def configure_device(self, name, mode, intensity=None, time=None):
        for d in self.devices:
            if d.get_name() == name:
                return d.configure(mode, intensity, time)
        return "Device not found"


# ============================================
# GUI (TKINTER)
# ============================================

class App:
    def __init__(self, root):
        self.control = ControlCenter()

        # Devices
        self.control.add_device(SmartBulb("Living Room"))
        self.control.add_device(SmartCurtain("Main Window"))
        self.control.add_device(SmartThermostat("Home"))

        root.title("Smart Home Control Panel")

        tk.Button(root, text="Turn ON All", command=self.turn_on).pack()
        tk.Button(root, text="Turn OFF All", command=self.turn_off).pack()
        tk.Button(root, text="Show Status", command=self.show_status).pack()

        # CONFIG SECTION (OBLIGATORIA)
        tk.Label(root, text="Configure Device").pack()

        self.device_entry = tk.Entry(root)
        self.device_entry.insert(0, "Device name")
        self.device_entry.pack()

        self.mode_entry = tk.Entry(root)
        self.mode_entry.insert(0, "Mode")
        self.mode_entry.pack()

        self.intensity_entry = tk.Entry(root)
        self.intensity_entry.insert(0, "Intensity (optional)")
        self.intensity_entry.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.insert(0, "Time (optional)")
        self.time_entry.pack()

        tk.Button(root, text="Configure", command=self.configure).pack()

        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()

    def turn_on(self):
        self.print_output(self.control.turn_on_all())

    def turn_off(self):
        self.print_output(self.control.turn_off_all())

    def show_status(self):
        self.print_output(self.control.get_status())

    def configure(self):
        name = self.device_entry.get()
        mode = self.mode_entry.get()

        intensity = self.intensity_entry.get()
        time = self.time_entry.get()

        # Convert empty strings to None
        intensity = intensity if intensity != "" else None
        time = time if time != "" else None

        result = self.control.configure_device(name, mode, intensity, time)
        self.print_output([result])

    def print_output(self, messages):
        self.output.delete(1.0, tk.END)
        for msg in messages:
            if msg:
                self.output.insert(tk.END, str(msg) + "\n")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()