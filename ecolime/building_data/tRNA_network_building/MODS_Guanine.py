#carriers [ x ]
# substrates [ x ] 

guanine_mods = {'G_to_m7G' : {'name' : '7-methylguanosine',  'input' : 'G', 'output' : 'm7G',
                              'machines' : {'RlmL_dim' : {'proteins' : {'b0948' : 'RlmKL'},
                                                          'RNA_position_substrates' :{'rRNA' : {2069 : {'LSU/23S/prokaryotic':1}}},
                                                          'carriers' : None
                                                         },
                                            'enzyme_new_RmtB' : {'proteins' : {'bnum' : 'RmtB'},  #warning: important not found
                                                        'RNA_position_substrates' : {'rRNA' :{1405 : {'SSU/16S/prokaryotic' : 1}}},
                                                        'carriers' : None
                                                       },
                                            'RsmG_mono' : {'proteins' : {'b3740' : 'RsmG'},
                                                           'RNA_position_substrates' :{'rRNA' : {527 : {'SSU/16S/prokaryotic' : 1}}},
                                                           'carriers' : None
                                                          },
                                            'YggH_mono' : {'proteins' : {'b2960' : 'TrmB'},
                                     'RNA_position_substrates' : {'tRNA' :{46 : {'b3853' : 1, #trna alaT (UGC)
                                                                        'b3276' : 1,#trna alaU (UGC)
                                                                        'b0203' : 1 , #trna alaV (UGC)
                                                                        'b2397' : 1, #trna alaW (GGC)
                                                                        'b2396' : 1, #trna alaX (GGC)
                                                                        'b2692' : 1 , # trna ArgZ (ACG)
                                                                        'b2691' : 1 ,#trna ArgQ (ACG)
                                                                        'b2694' : 1 ,#trna ArgV (ACG)
                                                                        'b2693' : 1 ,#trna ArgY (ACG)
                                                                        'b3796' : 1 ,#trna ArgX (CCG)
                                                                        'b1984' : 1 , #trna asnW (GUU)
                                                                        'b1989' : 1 , #trna asnV (GUU)
                                                                        'b1986' : 1 , #trna asnU (GUU)
                                                                        'b1977' : 1 , #trna asnT (GUU)
                                                                        'b0216': 1, #trna aspV (GUC)
                                                                        'b0206': 1, #trna aspU (GUC)
                                                                        'b3760': 1, #trna aspT (GUC)
                                                                        'b4165' : 1 , #trna glyY (GCC)
                                                                        'b4164' : 1 , #trna glyX (GCC)
                                                                        'b1911' : 1 , #trna glyW (GCC)
                                                                        'b4163' : 1 , #trna glyV (GCC)
                                                                        'b3797' : 1, #trna HisR (GUG)
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
                                                                        'b0666' : 1, #trna metU (CAU)
                                                                        'b0673' : 1, #trna metT (CAU)
                                                                        'b2967' : 1, #trna pheV (GAA)
                                                                        'b4134' : 1, #trna pheU (GAA)
                                                                        'b3273' : 1, #trna thrV (GGU)
                                                                        'b3979' : 1, #trna thrT (GGU)
                                                                        'b3761' : 1, #trna trpT (CCA)
                                                                        'b1665' : 1, #trna valV (GAC)
                                                                        'b1666' : 1, #trna valW (GAC)
                                                                        'b0744' : 1, #trna valT (UAC) 
                                                                        'b2401' : 1, #trna valU (UAC)
                                                                        'b2402' : 1, #trna valX (UAC)
                                                                        'b2403' : 1, #trna valY (UAC)
                                                                        'b0746' : 1 #rna valZ (UAC)
                                                                       }}
                                                                 }, 
                                                           'carriers' : None
                                                          }
                                           },
                              'metabolites' : {'amet_c' : -1,
                                               'ahcys_c' : 1} #may be missing 'h_c' : 1
                             },
               
                'G_to_m2G' : {'name' : 'N2-methylguanosine',  'input' : 'G', 'output' : 'm2G',
                              'machines' : {'RlmG_mono' : {'proteins' : {'b3084' : 'RmlG'},
                                                           'RNA_position_substrates' : {'rRNA' :{1835 : {'LSU/23S/prokaryotic' : 1}}},
                                                            'carriers' : None
                                                           },
                                            'RlmL_dim' : {'proteins' : {'b0948' : 'RlmL'},
                                                            'RNA_position_substrates' :{'rRNA' : {2445 : {'LSU/23S/prokaryotic' : 1} }},
                                                            'carriers' : None
                                                           },
                                            'RsmC_mono' : {'proteins' : {'b4371' : 'RsmC'},
                                                            'RNA_position_substrates' : {'rRNA' :{1207 : {'SSU/16S/prokaryotic' : 1}}},
                                                            'carriers' : None
                                                           },
                                            'RsmD_mono' : {'proteins' : {'b3465' : 'RsmD'},
                                                            'RNA_position_substrates' : {'rRNA' :{966 : {'SSU/16S/prokaryotic' : 1}}},
                                                            'carriers' : None
                                                           },
                                            'RsmJ_MONOMER' : {'proteins' : {'b3497' : 'RsmJ '},#important: not im model
                                                        'RNA_position_substrates' : {'rRNA' :{1516 : {'SSU/16S/prokaryotic' : 1}}},
                                                        'carriers' : None
                                                       }
                                           },
                              'metabolites' : {'amet_c' : -1,
                                               'ahcys_c' : 1,
                                               'h_c' : 1}
                             },
                'G_to_Gm' : {'name' : '2-O-methylguanosine',   'input' : 'G',    'output' : 'Gm',
                              'machines' : {'RlmB_dim' : {'proteins' : {'b4180' : 'RlmB'},
                                                          'RNA_position_substrates' : {'rRNA' :{2251 : {'LSU/23S/prokaryotic': 1}}},
                                                            'carriers' : None
                                                           },
                                                'TrmH_dim' : {'proteins' : {'b3651' : 'TrmH'},
                                                              'RNA_position_substrates' : {'tRNA' :{18 : {'b0668' : 1 , #trna glnW (UUG)
                                                                                              'b0670' : 1 , #trna glnU (UUG)
                                                                                              'b0664' : 1 , #trna glnX (CUG)
                                                                                              'b0665' : 1 , #trna glnV (CUG)     
                                                                                              'b2652' : 1, #trna ileY (CAU)
                                                                                               'b3069' : 1, #trna ileX (CAU)
                                                                                               'b1909' : 1 , #trna leuZ (UAA)
                                                                                               'b4369' : 1 , #trna leuP (CAG)
                                                                                               'b4370' : 1 , #trna leuQ (CAG)
                                                                                               'b3798' : 1 , #trna leuT (CAG)
                                                                                               'b4368' : 1 , #trna leu (CAG)
                                                                                               'b3174' : 1 , #trna leuU (GAG)
                                                                                               'b0666' : 1, #trna metU (CAU)
                                                                                               'b0673' : 1, #trna metT (CAU)
                                                                                                'b0971' : 1 , #trna serT (UGA)
                                                                                               'b1975' : 1 , #trna serU (CGA)
                                                                                               'b0883' : 1 , #trna serW (GGA)
                                                                                                'b1032' : 1 , #trna serX (GGA)
                                                                                                'b1230' : 1 , #trna tyrV (GUA)
                                                                                                'b3977' : 1 , #trna tyrU (GUA)
                                                                                                'b1231' : 1} #trna tyrT (GUA)
                                                                                          }},
                                                            'carriers' : None
                                                             }
                                           },
                              'metabolites' : {'amet_c' : -1,
                                               'ahcys_c' : 1,
                                               'h_c' : 1}
                             },
                'G_to_m1G' : {'name' : '1-methylguanosine', 'input' : 'G',  'output' : 'm1G',
                               'machines' : {'RrmA_dim_mod_2:zn2' : {'proteins' : {'b1822' : 'RlmA1'},
                                                                     'RNA_position_substrates' :{'rRNA':{745 :{'LSU/23S/prokaryotic':1}}},
                                                                     'carriers' : None
                                                                    },
                                             'TrmD_dim' : {'proteins' : {'b2607' : 'TrmD'},
                                                           'RNA_position_substrates' : {'tRNA' :{37 : { 'b4369' : 1 , #trna leuP (CAG)
                                                                                               'b4370' : 1 , #trna leuQ (CAG)
                                                                                               'b3798' : 1 , #trna leuT (CAG)
                                                                                               'b4368' : 1 , #trna leuV (CAG)
                                                                                               'b3174' : 1 , #trna leuU (GAG)
                                                                                               'b0672' : 1 , #trna leuW (UAG)
                                                                                               'b3799' : 1 , #trna proM (UGG)
                                                                                                'b2189' : 1 , #trna proL (GGG)
                                                                                                'b3545' : 1 , #trna proK (CGG)
                                                                                                 'b3796' : 1 }
                                                                                       }},#trna ArgX (CCG)
                                                           'carriers' : None
                                                          }
                                               },
                               'metabolites' : {'amet_c' : -1,
                                                'ahcys_c' : 1,
                                                'h_c' : 1}
                              },
              'G_to_preq1tRNA' : {'name' : '7-aminomethyl-7-deazaguanosine',
                                  'input' : 'G',
                                  'output' : 'preq1tRNA',
                                  'machines' : {'Tgt_hexa_mod_6:zn2' : {'proteins' : {'b0406' : 'Tgt'},
                                                            'RNA_position_substrates' : {'tRNA' :{34 : {'all' : 1}}},
                                                            'carriers' : None
                                                                       }
                                               },
                                  'metabolites' : {'preq1_c' : -1,
                                                  'gua_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'preq1tRNA_to_oQtRNA' : {'name' : 'epoxyqueuosine',
                                  'input' : 'preq1tRNA',
                                  'output' : 'oQtRNA',
                                  'machines' : {'QueA_mono' : {'proteins' : {'b0405' : 'QueA'},
                                                            'RNA_position_substrates' : {'tRNA' :{34 : {'all' : 1}}},
                                                            'carriers' : None
                                                              }
                                               },
                                  'metabolites' : {'amet_c' : -1,
                                                  'ade_c' : 1,
                                                  'met__L_c' : 1,
                                                  'h_c' : 1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'oQtRNA_to_QtRNA' : {'name' : 'queuosine',
                                  'input' : 'oQtRNA',
                                  'output' : 'QtRNA',
                                  'machines' : {'QueG_mono_mod_adocbl' : {'proteins' : {'b4166' : 'QueG'},
                                                            'RNA_position_substrates' : {'tRNA' :{34 : {'all' : 1}}},
                                                            'carriers' : None
                                                                         }
                                               },
                                  'metabolites' : {'h2o_c' : 1}
                                                  #oxidized e acceptor : 1
                                                  #reduced e acceptor : -1}
                                 }, 
    ###################################end##############################################
    ####################################################################################
                 'QtRNA_to_gluQtRNA' : {'name' : 'glutamyl-queuosine',
                                        'input' : 'QtRNA',
                                        'output' : 'gluQtRNA',
                                        'machines' : {'YadB_mono' : {'proteins' : {'b0144' : 'GluQRS'},
                                                                  #important: not in model
                                                                  'RNA_position_substrates' : {'tRNA' :{34 : { 'b0216': 1, #trna aspV (GUC)
                                                                                               'b0206': 1, #trna aspU (GUC)
                                                                                               'b3760': 1}}}, #trna aspT (GUC)
                                                                  'carriers' : None
                                                                 }
                                                     },
                                        'metabolites' : {'atp_c' : 1,
                                                        'glu__L_c' : -1,
                                                        'amp_c' : 1,
                                                        'ppi_c' : 1,
                                                        'h_c' : 2}
                                       }
                  }
                                     
                                      
               
