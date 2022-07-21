from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title("Country Flags")
root.geometry("600x400")
root.configure(background="snow")

get_input = Entry(root)
show_label = Label(root)

afghanistan_map = ImageTk.PhotoImage(Image.open ("Afghanistan.png"))
argentina_map = ImageTk.PhotoImage(Image.open ("Argentina.png"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
austria_map = ImageTk.PhotoImage(Image.open ("Austria.png"))
bahrain_map = ImageTk.PhotoImage(Image.open ("Bahrain.png"))
bangladesh_map = ImageTk.PhotoImage(Image.open ("Bangladesh.png"))
belgium_map = ImageTk.PhotoImage(Image.open ("Belgium.png"))
bhutan_map = ImageTk.PhotoImage(Image.open ("Bhutan.png"))
botswana_map = ImageTk.PhotoImage(Image.open ("Botswana.png"))
bulgaria_map = ImageTk.PhotoImage(Image.open ("Bulgaria.png"))
canada_map = ImageTk.PhotoImage(Image.open ("Canada.png"))
cambodia_map = ImageTk.PhotoImage(Image.open ("Cambodia.png"))
chile_map = ImageTk.PhotoImage(Image.open ("Chile.png"))
china_map = ImageTk.PhotoImage(Image.open ("China.png"))
cuba_map = ImageTk.PhotoImage(Image.open ("Cuba.png"))
czech_republic_map = ImageTk.PhotoImage(Image.open ("Czech Republic.png"))
denmark_map = ImageTk.PhotoImage(Image.open ("Denmark.png"))
egypt_map = ImageTk.PhotoImage(Image.open ("Egypt.png"))
estonia_map = ImageTk.PhotoImage(Image.open ("Estonia.png"))
ethiopia_map = ImageTk.PhotoImage(Image.open ("Ethiopia.png"))
fiji_map = ImageTk.PhotoImage(Image.open ("Fiji.png"))
finland_map = ImageTk.PhotoImage(Image.open ("Finland.png"))
france_map = ImageTk.PhotoImage(Image.open ("France.png"))
germany_map = ImageTk.PhotoImage(Image.open ("Germany.png"))
ghana_map = ImageTk.PhotoImage(Image.open ("Ghana.png"))
greece_map = ImageTk.PhotoImage(Image.open ("Greece.png"))
greenland_map = ImageTk.PhotoImage(Image.open ("Greenland.png"))
haiti_map = ImageTk.PhotoImage(Image.open ("Haiti.png"))
hungary_map = ImageTk.PhotoImage(Image.open ("Hungary.png"))
iceland_map = ImageTk.PhotoImage(Image.open ("Iceland.png"))
india_map = ImageTk.PhotoImage(Image.open ("India.png"))
indonesia_map = ImageTk.PhotoImage(Image.open ("Indonesia.png"))
iran_map = ImageTk.PhotoImage(Image.open ("Iran.png"))
iraq_map = ImageTk.PhotoImage(Image.open ("Iraq.png"))
ireland_map = ImageTk.PhotoImage(Image.open ("Ireland.png"))
italy_map = ImageTk.PhotoImage(Image.open ("Italy.png"))
japan_map = ImageTk.PhotoImage(Image.open ("Japan.png"))
jordan_map = ImageTk.PhotoImage(Image.open ("Jordan.png"))
kenya_map = ImageTk.PhotoImage(Image.open ("Kenya.png"))
kuwait_map = ImageTk.PhotoImage(Image.open ("Kuwait.png"))
libya_map = ImageTk.PhotoImage(Image.open ("Libya.png"))
luxembourg_map = ImageTk.PhotoImage(Image.open ("Luxembourg.png"))
madagascar_map = ImageTk.PhotoImage(Image.open ("Madagascar.png"))
malaysia_map = ImageTk.PhotoImage(Image.open ("Malaysia.png"))
maldives_map = ImageTk.PhotoImage(Image.open ("Maldives.png"))
maurities_map = ImageTk.PhotoImage(Image.open ("Mauritius.png"))
mexico_map = ImageTk.PhotoImage(Image.open ("Mexico.png"))
monaco_map = ImageTk.PhotoImage(Image.open ("Monaco.png"))
morocco_map = ImageTk.PhotoImage(Image.open ("Morocco.png"))
mozambique_map = ImageTk.PhotoImage(Image.open ("Mozambique.png"))
myanmar_map = ImageTk.PhotoImage(Image.open ("Myanmar.png"))
namibia_map = ImageTk.PhotoImage(Image.open ("Namibia.png"))
nepal_map = ImageTk.PhotoImage(Image.open ("Nepal.png"))
netherlands_map = ImageTk.PhotoImage(Image.open ("Netherlands.png"))
new_zealand_map = ImageTk.PhotoImage(Image.open ("New Zealand.png"))
nigeria_map = ImageTk.PhotoImage(Image.open ("Nigeria.png"))
north_korea_map = ImageTk.PhotoImage(Image.open ("North Korea.png"))
norway_map = ImageTk.PhotoImage(Image.open ("Norway.png"))
pakistan_map = ImageTk.PhotoImage(Image.open ("Pakistan.png"))
philipines_map = ImageTk.PhotoImage(Image.open ("Philippines.png"))
poland_map = ImageTk.PhotoImage(Image.open ("Poland.png"))
portugal_map = ImageTk.PhotoImage(Image.open ("Portugal.png"))
romania_map = ImageTk.PhotoImage(Image.open ("Romania.png"))
russia_map = ImageTk.PhotoImage(Image.open ("Russia.png"))
rwanda_map = ImageTk.PhotoImage(Image.open ("Rwanda.png"))
saudi_arabia_map = ImageTk.PhotoImage(Image.open ("Saudi Arabia.png"))
seychelles_map = ImageTk.PhotoImage(Image.open ("Seychelles.png"))
singapore_map = ImageTk.PhotoImage(Image.open ("Singapore.png"))
south_africa_map = ImageTk.PhotoImage(Image.open ("South Africa.png"))
south_korea_map = ImageTk.PhotoImage(Image.open ("South Korea.png"))
spain_map = ImageTk.PhotoImage(Image.open ("Spain.png"))
sri_lanka_map = ImageTk.PhotoImage(Image.open ("Sri Lanka.png"))
sudan_map = ImageTk.PhotoImage(Image.open ("Sudan.png"))
sweden_map = ImageTk.PhotoImage(Image.open ("Sweden.png"))
switzerland_map = ImageTk.PhotoImage(Image.open ("Switzerland.png"))
taiwan_map = ImageTk.PhotoImage(Image.open ("Taiwan.png"))
tanzania_map = ImageTk.PhotoImage(Image.open ("Tanzania.png"))
thailand_map = ImageTk.PhotoImage(Image.open ("Thailand.png"))
trinidad_tobago_map = ImageTk.PhotoImage(Image.open ("Trinidad and Tobago.png"))
turkey_map = ImageTk.PhotoImage(Image.open ("Turkey.png"))
uganda_map = ImageTk.PhotoImage(Image.open ("Uganda.png"))
united_arab_emirates_map = ImageTk.PhotoImage(Image.open ("United Arab Emirates.png"))
united_kingdom_map = ImageTk.PhotoImage(Image.open ("United Kingdom.png"))
united_states_of_america_map = ImageTk.PhotoImage(Image.open ("United States of America.png"))
venezuela_map = ImageTk.PhotoImage(Image.open ("Venezuela.png"))
vietnam_map = ImageTk.PhotoImage(Image.open ("Vietnam.png"))
yugoslavia_map = ImageTk.PhotoImage(Image.open ("Yugoslavia.png"))
zaire_map = ImageTk.PhotoImage(Image.open ("Zaire.png"))
zambia_map = ImageTk.PhotoImage(Image.open ("Zambia.png"))
zimbabwe_map = ImageTk.PhotoImage(Image.open ("Zimbabwe.png"))

maps_dictionary = { "Afghanistan" : afghanistan_map , 
                    "Argentina" : argentina_map ,
                    "Australia" : australia_map ,
                    "Austria" : austria_map,
                    "Bahrain" : bahrain_map,
                    "Bangladesh" : bangladesh_map ,
                    "Belgium" : belgium_map ,
                    "Bhutan" : bhutan_map ,
                    "Botswana" : botswana_map,
                    "Bulgaria" : bulgaria_map,
                    "Canada" : canada_map ,
                    "Cambodia" : cambodia_map,
                    "Chile" : chile_map ,
                    "China" : china_map,
                    "Cuba" : cuba_map,
                    "Czech Republic" : czech_republic_map,
                    "Denmark" : denmark_map,
                    "Egypt" : egypt_map,
                    "Estonia" : estonia_map,
                    "Ethiopia" : ethiopia_map,
                    "Fiji" : fiji_map,
                    "Finland" : finland_map,
                    "France" : france_map,
                    "Germany" : germany_map,
                    "Ghana" : ghana_map,
                    "Greece" : greece_map,
                    "Greenland" : greenland_map,
                    "Haiti" : haiti_map,
                    "Hungary" : hungary_map,
                    "Iceland" : iceland_map,
                    "India" : india_map,
                    "Indonesia" : indonesia_map,
                    "Iran" : iran_map,
                    "Iraq" : iraq_map,
                    "Ireland" : ireland_map,
                    "Italy" : italy_map,
                    "Japan" : japan_map,
                    "Jordan" : jordan_map,
                    "Kenya" : kenya_map,
                    "Kuwait" : kuwait_map,
                    "Libya" : libya_map,
                    "Luxembourg" : luxembourg_map,
                    "Madagascar" : madagascar_map,
                    "Malaysia" : malaysia_map,
                    "Maldives" : maldives_map,
                    "Mauritius" : maurities_map,
                    "Mexico" : mexico_map,
                    "Monaco" : monaco_map,
                    "Morocco" : morocco_map,
                    "Mozambique" : mozambique_map,
                    "Myanmar" : myanmar_map,
                    "Burma" : myanmar_map,
                    "Namibia" : namibia_map,
                    "Nepal" : nepal_map,
                    "Netherlands" : netherlands_map,
                    "New Zealand" : new_zealand_map,
                    "Nigeria" : nigeria_map,
                    "North Korea" : north_korea_map,
                    "Norway" : norway_map,
                    "Pakistan" : pakistan_map,
                    "Philipines" : philipines_map,
                    "Poland" : poland_map,
                    "Portugal" : portugal_map,
                    "Romania" : romania_map,
                    "Russia" : russia_map,
                    "Rwanda" : rwanda_map,
                    "Saudi Arabia" : saudi_arabia_map,
                    "Seychelles" : seychelles_map,
                    "Singapore" : singapore_map,
                    "South Africa" : south_africa_map,
                    "South Korea" : south_korea_map,
                    "Spain" : spain_map,
                    "Sri Lanka" : sri_lanka_map,
                    "Sudan" : sudan_map,
                    "Sweden" : sweden_map,
                    "Switzerland" : switzerland_map,
                    "Taiwan" : taiwan_map,
                    "Tanzania" : tanzania_map,
                    "Thailand" : thailand_map,
                    "Trinidad" : trinidad_tobago_map,
                    "Tobago" : trinidad_tobago_map,
                    "Turkey" : turkey_map,
                    "Uganda" : uganda_map,
                    "United Arab Emirates" : united_arab_emirates_map,
                    "United Kingdom" : united_kingdom_map,
                    "United States of America" : united_states_of_america_map,
                    "Venezuela" : venezuela_map,
                    "Vietnam" : vietnam_map,
                    "Yugoslavia" : yugoslavia_map,
                    "Zaire" : zaire_map,
                    "Zambia" : zambia_map,
                    "Zimbabwe" : zimbabwe_map,}

def showMaps():
    map_name = get_input.get()
    try:
        print(map_name)
        show_label['image'] = maps_dictionary[map_name]
    except(KeyError):
        messagebox.showinfo("Error", "Sorry, this flag is not available")

btn = Button(root , text="Show Map", bg="thistle", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()