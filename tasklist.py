from tkinter import * 
import tkinter.messagebox 
window=Tk()

window.title("Lista de Tarefas")
window.mainloop()

window=Tk()
window.title("Lista de tarefas")

frame_task=Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

entry_button=Button(window, text="Adicionar tarefa", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window, text="Apagar tarefa selecionada", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button= Button(window, text="Marcar como concluida", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
