import tkinter as tk
from tkinter import messagebox, simpledialog

# 15 Flashcards
flashcards = [
    {"q": "What is the capital of India?", "a": "New Delhi"},
    {"q": "What is the national animal of India?", "a": "Tiger"},
    {"q": "What is the national bird of India?", "a": "Peacock"},
    {"q": "What is the capital of Maharashtra?", "a": "Mumbai"},
    {"q": "Where is the Taj Mahal located?", "a": "Agra"},
    {"q": "Who is known as the Father of Computer?", "a": "Charles Babbage"},
    {"q": "Who created the Python programming language?", "a": "Guido van Rossum"},
    {"q": "Who invented the Internet?", "a": "Vint Cerf and Bob Kahn"},
    {"q": "What is the largest ocean on Earth?", "a": "Pacific Ocean"},
    {"q": "1 KB equals how many Bytes?", "a": "1024 Bytes"},
    {"q": "What is the full form of CPU?", "a": "Central Processing Unit"},
    {"q": "What is RAM?", "a": "Random Access Memory"},
    {"q": "When did India get independence?", "a": "15 August 1947"},
    {"q": "Who is called the Father of the Nation?", "a": "Mahatma Gandhi"},
    {"q": "What is the aim of PM Awas Yojana?",
     "a": "To provide affordable housing to poor people"}
]

current_index = 0


# ---------------- FUNCTIONS ----------------

def show_question():
    """Display current flashcard."""
    question_label.config(
        text=flashcards[current_index]["q"]
    )

    answer_label.config(text="")

    counter_label.config(
        text=f"Question {current_index + 1} / {len(flashcards)}"
    )


def show_answer():
    """Show answer of current flashcard."""
    answer_label.config(
        text="Answer: " + flashcards[current_index]["a"]
    )


def next_card():
    """Move to next flashcard."""
    global current_index

    if current_index < len(flashcards) - 1:
        current_index += 1
        show_question()
    else:
        messagebox.showinfo(
            "Completed",
            "You have completed all the flashcards!"
        )


def previous_card():
    """Move to previous flashcard."""
    global current_index

    if current_index > 0:
        current_index -= 1
        show_question()
    else:
        messagebox.showinfo(
            "First Card",
            "This is the first flashcard."
        )


def add_flashcard():
    """Add a new flashcard."""

    question = simpledialog.askstring(
        "Add Flashcard",
        "Enter your question:"
    )

    if question is None or question.strip() == "":
        return

    answer = simpledialog.askstring(
        "Add Flashcard",
        "Enter the answer:"
    )

    if answer is None or answer.strip() == "":
        return

    flashcards.append({
        "q": question,
        "a": answer
    })

    messagebox.showinfo(
        "Success",
        "New flashcard added successfully!"
    )

    show_question()


def edit_flashcard():
    """Edit current flashcard."""

    current_question = flashcards[current_index]["q"]
    current_answer = flashcards[current_index]["a"]

    new_question = simpledialog.askstring(
        "Edit Flashcard",
        "Edit question:",
        initialvalue=current_question
    )

    if new_question is None or new_question.strip() == "":
        return

    new_answer = simpledialog.askstring(
        "Edit Flashcard",
        "Edit answer:",
        initialvalue=current_answer
    )

    if new_answer is None or new_answer.strip() == "":
        return

    flashcards[current_index]["q"] = new_question
    flashcards[current_index]["a"] = new_answer

    messagebox.showinfo(
        "Success",
        "Flashcard updated successfully!"
    )

    show_question()


def delete_flashcard():
    """Delete current flashcard."""

    if len(flashcards) == 1:
        messagebox.showwarning(
            "Cannot Delete",
            "At least one flashcard must remain."
        )
        return

    result = messagebox.askyesno(
        "Delete Flashcard",
        "Are you sure you want to delete this flashcard?"
    )

    if result:
        global current_index

        flashcards.pop(current_index)

        if current_index >= len(flashcards):
            current_index = len(flashcards) - 1

        show_question()

        messagebox.showinfo(
            "Deleted",
            "Flashcard deleted successfully!"
        )


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("Flashcard Quiz - CodeAlpha Task 1")

root.geometry("650x500")

root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Flashcard Quiz App",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


# Counter
counter_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold")
)

counter_label.pack(pady=5)


# Question Card
question_frame = tk.Frame(
    root,
    bd=2,
    relief="solid"
)

question_frame.pack(
    padx=30,
    pady=10,
    fill="x"
)

question_label = tk.Label(
    question_frame,
    text="",
    font=("Arial", 16, "bold"),
    wraplength=550,
    justify="center",
    bg="lightyellow"
)

question_label.pack(
    padx=20,
    pady=30
)


# Answer
answer_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    wraplength=550,
    fg="blue"
)

answer_label.pack(pady=10)


# ---------------- NAVIGATION BUTTONS ----------------

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


show_button = tk.Button(
    button_frame,
    text="Show Answer",
    command=show_answer,
    bg="green",
    fg="white",
    width=14
)

show_button.grid(row=0, column=0, padx=5)


previous_button = tk.Button(
    button_frame,
    text="Previous",
    command=previous_card,
    width=12
)

previous_button.grid(row=0, column=1, padx=5)


next_button = tk.Button(
    button_frame,
    text="Next",
    command=next_card,
    width=12
)

next_button.grid(row=0, column=2, padx=5)


# ---------------- MANAGEMENT BUTTONS ----------------

manage_frame = tk.Frame(root)

manage_frame.pack(pady=15)


add_button = tk.Button(
    manage_frame,
    text="Add Flashcard",
    command=add_flashcard,
    width=14
)

add_button.grid(row=0, column=0, padx=5)


edit_button = tk.Button(
    manage_frame,
    text="Edit Flashcard",
    command=edit_flashcard,
    width=14
)

edit_button.grid(row=0, column=1, padx=5)


delete_button = tk.Button(
    manage_frame,
    text="Delete Flashcard",
    command=delete_flashcard,
    width=14
)

delete_button.grid(row=0, column=2, padx=5)


# Display first question
show_question()

# Start application
root.mainloop()