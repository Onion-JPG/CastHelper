import customtkinter
import riotAPI
import cassiopeia
import config

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("700x700")
root.title("Cast Helper")

class searchView(customtkinter.CTkFrame):
    def __init__(self, master=None):
        customtkinter.CTkFrame.__init__(self, master, width=600, height=400)
        self.pack(pady=20, padx=60, fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        label = customtkinter.CTkLabel(master=self, text="Summoner Search", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        self.summonerId = customtkinter.CTkEntry(master=self, placeholder_text="Summoner Name")
        self.summonerId.pack(pady=12, padx=10)

        self.searchButton = customtkinter.CTkButton(master=self, text="Search for Game", command=self.search)
        self.searchButton.pack()

        self.console = customtkinter.CTkTextbox(master=self, state="disabled", height=5)
        self.console.pack(pady=12, padx=10)

    def search(self):

        name = self.summonerId.get()
        apiKey = config.apikey

        cassiopeia.set_riot_api_key(apiKey)
        global summoner
        summoner = cassiopeia.get_summoner(name=name, region="NA")

        if (not summoner.exists): 
            self.console.configure(state="normal")
            self.console.delete("0.0", "end")
            self.console.insert("0.0", "User not found")
            self.console.configure(state="disable")
        else :
            self.console.configure(state="normal")
            self.console.delete("0.0", "end")
            self.console.insert("0.0", "User found, but not in a match!")
            self.console.configure(state="disable")

            if (not summoner.current_match.exists):
                self.console.configure(state="normal")
                self.console.delete("0.0", "end")
                self.console.insert("0.0", "user not in a match")
                self.console.configure(state="disable")
            else: 
                self.pack_forget()
                resultView(self.master).pack()

class resultView(customtkinter.CTkFrame):
    def __init__(self, master=None):
        customtkinter.CTkFrame.__init__(self, master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,4), weight=1)

        self.create_widgets()

    def create_widgets(self):
        switch_frame_button = customtkinter.CTkButton(master=self, text="Search for Another", command=self.switch_frame)
        switch_frame_button.grid(row=0, column=2)

        label = customtkinter.CTkLabel(master=self, text="Blue Side", font=("Roboto", 15))
        label.grid(row=1, column=0)

        label = customtkinter.CTkLabel(master=self, text="Red Side", font=("Roboto", 15))
        label.grid(row=1, column=4)

        riotAPI.parsing.getChamps(self, summoner)

    def switch_frame(self):
        self.pack_forget()
        searchView(self.master).pack()

searchView(root).pack()
root.mainloop()