#carriers : [ x ]
# substrates :  [ x ] 
cytidine_mods =   {'C_to_s2C' : {'name' : '2-thiocytidine',
                                 'input' : 'C',
                                 'output' : 's2C',
                                 'machines' : {'YdaO_mono' : {'proteins' : {'b1344' : 'TtcA'},
                                                              #important: should be dimer
                                                              'RNA_position_substrates' :{'tRNA' : {32 : {'b2692' : 1 , # trna ArgZ (ACG)
                                                                                                          'b2691' : 1 ,#trna ArgQ (ACG) #inosine
                                                                                                          'b2694' : 1 ,#trna ArgV (ACG)
                                                                                                          'b2693' : 1 ,#trna ArgY (ACG) #inosine
                                                                                                          'b3796' : 1 ,#trna ArgX (CCG) 
                                                                                                          'b0536' : 1  , #trna argU (UCU) #mnm5U
                                                                                                          'b2695' : 1}}
                                                                                         }, #trna serV (GCU)
                                                              'carriers' : {'trdrd_c': -1,
                                                                            'trdox_c': 1,
                                                                            'IscS_mod_2:pydx5p_mod_1:SH': -1,
                                                                            'IscS_mod_2:pydx5p': 1}
                                                              #Active enzyme contains an oxygen-sensitive [4Fe-4S] cluster
                                                             }
                                              },
                                 'metabolites' : {'cys__L_e' : - 1,
                                                  'ser__L_c' : 1  }
                                }, 
                   
                'C_to_m5C' : {'name' :'5-methylcytidine' ,
                              'input' : 'C',
                              'output' : 'm5C',
                              'machines' : {'RlmI_dim' : {'proteins' : {'b0967' : 'RlmI'},
                                                          'RNA_position_substrates' : {'rRNA':{1962:{'LSU/23S/prokaryotic cytosol': 1}}},
                                                          'carriers' : None
                                                             },
                                            'RsmB_mono' : {'proteins' : {'b3289' : 'RsmB'},
                                                           'RNA_position_substrates' :{'rRNA':{967 :{'SSU/16S/prokaryotic cytosol': 1}}},
                                                           'carriers' :None
                                                          },
                                            'RsmF_mono' : {'proteins' : {'b1835' : 'RsmF'},
                                                           'RNA_position_substrates' : {'rRNA':{1407:{'LSU/23S/prokaryotic cytosol': 1}}},
                                                           'carriers' : None
                                                          }
                                           },
                              'metabolites' : {'amet_c' : -1,
                                               'ahcys_c' : 1,
                                               'h_c' : 1}
                             }, 
                   
                   'C_to_Cm' : {'name': '2-O-methylcytdine',
                                'input' : 'C',
                                'output' : 'Cm',
                                'machines' : {'RlmM_mono' : {'proteins' : {'b2806' : 'RlmM'},
                                                            'RNA_position_substrates' :{'rRNA':{2498:{'LSU/23S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None
                                                           },
                                                'RsmI_mono' : {'proteins' : {'b3146' : 'RsmI'},
                                                            'RNA_position_substrates' :{'rRNA':{1402:{'SSU/16S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None
                                                           },
                                                'TrmJ_dim' : {'proteins' : {'b2532' : 'TrmJ'},
                                                            'RNA_position_substrates' : {'tRNA':{32 : {'b0664' : 1 , #trna glnX (CUG)
                                                                                               'b0665' : 1 , #trna glnV (CUG)
                                                                                               'b0971' : 1, #trna SerT (UGA)
                                                                                                      'b3761' :1, #trna trnpT (CCA)
                                                                                                      'b3171' :1, #trna fmetY (CAU)
                                                                                                     'b2814' :1 } #trna serT (UGA)
                                                                                        }},
                                                            'carriers' : None
                                                              #requires D-loop identity substrates
                                                              #modomics substrates !!
                                                             },
                                                'trmL_dim' : {'proteins' : {'b3606' : 'TrmL'},
                                                            #important : NOT IN MODEL
                                                            'RNA_position_substrates' : {'tRNA':{34 : {'b4369' : 1 , #trna leuP (CAG) #Cm
                                                                                               'b4370' : 1 , #trna leuQ (CAG) #Cm
                                                                                               'b3798' : 1 , #trna leuT (CAG) #Cm
                                                                                               'b4368' : 1 }}}, #trna leu (CAG) #Cm
                                                            'carriers' : None
                                                           }
                                                
                                               },
                                  'metabolites' : {'amet_c' : -1,
                                                  'ahcys_c' : 1,
                                                  'h_c' : 1}
                                 }, 
                   'C_to_ac4C' : {'name' : 'N4-acetylcytidine',
                                  'input' : 'C',
                                  'output' : 'ac4C',
                                  'machines' : {'TmcA_mono' : {'proteins' : {'b2474' : 'TmcA'},
                                                            'RNA_position_substrates' : {'tRNA':{34 : {'b3171' : 1 , #trna fmetY (CAU)
                                                                                               'b2816' : 1 , #trna fmetV (CAU)
                                                                                               'b2814' : 1 , #trna fmetZ (CAU)
                                                                                               'b2815' : 1  }}}, #trna fmetW (CAU)
                                                                                              
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'atp_c' : -1,
                                                  'h2o_c' : -1,
                                                  'accoa_c' : -1,
                                                  'adp_c' : 1,
                                                  'coa_c' : 1,
                                                  'pi_c' : 1,
                                                  'h_c' : 1}
                                 }, 
                   
                   'Cm_to_m4Cm' : {'name' : 'N4,2-O-dimethylcyidine',
                                  'input' : 'Cm',
                                  'output' : 'm4Cm',
                                  'machines' : {'RsmH_mono' : {'proteins' : {'b0082' : 'RsmH'},
                                                               #important : should be dimer
                                                            'RNA_position_substrates' :{'rRNA':{1402:{'SSU/16S/prokaryotic cytosol' : 1}}},
                                                            'carriers' : None}
                                               },
                                  'metabolites' : {'amet_c' : -1,
                                                  'ahcys_c' : 1,
                                                  'h_c' : 1}
                   }, 
   
       'C_to_m4C' : {'name' : 'N4-methylcyidine',
                     'input' : 'C',
                     'output' : 'm4C',
                     'machines' : {'RsmH_mono' : {'proteins' : {'b0082' : 'RsmH'},
                                                  #important : should be dimer
                                                  'RNA_position_substrates' :{'rRNA':{1402:{'SSU/16S/prokaryotic cytosol' : 1}}},
                                                  'carriers' : None}
                                  },
                     'metabolites' : {'amet_c' : -1,
                                      'ahcys_c' : 1,
                                      'h_c' : 1}
                    },
                   
                   'm4C_to_m4Cm' : {'name' : 'N4,2-O-dimethylcyidine',
                       'input' : 'm4C',
                       'output' : 'm4Cm',
                       'machines' : {'RsmH_mono' : {'proteins' : {'b0082' : 'RsmH'},
                                                    #important : should be dimer
                                                    'RNA_position_substrates' :{'rRNA':{1402:{'SSU/16S/prokaryotic cytosol' : 1}
                                                                                       }
                                                                               },
                                                    'carriers' : None
                                                   }
                                    },
                       'metabolites' : {'amet_c' : -1,
                                        'ahcys_c' : 1,
                                        'h_c' : 1}
                      }, 
                   
                   'C_to_k2C' : {'name' : '2-lysidine',
                                  'input' : 'C',
                                  'output' : 'k2C',
                                  'machines' : {'TilS_mono' : {'proteins' : {'b0188' : 'TilS'},
                                                            'RNA_position_substrates' : {'tRNA':{34 : {  'b2652' : 1, #trna ileY (CAU)
                                                                                               'b3069' : 1}}}, #trna ileX (CAU)
                                                            'carriers' :None}
                                               },
                                  'metabolites' : {'lys__L_c' : -1, 
                                                  'atp_c' : -1,
                                                  'amp_c' : 1,
                                                  'ppi_c' : 1,
                                                  'h_c' : 2}
                                } 
                   }
        #end!!!
                              
    ###################################end##############################################
    ####################################################################################
    
     ###################################end##############################################
    ####################################################################################

#DOES NOT OCCUR IN BACTERIA!! MODOMICS IS WRONG
    #'m4Cm_to_m44Cm' : {'name' : 'N4,N4,2-O-trimethylcyidine',
                                 # 'input' : 'm4Cm',
                                  #'output' : 'm44Cm',
                                  #'machines' : {'RsmH_mono' : {'proteins' : {'b0082' : 'RsmH'},
                                                                #important : should be dimer
                                                            #'RNA_position_substrates' :{'rRNA':{1402:{'SSU/16S/prokaryotic cytosol' : 1}}},
                                                          #  'carriers' : None}
                                            #   },
                                #   'metabolites' : {'amet_c' : -1,
                                                #  'ahcys_c' : 1,
                                               #   'h_c' : 1}
                    # }, 
    ###################################end##############################################
    ####################################################################################
 