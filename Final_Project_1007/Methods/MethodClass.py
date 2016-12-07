'''
Created on Dec 2, 2016

@author: apple
'''
class FundamentalMethods():
    '''
    classdocs
    '''
    def __init__(self, city, savepath):
        '''
        Constructor
        '''
        self.data=city
        self.savepath=savepath # .../results/201501_201502
class SituationMethods(FundamentalMethods):
    def briefSummary(self,level,name=[]):
        pass
        #TotalAccidennt()
        #TotalInjury()
        #TotalKilled()
    def PlotbyMonth(self,level,name=[]):
        pass
    def InjuryKillPIE(self,level,name=[]):
        pass
    def Map(self,level,name=[]):
        pass
    def BoroughCompare(self,level,name=[]):
        pass
    def RankTop10(self,level,name=[]):
        pass
'''
class SituationMethods(FundamentalMethods):
    def briefSummary(self,level,name=[]):
        pass
        #TotalAccidennt()
        #TotalInjury()
        #TotalKilled()
    def PlotbyMonth(self,SeverityMeasure,level,name=[]):
        pass
    def InjuryKillPIE(self,SeverityMeasure,level,name=[]):
        pass
    def Map(self,level,SeverityMeasure,name=[]):
        pass
    def BoroughCompare(self,SeverityMeasure,level,name=[]):
        pass
    def RankTop10(self,SeverityMeasure,level,name=[]):
        pass
'''


class ContributingMethods(FundamentalMethods):
    def InfluenceONSeverity(self,Influencer,SeverityMeasure,level,name=[],):
        pass
    def RelationshipBetweenInfluencer(self, Influencer0, Influencer1,level,name=[]):
        pass     