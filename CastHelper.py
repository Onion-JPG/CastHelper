import customtkinter
import cassiopeia
import riotAPI
import config

# The main driver for CastHelper

# Configuring the theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class LeagueSearchFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # master.title("CastHelperV2 - Search")
        
        label = customtkinter.CTkLabel(master=self, text="Summoner Search", font=("Roboto", 24))
        label.grid(row=0, column=0, padx=10, pady=12)
        
        self.summonerId = customtkinter.CTkEntry(self, placeholder_text="Summoner Name")
        self.summonerId.grid(row=1, column=0, padx=10, pady=12)

        searchButton = customtkinter.CTkButton(master=self, text="Search for Game", command=self.search)
        searchButton.grid(row=3, column=0, padx=10, pady=12)

        self.console = customtkinter.CTkTextbox(master=self, state="disabled", height=5)
        self.console.grid(row=4, column=0, padx=10, pady=12)

        returnButton = customtkinter.CTkButton(master=self, text="Return to Game Select", command=self.toGameSelect)
        returnButton.grid(row=5, column=0, padx=10, pady=12)

    def toGameSelect(self):
        self.destroy()
        GameFrame(self.master).grid(row=0, column=0, padx=10, pady=12)
        

    def search(self):
        global summoner

        name = self.summonerId.get()

        apiKey = config.apikey

        cassiopeia.set_riot_api_key(apiKey)
        summoner = cassiopeia.get_summoner(name=name, region="NA")

        if (summoner.exists): 
            # print("exist")
            if (summoner.current_match.exists):  
                # print("exist in game")          
                self.destroy()
                LeagueResultFrame(self.master).pack()
            else:
                # print("exist out of game")
                self.console.configure(state="normal")
                self.console.delete("0.0", "end")
                self.console.insert("0.0", "User found, but not in a match!")
                self.console.configure(state="disable")
        else :
            # print("not found")
            self.console.configure(state="normal")
            self.console.delete("0.0", "end")
            self.console.insert("0.0", "User not found")
            self.console.configure(state="disable")
            
#################################################################################################################################            

class LeagueResultFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # master.title("CastHelperV2 - Results")

        # making a new search button and placing it in the top middle
        switch_frame_button = customtkinter.CTkButton(master=self, text="Search for Another", command=self.toSearchFrame)
        switch_frame_button.grid(row=0, column=2)

        # creating a blue and red side label
        label = customtkinter.CTkLabel(master=self, text="Blue Side", font=("Roboto", 15))
        label.grid(row=0, column=0)
        label = customtkinter.CTkLabel(master=self, text="Red Side", font=("Roboto", 15))
        label.grid(row=0, column=4)

        # calling getChamps from our riotAPI file
        riotAPI.LeagueParsing.display(self, summoner)

    def toSearchFrame(self):
        self.destroy()
        LeagueSearchFrame(self.master).grid(row=0, column=0, padx=10, pady=12)

#################################################################################################################################            

class GameFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label = customtkinter.CTkLabel(master=self, text="Select Game", font=("Roboto", 24))
        label.grid(row=0, column=1, padx=10, pady=12)

        leagueButton = customtkinter.CTkButton(master=self, text="League of Legends", command=self.toLeagueOfLegends)
        leagueButton.grid(row=3, column=0, padx=10, pady=12)

        valButton = customtkinter.CTkButton(master=self, text="VALORANT", command=self.toValorant)
        valButton.grid(row=3, column=2, padx=10, pady=12)

    def toLeagueOfLegends(self):
        self.destroy()
        LeagueSearchFrame(self.master).grid(row=0, column=0, padx=10, pady=12)

    def toValorant(self):
        self.destroy()
        LeagueSearchFrame(self.master).grid(row=0, column=0, padx=10, pady=12)
        
#################################################################################################################################

class CastHelper(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CastHelperV2")
        self.geometry("1400x800")
        # self.after(0, lambda:root.state('zoomed'))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        GameFrame(self).grid(row=0, column=0, padx=10, pady=12)
    
root = CastHelper()
root.mainloop()