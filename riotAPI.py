import cassiopeia
import customtkinter
import os
from PIL import Image

class parsing:
    def getChamps(frame, summoner):
        counter = 6
        spellCount = 0
        num = 0

        for participant in summoner.current_match.blue_team.participants:

            if (num < 2) :
                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 20))
                frame.label.grid(row=counter, column=0)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 18))
                frame.label.grid(row=counter+1, column=0)

                image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "champion")
                champ_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, participant.champion.key + ".png")), size=(25, 25))
                frame.label = customtkinter.CTkLabel(master=frame, image=champ_image, text=None)
                frame.label.grid(row=counter+2, column=0)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 15))
                    frame.label.grid(row=counter+3+spellCount, column=0)
                    spellCount += 1
            else :
                if (num == 2) : counter = 2

                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 20))
                frame.label.grid(row=counter, column=1)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 18))
                frame.label.grid(row=counter+1, column=1)

                image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "champion")
                champ_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, participant.champion.key + ".png")), size=(25, 25))
                frame.label = customtkinter.CTkLabel(master=frame, image=champ_image, text=None)
                frame.label.grid(row=counter+2, column=1)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 15))
                    frame.label.grid(row=counter+3+spellCount, column=1)
                    spellCount += 1

            counter += 8
            num += 1

        counter = 2
        num = 0
        for participant in summoner.current_match.red_team.participants:
            if (num >= 3) :
                if (num == 3) :
                     counter = 6

                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 20))
                frame.label.grid(row=counter, column=4)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 18))
                frame.label.grid(row=counter+1, column=4)

                image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "champion")
                champ_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, participant.champion.key + ".png")), size=(25, 25))
                frame.label = customtkinter.CTkLabel(master=frame, image=champ_image, text=None)
                frame.label.grid(row=counter+2, column=4)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 15))
                    frame.label.grid(row=counter+3+spellCount, column=4)
                    spellCount += 1
            else :
                frame.label = customtkinter.CTkLabel(master=frame, text=participant.summoner.name, font=("Roboto", 20))
                frame.label.grid(row=counter, column=3)

                frame.label = customtkinter.CTkLabel(master=frame, text=cassiopeia.get_champion(key=participant.champion, region="NA").name, font=("Roboto", 18))
                frame.label.grid(row=counter+1, column=3)

                image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "champion")
                champ_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, participant.champion.key + ".png")), size=(25, 25))
                frame.label = customtkinter.CTkLabel(master=frame, image=champ_image, text=None)
                frame.label.grid(row=counter+2, column=3)

                spellCount = 0
                for spell in cassiopeia.get_champion(key=participant.champion, region="NA").spells :
                    frame.label = customtkinter.CTkLabel(master=frame, text=spell.name, font=("Roboto", 15))
                    frame.label.grid(row=counter+3+spellCount, column=3)
                    spellCount += 1

            counter += 8
            num += 1
      


        