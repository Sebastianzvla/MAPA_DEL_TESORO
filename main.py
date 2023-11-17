line1 = ["⬜","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Esconde tu tesoro!.\n")
print("         [A1, B1, C1]")
print("         [A2, B2, C2]")
print("         [A3, B3, C3]")
position = input("\nDonde quieres esconder el tesoro? ") 

Columa = position[0].lower()
fila = position[1]
x = int(fila)

if Columa == "a":
  map[x-1][0] = "X"
  
elif Columa == "b":
  map[x-1][1] = "X"

elif Columa == "c":
  map[x-1][2] = "X"
  
  #Alternativa
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"

print(" ")
print(f"{line1}\n{line2}\n{line3}")
