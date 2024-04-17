
import xml.etree.ElementTree as ET
import csv
import os
import re
from ProcessString import process_string

from edit_xml import edit_xml

# Define the process_string function
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))

    

def get_data(filename,XMLFILESCR,XMLFILECOOLIN,XMLStageCooling):
    """
    Parses a CSV file and checks if a condition is met, then edits the XML file accordingly.

    Args:
        filename: The filename of the CSV file.
        NewVaVName: The new name to replace in the XML file.
        XMLFILE: The filename of the XML file to edit.

    Returns:
        The number of rows in the CSV file (excluding header).
    """
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row
            next(reader, None)
            i = 0
            heatingstage=0
            for row in reader:
                i += 1
                # Check if a condition is met in the CSV row
                if row[12] == 'None':
                    print("Condition met at row", i)
                 
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-05-09"
                    OriginalAHU="AHU-05"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    # Edit the XML file
                    XMLFILE = "Template Cooling Only VAV Controlers/RP-V-5A.xml"
                    edit_xml(NewVaVName, XMLFILECOOLIN,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint,BoxCoef,heatingstage)
                if row[12] == 'SCR EH':
                    print("Condition met at row", i)
                   
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-01-01-01"
                    OriginalAHU="AHU-01-01"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    XMLFILE = "Template VAV SCR Controlers/RP-V4-A.xml"
                    edit_xml(NewVaVName, XMLFILESCR,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint, BoxCoef,heatingstage)
                if row[12] is not None and row[12] not in ['None', 'SCR EH']:
                    print("Condition met at row", i)
                  
                    NewVaVName= row[0]
                    NewAHUNAme=row[2]
                    NewMaxFlowSetpoint = row[13]
                    NewMinFlowSetpoint = row[14]
                    NewIntermediateFlowSetpoint = row[16]
                    BoxCoef= row[27]
                    OriginalVaVName="VAV-1-1-1"
                    OriginalAHU="AHU-01-01"
                    NewAHUNAme=process_string(NewAHUNAme)
                    NewVaVName=process_string(NewVaVName)
                    XMLFILE = "Template VAV SCR Controlers/RP-V4-A.xml"
                    heatingstage=0
                    if "2" in row[12]:
                        print("two stage")
                        heatingstage="2"
                    if "3" in row[12]:
                        print("3 stage")
                        heatingstage="3"
                    

                    edit_xml(NewVaVName, XMLStageCooling,OriginalAHU,OriginalVaVName,NewAHUNAme,NewMaxFlowSetpoint,NewMinFlowSetpoint,NewIntermediateFlowSetpoint,BoxCoef,heatingstage)
            
            
            return i  # Count the rows excluding header
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return 0  # Indicate error by returning 0

# Example usage

