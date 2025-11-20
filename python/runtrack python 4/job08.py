def jardin(type:str , saison:str):
    if type=="fruits" and saison=="hiver":
        print("orange ,mandarine et kiwi")
    elif type=="fruits" and saison=="eté":
        print("poire , fraise et cassis ")
    elif type=="légume" and saison=="hiver":
        print("carotte,topinambour,endive")
    elif type == "légume" and saison=="été":
        print("artichaut,aubergine,navet")
jardin("fruits","hiver")