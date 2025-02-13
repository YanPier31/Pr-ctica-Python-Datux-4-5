from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

def menu():
    console=Console()
    while True:
        menu_text = Text()
        menu_text.append("\n [bold cyan]Proyecto Datux[/bold cyan]\n", style="underline bold")
        menu_text.append("\n[1] Ingestar Data\n", style="green")
        menu_text.append("[2] Reporte de Ventas\n", style="blue")
        menu_text.append("[3] Salir\n", style="red")

        console.print(Panel(menu_text, title="[bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="green"))
        opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1","2","3"], default="3")

        if opcion == "1":
            pass
        elif opcion =="2":
            pass
        elif opcion =="3":
            pass
            break

