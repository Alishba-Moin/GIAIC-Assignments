import json     # Used to save and load book data
import os       # Used to check if the library file exists
import time     # Used to create a loading effect when adding books.
from rich.console import Console    # Provides a styled console for displaying colored text
from rich.table import Table        # Displays books in a tabular format
from rich.prompt import Prompt, Confirm # Used to get user input and confirmation
from rich.progress import Progress  # Shows a progress bar when adding books


LIBRARY_FILE = "library.json"    # File to store books
console = Console()     # Initializes the Rich console for printing formatted output.


#  Loading the Library from a File
def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return []
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


#  Saving the Library to a File
def save_library(books):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(books, file, indent=4)


# Displaying the Main Menu
def display_menu():
    console.print("\n[bold cyan]Personal Library Manager[/bold cyan]", style="bold white")
    console.print("1. Add a Book", style="bold green")
    console.print("2. Remove a Book", style="bold red")
    console.print("3. Search for a Book", style="bold blue")
    console.print("4. Display All Books", style="bold magenta")
    console.print("5. View Statistics", style="bold cyan")
    console.print("6. Exit", style="bold yellow")


# Adding a New Book
def add_book(books):
    title = Prompt.ask("Enter the book title")
    author = Prompt.ask("Enter the author")
    year = int(Prompt.ask("Enter the publication year"))
    genre = Prompt.ask("Enter the genre")
    read = Confirm.ask("Have you read this book?")

    with Progress() as progress:
        task = progress.add_task("[purple]Adding book...[/purple]", total=100)
        for _ in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)
    
    books.append({"title": title, "author": author, "year": year, "genre": genre, "read": read})
    save_library(books)
    console.print(f"✔ Book '[bold]{title}[/bold]' added successfully!", style="green")


# Removing a Book
def remove_book(books):
    title = Prompt.ask("Enter the title of the book to remove")
    updated_books = [book for book in books if book["title"].lower() != title.lower()]
    
    if len(updated_books) == len(books):
        console.print("Book not found!", style="bold red")
    else:
        save_library(updated_books)
        console.print(f"✔ Book '[bold]{title}[/bold]' removed successfully!", style="bold green")
        return updated_books

    return books
#  Searching for a Book
def search_book(books):
    query = Prompt.ask("Enter title or author to search").lower()
    found_books = [book for book in books if query in book["title"].lower() or query in book["author"].lower()]
    
    if not found_books:
        console.print("No books found!", style="bold yellow")
    else:
        table = Table(title="Search Results", show_header=True, header_style="bold blue")
        table.add_column("Title", style="bold cyan")
        table.add_column("Author", style="bold green")
        table.add_column("Year", style="bold yellow")
        table.add_column("Genre", style="bold magenta")
        table.add_column("Status", style="bold red")

        for book in found_books:
            status = "Read" if book["read"] else "Unread"
            table.add_row(book["title"], book["author"], book["year"], book["genre"], status)
        
        console.print(table)


# Displaying All Books
def display_books(books):
    if not books:
        console.print("No books in the library.", style="bold yellow")
        return
    
    table = Table(title="Library Books", show_header=True, header_style="bold blue")
    table.add_column("#", style="bold cyan")
    table.add_column("Title", style="bold cyan")
    table.add_column("Author", style="bold green")
    table.add_column("Year", style="bold yellow")
    table.add_column("Genre", style="bold magenta")
    table.add_column("Status", style="bold red")
    
    for index, book in enumerate(books, 1):
        status = "Read" if book["read"] else "Unread"
        table.add_row(str(index), book["title"], book["author"], book["year"], book["genre"], status)
    
    console.print(table)


#  Displaying Library Statistics
def display_statistics(books):
    total_books = len(books)
    if total_books == 0:
        console.print("No books in the library.", style="bold yellow")
        return
    
    read_books = sum(1 for book in books if book["read"])
    percentage_read = (read_books / total_books) * 100
    
    console.print("\n[bold cyan]Library Statistics[/bold cyan]", style="bold white")
    console.print(f"Total Books: [bold]{total_books}[/bold]", style="bold green")
    console.print(f"Books Read: [bold]{read_books}[/bold] ({percentage_read:.2f}%)", style="blue")
    console.print(f"Unread Books: [bold]{total_books - read_books}[/bold]", style="bold red")

def main():
    books = load_library()
    while True:
        display_menu()
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            add_book(books)
        elif choice == "2":
            books = remove_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            display_statistics(books)
        elif choice == "6":
            save_library(books)
            console.print("\n📚 [bold yellow]Library saved successfully! See you next time.[/bold yellow] 🚀\n", style="bold green")
            break


if __name__ == "__main__":
    main()
