# Open the XML file that Plural Eyes exported

import re

def getSubRecInfo(pexmlfile, itsfiledir, outfile): # Open the XML file that Plural Eyes exported, and make a table giving synced subrecording info. and offset times relative to the reference subrecording (i.e., the syncing offset provided by Plural Eyes)
    
    # example of a pexmlfile: '/Users/awarlau/LENAInteraction/ECECStudy/2015-05-29_Room1_BestSync_FCP_Premiere.xml'
    # example of an itsfiledir: '/Users/awarlau/LENAInteraction/ECECStudy/ITSFiles/'
    # example of an outfile: '/Users/awarlau/LENAInteraction/ECECStudy/2015-05-29_Room1_reltimes.csv'
    
    # Open the output file for writing and print the header line
    outf = open(outfile,'w')
    outf.write('childID,subWAV,origWAV,ITS,daygmt,subrecstartgmt,subrecendgmt,subrecITSstarts,subrecITSends,syncoffset,totaloverlapstart,totaloverlapend\n')
    
    # Define the lists that will store the data fields
    childids = []
    subrecwavs = []
    origwavs = []
    itsfiles = []
    dates = []
    startgmts = []
    endgmts = []
    subrecstartssec = []
    subrecendssec = []
    relstartssec = []
    totaloverlapstartsec = []
    totaloverlapendsec = []
    
    pexml = open(pexmlfile)
    for line in pexml:
        if re.search('<timebase>',line):
            cursr = re.search('<timebase>(.+?)</timebase>',line).group(1) # Number of bins per second in the Plural Eyes analysis
        if re.search('<name>',line):
            curname = re.search('<name>(.+?)</name>',line).group(1) # Current subrecording WAV filename
        if re.search('<start>',line):
            relstartbin = re.search('<start>(.+?)</start>',line).group(1) # Get the relative start time of the current subrecording in Plural Eyes bins
            relstartsec = int(relstartbin)/float(cursr) # Get the relative start time of the current subrecording in seconds
            curitsstart = re.search('_.+?_.+?_.+?_(.+?)_',curname).group(1)
            origwav = re.search('_(.+?_.+?_.+?)_',curname).group(1) + '.wav' # Get the name of the original WAV file containing this subrecording
            itsfile = re.search('_(.+?_.+?_.+?)_',curname).group(1) + '.its' # Get the name of the ITS file containing this subrecording
            
            # Get the child id for this synced subrecording
            its = open(itsfiledir + itsfile) 
            for line in its:
                if re.search('Child id', line):
                    childid = re.search('Child id="(.+?)"',line).group(1)
            its.close()
            
            # Get the rest of the necessary info. about the current subrecording
            its = open(itsfiledir + itsfile)
            for line in its:
                if re.search('<Recording num', line):
                    rstart = re.search('startTime="PT(.+?)S',line).group(1)
                    rend = re.search('endTime="PT(.+?)S',line).group(1)
                    if rstart==curitsstart: # only want info. for the subrecording that underwent syncing
                        
                        daygmt = re.search('startClockTime="(.+?)T',line).group(1)
                        startgmt = re.search('startClockTime=.+?T(.+?)Z',line).group(1)
                        endgmt = re.search('endClockTime=.+?T(.+?)Z',line).group(1)
                        
                        childids.append(childid)
                        subrecwavs.append(curname)
                        origwavs.append(origwav)
                        itsfiles.append(itsfile)
                        dates.append(daygmt)
                        startgmts.append(startgmt)
                        endgmts.append(endgmt)
                        subrecstartssec.append(rstart)
                        subrecendssec.append(rend)
                        relstartssec.append(relstartsec)
                        
                if re.search('All about the Bars', line):
                    break
            its.close()
            
    # The overlap period runs from relstartsec to rstart+min(rend-relstartsec)
    after_overlap_duration = []
    for i in range(len(childids)):
        after_overlap_duration.append(float(subrecendssec[i])-relstartssec[i])
    total_overlap_duration = min(after_overlap_duration)
    
    for i in range(len(childids)):
        
        # Compute total overlap start and end times
        totaloverlapstartsec.append(relstartssec[i])
        totaloverlapendsec.append(relstartssec[i]+total_overlap_duration)
        
        # Write this subrecording's info to a CSV file
        outf.write(childids[i] + ',' + subrecwavs[i] + ',' + origwavs[i] + ',' + itsfiles[i] + ',' + dates[i] + ',' + startgmts[i] + ',' + endgmts[i] + ',' + subrecstartssec[i] + ',' + subrecendssec[i] + ',' + str(relstartssec[i]) + ',' + str(totaloverlapstartsec[i]) + ',' + str(totaloverlapendsec[i]) +  '\n')
    
    outf.close()
    pexml.close()
    
    return
