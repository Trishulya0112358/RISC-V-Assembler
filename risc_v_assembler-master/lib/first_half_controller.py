from Phase1.file_preprocess import *
from Phase1.separate import *
from Phase1.mc_gen import *
from Phase1.memory import *
from Phase1.mergeDataText import *
from Phase1.breakToBasic import *
from Phase2.registers import RegisterTable
from Phase1.mcTotextMemory import mcToMemory

RegisterTable.Initialize()
# Removing Comments and Cleaning the Assembly Code File
preProcessObj = initParser('assemblyCode.asm') 
li = preProcessObj.preprocess_file()
preProcessObj.write_to_file('assemblyCodeProcessed.asm', li)

# Differentiating .data and .text segment
separateObj = text_data_seperator('assemblyCodeProcessed.asm', 'assemblyCodeData.asm', 'assemblyCodeText.asm')


# Creating Label Map - Removes label and add corresponding line number in another file
# Also replace all occurences of labels with corresponding number
dic, no_label_list = preProcessObj.generate_labels_and_list('assemblyCodeText.asm')
preProcessObj.write_to_file('assemblyCodeFinal.asm', no_label_list)