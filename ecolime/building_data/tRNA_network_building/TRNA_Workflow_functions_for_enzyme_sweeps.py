import minime
import pandas as pd
# python imports
import re
import json
from os.path import join
import cPickle
import statistics
import math
# third party imports
import pandas as pd
import escher
import cobra.test
import cloudpickle
# ecoli me
import ecolime
from ecolime.flat_files import *
from ecolime.ecoli_k12 import *
from ecolime import ribosome, tRNA_charging, transcription, translocation, chaperones
from minime.util import dogma
from minime import *
from minime.util import building
from minime.util.mass import compute_RNA_mass
from minime.solve.algorithms import binary_search, fva, solve_at_growth_rate
from minime.solve.symbolic import compile_expressions
import matplotlib

import sys
import os
import copy
from copy import deepcopy
from tqdm import tqdm

#import the me model tRNA sequences later for checking
from cloudpickle import load
infolder = '/home/ecatoiu/SBRG_github_clone/ecolime/prototype_notebooks/'
with open(infolder +"9_30_2016_prototype_59_tRNA_sequences.pickle", "rb") as infile:
    me = load(infile)
with open(infolder +"9_30_2016_prototype_59_tRNA_sequences_expressions.pickle", "rb") as infile:
    expressions = load(infile)


# # 1. Curating RNA modification details
def get_RNA_modification_reaction_details(modification_network, rna_type):
    """
    description :  
        creates a master dictionary with all modification (sub reactions) details and selects for RNA type. details
        include  position, enzyme, and RNA substrates that can undergo these modifications
    
    inputs : 
        Ecocyc/MODOMICS raw data : uridine/cytidine/guanine/adenine modification reaction details
        these inputs are dictionaries that describe each individual reaction that RNA can undergo
        
    output:
        returns a master dictionary with all the reaction details for each base
        {base: { modifications : {input/output, stoichiometric reactions, enzymes,
        carriers, rna type, rna position, rna substrates}}}
    
    """
    
    import  MODS_Adenine, MODS_Cytidine, MODS_Guanine , MODS_URIDINE_2 #raw dat
    #combine raw data into one master data
    rna_mod_details = {}
    guanine = MODS_Guanine.guanine_mods
    adenine = MODS_Adenine.adenine_mods
    cytidine = MODS_Cytidine.cytidine_mods
    uridine = MODS_URIDINE_2.uridine_mod
    #base_dict = {'Guanine_mods_paths':'G', 'Cytidine_mods_paths':'C', 'Adenine_mods_paths':'A', 'Uridine_mods_paths':'U'}

    rna_mod_details.update({'Guanine_mods_paths' :guanine})
    rna_mod_details.update({'Adenine_mods_paths' : adenine})
    rna_mod_details.update({'Cytidine_mods_paths' : cytidine})
    rna_mod_details.update({'Uridine_mods_paths' :uridine})
    #print '1A.', '\t' ,'OBTAINING modification details'
    
    #select tRNA/rRNA modifications
    import copy
    rna_mod_details_rna_type = copy.deepcopy(rna_mod_details)
    
    
    
    for base in rna_mod_details_rna_type.keys():
        if modification_network[base] == {}:
            del rna_mod_details_rna_type[base]
        
        else:
            for modification in rna_mod_details_rna_type[base].keys():


                if modification not in modification_network[base].keys():
                    del rna_mod_details_rna_type[base][modification]
                else:
                    enzyme_list = rna_mod_details_rna_type[base][modification]['machines'].keys()
                    for enzyme in enzyme_list:
                        rna_list = rna_mod_details_rna_type[base][modification]['machines'].get(enzyme).get('RNA_position_substrates').keys()
                        #deletes non-rna_type modifications details
                        for rna in rna_list:
                            if rna != rna_type:
                                del  rna_mod_details_rna_type[base][modification].get('machines').get(enzyme).get('RNA_position_substrates')[rna]
                        if  rna_mod_details_rna_type[base][modification].get('machines').get(enzyme).get('RNA_position_substrates') == {}:
                            del rna_mod_details_rna_type[base][modification].get('machines')[enzyme]
                        if rna_mod_details_rna_type[base][modification]['machines'] == {}:
                            del rna_mod_details_rna_type[base][modification]


    return rna_mod_details_rna_type


#1B : all nucleotides for each output modification group!

def get_RNA_modification_products(modification_network, rna_type):
    """
    description :  idenitfies the nucleotide associated with each final modification product
    input: calls 'get_RNA_modification_reaction_details(modification_network, rna_type)'
    output : dictionary with { final modification product : start nucleotide}
    """   
    
    import copy
    #calls the modification details
    
    total_RNA_modification_details = copy.deepcopy(get_RNA_modification_reaction_details(modification_network, rna_type))
    
    #print '1B.', '\t' ,'OBTAINING modification : nucleotide info'
    
    base_dict = {'Guanine_mods_paths':'G', 'Cytidine_mods_paths':'C', 'Adenine_mods_paths':'A', 'Uridine_mods_paths':'U'}
    modification_dict = {}
    for base in base_dict.keys():
        if base in total_RNA_modification_details.keys():
            
            for modification in total_RNA_modification_details.get(base).keys():
                modification_output = total_RNA_modification_details.get(base).get(modification).get('output')
                modification_input = total_RNA_modification_details.get(base).get(modification).get('input')
                if modification_output not in modification_dict.keys():
                    modification_dict.update({modification_output: base_dict[base]})
    return modification_dict


# # 2. Modomics Modification Network

# ## 2A. depth first search code
#finds all paths
#important depth-first search function


#11/6/16
#modified to use different input data

def find_all_paths(graph, start, end, path=[]):
    """
    description : depth-first search code taken from python help docs, used to identify all paths from parent node to leaf node
    [path] = ['nucleotide--> modification1' , '-->downstream reactions ' ,'-->final reaction']
    """ 
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start].get('upstream_rxns'):
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# ## 2B : all paths from root node to child node in modification network
#uses depth-first search algo
#OUTPUT: dictionary w/ Total_Modification : {'path #' : [upstream rxn list] }
#this imports the dictionary with modification inputs outputs {'modification' : 'input rxns upstream'}
#this function uses function (find_all_paths) to find all paths from each modification to a base!!!!!!!!

#11/6/2016
#this imports the dictionary with modification inputs outputs {'modification' : 'input rxns upstream'}
#this function uses function (find_all_paths) to find all paths from each modification to a base!!!!!!!!

#11/6/2016

#modified to use different input data
def get_all_paths_MODOMICS_network(modification_network,rna_type):
    """
    finds all paths in the modified network 
    """   
    import copy
    from copy import deepcopy
    
    base_dict = {'Guanine_mods_paths':'G', 'Cytidine_mods_paths':'C', 'Adenine_mods_paths':'A', 'Uridine_mods_paths':'U'}
    mod_paths = copy.deepcopy(modification_network)
    modification_products = copy.deepcopy(get_RNA_modification_products(modification_network, rna_type))
    
    
    trna_mod_path_dict = {}
    for base in base_dict.keys():
        base_modifications = mod_paths[base]
        for mod in base_modifications.keys():
            trna_mod_path_dict.update({mod : find_all_paths(base_modifications, mod, base_dict[base])})
    
    trna_modification_paths = {}
    for mod, paths in trna_mod_path_dict.iteritems():
        count = 0
        temp_dict = {}
        for path in paths:
            count = count + 1
            path_number = 'path_' + str(count)
            temp_dict.update({path_number : path})
        trna_modification_paths.update({mod : temp_dict})
    
    total_paths = {}
    for mod_output in modification_products.keys():
        temp_dict = {}
        #print '\n', mod_output,'\t', '\t',
        count = 0
        for modification in trna_modification_paths.keys():
            if mod_output == modification.split('_')[2]:
                for path_number, path in  trna_modification_paths.get(modification).iteritems():
                    count = count + 1
                    new_path_number = 'path_' + str(count)
                    temp_dict.update({new_path_number : path })
        mod = modification_products[mod_output] + '_to_' + mod_output
        if temp_dict != {}:
            total_paths.update({mod : temp_dict})

    for mod in total_paths.keys():
        mod_input = mod.split('_')[0]
        for path_number, path in total_paths.get(mod).iteritems():
            path.remove(mod_input)
    #print '2B. get_all_paths_MODOMICS_network'
    return total_paths


# ## 2C : import modification network enzyme/position details

# In[8]:

def get_enzymes_from_MODOMICS_network(modification_network, rna_type):
    """
    description:
        builds quick enzyme information [name, position] for each modification.  selects for tRNA type
        this quick information will be used later to correct for the depth-first search when multiple enzymes/positions
        are prevalent for the same modification sub-rxn (Y, D, Um, Cm, cmnm5Um)
        
    input:
        tRNA modomics network map
        
    output: 
        dictionary with {sub reaction  : {position : enzyme name}}"""
    
    import copy
    from copy import deepcopy
    mod_paths = copy.deepcopy(modification_network)
    
    rna_mod_paths = copy.deepcopy(mod_paths)
    #select only RNA_type positions (tRNA length < 76)
    
    base_dict = {'Guanine_mods_paths':'G', 'Cytidine_mods_paths':'C', 'Adenine_mods_paths':'A', 'Uridine_mods_paths':'U'}
    for base in base_dict.keys():
        for sub_rxn in mod_paths[base]:
            for position in mod_paths[base][sub_rxn].get('enzymes').keys():
                if rna_type == 'tRNA':
                    if position != u'20A' and int(position) > 76 :
                        del rna_mod_paths[base][sub_rxn].get('enzymes')[position]
                elif rna_type =='rRNA':
                    if position == u'20A' or int(position) <= 76: 
                        del rna_mod_paths[base][sub_rxn].get('enzymes')[position]
            if rna_mod_paths[base][sub_rxn].get('enzymes') == {}:
                del rna_mod_paths[base][sub_rxn]   
    #print '2C. get_enzymes_from_MODOMICS_network'            
    return rna_mod_paths

#takes raw modomics network and filters based on RNA TYPE input
# ## 2D : Adding full path enzyme detail to depth-first search result
#adds enzyme details to depth-first search result



def add_enzymes_to_rna_paths(modification_network, rna_type):
    """
    description: 
        adds enzyme, position information to paths from MODOMICS network
        BUG : (Um , Y, D , cmnm5Um, Cm) fixed by 'fix_path_count_for_multple_enzymes'
    input: 
        get_enzymes_from_MODOMICS_network(modification_network, rna_type) : enzyme, position information
        get_all_paths_MODOMICS_network(modification_network, rna_type): modification, path, upstream rxn information
    output: 
        dictionary, keeps track of all upstream rxns in each path
        total modification : { path number :  { 'sub rxn 1' : {position : [enzyme name]},
                                                'total_path_rxns' : [rxn list]}
                            } 
    """
    
   
    import copy
    total_tRNA_modification_paths = copy.deepcopy(get_all_paths_MODOMICS_network(modification_network, rna_type))
    #print total_tRNA_modification_paths
    trna_mods = copy.deepcopy(get_enzymes_from_MODOMICS_network(modification_network, rna_type))
    base_dict = {'Guanine_mods_paths':'G', 'Cytidine_mods_paths':'C', 'Adenine_mods_paths':'A', 'Uridine_mods_paths':'U'}
    
    
    
    all_mods_dict = {}
    for total_mod in total_tRNA_modification_paths:
        base = total_mod.split('_')[0]
        for key in base_dict.keys():
            if base_dict[key] == str(base):
                base = key
                
        
        total_mod_dict = {}
        for path_number, path_rxns in total_tRNA_modification_paths[total_mod].iteritems():
            path_dict = {}
            path_dict.update({'total_path_rxns': path_rxns})
            for sub_rxn in path_rxns:
                enzyme_dict = {}
                #use enzyme information from MODOMICS
                for position in trna_mods[base][sub_rxn].get('enzymes').keys():
                    enzyme =  trna_mods[base][sub_rxn].get('enzymes')[position]
                    enzyme_dict.update({ position : enzyme})
                path_dict.update({sub_rxn : enzyme_dict})
            total_mod_dict.update({path_number : path_dict})
        all_mods_dict.update({total_mod : total_mod_dict})
    #print '2D. add_enzymes_to_rna_paths'
    return all_mods_dict



def fix_path_count_for_multple_enzymes(modification_network, rna_type):
    
    """
    description: 
        fixes path counts for modifications that can occur at multiple positions (Um , Y, D , cmnm5Um, Cm)
        adjusts the path count to the correct position if modification is used upstream of final mod
        Um [32,34] --> cmnm5Um [34]
    input:
        'add_enzymes_to_rna_paths(modification_network, rna_type)': MODOMICS network with enzyme, position information
    output:
        MODOMICS network with enzyme, position information with correct path numbering 
    
    """
    
    import copy
    total_tRNA_modification_paths = copy.deepcopy(add_enzymes_to_rna_paths(modification_network, rna_type))
    #total_tRNA_modification_reaction_details =  copy.deepcopy(get_RNA_modification_reaction_details(modification_network, rna_type))
    base_dict = {'G' : 'Guanine_mods_paths', 'C' : 'Cytidine_mods_paths', 'A': 'Adenine_mods_paths','U' : 'Uridine_mods_paths'}

   
    #print 'adding enzymes to rna paths'
    #print total_tRNA_modification_paths
    
    total_mod_dict_final = {}
    for total_mod in total_tRNA_modification_paths.keys():
        nucleotide = total_mod.split('_')[0]
        base = base_dict[nucleotide]
        path_list_current = total_tRNA_modification_paths[total_mod].keys()
        path_dict = {}  # stores all path numbers
        
        #figure out all the positiosn available in a path 
        #if len(path_positions) != 1, we have found a bug!
        for path_number in path_list_current:
            path_position_list = []
            path_enzyme_list = {}
            total_path_rxns = total_tRNA_modification_paths[total_mod][path_number]['total_path_rxns']
            for sub_rxn in total_path_rxns:
                position = total_tRNA_modification_paths[total_mod][path_number][sub_rxn].keys()
                if len(position) == 1:
                    if position[0] not in path_position_list:
                        path_position_list.append(position[0])
                else:
                    path_position_list = position          
            #normal condition, only one position exists for the entire path
            if len(path_position_list) == 1:
                for sub_rxn in total_path_rxns:
                    enzyme_temp = total_tRNA_modification_paths[total_mod][path_number][sub_rxn].get(path_position_list[0])
                    #print total_mod, enzyme_temp
                    for enzyme in enzyme_temp:
                        if enzyme in path_enzyme_list.keys():
                            path_enzyme_list[enzyme] += 1
                        else:
                            path_enzyme_list.update({enzyme : 1})
                temp_dict = {} # stores all path numbers
                temp_dict.update({'enzymes' : path_enzyme_list})
                temp_dict.update({'position' : path_position_list[0]})
                temp_dict.update({'total_path_rxns' : total_path_rxns })
                
            else:
                #removes any inconsistencies in the position of upstream vs downstream reactions
                for position in path_position_list:
                    count = 0 
                    for sub_rxn in total_path_rxns:
                        if position in total_tRNA_modification_paths[total_mod][path_number][sub_rxn].keys():
                            count = count + 1
                    if count != len(total_path_rxns):
                        path_position_list.remove(position)
                        print '\t', '\t', 'Removed position [%s] for %s' %(position, total_mod),
                
                #adjusted normal case : occurs for U_to_Um [32,34] --> Um_to_cmnm5Um [34]         
                if len(path_position_list) == 1:
                    print '\t','\t',  ' --> occurs @ %s' %(path_position_list[0])
                    for sub_rxn in total_path_rxns:
                        enzyme_temp = total_tRNA_modification_paths[total_mod][path_number][sub_rxn].get(path_position_list[0])
                        for enzyme in enzyme_temp:
                            if enzyme in path_enzyme_list.keys():
                                path_enzyme_list[enzyme] += 1
                            else:
                                path_enzyme_list.update({enzyme : 1})
                    temp_dict = {} # stores all path numbers
                    temp_dict.update({'enzymes' : path_enzyme_list})
                    temp_dict.update({'position' : path_position_list[0]})
                    temp_dict.update({'total_path_rxns' : total_path_rxns })
                    path_dict.update({path_number : temp_dict})
                    
                    
                else:
                    #the path position list > 1 for (Um, Y, D, Cm)
                    #each position must be counted as its own individual path (right now it is counted as the same path)
                    print '\t', 'Creating new paths for %s' %(total_mod)          
                    count = 0
                    while len(path_position_list) >= len(path_list_current):
                        position = path_position_list[0]
                        path_enzyme_list = {}
                        count = count + 1
                        new_path_name = 'path_' + str(count)
                        enzyme_temp = total_tRNA_modification_paths[total_mod][path_number][sub_rxn].get(position)
                        for enzyme in enzyme_temp:
                            if enzyme in path_enzyme_list.keys():
                                path_enzyme_list[enzyme] += 1
                            else:
                                path_enzyme_list.update({enzyme : 1}) 
                        temp_dict = {} # stores all path numbers
                        temp_dict.update({'enzymes' : path_enzyme_list})
                        temp_dict.update({'position' : position})
                        temp_dict.update({'total_path_rxns' : total_path_rxns })
                        path_dict.update({new_path_name : temp_dict})
                        path_position_list.remove(position)
                continue
            path_dict.update({path_number : temp_dict})
        total_mod_dict_final.update({total_mod : path_dict})
    #print '2D. fix_path_count_for_multple_enzymes'
    return total_mod_dict_final

#adjusts path count to reflect the same modification being catalyzed by different enzymes and/or occuring at different positions
# ## 2E : Adding full path metabolite detail to depth-first search result
#Adds metabolite stoichiometry to total rxn path


def add_metabolites_to_rna_paths(modification_network, rna_type):
    """
    description: adds metabolites information to fixed modomics paths 
    input: 
        fix_path_count_for_multple_enzymes(modification_network, rna_type) : corrected path, enzyme, position details
        get_RNA_modification_reaction_details(modification_network, rna_type) : reaction details, metabolite details
    output: modomics paths with enzyme, metabolites, positions
    """
    
    import copy
    total_RNA_modification_details = copy.deepcopy(get_RNA_modification_reaction_details(modification_network, rna_type))
    temp_dict_4_final = copy.deepcopy(fix_path_count_for_multple_enzymes(modification_network, rna_type))
    #base_dict = {'G' : 'Guanine_mods_paths', 'C' : 'Cytidine_mods_paths', 'A': 'Adenine_mods_paths','U' : 'Uridine_mods_paths'}
    base_dict = {'G' : 'Guanine_mods_paths', 'C' : 'Cytidine_mods_paths', 'A': 'Adenine_mods_paths','U' : 'Uridine_mods_paths'}



    for total_mod in temp_dict_4_final:
        base = base_dict[total_mod.split('_')[0]]
        for path_number in temp_dict_4_final[total_mod]:
            path_rxn_metabolites = {}
            for sub_rxn in temp_dict_4_final[total_mod][path_number].get('total_path_rxns'):
                sub_rxn_stoich = total_RNA_modification_details[base][sub_rxn].get('metabolites')
                for met, met_stoich in sub_rxn_stoich.iteritems():
                    if met not in path_rxn_metabolites.keys():
                        path_rxn_metabolites.update({met : met_stoich})
                    else:
                        new_met_stoich = met_stoich + path_rxn_metabolites[met]
                        path_rxn_metabolites.update({met: new_met_stoich})
            temp_dict_4_final[total_mod][path_number].update({'metabolites' : path_rxn_metabolites}) 
    #print '2E. add_metabolites_to_rna_paths'
    return temp_dict_4_final


# ## 2F: add carriers

def add_carriers_to_rna_paths(modification_network, rna_type):
    """
    description :
        adds carrier information to modomics paths, also adds TusABCDE cluster to enzyme stoich when TrmU_mono is used
    input:
        add_metabolites_to_rna_paths(modification_network, rna_type): metabolite, enzyme info for modomics paths
        get_RNA_modification_reaction_details(modification_network, rna_type): reaction details (carrier info per enzyme)
    output:
        modomics paths with carrier/metabolite/position/enzyme info
        """
    import copy
    total_tRNA_modification_reaction_details =  copy.deepcopy(get_RNA_modification_reaction_details(modification_network, rna_type))
    temp_dict_4_final = copy.deepcopy(add_metabolites_to_rna_paths(modification_network, rna_type))
    base_dict = {'G' : 'Guanine_mods_paths', 'C' : 'Cytidine_mods_paths', 'A': 'Adenine_mods_paths','U' : 'Uridine_mods_paths'}
    
    
       
    for total_mod in temp_dict_4_final:
        nucleotide = total_mod.split('_')[0]
        base = base_dict[nucleotide]
        for path_number in temp_dict_4_final[total_mod]:
            carrier_temp_dict = {}
            for sub_rxn in temp_dict_4_final[total_mod][path_number]['total_path_rxns']:
                #mapping to reaction in master dictionary w/reaction details
                sub_rxn_details = total_tRNA_modification_reaction_details[base][sub_rxn]   
                for enzyme in sub_rxn_details['machines']:
                    #matches enzyme in paths to enzyme in details dictionary
                    if enzyme in temp_dict_4_final[total_mod][path_number]['enzymes']:
                        enzyme_path_stoich = temp_dict_4_final[total_mod][path_number]['enzymes'][enzyme] # need the enzyme stoich
                        carrier_info = sub_rxn_details['machines'][enzyme]['carriers']
                        #find carrier info          
                        if carrier_info:
                            for carrier, carrier_stoich in carrier_info.iteritems():
                                carrier_path_stoich = carrier_stoich * enzyme_path_stoich #multiply carrier stoich to reflect path enzyme stoich
                                if carrier not in carrier_temp_dict:
                                    carrier_temp_dict.update({carrier : carrier_path_stoich})
                                else:
                                    carrier_temp_dict[carrier] + carrier_path_stoich
                        
                        #some modifications in original model have multiple enzymes that catalyze reaction
                        #TusABCDE cluster interacts to facilitate reaction
                        # this adds these enzymes into the path data whenever 'TrmU_mono' is the enzyme used in a reaction
                        if total_tRNA_modification_reaction_details[base][sub_rxn]['machines'][enzyme].get('additional_enzymes'):
                            additional_enzymes = total_tRNA_modification_reaction_details[base][sub_rxn]['machines'][enzyme].get('additional_enzymes')
                            
                            for add_enzyme, add_enzyme_stoich in additional_enzymes.iteritems():                            
                                add_enzyme_stoich_path = add_enzyme_stoich * enzyme_path_stoich
                                if add_enzyme not in  temp_dict_4_final[total_mod][path_number]['enzymes']:
                                    temp_dict_4_final[total_mod][path_number]['enzymes'].update({add_enzyme : add_enzyme_stoich_path})
                                else:
                                    temp_dict_4_final[total_mod][path_number]['enzymes'][add_enzyme] += add_enzyme_stoich_path           
            if carrier_temp_dict == {}:
                temp_dict_4_final[total_mod][path_number].update({'carriers' :  None})
            else:
                temp_dict_4_final[total_mod][path_number].update({'carriers' :  carrier_temp_dict})
    #print '2F. add_carriers_to_rna_paths'
    return temp_dict_4_final


# ## 2G : Using enzyme/metabolite detail to determine equivalent paths
#total path checker
#checks if paths are equivalent based on "enzymes" or "metabolites"
#outputs a total modification : {equal path # : [all identical path numbers] }



def check_equivalent_RNA_MODOMICS_paths(modification_network, rna_type, enzyme_or_metabolite_or_carrier):
    """
    description : determines which paths in modomics path network are equivalent
    input: 
        user : 'enzymes', 'metabolites' or 'carriers' (carriers offers no additional information)
        user : 'rna_type'
        add_carriers_to_rna_paths(modification_network, rna_type) : modomics path network w/carrier,enzyme & metabolite details
        
    output: 
        assigns equivalent_paths to [path list]
        returns dictionary = {total modification : equivalent path # : [previously named modomics paths]}
    """
    import copy
    tRNA_path_rxn_details_dictionary = copy.deepcopy(add_carriers_to_rna_paths(modification_network, rna_type))
   
    
    mod_equivalent_paths_dict = {}
    for mod in tRNA_path_rxn_details_dictionary.keys():
        total_paths = tRNA_path_rxn_details_dictionary[mod].keys()   #list of total paths to be checked
        equal_path_count = 1
        temp_path_dict = {}
        while len(total_paths) > 0:
            path = total_paths[0]
            path_variable = tRNA_path_rxn_details_dictionary.get(mod).get(path).get(enzyme_or_metabolite_or_carrier)
            path_position = tRNA_path_rxn_details_dictionary.get(mod).get(path).get('position')
            total_paths.remove(path)
            temp_list = [path]

            for remaining_path in total_paths:
                remaining_path_variable = tRNA_path_rxn_details_dictionary.get(mod).get(remaining_path).get(enzyme_or_metabolite_or_carrier)
                remaining_path_position = tRNA_path_rxn_details_dictionary.get(mod).get(remaining_path).get('position')
                
                if path_variable == remaining_path_variable and path_position == remaining_path_position:  #this solves the various positions as different paths
                    temp_list.append(remaining_path)

            for matched_path in temp_list:
                if matched_path in total_paths:
                    total_paths.remove(matched_path)
            equal_path_name =  'equal_path_' + str(equal_path_count)    
            temp_path_dict.update({equal_path_name : temp_list})
            equal_path_count = equal_path_count + 1
            #base case: remove path1 from total_path list
        mod_equivalent_paths_dict.update({mod : temp_path_dict})
    #print '2G. check_equivalent_RNA_MODOMICS_paths'
    return mod_equivalent_paths_dict

#confirms the above checker gives same result regardless of enzyme/metabolite/carrier checking 


#this checks that paths are equivalent in both enzymes and metabolites~~~!!!!
#import copy
#modification_network = import_tRNA_network_for_enzyme_sweeps('TrmU_mono')
#rna_type = 'tRNA'
#check_paths_enzymes = copy.deepcopy(check_equivalent_RNA_MODOMICS_paths(modification_network, rna_type,'enzymes'))
#check_paths_metabolites = copy.deepcopy(check_equivalent_RNA_MODOMICS_paths(modification_network, rna_type,'metabolites'))

def enzyme_metabolite_agreement_checker(modification_network, rna_type, check_paths_enzymes, check_paths_metabolites):
    """
    description: 
        checks to see if path metabolite/enzyme info in checkers assign the same equivalent paths (they should)
    input:
        check_equivalent_RNA_MODOMICS_paths(rna_type,'enzymes') : equivalent paths dict
        check_equivalent_RNA_MODOMICS_paths(rna_type,'metabolites'): equivalent paths dict
        user: 'tRNA' or 'rRNA'
    output: 
        prints failure rate
    """
        
    print '\n','\n', 'checking metabolites and enzymes'
    count = 0
    checker_works_list = []
    for modification in check_paths_enzymes.keys():
        equi_metabolites = check_paths_metabolites[modification]
        equi_enzymes = check_paths_enzymes[modification]
        #equi_carriers = check_equivalent_RNA_MODOMICS_paths(path_dict, 'carriers')[modification]
    
        if equi_metabolites != equi_enzymes:
            count = count + 1
            print 'fail : %s ' %(modification)
            print  'metabolite check : ','\t',equi_metabolites
            print 'enzyme check : ' , '\t', equi_enzymes
            print path_dict[modification],'\n'
        else:
            checker_works_list.append(modification), '\t',
    print '\t' ,'\t' , 'Checker failed %i times' %(count)

#enzyme_metabolite_agreement_checker(modification_network, 'tRNA', check_paths_enzymes, check_paths_metabolites )


# # 3. RNA BNUM SUBSTRATES
# 

# ##  3A : creating master pandas dataframe from substrate details
#creates pandas DF with all bnum | modification | nucleotide | position data
#uses reaction details substrate information to create data frame


#get_RNA_modification_reaction_details(modification_network, rna_type)['Uridine_mods_paths'].keys()









#this code creates a DF where all trna bnumbers are listed as substrates of various modifications
#uses input data from manually currated modifications ( MODS_Adenine, MODS_Cytidine, MODS_Guanine , MODS_Queuosine, MODS_URIDINE_2)

def create_RNA_dataframe_from_substrates(modification_network, rna_type):
    """
    description:
        creates a master DF with bnum/modifications/positions from the master details dictionary
    input:
        get_RNA_modification_reaction_details(modification_network, rna_type) : substrate data for RNA modifications
    output: 
       dataframe     
    """
    import copy
    total_RNA_modification_details = copy.deepcopy(get_RNA_modification_reaction_details(modification_network, rna_type))
    
    df = pd.DataFrame()
    index = 0
    base_list = {'Uridine_mods_paths' : 'T', 'Adenine_mods_paths' : 'A',  'Guanine_mods_paths' : 'G', 'Cytidine_mods_paths':'C'}
      
    for base in base_list.keys():
        nucleotide = base_list[base]
        
        if base in total_RNA_modification_details.keys():

            for mod in total_RNA_modification_details.get(base).keys():
                mod_input = total_RNA_modification_details.get(base).get(mod).get('input')
                for machines in total_RNA_modification_details.get(base).get(mod).get('machines'):
                    RNA_position_substrates = total_RNA_modification_details.get(base).get(mod).get('machines')[machines].get('RNA_position_substrates')
                    for rna in RNA_position_substrates.keys():
                        #filters each sub reaction to see if it acts on RNA type
                        #now will be assigning substrates to DF
                        if rna == rna_type:
                            for position in RNA_position_substrates.get(rna):
                                substrates = RNA_position_substrates.get(rna)[position]


                                if 'all' in substrates.keys() and mod_input != base[0]:
                                    # this block assigns the proper substrates if downstream reaction is all substrates
                                    # and the input isnt a nucleotide                          
                                    while 'all' in substrates.keys() and mod_input != base[0] :  

                                        for mod_upstream in total_RNA_modification_details.get(base).keys():
                                            mod_upstream_output = total_RNA_modification_details.get(base).get(mod_upstream).get('output')

                                            if mod_upstream_output == mod_input: #find upstream reaction


                                                for machines in total_RNA_modification_details.get(base).get(mod_upstream).get('machines'):
                                                    RNA_position_substrates = total_RNA_modification_details.get(base).get(mod_upstream).get('machines')[machines].get('RNA_position_substrates')
                                                    #print '\t',  RNA_position_substrates

                                                    for rna in RNA_position_substrates.keys():
                                                        if rna =='tRNA':
                                                            for position in RNA_position_substrates.get(rna):
                                                                substrates_upstream = RNA_position_substrates.get(rna)[position]
                                                                substrates = substrates_upstream #equate old substrates to upstream substrate
                                                mod_input = total_RNA_modification_details.get(base).get(mod_upstream).get('input')
                                    #no restrictions on any upstream rxn:
                                    if 'all' in substrates.keys():
                                        mod_bnum = copy.deepcopy(substrates.keys())
                                        mod_bnum.remove('all')
                                        all_trna_bnum = trna_bnum_anticodon_start_position_dict.keys()
                                        #this if statement removes tRNAs with '0' as their value from being added
                                        # it is the restricted substrates (U_to_D, and others)
                                        if len(mod_bnum) > 0:
                                            for bnum in mod_bnum:
                                                all_trna_bnum.remove(bnum)
                                        for all_bnum in all_trna_bnum:
                                            df.loc[index, 'bnum'] = all_bnum
                                            df.loc[index, 'nucleotide'] = nucleotide
                                            df.loc[index, 'position'] = position
                                            df.loc[index, 'modification'] = mod
                                            df.loc[index, 'restriction'] = 'this is a substrate'
                                            index = index + 1
                                    else:
                                        #add substrates to DF                   
                                        for bnum in substrates.keys():
                                            df.loc[index, 'bnum'] = bnum
                                            df.loc[index, 'nucleotide'] = nucleotide
                                            df.loc[index, 'position'] = position
                                            df.loc[index, 'modification'] = mod
                                            if substrates[bnum] == 1:
                                                df.loc[index, 'restriction'] = 'this is a substrate'
                                                index = index + 1
                                            elif substrates[bnum] == 0: 
                                                df.loc[index, 'restriction'] = 'this is NOT a substrate'
                                                index = index + 1

                                else:

                                    if 'all' in substrates.keys(): 
                                        #these are the 'all' reactions with nucleotide inputs
                                        mod_bnum = copy.deepcopy(substrates.keys())
                                        mod_bnum.remove('all')
                                        all_trna_bnum = trna_bnum_anticodon_start_position_dict.keys()
                                        #this if statement removes tRNAs with '0' as their value from being added
                                        # it is the restricted substrates (U_to_D, and others)
                                        if len(mod_bnum) > 0:
                                            for bnum in mod_bnum:
                                                all_trna_bnum.remove(bnum)
                                        for all_bnum in all_trna_bnum:
                                            df.loc[index, 'bnum'] = all_bnum
                                            df.loc[index, 'nucleotide'] = nucleotide
                                            df.loc[index, 'position'] = position
                                            df.loc[index, 'modification'] = mod
                                            df.loc[index, 'restriction'] = 'this is a substrate'
                                            index = index + 1
                                    else: 
                                        #these are the reactions with restrictions on substrates
                                        for bnum in substrates.keys():
                                            df.loc[index, 'bnum'] = bnum
                                            df.loc[index, 'nucleotide'] = nucleotide
                                            df.loc[index, 'position'] = position
                                            df.loc[index, 'modification'] = mod
                                            if substrates[bnum] == 1:
                                                df.loc[index, 'restriction'] = 'this is a substrate'
                                                index = index + 1
                                            elif substrates[bnum] == 0: 
                                                df.loc[index, 'restriction'] = 'this is NOT a substrate'
                                                index = index + 1
    print '3A.  create_RNA_dataframe_from_substrates'

    return df




#create_RNA_dataframe_from_substrates(modification_network, rna_type)

#modification_network = import_tRNA_network_for_enzyme_sweeps('TrmU_mono')
#modification_network
#rna_type = 'tRNA'
#print network
#add_enzymes_to_rna_paths(modification_network , 'tRNA')
#fix_path_count_for_multple_enzymes(modification_network, rna_type)
#add_metabolites_to_rna_paths(modification_network, rna_type)
# ## 3B : Sequence allighment check 
# 
#adjusts dataframe to ensure sequence allignment







#this script uses TRNA sequence to check the manually created DF for trna substrates that cannot work!!!
#deletes 600 substrates (mainly the ones that use 'ALL' as restriction)

def check_RNA_substrate_with_sequences_adjust_D_loop_mods(modification_network, rna_type):
    """
    description: takes the master DF and checks each substrate/modification row with sequence agreement
    input: create_RNA_dataframe_from_substrates(modification_network, rna_type) --> master DF
    output: corrected DF with removed rows for sequence mismatch
    """
    with open('../9_30_2016_prototype_59_tRNA_sequences.pickle','rb') as infile:
        me = cPickle.load(infile)
        
    df = create_RNA_dataframe_from_substrates(modification_network, rna_type)
    if 'bnum' not in df.columns:
        return df
    
    base_list = {'Uridine' : 'T', 'Adenine' : 'A',  'Guanine' : 'G', 'Cytidine':'C'}
    #note ^ : sequences are given with 'T', not 'U'
    d_loop = { 17: 0,
              '17A': 1,
              18 : 2,
              19: 3,
              20 : 4,
              '20A' : 5,
              '20B': 6 }
    v_loop = {46 : -2, 
              47 : -1}

    for base in base_list.keys():
        print 'sequence checking DF for %s modifications' %(base)
        nucleotide = base_list[base]
        for trna in me.tRNA_data:
            bnum = trna.id.split('_')[1]
            if bnum in list(df.bnum):
                for index, row in df.iterrows():
                    if bnum == row.bnum and row.nucleotide == nucleotide and row.restriction == 'this is a substrate':
                        #this will check eveything but D-loop/V-loop @ 17A, 20A, 20B
                        if type(row.position) != str:
                            #pre-Dloop ( 0-16 )
                            if row.position <= 16:
                                seq = trna.trna_sequence_position_0_to_16
                                if seq[int(row.position)] != nucleotide:
                                    df.loc[index, 'sequence_check'] = 'fail'
                            #Dloop (17,18,19,20)
                            elif row.position >= 17 and row.position <= 20:
                                seq = trna.trna_sequence_position_17_20_Dloop
                                position_d_loop = d_loop[row.position]
                                seq = trna.trna_sequence_position_17_20_Dloop
                                if seq[position_d_loop] != nucleotide:
                                    df.loc[index, 'sequence_check'] = 'fail'
                            #Anticodon Region (21 - 45)
                            elif row.position >= 21 and row.position <= 45:
                                seq = trna.trna_sequence_position_21_to_45
                                if seq[int(row.position) - 21] != nucleotide:
                                    df.loc[index, 'sequence_check'] = 'fail'
                            #V-loop (46 - 47)
                            elif row.position >= 46 and row.position <= 47:
                                seq = trna.trna_sequence_position_46_47_Vloop
                                position_v_loop = v_loop[row.position]
                                if seq[position_v_loop] != nucleotide:
                                    df.loc[index, 'sequence_check'] = 'fail'
                            #CCA-end region (47-76)
                            elif row.position > 47:
                                seq = trna.trna_sequence_position_48_to_76
                                if seq[int(row.position) - 48] != nucleotide:
                                    df.loc[index, 'sequence_check'] = 'fail'   
                        #D-loop (17A, 20A, 20B)
                        elif type(row.position) == str:
                            position_d_loop = d_loop[row.position]
                            seq = trna.trna_sequence_position_17_20_Dloop
                            if seq[position_d_loop] != nucleotide:
                                df.loc[index, 'sequence_check'] = 'fail'


    print '\t' ,'\t' , 'DF length orginal : %i' %(len(df))      
    if 'sequence_check' in df.columns:
        df  = df[df.sequence_check != 'fail']
        df = df.reset_index()
        del df['index']
    print '\t' ,'\t' , 'DF length after sequence allignment : %i' %(len(df))
    #print   '3B. check_RNA_substrate_with_sequences_adjust_D_loop_mods'
    return df
#df = check_RNA_substrate_with_sequences_adjust_D_loop_mods(modification_network, 'tRNA')


# ## 3C : bnum modification dictionary 
#creates substrate modification dictionary from DF




def create_RNA_bnum_modification_dict(modification_network, rna_type):
    """
    description: 
        creates a modification dictionary with all sub_modifications available for each tRNA and position data
        
    input: 
        check_RNA_substrate_with_sequences_adjust_D_loop_mods(modification_network, rna_type) : corrected DF
        
    output: dictionary
        tRNA_bnum : {sub modification : [position list]}
    """
    bnum_mods = {}
    df = check_RNA_substrate_with_sequences_adjust_D_loop_mods(modification_network, rna_type)
    if 'bnum' not in df.columns:
        return bnum_mods
    for trna in trna_bnum_anticodon_start_position_dict.keys():
        modification_position = {}
        for index, row in df.iterrows():
            if row.bnum == trna and row.restriction == 'this is a substrate':
                positions = row.position
                old_positions = ''
                #if modification can occur at multiple positions, append to list
                if row.modification in list(modification_position.keys()):
                    old_positions = modification_position.pop(row.modification)
                    new_position = row.position
                    if type(old_positions) != list :
                        positions = [str(old_positions)]
                    else: 
                        positions = old_positions
                    positions.append(str(new_position))
                modification_position.update({row.modification: positions})
        bnum_mods.update({trna : modification_position})
   
    #adjust int -- > string in bnum_mods:
    for bnum in bnum_mods:
        for mod in bnum_mods.get(bnum):
            position_data  = bnum_mods.get(bnum).get(mod)
            #convert all positions to list [positions]
            if type(position_data) != list:
                position_data = [position_data]
            for single_position in position_data:
                if single_position != '20A':
                    single_position_string =  str(int(float(single_position)))
                    position_data.remove(single_position)
                    position_data.append(single_position_string)
            bnum_mods[bnum][mod] = position_data
    #conversion needed again?
    for bnum in bnum_mods:
        for mod in bnum_mods.get(bnum):
            position_data  = bnum_mods.get(bnum).get(mod)
            if type(position_data) != list:
                position_data = [position_data]
            for single_position in position_data:
                if single_position != '20A':
                    single_position_string =  str(int(float(single_position)))
                    position_data.remove(single_position)
                    position_data.append(single_position_string)
            bnum_mods[bnum][mod] = position_data
    #print '3C. create_RNA_bnum_modification_dict' 
    return bnum_mods
#create_RNA_bnum_modification_dict(modification_network, 'tRNA')

#adjust modification dictionary (above) to reflect true adenine modifications.
#modomics data (substrate = all) creates initial problems


#correct adenine modifications with proper priority and additional sequence rules

def adjust_adenine_RNA_mods(modification_network, rna_type):
    """
    description: 
        using restrictions in rna_mod details dict from ecocyc/modomics, some tRNA bnums are substrates for 
        multiple modifications at the same position. here, we use additional rules for adenine mods @ 37 / cytidine mods @34
        we adjust the modification dict accordingly
    input:
        create_RNA_bnum_modification_dict(modification_network, rna_type): modification dict
    output: 
        adjusted modification dict
    """
    # 1| A_to_m6A : 37A @ val/VAC only  
    # 2| A_to_i6A :  most tRNAs with 36A37A
    # 3| A_to_t6A : tRNAs with 34N35N36U37A (NNUA) (ile, met, thr, asn, lys, ser, arg)
    # 4| A_to_m2A : all the rest
    
    import copy
    correction_dict = copy.deepcopy(create_RNA_bnum_modification_dict(modification_network, rna_type))
    
    if correction_dict == {}:
        return correction_dict
    
    for bnum in correction_dict.keys():
        count = 0
        A_mods =['A_to_m6A', 'A_to_i6A', 'A_to_t6A','A_to_m2A']
        for A_mod in A_mods:
            if A_mod in correction_dict[bnum].keys():
                count = count + 1

        if count > 1:
            # m6A priority #1
            if 'A_to_m6A' in correction_dict[bnum].keys():
                A_mod_correct = A_mods
                A_mod_correct.remove('A_to_m6A')
                for A_mod in A_mod_correct:
                    if A_mod in correction_dict[bnum].keys():
                        del correction_dict[bnum][A_mod] #removes the additional A_mods
            else:
                for trna in me.tRNA_data.query(bnum):
                    sequence_34_37 = trna.trna_sequence_position_21_to_45[34 - 21:38-21]
                    sequence_36_37 = trna.trna_sequence_position_21_to_45[36 - 21:38-21]

                #i6A priority #2
                if sequence_36_37 == 'AA':
                    A_mod_correct = A_mods
                    A_mod_correct.remove('A_to_i6A')
                    for A_mod in A_mod_correct:
                        if A_mod in correction_dict[bnum].keys():
                            del correction_dict[bnum][A_mod]

                elif sequence_36_37 != 'AA':
                    #t6A priority #3
                    if 'T' == sequence_34_37[2]:
                        A_mod_correct = A_mods
                        A_mod_correct.remove('A_to_t6A')
                        for A_mod in A_mod_correct:
                            if A_mod in correction_dict[bnum].keys():
                                del correction_dict[bnum][A_mod]
                    #m2A priority #4
                    else:
                        A_mod_correct = A_mods
                        A_mod_correct.remove('A_to_m2A')
                        for A_mod in A_mod_correct:
                            if A_mod in correction_dict[bnum].keys():
                                del correction_dict[bnum][A_mod]
    #print '3C. adjust_adenine_RNA_mods'
    return correction_dict

#adjust_adenine_RNA_mods('tRNA')                            
        
#Cytidine
#should be no conflicts
#mods @ 32 have different substrates
# C_to_Cm : Leu / BAA
# C_to_k2C : ile/ CAU
# C_to_ac4C : fmet -- ecocyc!!

#function that:
#reduces SUB reactions in modification dictionary to include total reactions 
#instead replaces sub reactions with total modifications 


def reduce_subRXNs_to_totalRXNS(graph, modification_network):
    """
    description:
        takes adjusted modification dict and all the sub reaction and finds the total reactions for each bnum
        keeps track of all sub reactions that were removed from bnum mod dict
        this function is called later while looping through each tRNA bnum
    input: bnum_modification dict (for each bnum)
    output: reduced paths
        input of {bnum : sub_rxn [position]} ---> outputs { bnum : total-mod [position] }
    """
    import copy
    total_tRNA_products = copy.deepcopy(get_RNA_modification_products(modification_network , 'tRNA'))
    
    remove_list = []
    new_rxn_list = []
    base_dict = {'G':'Guanine', 'C':'Cytidine', 'A':'Adenine', 'U':'Uridine'}
    total_rxns = graph.keys()
    
    for rxn_1 in graph.keys():
        rxn_1_input = rxn_1.split('_')[0]
        rxn_1_output = rxn_1.split('_')[2]
        for rxn_2 in graph.keys():
            rxn_2_input = rxn_2.split('_')[0]
            rxn_2_output = rxn_2.split('_')[2]
            if rxn_1_output == rxn_2_input and graph[rxn_1] == graph[rxn_2] and rxn_1 not in remove_list:
                remove_list.append(rxn_1) #we know that rxn 1 is a upstream rxn      
    for rxn_1 in remove_list:
        del graph[rxn_1]   
    graph.update({'total_sub_rxns' : remove_list})
    remove_list = []
    do_not_remove_list = []
    temp_graph ={}
    
    #reduces redundant sub_rxns that lead to final mod
    for rxn in graph.keys():
        rxn_output = rxn.split('_')[2]
        for rxn_2 in graph.keys():
            rxn_2_output = rxn_2.split('_')[2]
            
            if rxn_output == rxn_2_output and rxn != 'total_sub_rxns' and rxn_2 != 'total_sub_rxns' and graph[rxn] == graph[rxn_2] and rxn != rxn_2:
                if rxn not in remove_list:
                    remove_list.append(rxn)
                if rxn_2 not in remove_list:
                    remove_list.append(rxn_2)
                
                new_rxn_output = rxn_output
                net_rxn_input = total_tRNA_products[new_rxn_output]
                new_rxn_name = net_rxn_input + '_to_' + new_rxn_output
                position = graph[rxn]
                temp_graph.update({new_rxn_name : position })
                                  
    for rxn_1 in remove_list:
        del graph[rxn_1]
    graph['total_sub_rxns'] = graph['total_sub_rxns'] + remove_list   
    remove_list = []
    
    for rxn in graph.keys():
        if rxn != 'total_sub_rxns':
            rxn_input = rxn.split('_')[0]
            if rxn_input in base_dict.keys():
                do_not_remove_list.append(rxn)
            else:
                remove_list.append(rxn)
                rxn_output = rxn.split('_')[2]
                total_input = total_tRNA_products[rxn_output]
                new_rxn = total_input + '_to_' + rxn_output
                position = graph[rxn]
                temp_graph.update({new_rxn : position })
 
    for rxn_1 in remove_list:
        del graph[rxn_1]
    graph['total_sub_rxns'] = graph['total_sub_rxns'] + remove_list  
    
    for new_rxn in temp_graph.keys():
        graph.update({new_rxn : temp_graph[new_rxn]})
        
    graph['total_sub_rxns'] = graph['total_sub_rxns'] + do_not_remove_list    
    return graph
                
#new_graph = copy.deepcopy(reduce_subRXNs_to_totalRXNS(graph))
#print len(new_graph['total_sub_rxns'])
#new_graph                

#calls previous function
#for every bnum in modification dictionary, reduce_subRXNs_to_totalRXNS runs
#turns sub reactions into total modifications


def create_final_bnum_modification_dict(modification_network, rna_type):
    """
    description: 
        calls reduce_subRXNs_to_totalRXNS to reduce the bnum modification dict to total reactions and keeps track
        of deleted sub-rxns
    input:
        adjust_adenine_RNA_mods(modification_network, rna_type) : bnum modification dictionary
    output: 
        bnum modification dict with total modifications rather than sub_rxns
    """
    import copy
    final_substrate_modification_dict = copy.deepcopy(adjust_adenine_RNA_mods(modification_network, rna_type))
    if final_substrate_modification_dict == {}:
        return final_substrate_modification_dict
    
    
    for bnum in final_substrate_modification_dict:
        graph = final_substrate_modification_dict[bnum]
        graph = reduce_subRXNs_to_totalRXNS(graph, modification_network)
        final_substrate_modification_dict.update({bnum : graph})
    print '3C. create_final_bnum_modification_dict'
    return final_substrate_modification_dict


# ##  3C : Result! 
# ### OUTPUT: each bnum : 'total modifications' : [@position], 'total sub modifications'}
#import copy
#final_substrate_modification_dict = copy.deepcopy(create_final_bnum_modification_dict('tRNA'))
#final_substrate_modification_dict
# # 4. Combining Mododomics Network Paths (2.) & Bnum Substrates  (3.) 

# ## 4A : code
#adds all paths to modification substrate dictionary
#bnum / 'total mod' : [ all available paths based on substrate details for sub reactions ] 


def add_MODOMICS_path_numbers_to_bnum_modification_dict(modification_network, rna_type):
    """
    description:
        identifies which modomics paths are present in the modification reactions for the bnum modification dict
    input:
        add_carriers_to_rna_paths(modification_network, rna_type) : modomics network path with enzymes, carriers, and metabolite details
    output: 
        bnum : {total_mod : [paths available to the bnum substrate]}  
    """
    import copy
    temp_dict_4_final = copy.deepcopy(add_carriers_to_rna_paths(modification_network, rna_type))
    final_substrate_modification_dict = copy.deepcopy(create_final_bnum_modification_dict(modification_network, 'tRNA'))
   
    
    bnum_temp_dict = {}
    if final_substrate_modification_dict =={}:
        return bnum_temp_dict
    
    for bnum in final_substrate_modification_dict:
        temp_dict = {}
        for total_mod in temp_dict_4_final:
            path_list = []

            if total_mod in final_substrate_modification_dict[bnum].keys():
                for path_number in temp_dict_4_final[total_mod]:
                    #check that the positions are aligned
                    path_position = temp_dict_4_final[total_mod][path_number]['position']
                    modification_postion = final_substrate_modification_dict[bnum][total_mod]

                    for mod_position in modification_postion:
                        if mod_position == str(path_position):
                            path_rxns = temp_dict_4_final[total_mod][path_number].get('total_path_rxns')
                            count = 0

                            for sub_rxn in path_rxns:
                                if sub_rxn in final_substrate_modification_dict[bnum]['total_sub_rxns']:
                                    count += 1
                            if count == len(path_rxns):
                                path_list.append(path_number)
            temp_dict.update({total_mod : path_list})
            remove_list = []
            for total_mod in temp_dict.keys():
                if len(temp_dict[total_mod]) == 0 :
                    remove_list.append(total_mod)
            for total_mod in remove_list:
                del temp_dict[total_mod]
        bnum_temp_dict.update({bnum : temp_dict})
    #print '4A. add_MODOMICS_path_numbers_to_bnum_modification_dict'
    return bnum_temp_dict

#uses equivalent path checker to determine if paths are redunant, substitutes individual paths for 'equivalent path #' 



def add_equivalent_paths_to_bnum_modification_dict(modification_network, rna_type, enzymes_or_metabolites):
    """
    description: converts the bnum modification dictionary path list -- > equivalent path list
        
    input: 
        add_MODOMICS_path_numbers_to_bnum_modification_dict(modification_network, rna_type) : 
        check_equivalent_RNA_MODOMICS_paths(rna_type, enzymes_or_metabolites) : checks equivalent paths
        
    output: 
     { bnum : { 'total_mod' : [equal path names] } } 
    """
    import copy
    mod_equivalent_paths = copy.deepcopy(check_equivalent_RNA_MODOMICS_paths(modification_network,rna_type, enzymes_or_metabolites))
    bnum_temp_dict_2 = copy.deepcopy(add_MODOMICS_path_numbers_to_bnum_modification_dict(modification_network, rna_type))
    if bnum_temp_dict_2 == {}:
        return bnum_temp_dict_2
    
    
    for bnum in bnum_temp_dict_2:
        for total_mod in mod_equivalent_paths:
            if total_mod in bnum_temp_dict_2[bnum].keys():

                for equal_path, path_list in mod_equivalent_paths[total_mod].iteritems():
                    for path_number in path_list:
                        if path_number in bnum_temp_dict_2[bnum][total_mod]:
                            if equal_path not in bnum_temp_dict_2[bnum][total_mod]:
                                bnum_temp_dict_2[bnum][total_mod] += [equal_path]
                            bnum_temp_dict_2[bnum][total_mod].remove(path_number)
    return bnum_temp_dict_2


# # 5. Collect all results













#import copy
#bnum modifications
#equal_paths_definitions = copy.deepcopy(check_equivalent_RNA_MODOMICS_paths(modification_network, 'tRNA','enzymes'))
#equal paths definitions




#equal_paths_definitions




#sub_path_details = copy.deepcopy(add_carriers_to_rna_paths(modification_network,'tRNA'))




#sub_path_details




#bnum_modification_dict = copy.deepcopy(add_equivalent_paths_to_bnum_modification_dict(modification_network, 'tRNA' , 'metabolites'))




#bnum_modification_dict







# # 6. Converting results into useable inputs



def build_trna_charging_AND_post_transcriptional_modification_of_tRNA(bnum_modification_dict , equal_paths_definitions, sub_path_details  ):
    """
    description : builds the post_transcriptional_modification_of_tRNA.txt file required for ME 2.0
    inputs : 
        bnum_modification_dict -->  {bnum : total_mod : [equal paths list]}
        equal_paths_definitions --> {total_mod : equal_path : [path#s list]}
        sub_path_details --> {total_mod : path# : path_details}
    output:
        saves the post_transcriptional_modification_of_tRNA.txt file
        returns the df ^
    """
    
    df_trna_substrates = pd.DataFrame()
    index = 0
    tRNA_charging = {}

    
    if bnum_modification_dict == {}:
        return tRNA_charging , df_trna_substrates
    
    for bnum in bnum_modification_dict:
        for total_mod in bnum_modification_dict[bnum]:
            for equal_path in bnum_modification_dict[bnum][total_mod]:
                #simply rename the equal path the first [path#] according to the definitions
                path_generic = equal_paths_definitions[total_mod][equal_path][0]
                df_trna_substrates.loc[index, 'bnum'] = bnum
                df_trna_substrates.loc[index, 'tRNA_total_mod'] = total_mod
                df_trna_substrates.loc[index, 'equal_path'] = path_generic
                #use sub_path_details to find position
                position = sub_path_details[total_mod][path_generic]['position']
                if position != '20A':
                    position = str(int(float(position)))
                df_trna_substrates.loc[index, 'position'] = position
                modification = total_mod.split('_')[2]
                df_trna_substrates.loc[index, 'modification'] = modification
                index = index + 1
                
    tRNA_charging = {}
    #print 'Building tRNA_charging.py'
    for index, row in df_trna_substrates.iterrows():
        temp_dict = {}
        position = row.position
        modification = row.modification
        mod_name = modification
        searchable_mod = row.tRNA_total_mod
        path = row.equal_path
        mod_name_w_path = mod_name + '_' + path
        mod_name_w_path = mod_name_w_path + '_at_' + str(position)
        
        #print mod_name_w_path, searchable_mod
        enzymes = sub_path_details[searchable_mod][path]['enzymes']
        #print searchable_mod, enzymes
        metabolites = sub_path_details[searchable_mod][path]['metabolites']
      
        carriers = sub_path_details[searchable_mod][path]['carriers']
        #print searchable_mod, carriers
        enzyme_list = []
        for enzyme in enzymes.keys():
            enzyme_stoich = enzymes[enzyme]
            i = 1
            while i <= enzyme_stoich:
                enzyme_list.append(enzyme)
                i = i + 1
        for enzyme in enzyme_list:    
            if 'enzyme_unknown' in enzyme:
                enzyme_list.remove(enzyme)
        if carriers == None:
            carriers = {}
        temp_dict['machines'] = enzyme_list
        temp_dict['metabolites'] = metabolites
        temp_dict['carriers'] = carriers
        tRNA_charging.update({mod_name_w_path: temp_dict})
    #print '5A. build_trna_charging_AND_post_transcriptional_modification_of_tRNA'
    return tRNA_charging, df_trna_substrates




#[trna_charging, df_trna_substrates] = build_trna_charging_AND_post_transcriptional_modification_of_tRNA(bnum_modification_dict , equal_paths_definitions, sub_path_details )



# In[63]:

def save_trna_charging_dictionary_or_post_transciptional_files(input_file, tRNA_enzyme):
    import json
    
    if type(input_file) == dict:
        trna_charging_path = 'modified_trna_charging_dict_json_files/'
        save_file_name = 'tRNA_charging_' +'removed_' + str(tRNA_enzyme) + '.json'
        with open(trna_charging_path + save_file_name, 'w') as f:
            json.dump(input_file, f)
            
    else: 
        #saves the file in correct format!
        path = 'modified_post_transcriptional_modification_of_tRNA_csv_files/'
        save_file_name = 'post_transcriptional_modification_of_tRNA_' + 'removed_' + str(tRNA_enzyme) + '.txt'
        input_file.to_csv(path + save_file_name,  sep =  '\t', index = False)
    print 'saved %s ' % (save_file_name)
    
    
    return

def save_trna_charging_dictionary_or_post_transciptional_files_positve_sweeps(input_file, tRNA_enzyme):
    import json
    
    if type(input_file) == dict:
        trna_charging_path = 'modified_trna_charging_dict_json_files/positive_enzyme_sweeps/'
        save_file_name = 'tRNA_charging_' +'ONLY_' + str(tRNA_enzyme) + '.json'
        with open(trna_charging_path + save_file_name, 'w') as f:
            json.dump(input_file, f)
            
    else:
        
        if 'bnum' not in input_file.columns:
       
            input_file = pd.DataFrame(columns = ['bnum', 'tRNA_total_mod','equal_path','position','modification'])
        
        
        #saves the file in correct format!
        path = 'modified_post_transcriptional_modification_of_tRNA_csv_files/positive_enzyme_sweeps/'
        save_file_name = 'post_transcriptional_modification_of_tRNA_' + 'ONLY_' + str(tRNA_enzyme) + '.txt'
        input_file.to_csv(path + save_file_name,  sep =  '\t', index = False)
    print 'saved %s ' % (save_file_name)
    
    
    return

