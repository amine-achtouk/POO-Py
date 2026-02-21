import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

from Personne import Person
from Formateur import Formateur
from Stagaire import Stagaire

FILE_NAME = "data_ofppt.json"



def save_to_json(data_dict):
    """Saves a single entry dictionary into the JSON file."""
    data_list = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                data_list = json.load(f)
            except json.JSONDecodeError:
                data_list = []

    data_list.append(data_dict)
    with open(FILE_NAME, "w") as f:
        json.dump(data_list, f, indent=4)

def load_initial_data():
    """Loads existing JSON data into the Treeview on startup."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                data_list = json.load(f)
                for item in data_list:
                    if item['type'] == "Formateur":
                        row = (item['cin'], item['nom'], item['age'], "Formateur", 
                               item['contrat'], f"{item['salaire']} DH", f"{item['heures']} h")
                    else:
                        row = (item['cin'], item['nom'], item['age'], "Stagiaire", 
                               item['filiere'], "---", f"Moy:{item['moyenne']}")
                    tv.insert('', 'end', values=row)

                if data_list:
                    Person.nb = data_list[-1]['cin']
                    cin_val.config(text=str(Person.nb + 1))
            except:
                pass



def modifVisib():
    if v.get() == 1: 
        contratText.config(state='normal'); salaireText.config(state='normal'); heuresText.config(state='normal')
        filiereText.config(state='disabled'); note1Text.config(state='disabled'); note2Text.config(state='disabled')
    else: # Stagiaire
        contratText.config(state='disabled'); salaireText.config(state='disabled'); heuresText.config(state='disabled')
        filiereText.config(state='normal'); note1Text.config(state='normal'); note2Text.config(state='normal')

def add():
    try:
        nom = nomText.get()
        age = ageText.get()
        if not nom or not age:
            messagebox.showwarning("Erreur", "Nom et Age sont obligatoires")
            return

        if v.get() == 1:
            obj = Formateur(nom, age, contratText.get(), salaireText.get(), heuresText.get())
            row = (obj.getCIN, obj.getNom, obj.getAge, "Formateur", 
                   obj.gettype_contrat, f"{obj.getsalaire} DH", f"{obj.getnbr_heures} h")
            json_entry = {
                "cin": obj.getCIN, "nom": obj.getNom, "age": obj.getAge, "type": "Formateur",
                "contrat": obj.gettype_contrat, "salaire": obj.getsalaire, "heures": obj.getnbr_heures
            }
        else:
            obj = Stagaire(nom, age, filiereText.get(), note1Text.get(), note2Text.get())
            row = (obj.getCIN, obj.getNom, obj.getAge, "Stagiaire", 
                   obj.getfeliere, "---", f"Moy:{obj.getmoyenne}")
            json_entry = {
                "cin": obj.getCIN, "nom": obj.getNom, "age": obj.getAge, "type": "Stagiaire",
                "filiere": obj.getfeliere, "moyenne": obj.getmoyenne
            }

        
        tv.insert('', 'end', values=row)
        save_to_json(json_entry)
        cin_val.config(text=str(Person.nb + 1))
        clear_fields()
        messagebox.showinfo("Succès", "Ajouté et sauvegardé dans JSON")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def clear_fields():
    for entry in [nomText, ageText, contratText, salaireText, heuresText, filiereText, note1Text, note2Text]:
        entry.delete(0, 'end')



root = tk.Tk()
root.geometry('1100x650')
root.title('OFPPT Manager Pro')


tk.Label(root, text='CIN:', font=('Arial', 10, 'bold')).place(x=20, y=20)
cin_val = tk.Label(root, text='1', fg="blue", font=('Arial', 10, 'bold'))
cin_val.place(x=100, y=20)

tk.Label(root, text='Nom:').place(x=20, y=50); nomText = tk.Entry(root); nomText.place(x=100, y=50)
tk.Label(root, text='Age:').place(x=20, y=80); ageText = tk.Entry(root); ageText.place(x=100, y=80)

v = tk.IntVar(value=1)
tk.Label(root, text='Type:').place(x=20, y=110)
tk.Radiobutton(root, text='Formateur', variable=v, value=1, command=modifVisib).place(x=100, y=110)
tk.Radiobutton(root, text='Stagiaire', variable=v, value=2, command=modifVisib).place(x=200, y=110)

tk.Label(root, text='Contrat:').place(x=20, y=140); contratText = tk.Entry(root); contratText.place(x=100, y=140)
tk.Label(root, text='Salaire:').place(x=20, y=170); salaireText = tk.Entry(root); salaireText.place(x=100, y=170)
tk.Label(root, text='Heures:').place(x=20, y=200); heuresText = tk.Entry(root); heuresText.place(x=100, y=200)

tk.Label(root, text='Filière:').place(x=350, y=140); filiereText = tk.Entry(root, state='disabled'); filiereText.place(x=430, y=140)
tk.Label(root, text='Note 1:').place(x=350, y=170); note1Text = tk.Entry(root, state='disabled', width=10); note1Text.place(x=430, y=170)
tk.Label(root, text='Note 2:').place(x=520, y=170); note2Text = tk.Entry(root, state='disabled', width=10); note2Text.place(x=580, y=170)

tk.Button(root, text='AJOUTER', command=add, bg="#28a745", fg="white", width=15).place(x=100, y=250)
tk.Button(root, text='VIDER', command=clear_fields, bg="#ffc107", width=15).place(x=250, y=250)

cols = ('cin', 'nom', 'age', 'type', 'd1', 'd2', 'd3')
tv = ttk.Treeview(root, columns=cols, show='headings', height=12)
headings = ['CIN', 'Nom', 'Age', 'Type', 'Détail 1', 'Détail 2', 'Détail 3']
for i, col in enumerate(cols):
    tv.heading(col, text=headings[i])
    tv.column(col, width=140, anchor="center")
tv.place(x=20, y=320, width=1050)


load_initial_data()
root.mainloop()