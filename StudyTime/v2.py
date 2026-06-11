import time
import rich as print

current_subject = None
start_time = None
total_time = 0
subject_set = []

def start_session():
    global start_time, current_subject
    if start_time is None:
        if len(subject_set) == 0:
            print("[red]No subjects available![/red] Add one first please. >>> ")
            return
        print("[cyan]Choose a subject: >>> [/cyan]")
        print(subject_set)
        current_subject = input(">>> ")
        if current_subject not in subject_set:
            print("[red]Invalid subject![/red]")
            current_subject = None
            return
        start_time = time.time()
        print(f"Session started for {current_subject}!")
    else:
        print("[green]Session already running![/green]")

def stop_session():
    global start_time, total_time, current_subject
    if start_time is not None:
        duration = time.time() - start_time
        total_time += duration
        start_time = None
        minutes = duration / 60
        print(f"[cyan]Session ended! You studied {current_subject} for {round(minutes, 2)} minutes.[/cyan]")
        print(">>> ")
    else:
        print("[red]No session running![/red]")
    current_subject = None


while True:
    x = input("\nCommand (add/remove/start/stop/list/total/quit) >>> ")
    if x == "add":
        y = input("Type in the name of the subject >>> ") # Make the add command be able to save its own list of subjects
        if y not in subject_set:
            subject_set.append(y)
        else:
            print("Subject already exists!")
        subject_set.append(y)
    elif x == "remove":
        y = input("Type in the name of the subject >>> ")
        if y in subject_set:
            subject_set.remove(y)
        else:
            print("Subject not found >>> ")
    elif x == "start":
        start_session()

    elif x == "stop":
        stop_session()
        
    elif x == "list":
        print(f"Subjects: {subject_set} >>> ")
        
    elif x == "total":
        minutes = total_time / 60
        print(f"Total study time: {round(minutes, 2)} minutes >>> ")
        
    elif x == "quit":
        print("Goodbye!")
        break
    
    else:
        print("Command not found >>> ")


# NOTES
# use rich library to style UI