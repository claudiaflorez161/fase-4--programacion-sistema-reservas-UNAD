# ============================================================
# INFORMACION DEL COMPONENTE PRACTICO  Ejercicio 1
# Fase 4 Componente Práctico-Practicas Simuladas Sistema de Gestion de clienetes, Servicios y Reservas 
# Curso: Programación - UNAD 213023_280
# Autor: William Beltrán
# Claudia Lorena Franco
# Farid Camilo Buitrago
# ============================================================

# ============================================
# NATIONAL OPEN AND DISTANCE UNIVERSITY (UNAD)
# COURSE: PROGRAMMING
# ACTIVITY: PHASE 4 - OOP
# STUDENT: William Beltrán
# Claudia Lorena Franco
# Farid Camilo Buitrago
# ============================================

# Practical Exercise - Simulated Practices: Customer, Service, and Reservation Management System
# Course: Programming - UNAD 213023_280
# Author: William Beltrán
# Claudia Lorena Franco
# Farid Camilo Buitrago
# Concepts applied:
# including custom exceptions, use of try/except, try/except/else, try/except/finally blocks, and exception chaining.


import tkinter as tk

# ============================================
# BASE CLASS (ENCAPSULATION)
# ============================================

"""
Custom exceptions module
Defines specific system errors
"""


class ClientError(Exception):
    """Raised when client data is invalid"""
    pass


class ServiceError(Exception):
    """Raised when a service is invalid"""
    pass


class ReservationError(Exception):
    """Raised when reservation cannot be processed"""
    pass