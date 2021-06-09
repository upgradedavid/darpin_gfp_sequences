#!/usr/bin/python3.9

# %%  Adds provided string to path of containing folder

def combpath(filename):
    
    # Obtain path of file using basic function from python
    containfolder = str(__file__)
    
    # Split at \ into list
    containfolder = containfolder.split('\\')
    
    # Remove last object. Important: returns removed, but modifies object
    containfolder.pop(-1)
    
    # Create joined object, no return
    containfolder = '\\'.join(containfolder)
    
    # Create list to fill with old path and new path
    comblist = list()
    comblist.append(containfolder)
    comblist.append(filename)
    
    # Join the list components together and create new object
    filepath = '\\'.join(comblist)
    
    # Return new path
    return(filepath)

# %% Read FASTA file per line into list

def fastareadline(fastafilename):
    input_file = open(fastafilename, 'r')

    # Extracting content into list of string
    allines = input_file.readlines()

    # Closing file
    input_file.close()
    
    return(allines)

def fastaoutputstring(string, outputfilename):
    currentfile = open(outputfilename, 'w')
    currentfile.write(string)
    currentfile.close()
    

# %% Create function that returns FASTA without breaks in the sequences
# Loop over each input line

# Modify FASTA file to put sequences into single lines
def fasta_removebreaks(listoflines):
    
    # Run over each line of the list
    for x in range(len(listoflines)-1):
        
        # Don't remove breaks if the next one is NOT a FASTA header
        if listoflines[x].startswith('>') or listoflines[x + 1].startswith('>'):
            pass

        # If not, remove all linebreaks
        else:
            listoflines[x] = listoflines[x].replace('\n', '')
    
    # Return a single string
    return(''.join(listoflines))

# Create function to write each sequence string as a CSV
def fasta_to_csv(seq_string):
    listoflines = seq_string.split()
    for x in range(len(listoflines)):
        if not listoflines[x].startswith('>'):
            tempsplit = list(listoflines[x])
            listoflines[x] = ','.join(tempsplit)
    
    return('\n'.join(listoflines))

def fastalist_whiterev(linelist):
    for x in range(len(linelist)):
        temp = linelist[x].split('\t')
        linelist[x] = ''.join(temp)
    return(''.join(linelist))

# Let's use this thing:
importedfile = fastareadline('./tcoffee_alldp.fasta')
print(importedfile)

# Remove linebreaks and get total string
importedfile_nobreak = fasta_removebreaks(importedfile)
print(importedfile_nobreak)

# Create csv between positions
#importedfile_nobreak_csvsplit = fasta_to_csv(importedfile_nobreak)
#fastaoutputstring(importedfile_nobreak_csvsplit, 'csvtest.txt')

#fastaoutputstring(importedfile_nobreak, 'testoutput.txt')

# Let's see whether we can now import the output from excel
#outputfromcsv = fastareadline('manualalignment.txt')
#backinto = fastalist_whiterev(outputfromcsv)
#fastaoutputstring(backinto, 'manualalignedformview.txt')

print("whaaaa")
