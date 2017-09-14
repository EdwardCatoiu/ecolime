uridine_mod = {'Y_to_m3Y' : {'name' : 'mod_3-methylpseudouridine',
                             'input':'Y',
                             'output' : 'm3Y',
                            'machines' : {'RlmH_dim' : {'proteins' : {'b0636' : 'RlmH'},
                                                      'RNA_position_substrates' : {'rRNA' : {1915: {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                             }, ###end
############################################################
               
               'Um_to_cmnm5Um' : {'name' : 'mod_5-carboxymethylaminomethyl-2-O-methyluridine',
                                  'input':'Um',
                                  'output' : 'cmnm5Um',
                                  'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                              'b3741' : 'MnmG_dim'},
                                                                                'RNA_position_substrates' : {'tRNA' : {34 : {'b1909' : 1}}}, #trna LeuZ (UAA)  
                                                                                'carriers' : None
                                                                               }
                                          },
                           'metabolites' : {'gtp_c': -1,
                                                  'mlthf_c' : -1,
                                                  'gly_c' : -1,
                                                  #oxidized e acceptor : -1
                                                  'h2o_c' :-1,
                                                  'gdp_c' : 1,
                                                  'dhf_c' : 1,
                                                  #reduce e acceptor
                                                  'pi_c' : 1,
                                                  'h_c' : 2  
                                                 }
                                  }, #end
               
               ##########################################################################
               

               
                'U_to_Y' : {'name' : 'mod_pseudouridine',
                            'input':'U',
                             'output' : 'Y',
                            'machines' : {'RluA_mono' : {'proteins' : {'b0058' : 'RluA'},
                                                      'RNA_position_substrates' : {'tRNA' : { 32 : {'b1910' : 1, #'trna CysT (GCA)
                                                                                         'b1909' : 1, #trna LeuZ (UAA)
                                                                                         'b2967' : 1,#trna pheV (GAA)
                                                                                         'b4134' : 1} #trna PheU (GAA)
                                                                                             }, 
                                                                                   'rRNA' : {746 : {'LSU/23S/prokaryotic':1}
                                                                                            }
                                                                                   },
                                                      'carriers' : None
                                                      },
                                         
                                          'RluB_mono' : {'proteins' : {'b1269' : 'RluB'},
                                                      'RNA_position_substrates' : {'rRNA' : {2605 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },
                                          'RluC_mono' : {'proteins' : {'b1086' : 'RluC'},
                                                      'RNA_position_substrates' :{'rRNA' : {2504 : {'all':1},
                                                                                            2580 : {'all':1},
                                                                                            995 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },
                                          
                                          'RluD_mono_mod_1:mg2' : {'proteins' : {'b2594' : 'RluD'},
                                                      'RNA_position_substrates' : {'rRNA' : {1915 : {'LSU/23S/prokaryotic cytosol':1},
                                                                                  1911 : {'LSU/23S/prokaryotic cytosol':1},
                                                                                  1917 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },

                                          'YmfC_mono' : {'proteins' : {'b1135' : 'RluE'},
                                                      'RNA_position_substrates' : {'rRNA' : {2457 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },
                                          'YjbC_mono' : {'proteins' : {'b4022' : 'RluF'},
                                                      'RNA_position_substrates' :{'rRNA' :  {2604 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },
                                          


                                          'TruD_mono' : {'proteins' : {'b2745' : 'TruD'},
                                                      'RNA_position_substrates' : {'tRNA' : {13 : {'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1 #trna gltW (SUC) #mnm5s2U
                                                                                        }} 
                                                                                  }, #http://www.jbc.org/content/279/18/18107.long
                                                      'carriers' : None
                                                      },
                                          'YqcB_mono' : {'proteins' : {'b2791' : 'TruC'},
                                                      'RNA_position_substrates' : {'tRNA' : {65 : {'b3760' : 1, #trna AspT (GUC)
                                                                                         'b0206' : 1, #trna AspU (GUC)
                                                                                         'b0216' : 1 ,#trna AspV (GUC) 
                                                                                         'b0202' : 1, #trna IleV (GAU)
                                                                                         'b3277' : 1, #trna IleU (GAU)
                                                                                         'b3852' : 1}}}, #trna IleT (GAU)
                                                      'carriers' : None
                                                      },
                                          'TruB_mono' : {'proteins' : {'b3166' : 'TruB'},
                                                      'RNA_position_substrates' : {'tRNA' :  {55 : {'all':1}}},
                                                      'carriers' : None
                                                      },
                                          'TruA_dim' : {'proteins' : {'b2318' : 'TruA'},
                                                      'RNA_position_substrates' :{'tRNA' :  {38 : {'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                         'b0665' : 1 , #trna GlnV (CUG)
                                                                                         'b0664' : 1 , #trna GlnX (CUG)
                                                                                         'b3797' : 1, # trna His (GUG)
                                                                                         'b4369' : 1, #trna LeuP (CAG)
                                                                                         'b4370' : 1, #trna LeuQ (CAG)
                                                                                         'b3798' : 1, #trna LeuT (CAG)
                                                                                         'b4368' : 1, #trna LeuV (CAG)
                                                                                         'b3174' : 1 }, #trna LeuU (GAG)
                                                                                   39 : {'b1984' : 1 , #trna AsnW (GUU)
                                                                                         'b1989' : 1 , #trna asnV (GUU)
                                                                                         'b1986' : 1 , #trna asnU (GUU)
                                                                                         'b1977' : 1 , #trna asnT (GUU)
                                                                                         'b1910' : 1, #'trna CysT (GCA)
                                                                                         'b0665' : 1 , #trna GlnV (CUG)
                                                                                         'b0664' : 1 , #trna GlnX (CUG)
                                                                                        'b3797' : 1, # trna His (GUG) 
                                                                                         'b3069' : 1, #trna ileX (CAU),
                                                                                         'b1909' : 1, #trna LeuZ (UAA),
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (UUU)#mnm5s2U
                                                                                         'b0666' : 1 , #trna MetU (CAU)
                                                                                         'b0673' : 1 , #trna metT (CAU)
                                                                                         'b2967' : 1,#trna pheV (GAA)
                                                                                         'b4134' : 1, #trna PheU (GAA)
                                                                                         'b1230' : 1, # trna TyrV/GUA
                                                                                         'b3977' : 1, # trna TyrU/GUA
                                                                                         'b1231' : 1 }, # trna TyrT/GUA
                                                                                   40 : {'b0536' : 1 , #trna ArgU/UCU
                                                                                         'b4369' : 1, #trna LeuP (CAG)
                                                                                         'b4370' : 1, #trna LeuQ (CAG)
                                                                                         'b3798' : 1, #trna LeuT (CAG)
                                                                                         'b4368' : 1, #trna LeuV (CAG)
                                                                                         'b1032' : 1 ,#trna SerX / GGA
                                                                                         'b0883' : 1 } #trna SerW /GGA
                                                                                  }},
                                                      'carriers' : None
                                                      },
                                          
                                          'RsuA_mono' : {'proteins' : {'b2183' : 'RsuA'},
                                                      'RNA_position_substrates' : {'rRNA' : {516 : {'SSU/16S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                         }
                                          },
                                                                                          
                            'metabolites' : {}
                                  }, #end
############################################################
               'U_to_Um' : {'name' : 'mod_2-O-methyluridine',
                            'input':'U',
                            'output' : 'Um',
                            'machines' : {'RrmJ_mono' : {'proteins' : {'b3179' : 'RmlE'},
                                                      'RNA_position_substrates' : {'rRNA' : {2552 : {'LSU/23S/prokaryotic cytoso':1}}},
                                                      'carriers' : None
                                                        },
                                          'TrmJ_dim' : {'proteins' : {'b2532' : 'TrmJ'},
                                                      'RNA_position_substrates' : {'tRNA' : {32 : {'b0971' : 1 , #trna SerT/UGA
                                                                                        'b0664':1, #ecocyc, modomics
                                                                                        'b0668':1} #ecocyc
                                                                                  }},
                                                      'carriers' : None
                                                       },
                                          'trmL_dim' : {'proteins' : {'b3606' : 'TrmL'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b1909' :  1}}}, #'trnaLeuZ'                                                                          #the enzyme requires the presence of the ms2i6
                                                              #modification at the A37 nucleotide for activity
                                                              #--ecocyc 
                                                                                   #IMPORTANT ; BNUMBER NOT IN MODEL!!
                                                      'carriers' : None
                                                     }
                                         },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                           }, #end
               ###########################################################
                'U_to_s4U' : {'name' : 'mod_4-thiouridine',
                                  'input':'U',
                             'output' : 's4U',
                            'machines' : {'ThiI_mono' : {'proteins' : {'b0423' : 'ThiI'},
                                                      'RNA_position_substrates' : {'tRNA' : {8 : {'b3760' : 1, #'trna aspT (GUC) #queosine
                                                                                        'b0206' : 1, #'trna aspU (GUC) #queosine
                                                                                        'b0216' : 1, #'trna aspV (GUC)    #queosine
                                                                                         'b1977' : 1, #'trna asnT (GUU) #queuosine
                                                                                        'b1986' : 1, #'trna asnU (GUU) #queuosine
                                                                                        'b1989' : 1, #'trna asnV (GUU) #queuosine
                                                                                        'b1984' : 1, #'trna asnW (GUU) #queuosine
                                                                                       'b1910' : 1, #'trna CysT (GCA)
                                                                                        'b0668' : 1 , #trna GlnW (UUG)
                                                                                        'b0670' : 1 , #trna GlnU (UUG)
                                                                                        'b0665' : 1 , #trna GlnV (CUG)
                                                                                        'b0664' : 1 , #trna GlnX (CUG)
                                                                                        'b2864' : 1, #trna glyU (CCC)
                                                                                        'b3797' : 1, #trna hisR (GUG) #queosine     
                                                                                        'b2652' : 1, #trna ileY (CAU) #k2C
                                                                                        'b3069' : 1, #trna ileX (CAU) #k2C
                                                                                        'b1909' :  1, #'trnaLeuZ' 
                                                                                         'b0666' : 1, #trna metU (CAU)  #ac4C
                                                                                        'b0673' : 1, #trna metT (CAU) #ac4C
                                                                                       'b2967' : 1,#trna pheV (GAA)
                                                                                        'b4134' : 1, #trna PheU (GAA)
                                                                                       'b0971' : 1 , #trna SerT/UGA
                                                                                       'b2695' :1, #trna SerV/GCU
                                                                                        'b1032' : 1 ,#trna SerX / GGA
                                                                                        'b0883' : 1 , #trna SerW /GGA
                                                                                        'b3761' : 1 , # trna TrpT/CCA
                                                                                        'b1230' : 1 , #trna tyrV (GUA) #queosine
                                                                                        'b3977' : 1 , #trna tyrU (GUA) #queosine
                                                                                        'b1231' : 1, #trna tyrT (GUA)#queosine
                                                                                        'b0744' : 1, #trna valT (UAC)  #cmo5U
                                                                                        'b2401' : 1, #trna valU (UAC)  #cmo5U
                                                                                        'b2402' : 1, #trna valX (UAC)  #cmo5U
                                                                                        'b2403' : 1, #trna valY (UAC)  #cmo5U
                                                                                        'b0746' : 1, #rna valZ (UAC) #cmo5U
                                                                                        'b1666' :1 ,# trna ValW/GAC
                                                                                        'b1665' :1 }# trna valV/GAC
                                                                                  }},
                                                      'carriers' :{'trdrd_c': -1,
                                                                   'trdox_c': 1,
                                                                   'IscS_mod_2:pydx5p_mod_1:SH': -1,
                                                                   'IscS_mod_2:pydx5p': 1}
                                                      }
                                          },
                            'metabolites' : {'atp_c': -1,
                                             'amp_c': 1,
                                             'ppi_c': 1,
                                             'h_c': 1}
                                 }, #end
                        ############################################################
                        
                    'U_to_s2U' : {'name' : 'mod_2-thiouridine',
                                  'input':'U',
                             'output' : 's2U',
                            'machines' : {'TrmU_mono' : {'proteins' : {'b1133' : 'MnmA'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                         'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                         'b0749' : 1, #trna lysQ (UUU) 
                                                                                         'b0743' : 1, #trna lysT (UUU)  
                                                                                         'b2404' : 1, #trna lysV (UUU)  
                                                                                         'b0747' : 1, #trna lysY (UUU) 
                                                                                         'b0745' : 1, #trna lysW (UUU)  
                                                                                         'b0748' : 1} #trna lysZ (UUU) 
                                                                                  }},
                                                         
                                                         
                                                       'carriers' : {'IscS_mod_2:pydx5p_mod_1:SH': -1,
                                                                    'trdrd_c': -1,
                                                                    'IscS_mod_2:pydx5p': 1,
                                                                    'trdox_c': 1},
                                                         'additional_enzymes' : {
                                                                    'YheLMN_cplx' :1 ,
                                                                    'YccK_mono' :1, 
                                                                    'YhhP_mono' : 1}
                                                          #A sulfur relay system consisting of 
                    #IscS and the TusABCDE proteins is required for delivery of the sulfur atom}
                    #http://ecocyc.org/ECOLI/NEW-IMAGE?type=REACTION&object=RXN0-2023
                    
                                                      }
                                          },
                            'metabolites' : {'atp_c' : -1,
                                             'amp_c' : 1,
                                             'ppi_c' : 1,
                                             'h_c' : 1
                                            }
                                  }, #end
               #################################################################################
                        
                        
                   
                        
                        
                    'U_to_nm5U' : {'name' : '5-aminomethyluridine',
                                   'input':'U',
                             'output' : 'nm5U',
                            'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                       'b3741' : 'MnmG_dim'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b3978' : 1, #trna GlyT (UCC)#mnm5U
                                                                                         'b0536' :1, #trna argU (UCU) #mnm5U @34
                                                                                        'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (UUU)#mnm5s2U
                                                                                        'b3969' : 1, #trna gltT (UUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (UUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (UUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (UUC) #mnm5s2U
                                                                                        #'b1909' :  1,#'trnaLeuZ'
                                                                                         'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                                                                                         'b0668' :1
                                                                                                  } #trna GlnW ($UG) #cmnm5s2U 

                                                                                  }},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'gtp_c': -1,
                                             'mlthf_c' : -1,
                                             'nh4_c' : -1,
                                             #oxidized e acceptor : -1
                                             'h2o_c' :-1,
                                             'gdp_c' : 1,
                                             'dhf_c' : 1,
                                             #reduce e acceptor
                                             'pi_c' : 1
                                            }
                                  }, #end
               
               
#################################################
                        
                        
                    'U_to_m5U' : {'name' : 'mod_5-methyluridine',
                                  'input':'U',
                             'output' : 'm5U',
                            'machines' : {'RumB_mono_mod_1:4fe4s' : {'proteins' : {'b0859' : 'RlmC'},
                                                      'RNA_position_substrates' :{'rRNA' :  {747 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },
                                          'RumA_mono_mod_1:4fe4s' : {'proteins' : {'b2785' : 'RlmD'},
                                                      'RNA_position_substrates' : {'rRNA' : {1939 : {'LSU/23S/prokaryotic cytosol':1}}},
                                                      'carriers' : None
                                                      },
                                          'TrmA_mono' : {'proteins' : {'b3965' : 'TrmA'},
                                                      'RNA_position_substrates' : {'tRNA' : {54 : {'all':1}}},
                                                      'carriers' : None
                                                      },
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
######################################################
                        
                        
                    'U_to_m3U' : {'name' : 'mod_3-methyluridine',
                                  'input':'U',
                             'output' : 'm3U',
                            'machines' : {'YggJ_dim' : {'proteins' : {'b2946' : 'RsmE'},
                                                      'RNA_position_substrates' : {'rRNA' : {1498 : {'SSU/16S/prokaryotic cytosol':1}}},  
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
###################################################
                        
                        
                    'U_to_ho5U' : {'name' : 'mod_5-hydroxyuridine',
                                   'input' : 'U',
                                   'output' : 'ho5U',
                            'machines' : {'enzyme_unknown2' : {'proteins' : {'bnum' : 'name'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0672' : 1, #leuW (UAG)
                                                                                                   'b0744' : 1, #tRNAvalT UAC
                                                                                                   'b2401' : 1, #tRNAvalU  UAC
                                                                                                   'b2402' : 1, #tRNAvalX UAC
                                                                                                   'b2403' : 1, #tRNAvalY UAC
                                                                                                   'b0971' : 1, #tRNAserT UGA
                                                                                                   'b3799' : 1, #Trna ProM (UGG)
                                                                                                   'b3976' : 1, #Trna thrU (UGU)
                                                                                                   'b3853' : 1, #Trna alaT (UGC)
                                                                                                   'b3276' : 1, #Trna alaU (UGC)
                                                                                                   'b0203' : 1 #Trna alaV (UGC)
                                                                                                  }}},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {}
                                  }, #end
#####################################################


                        
                        
                    'U_to_DDusA' : {'name' : 'mod_dihydrouridine',
                                'input' : 'U',
                                   'output' : 'DDusA',
                            'machines' : {'DusA_mono' : {'proteins' : {'b4049' : 'DusA'},
                                                      'RNA_position_substrates' :{'tRNA' :  {20 :  {'b3171' : 1 , #trna fmetY (CAU)
                                                                                          'b2816' : 1 , #trna fmetV (CAU)
                                                                                          'b2814' : 1 , #trna fmetZ (CAU)
                                                                                          'b2815' : 1 }, #trna fmetW (CAU)
                                                                                  '20A' : {'b3171' : 1 , #trna fmetY (CAU)
                                                                                           'b2816' : 1 , #trna fmetV (CAU)
                                                                                           'b2814' : 1 , #trna fmetZ (CAU)
                                                                                           'b2815' : 1 }, #trna fmetW (CAU)
                                                                                  17 : {'b3171' : 1 , #trna fmetY (CAU)
                                                                                        'b2816' : 1 , #trna fmetV (CAU)
                                                                                        'b2814' : 1 , #trna fmetZ (CAU)
                                                                                        'b2815' : 1 }, #trna fmetW (CAU)
                                                                                  16 : {'b3171' : 1 , #trna fmetY (CAU)
                                                                                        'b2816' : 1 , #trna fmetV (CAU)
                                                                                        'b2814' : 1 , #trna fmetZ (CAU)
                                                                                        'b2815' : 1 }}}, #trna fmetW (CAU)
                                                      'carriers' : None
                                                      }
                                        
                                          
                                          },
                            'metabolites' : {'nadph_c' : -1,
                                             'h_c' : -1,
                                            'nadp_c' : 1}
                                  }, #end
                'U_to_DDusgen' : {'name' : 'mod_dihydrouridine',
                                'input' : 'U',
                                   'output' : 'DDusgen',
                            'machines' : { 'generic_Dus' : {'proteins' : {'b3260' : 'DusB', #or
                                                                        'b2140' : 'DusC'},
                                                      'RNA_position_substrates' : {'tRNA' : {20 :  {'b3171' : 0 , #trna fmetY (CAU)
                                                                                          'b2816' : 0 , #trna fmetV (CAU)
                                                                                          'b2814' : 0 , #trna fmetZ (CAU)
                                                                                          'b2815' : 0,
                                                                                                   'all' : 1}, #trna fmetW (CAU)
                                                                                  '20A' : {'b3171' : 0 , #trna fmetY (CAU)
                                                                                           'b2816' : 0 , #trna fmetV (CAU)
                                                                                           'b2814' : 0 , #trna fmetZ (CAU)
                                                                                           'b2815' : 0,
                                                                                                   'all' : 1 }, #trna fmetW (CAU)
                                                                                  17 : {'b3171' : 0 , #trna fmetY (CAU)
                                                                                        'b2816' : 0 , #trna fmetV (CAU)
                                                                                        'b2814' : 0 , #trna fmetZ (CAU)
                                                                                        'b2815' : 0,
                                                                                                   'all' : 1 }}}, #trna fmetW (CAU)
                                                      'carriers' : None
                                                      }
                                          
                                          },
                            'metabolites' : {'nadph_c' : -1,
                                             'h_c' : -1,
                                            'nadp_c' : 1}
                                  }, #end
               
                
######################################################################
               'U_to_cmnm5U' : {'name' : 'mod_5-carboxymethylaminomethyluridine',
                                'input' : 'U',
                                   'output' : 'cmnm5U',
                            'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                       'b3741' : 'MnmG_dim'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (UUU)#mnm5s2U
                                                                                         'b3978' : 1, #trna GlyT ({CC)#mnm5U
                                                                                        'b0536' :1, #trna argU ({CU) #mnm5U @34
                                                                                        'b1909' :  1,#'trnaLeuZ'
                                                                                         'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                                                                                         'b0668' :1 , #trna GlnW ($UG) #cmnm5s2U
                                                                                        'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1} #trna gltW (SUC) #mnm5s2U
                                                                                        
                                                                                  }}, 
                                                                       
                                                      'carriers' : None
                                                                         }
                                          },
                             'metabolites' : {'gtp_c': -1,
                                                  'mlthf_c' : -1,
                                                  'gly_c' : -1,
                                                  #oxidized e acceptor : -1
                                                  'h2o_c' :-1,
                                                  'gdp_c' : 1,
                                                  'dhf_c' : 1,
                                                  #reduce e acceptor
                                                  'pi_c' : 1,
                                                  'h_c' : 2  
                                                 }
                                  }, #end
               ####################################################################################
               
               'se2U_to_nm5se2U' : {'name' : 'mod_5-aminomethyl-2-selenouridine',
                                    'input' : 'se2U',
                                   'output' : 'nm5se2U',
                            'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                       'b3741' : 'MnmG_dim'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'all':1}}},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'gtp_c': -1,
                                             'mlthf_c' : -1,
                                             'nh4_c' : -1,
                                             #oxidized e acceptor : -1
                                             'h2o_c' :-1,
                                             'gdp_c' : 1,
                                             'dhf_c' : 1,
                                             #reduce e acceptor
                                             'pi_c' : 1
                                            }
                                  }, #end
##########################################################
               'se2U_to_cmnm5se2U' : {'name' : 'mod_5-carboxymethylaminomethyl-2-selenouridine',
                                      'input' : 'se2U',
                                   'output' : 'cmnm5se2U',
                            'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                       'b3741' : 'MnmG_dim'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'all':1}}},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'gtp_c': -1,
                                                  'mlthf_c' : -1,
                                                  'gly_c' : -1,
                                                  #oxidized e acceptor : -1
                                                  'h2o_c' :-1,
                                                  'gdp_c' : 1,
                                                  'dhf_c' : 1,
                                                  #reduce e acceptor
                                                  'pi_c' : 1,
                                                  'h_c' : 2  
                                                 }
                                  }, #end
               
               
################################################################################
               
               
               's2U_to_nm5s2U' : {'name' : 'mod_5-aminomethyl-2-thiouridine',
                                  'input' : 's2U',
                                   'output' : 'nm5s2U',
                            'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                       'b3741' : 'MnmG_dim'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {
                                                                                           'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                                                                                         'b0668' :1 , #trna GlnW ($UG) #cmnm5s2U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1 #trna lysZ (UUU)#mnm5s2U
                                                                                         }}
                                                                                  },
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'gtp_c': -1,
                                             'mlthf_c' : -1,
                                             'nh4_c' : -1,
                                             #oxidized e acceptor : -1
                                             'h2o_c' :-1,
                                             'gdp_c' : 1,
                                             'dhf_c' : 1,
                                             #reduce e acceptor
                                             'pi_c' : 1
                                            }
                                  }, #end
               
               #########################################################################
            's2U_to_ges2U' : {'name' : 'mod_2-geranylthiouridine',
                                 'input' : 's2U',
                                   'output' : 'ges2U',
                            'machines' : {'YbbB_dim' : {'proteins' : {'b0503' : 'MnmH'},  #IMPORTANT : not in modeL!!!!
                                                      'RNA_position_substrates' :{'tRNA' :  {34 : {'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                        'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (UUU)#mnm5s2U
                                                                                         'b3969': 1, #trna GluT ( UUC )
                                                                                         'b3757': 1, #trna GluU ( UUC )
                                                                                         'b4008': 1, #trna GlV ( UUC )
                                                                                        'b2590': 1}}}, #trna GluW (UUC)
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'grdp_c' : 1,
                                            'ppi_c' : -1,
                                            }#predicted reaction 
                                  }, #end
#http://www.nature.com/nchembio/journal/v8/n11/full/nchembio.1070.html
               ##############################################################
               
               
               
     
               's2U_to_cmnm5s2U' : {'name' : 'mod_5-carboxymethylaminomethyl-2-thiouridine',
                                    'input' : 's2U',
                                   'output' : 'cmnm5s2U',
                            'machines' : {'MnmEG_cplx_mod_fad_mod_2:k' : {'proteins' : {'b3706' : 'MnmE_dim',
                                                                                       'b3741' : 'MnmG_dim'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (UUU)#mnm5s2U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                         'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                                                                                         'b0668' :1 }} #trna GlnW ($UG) #cmnm5s2U
                                                                                         
                                                                                  },
                                                     'carriers' : None
                                                                          }
                                           
                                          },
                            'metabolites' : {'gtp_c': -1,
                                                  'mlthf_c' : -1,
                                                  'gly_c' : -1,
                                                  #oxidized e acceptor : -1
                                                  'h2o_c' :-1,
                                                  'gdp_c' : 1,
                                                  'dhf_c' : 1,
                                                  #reduce e acceptor
                                                  'pi_c' : 1,
                                                  'h_c' : 2  
                                                 }
                                  }, #end
               
###############################################################
               
               'nm5U_to_mnm5U' : {'name' : 'mod_5-methylaminomethyluridine',
                                  'input' : 'nm5U',
                                   'output' : 'mnm5U',
                            'machines' : {'MnmC_mono_mod_fad' : {'proteins' : {'b2324' : 'MnmCD'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {
                            'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                            'b0668' :1 , #trna GlnW ($UG) #cmnm5s2U
                                                                                         'b3978' : 1, #trna GlyT ({CC)#mnm5U
                                                                                         'b0536' :1, #trna argU ({CU) #mnm5U @34
                                                                                        'b0749' : 1, #trna lysQ (SUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (SUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (SUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (SUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (SUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (SUU)#mnm5s2U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1 #trna gltW (SUC) #mnm5s2U
                                                                                         #'b1909' :  1#'trnaLeuZ' \)AA
                                                                                                  }} 
                                                                                  },
                

                                                      'carriers' : None
                                                               #important:check ecocyc for accuracy
                                                               
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
########################################################
                'nm5se2U_to_mnm5se2U' : {'name' : 'mod_5-aminomethyl-2-selenouridine',
                                         'input' : 'nm5se2U',
                                   'output' : 'mnm5se2U',
                            'machines' : {'MnmC_mono_mod_fad' : {'proteins' : {'b2324' : 'MnmCD'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0749' : 1, #trna lysQ (SUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (SUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (SUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (SUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (SUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (SUU)#mnm5s2U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                        'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                                                                                         'b0668' :1 }} #trna GlnW ($UG) #cmnm5s2U
                                                                                  },
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
#########################################################################################
               
                's2U_to_se2U' : {'name' : 'mod_2-selenouridine',
                                       'input' : 's2U',
                                   'output' : 'se2U',
                               #hypothetical reaction
                            'machines' : {'YbbB_dim' : {'proteins' : {}, #neeed enzymes
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'all' : 1 }} },
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'selnp_c' : -1,
                                            'H2O3PS_c' : 1} #new metabolite
                                       #thiophosphate important
                                  }, #end
               
               
               'nm5s2U_to_nm5se2U' : {'name' : 'mod_5-aminomethyl-2-selenouridine',
                                       'input' : 'nm5s2U',
                                   'output' : 'nm5se2U',
                            'machines' : {'YbbB_dim' : {'proteins' : {'b0503' : 'MnmH'}, #important : not in model
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                         'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                         'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1 #trna lysZ (UUU)#mnm5s2U
                                                                                        }}
                                                                                   
                                                                                  },
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'selnp_c' : -1,
                                            'H2O3PS_c' : 1} #new metabolite
                                       #thiophosphate important
                                  }, #end
###############################################################################################
                'mnm5U_to_mnm5s2U' : {'name' : 'mod_5-methylaminomethyl-2-thiouridine',
                                      'input' : 'mnm5U',
                                   'output' : 'mnm5s2U',
                            'machines' : {'TrmU_mono' : {'proteins' : {'b1133' : 'MnmA'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                         'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (UUU)#mnm5s2U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1 #trna gltW (SUC) #mnm5s2U
                                                                                        }}},
                                                      'carriers' : {'IscS_mod_2:pydx5p_mod_1:SH': -1,
                                                                    'trdrd_c': -1,
                                                                    'IscS_mod_2:pydx5p': 1,
                                                                    'trdox_c': 1},
                                                         'additional_enzymes' : {
                                                                    'YheLMN_cplx' :1 ,
                                                                    'YccK_mono' :1, 
                                                                    'YhhP_mono' : 1}
                                                      }
                                          },
                            'metabolites' : {'atp_c' : -1,
                                             'amp_c' : 1,
                                             'ppi_c' : 1,
                                             'h_c' : 1
                                            }
                                  }, #end
               #important : check tusE carriers
#############################################################################################
               
                'nm5s2U_to_mnm5s2U' : {'name' : 'mod_5-methylaminomethyl-2-thiouridine',
                                       'input' : 'nm5s2U',
                                   'output' : 'mnm5s2U',
                            'machines' : {'MnmC_mono_mod_fad' : {'proteins' : {'b2324' : 'MnmCD'},
                                                      'RNA_position_substrates' :{'tRNA' :  {34 : {'b0749' : 1, #trna lysQ (SUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (SUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (SUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (SUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (SUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (SUU)#mnm5s2U
                                                                                       'b0670' :1 , #trna GlnU ($UG) #cmnm5s2U 
                                                                                         'b0668' :1 , #trna GlnW ($UG) #cmnm5s2U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1 #trna gltW (SUC) #mnm5s2U
                                                                                        }}},
                                                                 #mnm5s2U
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
###################################################################################################
               
                'mnm5s2U_to_mnm5se2U' : {'name' : 'mod_5-methylaminomethyl-2-selenouridine',
                                         'input' : 'mnm5s2U',
                                   'output' : 'mnm5se2U',
                            'machines' : {'YbbB_dim' : {'proteins' : {'b0503' : 'MnmH'},#important : not in model
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                         'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                       'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1 #trna lysZ (UUU)#mnm5s2U
                                                                                        }}},
                                                      #mnm5s2U

                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'selnp_c' : -1,
                                            'H2O3PS_c' : 1} #new metabolite
                                       #thiophosphate important
                                  }, #end
               ###################################################################################
               


               'mnm5s2U_to_mnm5ges2U' : {'name' : 'mod_5-methylaminomethyl-2-geranylthiouridine',
                                         'input' : 'mnm5s2U',
                                   'output' : 'mnm5ges2U',
                            'machines' : {'YbbB_dim' : {'proteins' : {'b0503' : 'MnmH'},#important : not in model
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                         'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 , #trna GlnU (UUG)
                                                                                        'b0749' : 1, #trna lysQ (UUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (UUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (UUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (UUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (UUU)#mnm5s2U  
                                                                                         'b0748' : 1 #trna lysZ (UUU)#mnm5s2U
                                                                                        }}},
                                                      #mnm5s2U
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'grdp_c' : 1,
                                            'ppi_c' : -1,
                                            }#predicted reaction 
                                  }, #end
#http://www.nature.com/nchembio/journal/v8/n11/full/nchembio.1070.html

#######################################################
               #stopped here 9/30/16
                'ho5U_to_mo5U' : {'name' : 'mod_5-methoxyuridine', 
                                  'input' : 'ho5U',
                                   'output' : 'mo5U',
                            'machines' : {'YecP_mono' : {'proteins' : {'b1870' : 'enzyme_new_CmoA'},
                                                      #important (enzyme name and metabolites)
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0672' : 1, #leuW (UAG)
                                                                                                   'b0744' : 1, #tRNAvalT UAC
                                                                                                   'b2401' : 1, #tRNAvalU  UAC
                                                                                                   'b2402' : 1, #tRNAvalX UAC
                                                                                                   'b2403' : 1, #tRNAvalY UAC
                                                                                                   'b0971' : 1, #tRNAserT UGA
                                                                                                   'b3799' : 1, #Trna ProM (UGG)
                                                                                                   'b3976' : 1, #Trna thrU (UGU)
                                                                                                   'b3853' : 1, #Trna alaT (UGC)
                                                                                                   'b3276' : 1, #Trna alaU (UGC)
                                                                                                   'b0203' : 1 #Trna alaV (UGC)
                                                                                                  }}},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {}#'http://ecocyc.org/ECOLI/NEW-IMAGE?type=REACTION&object=RXN0-7066'
                                  }, #end
######################################################
                'ho5U_to_cmo5U' : {'name' : 'mod_5-oxyacetic acid',
                                   'input' : 'ho5U',
                                   'output' : 'cmo5U',
                            'machines' : {'YecP_mono' : {'proteins' : {'b1871' : 'CmoB'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0672' : 1, #leuW (UAG)
                                                                                                   'b0744' : 1, #tRNAvalT UAC
                                                                                                   'b2401' : 1, #tRNAvalU  UAC
                                                                                                   'b2402' : 1, #tRNAvalX UAC
                                                                                                   'b2403' : 1, #tRNAvalY UAC
                                                                                                   'b0971' : 1, #tRNAserT UGA
                                                                                                   'b3799' : 1, #Trna ProM (UGG)
                                                                                                   'b3976' : 1, #Trna thrU (UGU)
                                                                                                   'b3853' : 1, #Trna alaT (UGC)
                                                                                                   'b3276' : 1, #Trna alaU (UGC)
                                                                                                   'b0203' : 1 #Trna alaV (UGC)
                                                                                                  }}},
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
######################################################
                'cmnm5U_to_nm5U' : {'name' : 'mod_5-aminomethyluridine',
                                    'input' : 'cmnm5U',
                                   'output' : 'nm5U',
                            'machines' : {'MnmC_mono_mod_fad' : {'proteins' : {'b2324' : 'MnmCD'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0749' : 1, #trna lysQ (SUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (SUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (SUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (SUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (SUU)#mnm5s2U  
                                                                                         'b0748' : 1, #trna lysZ (SUU)#mnm5s2U
                                                                                         'b0536' :1, #trna argU ({CU) #mnm5U @34
                                                                                        'b3978' : 1, #trna GlyT ({CC)#mnm5U
                                                                                         'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1 #trna gltW (SUC) #mnm5s2U
                                                                                        }}},
                                                                 
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'glx_c' :1 }
                                  }, #end
######################################################
                'cmnm5U_to_cmnm5Um' : {'name' : 'mod_5-carboxymethylaminomethyl-2-O-methyluridine',
                                      'input' : 'cmnm5U',
                                   'output' : 'cmnm5Um',
                            'machines' : {'trmL_dim' : {'proteins' : {'b3606' : 'TrmL'},  ####not in model important
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b1909' : 1}}},#'trnaLeuZ'
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c' : -1 ,
                                             'h_c' : 1,
                                            'ahcys_c' : 1}
                                  }, #end
######################################################
                'cmnm5U_to_cmnm5s2U' : {'name' : 'mod_5-carboxymethylaminomethyl-2-thiouridine',
                                        'input' : 'cmnm5U',
                                        'output' : 'cmnm5s2U',
                                        'machines' : {'TrmU_mono' : {'proteins' : {'b1133' : 'MnmA'},
                                                                     'RNA_position_substrates' : {'tRNA' : {34 : {'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1 }}
                                                                                                 }, #trna GlnU (UUG)
                                                                     'carriers' : {'IscS_mod_2:pydx5p_mod_1:SH': -1,
                                                                                   'trdrd_c': -1,
                                                                                   'IscS_mod_2:pydx5p': 1,
                                                                                   'trdox_c': 1},
                                                                     'additional_enzymes' : {
                    'YheLMN_cplx' :1 ,
                    'YccK_mono' :1, 
                    'YhhP_mono' : 1}
                                                         #A sulfur relay system consisting of 
                    #IscS and the TusABCDE proteins is required for delivery of the sulfur atom}
                    #http://ecocyc.org/ECOLI/NEW-IMAGE?type=REACTION&object=RXN0-2023
                    
                                                      }
                                          },
                            'metabolites' : {'atp_c' : -1,
                                             'amp_c' : 1,
                                             'ppi_c' : 1,
                                             'h_c' : 1
                                            }
                                  }, #end
######################################################
                'cmnm5se2U_to_nm5se2U' : {'name' : 'mod_5-aminomethyl-2-selenouridine',
                                          'input' : 'cmnm5se2U',
                                   'output' : 'nm5se2U',
                           'machines' : {'MnmC_mono_mod_fad' : {'proteins' : {'b2324' : 'MnmCD'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 :{'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                        'b0749' : 1, #trna lysQ (SUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (SUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (SUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (SUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (SUU)#mnm5s2U  
                                                                                         'b0748' : 1 #trna lysZ (SUU)#mnm5s2U
                                                                                       }}}, #mnm5s2U
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'glx_c' :1 }
                                  }, #end
######################################################
                'cmnm5s2U_to_nm5s2U' : {'name' : 'mod_5-aminomethyl-2-thiouridine',
                                        'input' : 'cmnm5s2U',
                                   'output' : 'nm5s2U',
                            'machines' : {'MnmC_mono_mod_fad' : {'proteins' : {'b2324' : 'MnmCD'},
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b3969' : 1, #trna gltT (SUC) #mnm5s2U
                                                                                         'b3757' : 1, #trna gltU (SUC) #mnm5s2U
                                                                                         'b4008' : 1, #trna gltV (SUC) #mnm5s2U
                                                                                         'b2590' : 1, #trna gltW (SUC) #mnm5s2U
                                                                                        'b0749' : 1, #trna lysQ (SUU)#mnm5s2U 
                                                                                         'b0743' : 1, #trna lysT (SUU) #mnm5s2U 
                                                                                         'b2404' : 1, #trna lysV (SUU) #mnm5s2U 
                                                                                         'b0747' : 1, #trna lysY (SUU)#mnm5s2U 
                                                                                         'b0745' : 1, #trna lysW (SUU)#mnm5s2U  
                                                                                         'b0748' : 1 #trna lysZ (SUU)#mnm5s2U
                                                                                        }}}, 
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'glx_c' :1 }
                                  }, #end
######################################################
                'U_to_acp3U' : {'name' : 'mod_3-amino-3-carboxypropyluridine',
                                        'input' : 'U',
                                   'output' : 'acp3U',
                            'machines' : {'enzyme_unknown' : {'proteins' : {'bnum' : 'name'},
                                                      'RNA_position_substrates' : {'tRNA' : {47 : {'b2967' : 1,#trna pheV (GAA)
                                                                                         'b4134' : 1}}}, #trna PheU (GAA)
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'amet_c': -1,
                                             '5mta_c': 1,
                                             'h_c': 1}
                                  }, #end
               
             
######################################################
                'cmnm5s2U_to_cmnm5se2U' : {'name' : 'mod_5-carboxymethylaminomethyl-2-selenouridine',
                                           'input' : 'cmnm5s2U',
                                   'output' : 'cmnm5se2U',
                            'machines' : {'YbbB_dim' : {'proteins' : {'b0503' : 'MnmH'},   #important not in model
                                                      'RNA_position_substrates' : {'tRNA' : {34 : {'b0668' : 1 , #trna GlnW (UUG)
                                                                                         'b0670' : 1}}}, #trna GlnU (UUG)
                                                                                         
                                                      'carriers' : None
                                                      }
                                          },
                            'metabolites' : {'selnp_c' : -1,
                                            'H2O3PS_c' : 1} #new metabolite
                                       #thiophosphate important
                                  } #end
               }
######################################################
               
               
#               'modification' : {'name' : '',
                                 #'input' : '',
                                #'output' : '',
#                            'machines' : {'enzyme' : {'proteins' : {'bnum' : 'name'},
#                                                      'rna_type' : '',
#                                                      'RNA_position_substrates' : {position : {'substrate' : 1}},
#                                                      'carriers' : None
#                                                      }
#                                          },
#                            'metabolites' : {}
#                                  }, #end
#               ######################################################