import itertools
import random
import numpy as npy

POPULATION_SIZE=50
GENERATION_SIZE=100
PROBOFMUTATION=0.05
PROBOFCROSSOVER=0.7
PERLOCUSPROBCROSSOVER=0.5


class populasyon:

    kromozomlar = []

    def __init__(self,pop,tourpop,fitpop,yenipop):
        self.pop=pop ##popülasyon dizisi
        self.tourpop=tourpop ##popülasyon için turnuva seçilim sonrası oluşacak dizi
        self.fitpop=fitpop ##popülasyondaki her kromozomun uygunluk dizisi
        self.yenipop=yenipop ##gelecek nesil nüfusu

    def kromozomolustur(self,kromozom_uzunlugu):
        gen_kod=''
        for i in range(kromozom_uzunlugu):
            temp = str(random.randint(0, 1))
            gen_kod += temp
        return (gen_kod)
        n = 8
        str1 = rand_key(n)

        for i in range(100):
            str1 = rand_key(n)
            kromozomlar.append(str1)
        for i in kromozomlar:
            print(i)
        sonu = 0

    def sembolikkromozomolustur(self,kromozom_uzunlugu):
        gen_kod=''
        for i in range(kromozom_uzunlugu):
            gen_kod+=chr(random.randint(57,139))
            return gen_kod

    def populasyonekle(self,kromozom_uzunlugu):
        self.pop.append(self.kromozomolustur(kromozom_uzunlugu))
        return self.pop

    def uygunlukolc(self,populasyon):
        for git in populasyon:
            uygunlukdegeri=0
            for i in range(len(git)):
                if git[i] == '1' :
                    uygunlukdegeri+=1
                elif git[i]== '0' :
                    uygunlukdegeri+=0
            self.fitpop.append(uygunlukdegeri)

    def binarymutasyon(self,kromozom):
        temp=list(kromozom)
        for i in range(len(temp)):
            if random.random() <= PROBOFMUTATION:
                if temp[i] == '0':
                    temp[i] = '1'
                elif temp[i] == '1':
                    temp[i] = '0'
        return ''.join(temp)

    def sembolikmutasyon(self,kromozom):
        temp=list(kromozom)
        for i in range(len(temp)):
            if random.random() <= PROBOFMUTATION:
                temp[i]=chr(ord(temp[i])+1)
        return ''.join(temp)

    def k_noktasicaprazlama(self, k_noktasi, kromozom_bir, kromozom_iki, kromozom_uzunlugu):
        caprazlamadizi=[]
        if random.random() <= PROBOFCROSSOVER :
            for i in range(k_noktasi):
                random_nokta=random.randint(0, kromozom_uzunlugu-1)
                if random_nokta in caprazlamadizi:
                    random_nokta=random.randint(0,kromozom_uzunlugu-1)
                    caprazlamadizi.append(random_nokta)
                else:
                    caprazlamadizi.append(random_nokta)
            siralidizi = sorted(caprazlamadizi)
            print(siralidizi)
            siralidiziuzunluk = len(siralidizi)
            birkromocaprazlama= ''
            ikikromocaprazlama= ''

            if siralidiziuzunluk == 1 :
                birkromocaprazlama += kromozom_bir[:siralidizi[0]] + kromozom_iki[siralidizi[0]:]
                ikikromocaprazlama += kromozom_bir[:siralidizi[0]] + kromozom_iki[siralidizi[0]:]

            elif siralidiziuzunluk % 2 != 0:
                birkromocaprazlama += kromozom_bir[:siralidizi[0]]
                ikikromocaprazlama += kromozom_iki[:siralidizi[0]]
                for j in range(len(siralidizi)):
                    if j == siralidiziuzunluk - 1:
                        birkromocaprazlama += kromozom_iki[siralidizi[siralidiziuzunluk-1]:]
                        ikikromocaprazlama += kromozom_bir[siralidizi[siralidiziuzunluk-1]:]
                    elif j % 2 == 0:
                        birkromocaprazlama += kromozom_iki[siralidizi[j]:siralidizi[j+1]]
                        ikikromocaprazlama += kromozom_bir[siralidizi[j]:siralidizi[j+1]]
                    elif j % 2 != 0:
                        birkromocaprazlama += kromozom_bir[siralidizi[j]:siralidizi[j+1]]
                        ikikromocaprazlama += kromozom_iki[siralidizi[j]:siralidizi[j+1]]

            elif siralidiziuzunluk % 2 == 0:
                birkromocaprazlama += kromozom_bir[:siralidizi[0]]
                ikikromocaprazlama += kromozom_iki[:siralidizi[0]]
                for j in range(len(siralidizi)):
                    if j == siralidiziuzunluk -1:
                        birkromocaprazlama += kromozom_bir[siralidizi[siralidiziuzunluk-1]:]
                        ikikromocaprazlama += kromozom_iki[siralidizi[siralidiziuzunluk-1]:]
                    elif j % 2 == 0:
                        birkromocaprazlama += kromozom_iki[siralidizi[j]:siralidizi[j+1]]
                        ikikromocaprazlama += kromozom_bir[siralidizi[j]:siralidizi[j+1]]
                    elif j % 2 != 0:
                        birkromocaprazlama += kromozom_bir[siralidizi[j]:siralidizi[j+1]]
                        ikikromocaprazlama += kromozom_iki[siralidizi[j]:siralidizi[j+1]]

            print("Çaprazlanan çocuk bir %s" % (birkromocaprazlama))
            print("Çaprazlanan çocuk iki %s" % (ikikromocaprazlama))
            return birkromocaprazlama, ikikromocaprazlama
        else:
            return kromozom_bir,kromozom_iki

    def teknoktacaprazlama(self, kromozom_bir, kromozom_iki, kromozom_uzunlugu):

        if random.random() <= PROBOFCROSSOVER:
           teknokta=random.randint(0, kromozom_uzunlugu-1)
           print("çaprazlama noktası %d" %(teknokta))
           return kromozom_bir[:teknokta]+kromozom_iki[teknokta:], kromozom_bir[teknokta:] + kromozom_iki[:teknokta]
        else:
            return  kromozom_bir, kromozom_iki

    def uniformcaprazlama(self,kromozom_bir,kromozom_iki,kromozom_uzunlugu):

        temp1=list(kromozom_bir)
        temp2=list(kromozom_iki)
        if random.random() <= PROBOFMUTATION:
            for i in range(kromozom_uzunlugu):
                if random.random() <= PERLOCUSPROBCROSSOVER:
                    t=temp1[i]
                    temp1[i] = temp2[i]
                    temp2[i]=t
            kromozom_bir=''.join(temp1)
            kromozom_iki=''.join(temp2)
            return kromozom_bir,kromozom_iki
        else:
            return kromozom_bir,kromozom_iki

    def uygunlukoranlısecilim(self,uygunlukdizisi):
        toplamuygunluk=npy.sum(uygunlukdizisi)
        temparray=npy.array(uygunlukdizisi)
        uygunlukorani=npy.true_divide(temparray, toplamuygunluk)
        ilkrasgelesecilim=random.randint(0, len(uygunlukorani)-1)
        ikincirandomsecilim=random.randint(0,len(uygunlukorani)-1)
        return self.pop[ilkrasgelesecilim],self.pop[ikincirandomsecilim]

    def turnuvasecilim(self,boyut):
        randarray=[]
        fittuarray=[]
        for i in range(boyut):
            rasgeledeger=random.randint(0,len(self.fitpop) - 1)
            randarray.append(rasgeledeger)
        for j in randarray:
            fittuarray.append(self.fitpop[j])

        print("uygunluk dizisi %s" %(fittuarray))
        maxdeger=max(fittuarray)
        print(maxdeger)

        for k in range(len(fittuarray)):
            if maxdeger==fittuarray[k]:
                self.tourpop.append(self.pop[randarray[k]])
                break

    def elitizm(self,element):
        siraliindeks=npy.argsort(self.fitpop)
        siralanmis=siraliindeks[-element:]
        for i in range(len(siralanmis)):
            print("elitizm element")
            return self.pop[siralanmis[i]]

    def rastrigin(self, kromozom):
      list(itertools.combinations_with_replacement('01',4))


if(__name__=="__main__"):

    pops=populasyon([], [], [], [])
    a=0
    for i in range(POPULATION_SIZE):
     pops.populasyonekle(8)  ##popülasyon oluşuyor
    pops.uygunlukolc(pops.pop)  ##uygunluk değeri ölç
    print("Başlangıç popülasyonu %s" %(pops.pop))
    print("Başlangıç popülasyonunun uzunluğu %d" %len(pops.pop))
    print("İlk uygunluk dizisi %s" %(pops.fitpop))
    pops.elitizm(2)
    while a < GENERATION_SIZE:
        print("Nesil %d" %(a))
        a+=1
        pops.yenipop=[]
        for j in range(POPULATION_SIZE):
            pops.turnuvasecilim(3)
        print("Turnuva seçilim sonrası dizi %s" %(pops.tourpop))
        print("Turnuva seçilim sonucu dizi uzunluğu %s" %len(pops.tourpop))
        for k in range(0, len(pops.tourpop)):
            if len(pops.tourpop) == 0:
                break
            else:
                print("Oluşturulacak turnuva dizisi %s" %pops.tourpop)
                ebeveynbir=pops.tourpop[0]
                ebeveyniki=pops.tourpop[1]
                x,y=pops.k_noktasicaprazlama(3,ebeveynbir,ebeveyniki,16)
                cocukbir=pops.binarymutasyon(x)
                cocukiki=pops.binarymutasyon(y)
                print("Çocuk bir %s" %(cocukbir))
                print("Çocuk iki %s" %(cocukiki))
                pops.yenipop.append(cocukbir)
                pops.yenipop.append(cocukiki)
                pops.fitpop=[]
                pops.uygunlukolc(pops.yenipop)
                pops.tourpop.remove(ebeveynbir)
                pops.tourpop.remove(ebeveyniki)
                print("Oluşturulan yeni nesil %s"%(pops.yenipop))


        if max(pops.fitpop) == 30:
            print("Optimal cevap bulundu")
            break
