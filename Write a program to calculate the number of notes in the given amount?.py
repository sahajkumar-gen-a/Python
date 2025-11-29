#Write a program to calculate the number of notes in the given amount?
ammount=int(input("enter your ammount="))
notes_of_2000=ammount//2000
notes_of_500=(ammount%2000)//500
notes_of_100=((ammount%2000)%500)//100
print("notes of 2000=",notes_of_2000)
print("notes of 500=",notes_of_500)
print("notes of 100=",notes_of_100)