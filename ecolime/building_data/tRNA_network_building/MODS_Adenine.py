# carriers [ ] 
# substrates [ x ] 
adenine_mods = {'A_to_m2A' : {'name' : '2-methyladenosine',
                                  'input' : 'A',
                                  'output' : 'm2A',
                                  'machines' : {'RlmN_mono_mod_1:4fe4s' : {'proteins' : {'b2517' : 'RlmN'},
                                                                           'RNA_position_substrates' :{'tRNA' : {37 : {'all' : 1}},
                                                                                                       'rRNA' : {2503 : {'LSU/23S/prokaryotic' : 1}}
                                                                                                      },
                                                                           'carriers' : None
                                                                          },
                                               },
                              
                                               
                                  'metabolites' : {'amet_c' : -2,
                                                  #reduced 2Fe-2S ferredoxin : -2
                                                  'ahcys_c' : 1,
                                                  'met__L_c' : 1,
                                                  'dad__5_c' : 1}
                                                  #oxidized 2Fe-2S ferredoxin : 2}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'A_to_m6A' : {'name' : 'N6-methyladenosine',
                                  'input' : 'A',
                                  'output' : 'm6A',
                                  'machines' : {'enzyme_new_ErmBC' : {'proteins' : {'bnum' : 'ErmBC'},
                                                            #important : not found
                                                            'RNA_position_substrates' : {'rRNA' : {2058 : {'LSU/23S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None
                                                           },
                                                'RlmF_mono' : {'proteins' : {'b0807' : 'RlmF'},
                                                            'RNA_position_substrates' :{'rRNA' :  {1618 : {'LSU/23S/prokaryotic cytosol' : 1}}},
                                                            'carriers' :None
                                                           },
                                                'RlmJ_MONOMER' : {'proteins' : {'b3499' : 'RlmJ'},
                                                            #important : not ni model
                                                            'RNA_position_substrates' :{'rRNA' :  {2030 : {'LSU/23S/prokaryotic cytosol' : 1}}},
                                                            'carriers' :None
                                                           },
                                                'KsgA_mono' : {'proteins' : {'b0051' : 'RmsA'},
                                                            'RNA_position_substrates' : {'rRNA' : {1518 : {'SSU/16S/prokaryotic cytosol' : 1},
                                                                                        1519 : {'SSU/16S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None
                                                           },
                                                'YfiC_mono' : {'proteins' : {'b2575' : 'TrmM'},
                                                            'RNA_position_substrates' : {'tRNA' : {37 : { 'b0744' : 1, #trna valT (UAC)  #cmo5U
                                                                                               'b2401' : 1, #trna valU (UAC) #cmo5U
                                                                                               'b2402' : 1, #trna valX (UAC) #cmo5U
                                                                                               'b2403' : 1, #trna valY (UAC) #cmo5U
                                                                                               'b0746' : 1}}}, #trna valZ (UAC) #cmo5U
                                                            'carriers' :None
                                                            }
                                               },
                                  'metabolites' : {'amet_c' : -1,
                                                  'ahcys_c' : 1,
                                                  'h_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'm6A_to_m66A' : {'name' : 'N6,N6-dimethyladenosine',
                                  'input' : 'm6A',
                                  'output' : 'm66A',
                                  'machines' : {'KsgA_mono' : {'proteins' : {'b0051' : 'RmsA'},
                                                            'RNA_position_substrates' : {'rRNA' : {1518 : {'SSU/16S/prokaryotic cytosol' : 1},
                                                                                        1519 : {'SSU/16S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'amet_c' : -1,
                                                  'ahcys_c' : 1,
                                                  'h_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'A_to_I' : {'name' : 'inosine',
                                  'input' : 'A',
                                  'output' : 'I',
                                  'machines' : {'TadA_dim_mod_2:zn2' : {'proteins' : {'b2559' : 'TadA'},
                                                            'RNA_position_substrates' : {'tRNA' : {34 : {'b2692' : 1 , # trna ArgZ (ACG) #inosine
                                                                                               'b2691' : 1 ,#trna ArgQ (ACG) #inosine
                                                                                               'b2694' : 1 ,#trna ArgV (ACG) #inosine
                                                                                               'b2693' : 1 }}},#trna ArgY (ACG) #inosine
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'h_c' : -1,
                                                  'h2o_c' : -1,
                                                  'nh4_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'A_to_m1A' : {'name' : '1-methyladenosine',
                                  'input' : 'A',
                                  'output' : 'm1A',
                                  'machines' : {'enzyme_new_NpmA' : {'proteins' : {'bnum' : 'NpmA'},
                                                            #important: not found
                                                            'RNA_position_substrates' : {'rRNA' : {1408 : {'SSU/16S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {}
                                 }, 
    ###################################end##############################################
    ####################################################################################

                 'A_to_i6A' : {'name' : 'N6-isopentenyladenosine',
                                  'input' : 'A',
                                  'output' : 'i6A',
                                  'machines' : {'MiaA_dim_mod_2:mg2' : {'proteins' : {'b4171' : 'MiaA'},
                                                            'RNA_position_substrates' : {'tRNA' : {37 : {'all' : 1}}},
                                                                        'restrictions' : {37 : 'A',
                                                                                          36 : 'A'},
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'dmpp_c' : 1,
                                                  'ppi_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'i6A_to_ms2i6A' : {'name' : '2-methylthio-N6-isopentenyladenosine',
                                  'input' : 'i6A',
                                  'output' : 'ms2i6A',
                                  'machines' : {'MiaB_mono_mod_1:4fe4s' : {'proteins' : {'b0661' : 'MiaB'},
                                                            'RNA_position_substrates' : {'tRNA' : {37 : {'b1910' : 1 , #trna cysT (GCA)
                                                                                               'b1909' : 1, #trna leuZ (UAA)
                                                                                              'b2967' : 1, #trna pheV (GAA)
                                                                                               'b4134' : 1, #trna pheU (GAA)
                                                                                               'b0971' : 1 , #trna serT (UGA)
                                                                                               'b1975' : 1 , #trna serU (CGA)
                                                                                              'b3761' : 1, #trna trpT (CCA)
                                                                                               'b1230' : 1 , #trna tyrV (GUA)
                                                                                                'b3977' : 1 , #trna tyrU (GUA)
                                                                                                'b1231' : 1}} #trna tyrT (GUA)
                                                                                        },
                                                            'carriers' :  {
                  'IscS_mod_2:pydx5p_mod_1:SH': -1,
                  'IscS_mod_2:pydx5p': 1,
                  'fldrd_c': -1,
                  'fldox_c': 1 }
                                                                          }
                                               },
                                  'metabolites' : {'amet_c' : -2,
                                                  #sulfur carrier : -1,
                                                  #reduced electron acceptor : -1,
                                                  'ahcys_c' : 1,
                                                  #unsulfurated sulfur carrier : 1,
                                                  'met__L_c' : 1,
                                                  'dad__5_c' : 1,
                                                  #oxidized electron acceptor : 1
                                                  'h_c' : 2}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'A_to_t6A' : {'name' : 'N6-threonylcaramoyladenosine',
                                  'input' : 'A',
                                  'output' : 't6A',
                                  'machines' : {'TsaBCDE' : {'proteins' : {'b3064' : 'TsaD',
                                                                           'b3282' : 'TsaC',
                                                                         'b1807' : 'tsaB',
                                                                         'b4168' : 'tsaE'},
                                                            #important : not in model
                                                            'RNA_position_substrates' :{'tRNA' :  {37 : {'all' : 1}}},
                                                            'restrictions' : {36 : 'A',
                                                                             34 :'not_A',
                                                                             35: 'not_A'},
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'amp_c': 1,
 'atp_c': -1,
 'h2o_c': 1,
 'h_c': 1,
 'hco3_c': -1,
 'ppi_c': 1,
 'thr__L_c': -1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 't6A_to_m6t6A' : {'name' : 'N6-methyl-N6-threonylcarbamoyladenosine',
                                  'input' : 't6A',
                                  'output' : 'm6t6A',
                                  'machines' : {'EG11503_MONOMER' : {'proteins' : {'b0195' : 'TrmO'},
                                                            #not in model; IMPORTANT
                                                            'RNA_position_substrates' : {'tRNA' : {37 : {'b3273' : 1, #trna thrV (GGU)
                                                                                               'b3979' : 1}}}, #trna thrT (GGU)
                                                            'carriers' :None}
                                               },
                                  'metabolites' : {'amet_c' : -1,
                                                  'ahcys_c' : 1,
                                                  'h_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 't6A_to_ct6A' : {'name' : 'cyclic N6-threonylcarbamoyladenosine',
                                  'input' : 't6A',
                                  'output' : 'ct6A',
                                  'machines' : {'TcdA_dim' : {'proteins' : {'b2812' : 'TcdA'},
                                                            #not in model; IMPORTANT
                                                            'RNA_position_substrates' : {'tRNA' : {37 : { 'b1984' : 1 , #trna asnW (GUU)
                                                                                               'b1989' : 1 , #trna asnV (GUU)
                                                                                               'b1986' : 1 , #trna asnU (GUU)
                                                                                               'b1977' : 1 , #trna asnT (GUU)
                                                                                               'b2348' : 1  , #trna argW (CCU)
                                                                                               'b0536' : 1  , #trna argU (UCU)
                                                                                              'b2652' : 1, #trna ileY (CAU)
                                                                                               'b3069' : 1, #trna ileX (CAU)
                                                                                               'b0202' : 1, #trna ileV (GAU)
                                                                                               'b3277' : 1, #trna ileU (GAU)
                                                                                               'b3852' : 1, #trna ileT (GAU) 
                                                                                              'b0749' : 1, #trna lysQ (UUU) #mnm5s2U
                                                                                                'b0743' : 1, #trna lysT (UUU)  #mnm5s2U
                                                                                                'b2404' : 1, #trna lysV (UUU)  #mnm5s2U
                                                                                                'b0747' : 1, #trna lysY (UUU)  #mnm5s2U
                                                                                                'b0745' : 1, #trna lysW (UUU)  #mnm5s2U
                                                                                                'b0748' : 1, #trna lysZ (UUU)    #mnm5s2U
                                                                                                'b0666' : 1, #trna metU (CAU) #ac4C 
                                                                                                'b0673' : 1, #trna metT (CAU) #ac4C
                                                                                               'b2695' : 1}}}, #trna serV (GCU) 
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'atp_c' : -1,
                                                  'adp_c' : 1,
                                                  'pi_c' : 1,
                                                  'h_c' : 1}
                                 }
                 }
                
    ###################################end##############################################
    ####################################################################################