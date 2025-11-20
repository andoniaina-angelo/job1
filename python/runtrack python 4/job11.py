def time_to_text(minutes):
    if minutes<=59:
        x= 0
    if minutes >=60:
        r=minutes%60 
        x=minutes-r  
    y=minutes-x
    print(f"{x} heures et {y} minutes")
time_to_text(126)