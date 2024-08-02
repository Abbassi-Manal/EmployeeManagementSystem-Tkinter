# import customtkinter
from tkinter  import *
import tkinter  as tk
from tkinter import ttk , messagebox
from Database import *
from page2 import Page2Frame  
from ttkthemes import ThemedTk
from datetime import datetime

class GUI:
    def __init__(self):    
        self.DB = Database(host='localhost',user='root',password='',database='employees_managements_tkinter')
        # J'ai choisi de modifier le style c'est pour cela j'ai cherché à modifier le theme 
        # et dans ce sens j'utilise ThemedTk au lieu de Tk ;)
        # self.app = Tk() 
        self.app = ThemedTk(theme="arc")
        # self.app.configure(bg ="yellow")
        self.notebook = ttk.Notebook(self.app)
        self.notebook.grid(row=0 , column=0 )

        self.frame = Frame(self.notebook)
        self.frame.grid(row=0 , column=0 , pady= 20)
        # **********************************Frame 1 *********************************************************
        self.DB.employees_table()
        self.DB.paiements_table()
       
        self.app.title("Employee Management system")
        
        
        # *************************************************************************************************************
        # information employee
        self.title_employe = ttk.Label(self.frame,text='Enregistrement des employes' ,font=12  ).grid(row =0, padx=20 , pady=10)

        self.matricule_lbl = ttk.Label(self.frame,text='MATRICULE'  ).grid(row =1, padx=20 , pady=10)
        self.matricule = ttk.Entry(self.frame) 
        self.matricule.grid(row = 1 , column =1)

        
        self.nom_lbl = ttk.Label(self.frame,text='NOM'  ).grid(row =2 , padx=20 , pady=10 )
        self.nom = ttk.Entry(self.frame) 
        self.nom.grid(row = 2 , column =1)

        self.prenom_lbl = ttk.Label(self.frame,text='PRENOM'  ).grid(row =3 , padx=20 , pady=10)
        self.prenom = ttk.Entry(self.frame) 
        self.prenom.grid(row = 3 , column =1)

        self.salaire_lbl = ttk.Label(self.frame,text='SALAIRE'  ).grid(row =4,padx=20 , pady=10)
        self.salaire = ttk.Entry(self.frame  ) 
        self.salaire.grid(row = 4 , column =1)

        # Butthon
        self.ajouter_emp = ttk.Button(self.frame , text="Ajouter" , command=self.insert_emp ).grid(row =5 , column = 0 ,padx=20 , pady=10)
        self.supprimer_emp = ttk.Button(self.frame , text="Supprimer",command=self.delete_emp).grid(row =5 ,column =1 ,padx=20 , pady=10)
        columns = ["MATRICULE" , "NOM" , "PRENOM" , "SALAIRE"]

        # Creation de  Treeview
        self.tree_emp = ttk.Treeview(self.frame, columns=columns, show='headings')

        # Ajout des colonnes
        for i, col in enumerate(columns):
            self.tree_emp.column("#" + str(i + 1), anchor=tk.CENTER ,width=180)
            self.tree_emp.heading("#" + str(i + 1), text=col)

        self.tree_emp.grid(row=1, column=2, rowspan=5, sticky="ns", padx=20)

        # Ajout de scrollbar 
        self.scrollbar_emp = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree_emp.yview)
        self.scrollbar_emp.grid(row=1, column=3, rowspan=5, sticky="ns")
        self.tree_emp.configure(yscrollcommand=self.scrollbar_emp.set)
        self.add_treeview_emp()
        
        # *************************************************************************

        # information paiements
        self.title_paiements = ttk.Label(self.frame,text='Enregistrement de paiements', font=12  ).grid(row =6, padx=20 , pady=10)

        self.matricule_lbl = ttk.Label(self.frame,text='MATRICULE'  ).grid(row =7, padx=20 , pady=10)
        self.matricule_2 = ttk.Entry(self.frame) 
        self.matricule_2.grid(row = 7 , column =1)

        self.annee_lbl = ttk.Label(self.frame,text='ANNEE'  ).grid(row =8 , padx=20 , pady=10)
        self.annee = ttk.Entry(self.frame) 
        self.annee.grid(row = 8 , column =1)

        self.mois_lbl = ttk.Label(self.frame,text='MOIS'  ).grid(row =9 , padx=20 , pady=10 )
        # self.mois = tk.Listbox(self.app) 
        mois_options = ["Janvier","Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre", "Octobre", "Novembre","Décembre"]
        self.mois = tk.StringVar(self.frame )
        self.mois.set(mois_options[0])
        self.mois_dropdown = ttk.OptionMenu(self.frame, self.mois, *mois_options )
        self.mois_dropdown.grid(row = 9 , column =1  ,sticky='ew')


        self.jour_lbl = ttk.Label(self.frame,text='JOUR'  ).grid(row =10, padx=20 , pady=10 )
        jour_options = [i for i in range(1,32)]
        self.jour = tk.StringVar(self.frame)
        self.jour.set(jour_options[0])
        self.jour_dropdown = ttk.OptionMenu(self.frame, self.jour, *jour_options )
        self.jour_dropdown.grid(row = 10 , column =1 ,sticky='ew')

        self.montant_lbl = ttk.Label(self.frame,text='MONTANT'  ).grid(row =11,padx=20 , pady=10)
        self.montant= ttk.Entry(self.frame) 
        self.montant.grid(row = 11 , column =1)

        # Butthon
        self.ajouter_pay = ttk.Button(self.frame , text="Ajouter", command=self.insert_pay  ).grid(row =12 , column = 0 ,padx=20 , pady=10)
        self.supprimer_pay = ttk.Button(self.frame , text="Supprimer" , command=self.delete_pay).grid(row =12 ,column =1 ,padx=20 , pady=10)
        self.requete_pay = ttk.Button(self.frame , text="Requete" , command=self.show_frame2).grid(row =13 ,column =0 , columnspan=2,padx=20 , pady=10 )

        # Create Treeview
        columns2 = ["MATRICULE" ,"ANNEE", "MOIS" , "JOUR" , "MONTANT"]

        self.tree_pay = ttk.Treeview(self.frame, columns=columns2, show='headings' )

        # Add columns
        for i, col in enumerate(columns2):
            self.tree_pay.column("#" + str(i + 1), anchor=tk.CENTER , width=145)
            self.tree_pay.heading("#" + str(i + 1), text=col)

        # Use the grid method instead of pack
        self.tree_pay.grid(row=7, column=2, rowspan=7, sticky="ns", padx=20)

        # Add scrollbar if needed
        self.scrollbar_pay = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree_pay.yview)
        self.scrollbar_pay.grid(row=7, column=3, rowspan=7, sticky="ns")
        self.tree_pay.configure(yscrollcommand=self.scrollbar_pay.set)
        self.add_treeview_pay()
         
        self.notebook.add(self.frame, text="Information des employés" , sticky="nsew")
        self.frame2 = Page2Frame(self.notebook )
        self.notebook.add(self.frame2, text="historique & recherche" , sticky="nsew")

    
    def show_frame2(self):
            self.notebook.select(1)
    
    def add_treeview_emp(self):
        employees = self.DB.fetch_employees()
        self.tree_emp.delete(*self.tree_emp.get_children())
        for employee in employees:
            self.tree_emp.insert('' , END , values=employee)

    def add_treeview_pay(self):
        paiements = self.DB.fetch_paiements()
        self.tree_pay.delete(*self.tree_pay.get_children())
        for paiement in paiements:
            self.tree_pay.insert('' , END , values=paiement[1:])

    def insert_emp(self):
        matricule = self.matricule.get()
        nom = self.nom.get()
        prenom = self.prenom.get()
        salaire = self.salaire.get()
        if not (matricule and nom and prenom and salaire):
            messagebox.showerror( ' Error' , 'Veuiller remplir tous les champs. ')
        elif (self.DB.matricule_exists(matricule)):
                messagebox.showerror( ' Error' , 'Matricule deja existe ')
                self.matricule.focus_set()
        elif not (nom.isalpha()):
                messagebox.showerror( ' Error' , 'Veuillez modifier le nom  ')
                self.nom.focus_set()
        elif not (prenom.isalpha()):
                messagebox.showerror( ' Error' , 'Veuillez modifier le prenom ')
                self.prenom.focus_set()
        elif not (salaire.isdecimal()):
                messagebox.showerror( ' Error' , 'Veuillez modifier salaire   ')
                self.salaire.focus_set()
        
        else :
                self.DB.insert_employee(matricule , nom , prenom , salaire)
                self.add_treeview_emp()
                self.frame2.add_tree()
                self.clear()
                messagebox.showinfo('Success', "Insertion avec succes")

    def insert_pay(self):
        matricule_2 = self.matricule_2.get()
        annee = self.annee.get()
        mois = self.mois.get()
        jour = self.jour.get()
        montant = self.montant.get()
        if not (matricule_2 and annee and mois and jour and montant):
            messagebox.showerror( ' Error' , 'Enter all fields. ')
        elif not ( self.DB.matricule_exists(matricule_2)):
                messagebox.showerror( ' Error' , 'Matricule n\'existe pas ')
                self.matricule_2.focus_set()
        elif not (annee.isdigit() and  int(annee) > 1900 and int(annee) <= datetime.now().year):
                messagebox.showerror( ' Error' , 'Veuillez modifier l\'annee ')
                self.annee.focus_set()
        elif not (montant.isdecimal()):
                messagebox.showerror( ' Error' , 'Veuillez modifier montant  ')
                self.montant.focus_set()
        else :
                self.DB.insert_paiements(matricule_2,  annee , mois , jour, montant)
                self.add_treeview_pay()
                self.clear()
                messagebox.showinfo('Success', "Insertion avec succes")

    def delete_emp(self):
        matricule = self.matricule.get()
        selected_item = self.tree_emp.selection()
        if (matricule):
            self.DB.delete_employee(matricule)
            self.add_treeview_emp()
            self.add_treeview_pay()
            self.frame2.add_tree()
            self.clear()
            messagebox.showinfo("success", "Suppression avec succes ")
        elif (selected_item):
            matricule = self.tree_emp.item(selected_item, 'values')[0]
            self.DB.delete_employee(matricule)
            self.add_treeview_emp()
            self.add_treeview_pay()
            self.frame2.add_tree()
            messagebox.showinfo("success", "Suppression avec succes ")
        else:
            messagebox.showerror("Error", "Veuillez selectionner ou saisir matricule souhaitant supprimée ")
    def delete_pay(self):
        matricule = self.matricule_2.get()
        selected_item = self.tree_pay.selection()
        if (matricule) :
            self.DB.delete_paiements(matricule)
            self.add_treeview_pay()
            self.clear()
            messagebox.showinfo("success", "Suppression avec succes ")
        elif (selected_item):
            matricule = self.tree_pay.item(selected_item, 'values')[0]
            self.DB.delete_paiements(matricule)
            self.add_treeview_pay()
            self.clear()
            messagebox.showinfo("success", "Suppression avec succes ")
        else:
            messagebox.showerror("Error", "Veuillez selectionner ou saisir matricule souhaitant supprimée ")

    def clear(self):
        self.matricule.delete(0,END)
        self.nom.delete(0,END)
        self.prenom.delete(0,END)
        self.salaire.delete(0,END)
        self.matricule_2.delete(0,END)
        self.annee.delete(0,END)
        self.mois.set("Janvier")
        self.jour.set("1")
        self.montant.delete(0,END)

if __name__ == "__main__":
    app = GUI()
    app.frame.mainloop()