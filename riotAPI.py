import cassiopeia
import customtkinter

class parsing:
    def getChamps(frame, summoner):
        counter = 6
        spellCount = 0
        num = 0

        for participant in summoner.current_match.blue_team.participants:

            if (num < 2) :
                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 15))
                frame.label.grid(row=counter, column=0)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 12))
                frame.label.grid(row=counter+1, column=0)

                # image_path = cassiopeia.get_champion(key=participant.champion, region="NA"). loading_image_url
                # frame.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 10))
                    frame.label.grid(row=counter+2+spellCount, column=0)
                    spellCount += 1
            else :
                if (num == 2) : counter = 2

                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 15))
                frame.label.grid(row=counter, column=1)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 12))
                frame.label.grid(row=counter+1, column=1)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 10))
                    frame.label.grid(row=counter+2+spellCount, column=1)
                    spellCount += 1

            counter += 7
            num += 1

        counter = 2
        num = 0
        for participant in summoner.current_match.red_team.participants:
            if (num >= 3) :
                if (num == 3) :
                     counter = 6

                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 15))
                frame.label.grid(row=counter, column=4)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 12))
                frame.label.grid(row=counter+1, column=4)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 10))
                    frame.label.grid(row=counter+2+spellCount, column=4)
                    spellCount += 1
            else :
                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 15))
                frame.label.grid(row=counter, column=3)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 12))
                frame.label.grid(row=counter+1, column=3)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 10))
                    frame.label.grid(row=counter+2+spellCount, column=3)
                    spellCount += 1

            counter += 7
            num += 1
      


        