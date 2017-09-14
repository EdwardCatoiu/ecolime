# carriers [ x ] 
# substrates [ x  ] 

queuosine_mods = {'G_to_preq1tRNA' : {'name' : '7-aminomethyl-7-deazaguanosine',
                                  'input' : 'G',
                                  'output' : 'preq1tRNA',
                                  'machines' : {'Tgt_hexa_mod_6:zn2' : {'proteins' : {'b0406' : 'Tgt'},
                                                            'rna_type' : 'tRNA',
                                                            'RNA_position_substrates' : {34 : {'all' : 1}},
                                                            'carriers' : {}
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
                                                            'rna_type' : 'tRNA',
                                                            'RNA_position_substrates' : {34 : {'substrate' : 1}},
                                                            'carriers' : {}
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
                                                            'rna_type' : 'tRNA',
                                                            'RNA_position_substrates' : {34 : {'substrate' : 1}},
                                                            'carriers' : {}
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
                                        'machines' : {'enzyme' : {'proteins' : {'b0144' : 'GluQRS'},
                                                                  #important: not in model
                                                                  'rna_type' : 'tRNA',
                                                                  'RNA_position_substrates' : {34 : { 'b0216': 1, #trna aspV (GUC)
                                                                                               'b0206': 1, #trna aspU (GUC)
                                                                                               'b3760': 1}}, #trna aspT (GUC)
                                                                  'carriers' : {}
                                                                 }
                                                     },
                                        'metabolites' : {'atp_c' : 1,
                                                        'glu__L_c' : -1,
                                                        'amp_c' : 1,
                                                        'ppi_c' : 1,
                                                        'h_c' : 2}
                                       }
                  }
                                     
                                      