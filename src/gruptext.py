import os
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from shutil import copyfile

console = Console()

class GrubText:
    def __init__(self):
        self.directory = "grubtext_pages"
        self.shared_directory = "shared_grubtext"
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.exists(self.shared_directory):
            os.makedirs(self.shared_directory)

    def show_home(self):
        console.clear()
        console.print(Panel("[bold magenta]GrubText Encyclopedia[/bold magenta]", style="bold green"))
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Action", justify="center")
        table.add_row("[bold]1.[/bold] View Pages")
        table.add_row("[bold]2.[/bold] Create New Page")
        table.add_row("[bold]3.[/bold] Edit Page")
        table.add_row("[bold]4.[/bold] Search Pages")
        table.add_row("[bold]5.[/bold] Export Page")
        table.add_row("[bold]6.[/bold] Import Page")
        table.add_row("[bold]7.[/bold] Backup & Restore")
        table.add_row("[bold]8.[/bold] Exit")
        console.print(table)
        action = Prompt.ask("Choose an action", choices=["1", "2", "3", "4", "5", "6", "7", "8"])
        if action == "1":
            self.view_pages()
        elif action == "2":
            self.create_page()
        elif action == "3":
            self.edit_page()
        elif action == "4":
            self.search_pages()
        elif action == "5":
            self.export_page()
        elif action == "6":
            self.import_page()
        elif action == "7":
            self.backup_restore()
        else:
            console.print("[bold red]Exiting...[/bold red]")
            exit()

    def view_pages(self):
        console.clear()
        console.print(Panel("[bold cyan]Available Pages[/bold cyan]", style="bold yellow"))
        pages = os.listdir(self.directory)
        if pages:
            table = Table(show_header=True, header_style="bold blue")
            table.add_column("Page Name", justify="left")
            for page in pages:
                table.add_row(page)
            console.print(table)
            choice = Prompt.ask("Enter page name to view", default="", choices=pages + ["back"])
            if choice != "back":
                self.view_page(choice)
            else:
                self.show_home()
        else:
            console.print("[bold red]No pages available.[/bold red]")
            self.show_home()

    def view_page(self, page_name):
        file_path = os.path.join(self.directory, page_name)
        with open(file_path, "r") as file:
            content = file.read()
        console.clear()
        console.print(Panel(f"[bold yellow]{page_name}[/bold yellow]", style="bold green"))
        console.print(content)
        console.print("[bold cyan]Press any key to return to home[/bold cyan]")
        console.input()

    def create_page(self):
        console.clear()
        console.print(Panel("[bold green]Create New Page[/bold green]", style="bold blue"))
        title = Prompt.ask("Enter the title of your page")
        filename = title.replace(" ", "_") + ".grup"
        content = Prompt.ask("Enter the content of your page")
        author = Prompt.ask("Enter author name", default="Unknown")
        metadata = {
            "author": author,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        page_data = {
            "metadata": metadata,
            "content": content
        }
        file_path = os.path.join(self.directory, filename)
        with open(file_path, "w") as file:
            json.dump(page_data, file, indent=4)
        console.print(f"[bold green]Page '{title}' created successfully![/bold green]")
        console.input("[bold cyan]Press any key to return to home[/bold cyan]")
        self.show_home()

    def edit_page(self):
        console.clear()
        console.print(Panel("[bold yellow]Edit Existing Page[/bold yellow]", style="bold red"))
        pages = os.listdir(self.directory)
        if pages:
            table = Table(show_header=True, header_style="bold blue")
            table.add_column("Page Name", justify="left")
            for page in pages:
                table.add_row(page)
            console.print(table)
            filename = Prompt.ask("Enter page name to edit", choices=pages)
            file_path = os.path.join(self.directory, filename)
            with open(file_path, "r") as file:
                page_data = json.load(file)
            new_content = Prompt.ask("Enter the new content", default=page_data["content"])
            page_data["content"] = new_content
            with open(file_path, "w") as file:
                json.dump(page_data, file, indent=4)
            console.print(f"[bold green]Page '{filename}' edited successfully![/bold green]")
        else:
            console.print("[bold red]No pages available to edit.[/bold red]")
        console.input("[bold cyan]Press any key to return to home[/bold cyan]")
        self.show_home()

    def search_pages(self):
        console.clear()
        console.print(Panel("[bold cyan]Search Pages[/bold cyan]", style="bold red"))
        search_query = Prompt.ask("Enter keyword to search for")
        pages = os.listdir(self.directory)
        matched_pages = []
        for page in pages:
            file_path = os.path.join(self.directory, page)
            with open(file_path, "r") as file:
                page_data = json.load(file)
                if search_query.lower() in page_data["content"].lower() or search_query.lower() in page:
                    matched_pages.append(page)
        if matched_pages:
            table = Table(show_header=True, header_style="bold blue")
            table.add_column("Matched Pages", justify="left")
            for page in matched_pages:
                table.add_row(page)
            console.print(table)
            choice = Prompt.ask("Enter page name to view", default="", choices=matched_pages + ["back"])
            if choice != "back":
                self.view_page(choice)
            else:
                self.show_home()
        else:
            console.print(f"[bold red]No pages matched '{search_query}'[/bold red]")
            self.show_home()

    def export_page(self):
        console.clear()
        console.print(Panel("[bold green]Export Page[/bold green]", style="bold blue"))
        pages = os.listdir(self.directory)
        if pages:
            table = Table(show_header=True, header_style="bold blue")
            table.add_column("Page Name", justify="left")
            for page in pages:
                table.add_row(page)
            console.print(table)
            filename = Prompt.ask("Enter page name to export", choices=pages)
            file_path = os.path.join(self.directory, filename)
            shared_path = os.path.join(self.shared_directory, filename)
            copyfile(file_path, shared_path)
            console.print(f"[bold green]Page '{filename}' exported successfully![/bold green]")
        else:
            console.print("[bold red]No pages available to export.[/bold red]")
        console.input("[bold cyan]Press any key to return to home[/bold cyan]")
        self.show_home()

    def import_page(self):
        console.clear()
        console.print(Panel("[bold yellow]Import Page[/bold yellow]", style="bold cyan"))
        shared_pages = os.listdir(self.shared_directory)
        if shared_pages:
            table = Table(show_header=True, header_style="bold blue")
            table.add_column("Shared Pages", justify="left")
            for page in shared_pages:
                table.add_row(page)
            console.print(table)
            filename = Prompt.ask("Enter page name to import", choices=shared_pages)
            shared_path = os.path.join(self.shared_directory, filename)
            file_path = os.path.join(self.directory, filename)
            copyfile(shared_path, file_path)
            console.print(f"[bold green]Page '{filename}' imported successfully![/bold green]")
        else:
            console.print("[bold red]No shared pages available to import.[/bold red]")
        console.input("[bold cyan]Press any key to return to home[/bold cyan]")
        self.show_home()

    def backup_restore(self):
        console.clear()
        console.print(Panel("[bold magenta]Backup & Restore[/bold magenta]", style="bold green"))
        action = Prompt.ask("Choose an action", choices=["backup", "restore"])
        if action == "backup":
            backup_dir = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            os.makedirs(backup_dir)
            for page in os.listdir(self.directory):
                copyfile(os.path.join(self.directory, page), os.path.join(backup_dir, page))
            console.print(f"[bold green]Backup created successfully in {backup_dir}[/bold green]")
        elif action == "restore":
            backup_dirs = [d for d in os.listdir() if d.startswith('backup_')]
            if backup_dirs:
                table = Table(show_header=True, header_style="bold blue")
                table.add_column("Backup Directories", justify="left")
                for backup in backup_dirs:
                    table.add_row(backup)
                console.print(table)
                backup_dir = Prompt.ask("Choose a backup directory to restore", choices=backup_dirs)
                for page in os.listdir(backup_dir):
                    copyfile(os.path.join(backup_dir, page), os.path.join(self.directory, page))
                console.print(f"[bold green]Backup restored successfully![/bold green]")
            else:
                console.print("[bold red]No backups available to restore.[/bold red]")
        console.input("[bold cyan]Press any key to return to home[/bold cyan]")
        self.show_home()

if __name__ == "__main__":
    grubtext = GrubText()
    grubtext.show_home()
