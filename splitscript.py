import sys
sys.path.append('/Users/awarlau/LENAInteraction/Analysis/LENAPostProcessing')
import subrecordings

subrecordings.splitAllAudio('/Users/awarlau/LENAInteraction/ECECStudy/WAVFiles/','/Users/awarlau/LENAInteraction/ECECStudy/ITSFiles/','/Users/awarlau/LENAInteraction/ECECStudy/SplitWAVFiles/','/Users/awarlau/LENAInteraction/ECECStudy/subrecinfo.csv')

# subrecordings.shortSegmentAllAudio('/Users/awarlau/LENAInteraction/ECECStudy/SplitWAVFiles/','/Users/awarlau/LENAInteraction/ECECStudy/ShortWAVFiles/')
