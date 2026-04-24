import flet as ft
print(f"Flet version: {ft.__version__}")
try:
    print(f"Colors access: {ft.colors}")
except Exception as e:
    print(f"Colors access ERROR: {e}")

try:
    from flet import colors
    print("Import from flet.colors successful")
except Exception as e:
    print(f"Import from flet.colors ERROR: {e}")
