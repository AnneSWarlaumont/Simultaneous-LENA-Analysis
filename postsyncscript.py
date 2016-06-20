import sys, subprocess

sys.path.append('/Users/awarlau/LENAInteraction/ECECStudy/SimultaneousLENAPostProcess/')
import postPluralEyes

sys.path.append('/Users/awarlau/HomeBankCode/lena-its-tools')
import relabel

postPluralEyes.getSubRecInfo('/Users/awarlau/LENAInteraction/ECECStudy/2015-05-29_Room1_BestSync_FCP_Premiere.xml','/Users/awarlau/LENAInteraction/ECECStudy/ITSFiles/','/Users/awarlau/LENAInteraction/ECECStudy/2015-05-29_Room1_reltimes.csv')

subprocess.call(["perl","/Users/awarlau/HomeBankCode/lena-its-tools/segments.pl",'/Users/awarlau/LENAInteraction/ECECStudy/ITSFiles/e20150601_171803_010569.its','/Users/awarlau/LENAInteraction/ECECStudy/LENASegments/e20150601_171803_010569_LENASegments.csv'])

relabel.relabel_human_near('/Users/awarlau/LENAInteraction/ECECStudy/LENASegments/e20150601_171803_010569_LENASegments.csv','/Users/awarlau/LENAInteraction/ECECStudy/WAVFiles/e20150601_171803_010569.wav','/Users/awarlau/LENAInteraction/ECECStudy/CorrectedSegments/e20150601_171803_010569_CorrectedSegments.csv',17.2666666667,3373.18) # In future, we will want to get these inputs automatically from reading the day and room's reltimes.csv file.