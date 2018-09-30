import numpy as np 
import operator
from enum import Enum
import numpy as np
import pandas as pd
   
class record:
    def __init__(self,year,earn=0.0,contrib=0.0,kids=False,disab=False):
        self.year = year
        self.earn = earn
        self.contrib = contrib
        self.kids = kids
        self.disab = disab

class rules:
    def __init__(self,qpp=False):
        bnames = ['byear','era','nra','lra']
        ynames = ['year','ympe','exempt','worker','employer','selfemp','arf','drc','nympe','reprate',
            'droprate','pu1','pu2','pu3','pu4','survmax60', 'survmax65', 'survage1', 'survage2', 
			 'survrate1', 'survrate2','era','nra','lra','test','supp','disab_rate','disab_base','cola']
        self.qpp = qpp
        self.start = 1966

        if (self.qpp==True):     
            self.yrspars = pd.read_excel('params/qpp_history.xlsx',names=ynames)
        else :
            self.yrspars = pd.read_excel('params/cpp_history.xlsx',names=ynames)
        self.stop  = np.max(self.yrspars['year'].values)
        self.yrspars = self.yrspars.set_index('year')
        self.cpi = 0.02
        self.wgr = 0.03     
    def ympe(self,year):
        if (year>self.stop):
            value = self.yrspars.loc[self.stop,'ympe']
            value *= (1.0+self.wgr)**(year-self.stop) 
        else:
            value = self.yrspars.loc[self.stop,'ympe']
        return value
    def exempt(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'exempt']
        else :
           value = self.yrspars.loc[year,'exempt']
        return value
    def worktax(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'worker']
        else :
           value = self.yrspars.loc[year,'worker']
        return value
    def empltax(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'employer']
        else :
           value = self.yrspars.loc[year,'employer']
        return value
    def tax(self,year):
        return self.worktax(year)+self.empltax(year)
    def selftax(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'selfemp']
        else :
            value = self.yrspars.loc[self.stop,'selfemp']        
        return value
    def arf(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'arf']
        else :
            value = self.yrspars.loc[year,'arf']  
        return value
    def drc(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'drc']
        else :
            value = self.yrspars.loc[year,'drc']  
        return value
    def nympe(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'nympe']
        else :
            value = self.yrspars.loc[year,'nympe']  
        return value
    def reprate(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'reprate']
        else :
            value = self.yrspars.loc[year,'reprate']  
        return value        
    def droprate(self,year):
        if (year > self.stop):
            value = self.yrspars.loc[self.stop,'droprate']
        else :
            value = self.yrspars.loc[year,'droprate']  
        return value
    def pu1(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year        
        return self.yrspars.loc[yr,'pu1']
    def pu2(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year 
        return self.yrspars.loc[yr,'pu2']
    def pu3(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year 
        return self.yrspars.loc[yr,'pu3']
    def pu4(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year
        return self.yrspars.loc[yr,'pu4']      
    def survmax60(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year
        return self.yrspars.loc[yr,'survmax60']
    def survmax65(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'survmax65']
    def survage1(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'survage1']
    def survage2(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'survage2']
    def survrate1(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'survrate1']
    def survrate2(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'survrate2']
    def era(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'era']
    def nra(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'nra']
    def test(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'test']
    def supp(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'supp']
    def disab_rate(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'disab_rate']
    def disab_base(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'disab_base']
    def cola(self,year):
        if year > self.stop :
            yr = self.stop
        else:
            yr = year

        return self.yrspars.loc[yr,'cola']
    def chgpar(self,name,y0,y1,value):
        if (name in self.yrspars.columns):
            for i in range(y0,y1+1):
                self.yrspars.loc[i,name] = value 
        else :
            for i in range(y0,y1+1):
                self.byrpars.loc[i,name] = value   

class account:
    def __init__(self,byear=None,rules=None):
        self.byear = byear
        self.claimage = None
        self.history = []    
        self.ncontrib = 0  
        self.ampe = 0.0
        self.receiving = False
        self.rules = rules
        self.benefit = 0.0
    def MakeContrib(self,year,earn,kids=False):
        if year>=self.rules.start:
            taxable = np.min([earn,self.rules.ympe(year)])
            if taxable > self.rules.exempt(year):
                taxable -= self.rules.exempt(year)
            else :
                taxable = 0.0    
            contrib = self.rules.worktax(year) * taxable 
            years = [self.history[p].year for p in range(self.ncontrib)] 
            self.history.append(record(year,earn=earn,contrib = contrib,kids=kids))      
            self.ncontrib +=1
    def ClaimCPP(self,year):
        currage = self.gAge(year)
        if self.claimage!=None:
            print('already claimed at ',self.claimage,' ...')
        else :
            if currage >= self.rules.era(year):
                self.claimage = currage
                self.receiving = True
                self.CalcAMPE(year)
                self.CalcBenefit(year)
    
            else :
                print('not yet eligible...')
    def gAge(self,year):
        return year - self.byear
    def gYear(self,age):
        return self.byear + age
    def CalcAMPE(self,year):
        # parameters
        yr18 = np.max([self.gYear(18),self.rules.start])
        yr70 = np.min([self.gYear(70),year])
        nyrs = yr70-yr18
        yrs = [self.history[p].year for p in range(self.ncontrib)]
        ympe = [self.rules.ympe(i) for i in yrs]
        exempt = [self.rules.exempt(i) for i in yrs]
        kids = [self.history[p].kids for p in range(self.ncontrib)]
        disab = [self.history[p].disab for p in range(self.ncontrib)]
        earn = [self.history[p].earn for p in range(self.ncontrib)]
        nympe = self.rules.nympe(year)
        # unadjusted pensionable earnings
        upe = [np.min([earn[i],ympe[i]]) for i in range(self.ncontrib)]
        upe = [np.where(upe[i]<exempt[i],0.0,upe[i]) for i in range(self.ncontrib)]
        # average ympe last 5 years
        avgympe = np.mean([self.rules.ympe(i) for i in range(year-nympe+1,year+1)])
        # compute ape
        ape = [upe[i]/ympe[i]*avgympe for i in range(self.ncontrib)]
        # need provision for disability
        ndrop = 0
        dropped = np.full(self.ncontrib, False)
        for i in range(self.ncontrib):
            if (upe[i]==0.0 and disab[i]==True):
                dropped[i] = True
                ndrop +=1        
        # dropout years for childrearing (CRD01)
        ndrop = 0
        dropped = np.full(self.ncontrib, False)
        for i in range(self.ncontrib):
            if (upe[i]==0.0 and kids[i]==True):
                dropped[i] = True
                ndrop +=1
        # compute average ape
        avgape = np.sum(ape)/(nyrs - ndrop)
        # Child rearing provision (CRD02)
        for i in range(self.ncontrib):
            if (ape[i]<avgape and kids[i]==True):
                ape[i] = 0.0
                dropped[i] = True
                ndrop +=1
        # need add provision working past 65
                
        # General dropout
        gdrop = int(np.ceil(self.rules.droprate(year)*(self.ncontrib - ndrop)))
        apef = [ape[i] for i in range(self.ncontrib) if dropped[i]==False]
        ixf = np.asarray(apef).argsort()[gdrop-1:]
        yrsf  = [yrs[i] for i in range(self.ncontrib) if dropped[i]==False]
        yrstodrop = [yrsf[i] for i in ixf] 
        for i in range(self.ncontrib):
            if (yrs[i] in yrstodrop and gdrop!=0):
                ape[i] = 0
                dropped[i] = True
                ndrop +=1
                gdrop -=1
        self.ampe = (1/12)*np.sum(ape)/(nyrs - ndrop)
    def CalcBenefit(self,year):
        if self.receiving==True:
            if (self.gAge(year)==self.claimage):
                nra = self.rules.nra(year)
                arf = self.rules.arf(year)
                drc = self.rules.drc(year)
                age = self.gAge(year)
                self.benefit = self.rules.reprate(year) * self.ampe 
                if (age<nra):
                    self.benefit *= 1.0+arf*(age-nra)
                else :
                    self.benefit *= 1.0+drc*(age-nra)                       
        else:
            self.benefit = 0.0          
    def RunCase(self,retage=60,claimage=65,ratio=1.0):
        for a in range(18,retage):
            yr = self.gYear(a)
            self.MakeContrib(yr,earn=self.rules.ympe(yr)*ratio)
        self.ClaimCPP(self.gYear(claimage))    
        return
    def ResetCase(self):
        self.claimage = None
        self.history = []    
        self.ncontrib = 0  
        self.ampe = 0.0
        self.receiving = False
        self.benefit = 0.0           
