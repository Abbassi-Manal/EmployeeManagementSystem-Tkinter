import tkinter as tk
from tkinter import ttk , messagebox
from tkinter  import *
from Database import *
from datetime import datetime

class Page2Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.DB = Database(host='localhost',user='root',password='',database='employees_managements_tkinter')
        
        # self.notebook = notebook
        self.title = ttk.Label(self , text="Listes des paiements durant un mois" ,font=12).grid(row=0 , column=0 , pady=10)
        self.annee = ttk.Entry(self)
        self.annee.grid(row=1 , column=0)

        mois_options = ["Janvier","Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre", "Octobre", "Novembre","Décembre"]
        self.mois = tk.StringVar(self)
        self.mois.set(mois_options[0])
        self.mois_dropdown = ttk.OptionMenu(self, self.mois, *mois_options )
        self.mois_dropdown.grid(row = 1 , column =1  ,sticky='ew' )

        self.verifier = ttk.Button(self, text="Verifier" , command=self.search_emp).grid(row=1 , column=2 , padx=10)
        self.enregistrement = ttk.Button(self, text="Enregistrement" , command= self.show_frame1).grid(row=1 , column=3 ,padx=10)

        columns = ["MATRICULE" ,"NOM" , "PRENOM","ANNEE", "MOIS"  , "MONTANT" , "RESTE"]
        self.tree_1 = ttk.Treeview(self , columns = columns , show='headings' )
        # self.add_tree()
        for i , col  in enumerate(columns):
            self.tree_1.column("#" + str(i + 1), anchor=tk.CENTER  ,width=140)
            self.tree_1.heading("#" + str(i + 1), text=col)
        self.tree_1.grid(column=0 , row= 2 , columnspan =6 ,sticky="nsew" ,padx=10, pady=10)
        self.scrollbar_pay = ttk.Scrollbar(self, orient="vertical", command=self.tree_1.yview)
        self.scrollbar_pay.grid(row=2, column=7, sticky="ns")
        self.tree_1.configure(yscrollcommand=self.scrollbar_pay.set)
        #     *********************************Part 2 *****************************************************
        self.title_2 = ttk.Label(self , text=" Historique du paiement d'un employé durant un mois" ,font=12).grid(row=7 , column=0 , pady=10)
        self.annee_2 = ttk.Entry(self )
        self.annee_2.grid(row=8 , column=0)

        mois_options_2 = ["Janvier","Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre", "Octobre", "Novembre","Décembre"]
        self.mois_2 = tk.StringVar(self)
        self.mois_2.set(mois_options_2[0])
        self.mois_dropdown_2 = ttk.OptionMenu(self, self.mois_2, *mois_options_2 )
        self.mois_dropdown_2.grid(row = 8 , column =1  ,sticky='ew' )
        self.emp = ttk.Entry(self )
        self.emp.grid(row=8 , column=2)

        self.verifier_2 = ttk.Button(self, text="Verifier" ,command=self.search_histo).grid(row=8 , column=3 , padx=10)

        columns_2 = ["MATRICULE" ,"NOM" , "PRENOM","ANNEE", "MOIS" ,"JOUR" , "MONTANT" ]
        self.tree_2 = ttk.Treeview(self , columns = columns_2 , show='headings'  )
        
        for i , col  in enumerate(columns_2):
            self.tree_2.column("#" + str(i + 1), anchor=tk.CENTER  ,width=140)
            self.tree_2.heading("#" + str(i + 1), text=col)
        self.tree_2.grid(column=0 , row= 9 , columnspan =6 ,sticky="nsew" ,padx=10, pady=10)
        self.scrollbar_pay = ttk.Scrollbar(self, orient="vertical", command=self.tree_2.yview)
        self.scrollbar_pay.grid(row=9, column=7, sticky="ns")
        self.tree_2.configure(yscrollcommand=self.scrollbar_pay.set)
    
    def add_tree(self):
        data = self.DB.history()
        self.tree_1.delete(*self.tree_1.get_children())
        for result in data :
            calculated_value = result[-1] if result[-1] > 0 else 0
            selected_columns = result[:5] + (result[-2] ,) + (calculated_value,) 
            self.tree_1.insert('', END , values=selected_columns)
            
    def add_tree_2(self):
        data = self.DB.history()
        self.tree_2.delete(*self.tree_2.get_children())
        for result in data :
            self.tree_2.insert('', END , values=result[:7] )

    def show_frame1(self ):
        self.master.select(0) 

    def search_emp(self):
        annee = self.annee.get()
        mois = self.mois.get()
        data = self.DB.search_by_emp('',annee , mois)
        self.tree_1.delete(*self.tree_1.get_children())
        
        if not (annee and mois ):
            messagebox.showerror("Error" , "Veuiller remplire les champs")
        elif not (annee.isdigit() and  int(annee) > 1900 and int(annee) <= datetime.now().year):
                messagebox.showerror( ' Error' , 'Veuillez modifier l\'annee ')
                self.annee.focus_set()
        elif not(data):
            messagebox.showinfo("Info" , "Il y'a pas de resultats liés a ces données")
        else:
            for result in data :
                selected_columns = result[:5] + (result[-2] ,) + (result[-1] if result[-1] > 0 else 0,) 
                self.tree_1.insert('', END , values=selected_columns)

    def search_histo(self):
        annee_2 = self.annee_2.get()
        mois_2 = self.mois_2.get()
        emp = self.emp.get()
        data = self.DB.search_by_emp(emp,annee_2 , mois_2)
        self.tree_2.delete(*self.tree_2.get_children())
        
        if not ( emp ,annee_2 and mois_2 ):
            messagebox.showerror("Error" , "Veuiller remplir les champs")
        elif not (annee_2.isdigit() and  int(annee_2) > 1900 and int(annee_2) <= datetime.now().year):
                messagebox.showerror( ' Error' , 'Veuillez modifier l\'annee ')
                self.annee_2.focus_set()
        elif not(data):
            messagebox.showinfo("Info" , "Il y'a pas de resultats liés a ces données")
        else :
            for result in data :
                self.tree_2.insert('', END , values=result[:7] )

