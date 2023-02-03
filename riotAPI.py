import cassiopeia
import customtkinter

class parsing:
    def getChamps(frame, summoner):

        counter = 2
        spellCount = 0

        for participant in summoner.current_match.blue_team.participants:
            frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 20))
            frame.label.grid(row=counter, column=0)

            frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 18))
            frame.label.grid(row=counter+1, column=0)

            spellCount = 0
            for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 15))
                frame.label.grid(row=counter+2+spellCount, column=0)
                spellCount += 1

            counter += 6

        counter = 2
        for participant in summoner.current_match.red_team.participants:
            frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 20))
            frame.label.grid(row=counter, column=3)

            frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 15))
            frame.label.grid(row=counter+1, column=3)

            spellCount = 0
            for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 15))
                frame.label.grid(row=counter+2+spellCount, column=3)
                spellCount += 1

            counter += 6
      


        