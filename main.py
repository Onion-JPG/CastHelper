# import libraries, customtkinter for formating, cassiopeia for API connection
import customtkinter
import cassiopeia

# our files, riotAPI is how we get the info from the game, config contains JUST
# an api key for the riot games API
import riotAPI
import config

# main driver for CastHelper, we use customtkinter for ease of use and default
# formating that looks good. I don't super understand how it works but it does!

# setting default appearance and color theme to the system default
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# making a CTk object, setting it's defualt size to be 800 x 800 and 
# setting its application name to Cast Helper
root = customtkinter.CTk()
root.geometry("800x800")
root.title("Cast Helper")

# search view class, where the search is made
class searchView(customtkinter.CTkFrame):
    # the init method
    def __init__(self, master=None):
        customtkinter.CTkFrame.__init__(self, master, width=600, height=400)
        self.pack(pady=20, padx=60, fill="both", expand=True)
        self.create_widgets()

    # the create widgets method, we define the default screen here
    def create_widgets(self):
        # label for search
        label = customtkinter.CTkLabel(master=self, text="Summoner Search", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        # text box to input the summoner name into
        self.summonerId = customtkinter.CTkEntry(master=self, placeholder_text="Summoner Name")
        self.summonerId.pack(pady=12, padx=10)

        # search button that searches
        self.searchButton = customtkinter.CTkButton(master=self, text="Search for Game", command=self.search)
        self.searchButton.pack()

        # "console" text box to show result if the search doesnt work
        self.console = customtkinter.CTkTextbox(master=self, state="disabled", height=5)
        self.console.pack(pady=12, padx=10)

    # the search method, we search for a summoner here
    def search(self):
        # initializing variables
        global summoner
        name = self.summonerId.get()

        # config.apikey is a file that contains JUST the apikey, not included
        # in the git for security reasons. 
        apiKey = config.apikey

        # setting key and getting summoner through api
        cassiopeia.set_riot_api_key(apiKey)
        summoner = cassiopeia.get_summoner(name=name, region="NA")

        # if the summoner does not exist, ie. typo in name
        if (not summoner.exists): 
            self.console.configure(state="normal")
            self.console.delete("0.0", "end")
            self.console.insert("0.0", "User not found")
            self.console.configure(state="disable")
        else :
            # summoner was found but they arent in a game
            if (not summoner.current_match.exists):            
                self.console.configure(state="normal")
                self.console.delete("0.0", "end")
                self.console.insert("0.0", "User found, but not in a match!")
                self.console.configure(state="disable")
            # user found and in a game, we search the summoner now
            else: 
                self.pack_forget()
                resultView(self.master).pack()

# result view class, where the results are shown
class resultView(customtkinter.CTkFrame):
    # init method for result view
    def __init__(self, master=None):
        customtkinter.CTkFrame.__init__(self, master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,4), weight=1)
        self.create_widgets()

    # create widgets method for result view
    def create_widgets(self):
        # making a new search button and placing it in the top middle
        switch_frame_button = customtkinter.CTkButton(master=self, text="Search for Another", command=self.switch_frame)
        switch_frame_button.grid(row=1, column=2)

        # creating a blue and red side label
        label = customtkinter.CTkLabel(master=self, text="Blue Side", font=("Roboto", 15))
        label.grid(row=1, column=0)
        label = customtkinter.CTkLabel(master=self, text="Red Side", font=("Roboto", 15))
        label.grid(row=1, column=4)

        # calling getChamps from our riotAPI file
        riotAPI.parsing.getChamps(self, summoner)

    # switch frame method forgets / deletes the info on this screen and changes over to the search view
    def switch_frame(self):
        self.pack_forget()
        searchView(self.master).pack()

searchView(root).pack()
root.mainloop()