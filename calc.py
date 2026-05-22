val = ""

while val != "stop":
    val = input("skriv matte problem -> ")

    def dela_uttryck(val):
        resultat = []
        tal = ""
        operatorer = "()+-*/"
        for tecken in val:
            if tecken in operatorer:
                #print(tal)
                #print("ba",tecken)
                if tal != "":
                    resultat.append(float(tal))
                resultat.append(tecken)
                tal = ""
            else:
                tal += tecken
                
        if tal != "":
            resultat.append(float(tal))
        return resultat
     
    inputs = dela_uttryck(val)    

    def hitta_index(lista, värde):
        return [i for i, element in enumerate(lista) if element == värde]
              
    def calc(inputs):
        Vparanteser=hitta_index(inputs,"(")
        Hparanteser=hitta_index(inputs,")")
        if len(Vparanteser) > 0:
            for i in range(len(Vparanteser)):
                #print(inputs)
                delproblem = []
                delproblem = inputs[Vparanteser[0]+1:Hparanteser[0]]
                print(delproblem,type(inputs[Vparanteser[0]-1]),inputs)
                if type(inputs[Vparanteser[0]-1]) == float:
                    try:
                        if type(inputs[Hparanteser[0]+1]) == float:
                            inputs[Vparanteser[0]:Hparanteser[0]+1]= ["*",calc(delproblem),"*"]
                            #print(inputs)
                        else:
                            inputs[Vparanteser[0]:Hparanteser[0]+1]= ["*",calc(delproblem)]
                            #print(inputs)
                    except IndexError:
                        inputs[Vparanteser[0]:Hparanteser[0]+1]= ["*",calc(delproblem)]
                        #print(inputs)
                        
                elif type(inputs[Vparanteser[0]-1]) != float:
                    try:
                        if type(inputs[Hparanteser[0]+1]) == float:   
                            inputs[Vparanteser[0]:Hparanteser[0]+1]= [calc(delproblem),"*"]
                            #print(inputs)
                    except IndexError:
                        pass
                else:
                    inputs[Vparanteser[0]:Hparanteser[0]+1]= [calc(delproblem)]
                    #print(inputs)
                #del inputs[Vparanteser[0]+1:Hparanteser[0]]
                list.clear(Vparanteser)
                list.clear(Hparanteser)
                delproblem = ""
                Vparanteser=hitta_index(inputs,"(")
                Hparanteser=hitta_index(inputs,")")
            multiplikation=hitta_index(inputs,"*")
        else:
            multiplikation=hitta_index(inputs,"*")
            
        if len(multiplikation) > 0:
            for i in range(len(multiplikation)):
                #print(inputs,multiplikation[0],multiplikation[0]-1, multiplikation[0]+1)
                inputs[multiplikation[0]] = float(inputs[multiplikation[0]-1]) * float(inputs[multiplikation[0]+1])
                del inputs[multiplikation[0]-1]
                del inputs[multiplikation[0]]
                list.clear(multiplikation)
                multiplikation=hitta_index(inputs,"*")
                #print(inputs)
            division=hitta_index(inputs,"/")
        else:
            division=hitta_index(inputs,"/")
            
        if len(division) > 0:
            for i in range(len(division)):
                #print(inputs,division[0],division[0]-1, division[0]+1)
                inputs[division[0]] = float(inputs[division[0]-1]) / float(inputs[division[0]+1])
                del inputs[division[0]-1]
                del inputs[division[0]]
                list.clear(division)
                division=hitta_index(inputs,"/")
            subtraktion=hitta_index(inputs,"-")
        else:
            subtraktion=hitta_index(inputs,"-")
            
        if len(subtraktion) > 0:
            for i in range(len(subtraktion)):
                #print(inputs,subtraktion[0],subtraktion[0]-1, subtraktion[0]+1)
                if subtraktion[0]-1 < 0:
                    inputs[subtraktion[0]] = float(inputs[subtraktion[0]+1]) * -1
                    del inputs[subtraktion[0]+1]
                    list.clear(subtraktion)
                    subtraktion=hitta_index(inputs,"-")
                    continue
                else:
                    inputs[subtraktion[0]] = float(inputs[subtraktion[0]-1]) - float(inputs[subtraktion[0]+1])
                del inputs[subtraktion[0]-1]
                del inputs[subtraktion[0]]
                list.clear(subtraktion)
                subtraktion=hitta_index(inputs,"-")
            addition=hitta_index(inputs,"+")
        else:
            addition=hitta_index(inputs,"+")
            
        if len(addition) > 0:
            for i in range(len(addition)):
                #print(addition[0],addition[0]-1, addition[0]+1)
                inputs[addition[0]] = float(inputs[addition[0]-1]) + float(inputs[addition[0]+1])
                del inputs[addition[0]-1]
                del inputs[addition[0]]
                list.clear(addition)
                addition=hitta_index(inputs,"+")
        
        return(inputs[0])
    calc(inputs)
    print(f"Svar: {inputs} ")
    list.clear(inputs)
                