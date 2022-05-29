###################Projeto###################
## Autores: Luara Teodoro Lima ; Paloma Ketnyn Machado ; Uriel Gonçalves Paiva da conceição
## Turma: FEAU-5UNA
## Matriculas: 02011062 ; 02010030 ; 02010287
## versão: 2.5v
#############################################
g=1;t=0

while t<1:
    y=0;v=0;h=0;i=0;z=1;d=0;j=0;j2=0
    listtemp=[] #lista temporaria
    LG1T=[];LG2T=[]  #dados dos arquivos puros
    LG1TT=[];LG2TT=[] # 1 linha de dados do arquivo por elemento
    LG1TTU=[];LG2TTU=[] # lista por dado unitario
    LG110=[];LG210=[] # lista com a cada 3 unidades serem 1 elemento
    LG19=[];LG29=[] # lista com a cada 3 elementos serem 1 elemento
    LG1TTUF=[];LG2TTUF=[] # lista por dado unitario Final
    LG110F=[];LG210F=[] # lista com a cada 10 unidades serem 1 elemento Final
    LG121=[]; LG221=[]# lista com a cada 21 elementos serem 1 elemento
    R=[];E=[]; D=[]
    #####################NOME DOS ArQUIVOS#######################################
    print("Digite o nome + extensão do arquivo: \n Exemplo:gene.txt \n")
    a1= str(input("Digite o nome do primeiro arquivo: "))
    a2= str(input("Digite o nome do segundo arquivo: "))
    ###########leitura e manipulação do primeiro arquivo##############
    arq=open(a1,"r")
    arq.readline() #pula a primeira linha
    l=0;k=0;p=0;kk=0
    for linha in arq:
        c=linha[:-1].split('\n')
        print("Carregando...")       ####passa todos os dados para 1 lista
        LG1T.append(c)
    arq.close()
    while l < len(LG1T):
        LG1TT.append(LG1T[l][0])  ##configura a lista para ficar 1 linha do arquivo por elemento
        l=l+1
    while k < len(LG1TT):
        m=0
        while m < len(LG1TT[k]):
            LG1TTU.append(LG1TT[k][m]) ##configura a lista para cada elemento ser uma letra
            m=m+1
        k=k+1
    o=len(LG1TTU)
    while len(LG1TTU) % 3 !=0:
        LG1TTU.append("N/D")
    while p < len(LG1TTU):
        listtemp=[]
        listtemp.append(LG1TTU[p]+LG1TTU[p+1]+LG1TTU[p+2])               
        LG110.append(listtemp[0])   ##configura para cada 3 letras serem 1 elemento da lista
        p=p+3
    q=len(LG121)
    #################################################
    #while kk < len(LG110)-7:
    #    listtemp=[]
    #    listtemp.append(LG110[kk]+LG110[kk+1]+LG110[kk+2]+LG110[kk+3]+LG110[kk+4]+LG110[kk+5]+LG110[kk+6])               
    #    LG121.append(listtemp[0])   ##configura para cada 7 elementos serem 1 elemento da lista
    #    kk=kk+7
    #kk1=len(LG121)
    ######################################################################################################
    while kk < len(LG1TTU)-21:
        listtemp=[]
        listtemp.append(LG1TTU[kk]+LG1TTU[kk+1]+LG1TTU[kk+2]+LG1TTU[kk+3]+LG1TTU[kk+4]+LG1TTU[kk+5]+LG1TTU[kk+6]+LG1TTU[kk+7]+LG1TTU[kk+8]+LG1TTU[kk+9]
                        +LG1TTU[kk+10]+LG1TTU[kk+11]+LG1TTU[kk+12]+LG1TTU[kk+13]+LG1TTU[kk+14]+LG1TTU[kk+15]+LG1TTU[kk+16]+LG1TTU[kk+17]+LG1TTU[kk+18]
                        +LG1TTU[kk+19]+LG1TTU[kk+20]
                        )               
        LG121.append(listtemp[0])   ##configura para cada 21 letras serem 1 elemento da lista
        kk=kk+1
    c1=len(LG110)
    #######leitura e manipulação do segundo arquivo##############
    arq=open(a2,"r")
    arq.readline() #pula a primeira linha
    l=0;k=0;p=0;kk=0
    for linha in arq:
        c=linha[:-1].split('\n')
        print("Carregando...")       ####passa todos os dados para 1 lista
        LG2T.append(c)
    arq.close()
    while l < len(LG2T):
        LG2TT.append(LG2T[l][0])  ##configura a lista para ficar 1 linha do arquivo por elemento
        l=l+1
    while k < len(LG2TT):
        m=0
        while m < len(LG2TT[k]):
            LG2TTU.append(LG2TT[k][m]) ##configura a lista para cada elemento ser uma letra
            m=m+1
        k=k+1
    o2=len(LG2TTU)
    while len(LG2TTU) % 3 !=0:
        LG2TTU.append("N/D")
    while p < len(LG2TTU):
        listtemp=[]
        listtemp.append(LG2TTU[p]+LG2TTU[p+1]+LG2TTU[p+2])               
        LG210.append(listtemp[0])   ##configura para cada 3 letras serem 1 elemento da lista
        p=p+3
    q2=len(LG210)
    ###################################################################################
    #while kk < len(LG210)-7:
    #    listtemp=[]
    #    listtemp.append(LG210[kk]+LG210[kk+1]+LG210[kk+2]+LG210[kk+3]+LG210[kk+4]+LG210[kk+5]+LG210[kk+6])               
    #    LG221.append(listtemp[0])   ##configura para cada 7 elementos serem 1 elemento da lista
    #    kk=kk+1
    #kk2=len(LG221)
    #######################################################################################
    while kk < len(LG2TTU)-21:
        listtemp=[]
        listtemp.append(LG2TTU[kk]+LG2TTU[kk+1]+LG2TTU[kk+2]+LG2TTU[kk+3]+LG2TTU[kk+4]+LG2TTU[kk+5]+LG2TTU[kk+6]+LG2TTU[kk+7]+LG2TTU[kk+8]+LG2TTU[kk+9]
                        +LG2TTU[kk+10]+LG2TTU[kk+11]+LG2TTU[kk+12]+LG2TTU[kk+13]+LG2TTU[kk+14]+LG2TTU[kk+15]+LG2TTU[kk+16]+LG2TTU[kk+17]+LG2TTU[kk+18]
                        +LG2TTU[kk+19]+LG2TTU[kk+20]
                        )               
        LG221.append(listtemp[0])   ##configura para cada 21 letras serem 1 elemento da lista
        kk=kk+1
    c1=len(LG210)
    ##############PROCESSO###################################################################
    if len(LG1TTU) > len(LG2TTU):
        C = len(LG1TTU)
        while len(LG2TTU)<C:
            LG2TTU.append("N/D")
    elif len(LG1TTU) < len(LG2TTU):      ###igualar as listas unitarias
        C = len(LG2TTU)
        while len(LG1TTU)<C:
            LG1TTU.append("N/D")
    ###################################################################################
    if len(LG110) > len(LG210):
        C = len(LG110)
        while len(LG210)<C:
            LG210.append("N/D")
    elif len(LG110) < len(LG210):       ###igualar as listas de 3 em 3
        C = len(LG210)
        while len(LG110)<C:
            LG110.append("N/D")
    ##################################################################################
    print("Analisando...")
    while y < len(LG1TTU):
        if LG1TTU[y] != LG2TTU[y]:
            LG1TTUF.append(LG1TTU[y])      ##separação unitaria
            LG2TTUF.append(LG2TTU[y])
            E.append(str(y+1))
        y=y+1
    ################################################################################
    print("Analisando...")
    while v < len(LG110):
        if LG110[v] != LG210[v]:
            LG110F.append(LG110[v])    ##separação de 3 em 3
            LG210F.append(LG210[v])
            R.append(str(v+1))
        v=v+1
    ###################################################################################
    while z < len(LG110)-1:
        if LG110[z-1] != LG210[z-1] and LG110[z] != LG210[z] and LG110[z+1] != LG210[z+1]:
            LG19.append(LG110[z-1]+LG110[z]+LG110[z+1])    ##separação de 9 em 9
            LG29.append(LG210[z-1]+LG210[z]+LG210[z+1])
            D.append(str(z))
        z=z+1
    ################################################################################
    print("Analisando...")
    LG221F=LG221
    while j < len(LG121):
        if LG121[j] in LG221:
            LG221F.remove(LG121[j])
        j=j+1
    LG121F=LG121
    while j2 < len(LG221):
        if LG221[j2] in LG121:
            LG121F.remove(LG221[j2])
        j2=j2+1
    LG21F=LG121F+LG221F
    while len(LG121F)>len(LG221F):
        LG221F.append("N/D")     
    while len(LG121F)<len(LG221F):
        LG121F.append("N/D")    
    #################################################################################
    ff=len(LG110F)
    ff2=len(LG21F)
    if q<q2:
        tt=(len(LG210F)/q2)*100
    else:
       tt=(len(LG110F)/q)*100
    if len(LG110F) == 0:
        LG110F.append("N/D")    ##separação de 3 em 3
        LG210F.append("N/D")
        R.append("N/D")
    if len(LG1TTUF) == 0:
        LG1TTUF.append("N/D")      ##separação unitaria
        LG2TTUF.append("N/D")
        E.append("N/D")
    print("########################################################")
    print("quantidade de sequencia de DNA do primeiro arquivo:")
    print(o)
    print("quantidade de sequencia de DNA compactado em 3 do primeiro arquivo:")
    print(q)
    print("========================================================")
    print("quantidade de sequencia de DNA do segundo arquivo:")
    print(o2)
    print("quantidade de sequencia de DNA compactado em 3 do segundo arquivo:")
    print(q2)
    print("########################################################")
    print("quantidade de elementos de 3 em 3 diferentes:")
    print(ff)
    print("========================================================")
    print("quantidade de elementos diferentes:")
    print(ff2)
    print("########################################################")
    print("%","de sequencia de codons diferentes das duas amostras:")
    print(tt,"%")
    print("########################################################")
    print("Gerando arquivos...")
###############################################################################
    arq=open("analise_de_3_em_3_{}.txt".format(g),"w")
    arq.write(str("codon"+"\t"+"DNA1"+"\t"+"DNA2"+"\n"))
    while h<len(LG110F):
        arq.write(str(R[h]+"\t"+LG110F[h]+"\t"+LG210F[h]+"\n"))
        h=h+1
    arq.close()
###############################################################################
    arq=open("analise_de_diferença_{}.txt".format(g),"w")
    arq.write(str("elemento"+"\t"+"DNA1"+"\t"+"DNA2"+"\n"))
    while i<len(LG121F):
        arq.write(str("\t"+LG121F[i]+"\t"+LG221F[i]+"\n"))
        i=i+1
    arq.close()
###############################################################################
    arq=open("analise_de_9_em_9_{}.txt".format(g),"w")
    arq.write(str("região"+"\t"+"DNA1"+"\t"+"DNA2"+"\n"))
    while d<len(LG29):
        arq.write(str(D[d]+"\t"+LG19[d]+"\t"+LG29[d]+"\n"))
        d=d+1
    arq.close()
    g=g+1
    print("Arquivos criados com sucesso!")
    t=int(input("digite 0 para fazer outra analise ou 1 para parar:\n"))