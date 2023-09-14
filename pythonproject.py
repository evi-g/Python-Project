import math
import numpy as np

print("ASKISI ARXES GLWSSWN KAI METAFRASTWN")

n = input("Give the number of documents (N): ")  # Eisodos arithmou gia to plithos twn eggrafwn

max_k = math.factorial(int(n))/(math.factorial(int(n)-2)*math.factorial(2))  # Megistos arithmos zeugwn

all_d = np.empty((int(n)), type(list))  # arxikopoiisi mitroou pou perilamvanei listes me tis lekseis kathe keimenou


for i in range(0, int(n)):
    d_i = input("Give the " + str(i+1) + " text: ")

    x = d_i.split()    # diaxwrismos twn leksewn. apo ta keimena kratame mono tis lekseis
    all_d[i] = x       # kathe mia grammi tou pinaka all_d periexei lista me tis lekseis


all_words = []          # arxikopoiisi listas all_words. Edw tha mpoun oles oi lekseis olwn twn keimenwn apo mia fora
for i in range (0, int(n)):
    for j in all_d[i]:
        if j not in all_words:
            all_words.append(j)


vectors = np.empty((int(n), len(all_words)), type(int))     # Arxikopoiisi pinaka pou kathe grammi tha periexei
                                                            # ena dianusma opws to perigrafei i ekfwnisi

for i in range(0,  int(n)):
    for j in range(0, len(all_words)):
        temp = all_d[i].count(all_words[j])         # stin metavliti temp kataxwroume enan akeraio 0, 1, 2 ...
                                                    # analoga me to poses fores emfanizetai kathe leksi sto kathe keimeno
        vectors[i][j] = temp


print(" ")

sims = []               # lista pou tha apothikeusoume ta similarities

# Diplo for gia na sugkrinoume ola ta keimena metaksu tous
for i in range(0,  int(n)-1):
    for j in range(i+1,  int(n)):
        a = np.dot(vectors[i], vectors[j])   # prakseis metaksu twn dianusmatwn opws anagrafontai stin ekfwnisi
        b = np.linalg.norm(vectors[i])       # prakseis metaksu twn dianusmatwn opws anagrafontai stin ekfwnisi
        c = np.linalg.norm(vectors[j])       # prakseis metaksu twn dianusmatwn opws anagrafontai stin ekfwnisi

        sim = a/(b*c)           # pososto metaksu trexontwn dianusmatwn < 1
        temp = ("d" + str(i+1) + "," + "d" + str(j+1), sim)  # apothikeusi onomatwn twn dianusmatwn me ta pososta
        sims.append(temp)   # kataxwrisi mesa se lista twn posostwn

sorted = sorted(sims, key=lambda tup: tup[1], reverse =True)        # sortarisma listas me pososta


while True:
    k = input("Give the number of most similar documents you want with K < " + str(max_k) + " or press 0 to exit: ")

    if int(k) == 0:

        print("\n ------------------- BYE! -------------------")

        break
    elif int(k) < int(max_k):
        print(sorted[0:int(k)], "\n")
    else:
        pass