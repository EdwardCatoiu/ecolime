
#trying something new
uridine_mods_paths = {'U_to_DDusA' : {'upstream_rxns' : ['U'],
                                 'enzymes' : {20:['DusA_mono'],
                                             '20A':['DusA_mono'],
                                             17:['DusA_mono'],
                                             16:['DusA_mono']}},
                      'U_to_DDusgen' : {'upstream_rxns' : ['U'],
                                 'enzymes' : {20:['generic_Dus'],
                                             '20A':['generic_Dus'],
                                             17:['generic_Dus'],
                                             16:['generic_Dus']}},
                     'U_to_Um' : {'upstream_rxns' : ['U'],
                                  'enzymes' : {2552:['RrmJ_mono'],
                                              32 : ['TrmJ_dim'],
                                              34 :['trmL_dim' ]}},
                     
                     'U_to_Y' : {'upstream_rxns' : ['U'],
                                'enzymes' : {32:['RluA_mono'],
                                            746 : ['RluA_mono'],
                                           2605:['RluB_mono'],
                                            2504 :['RluC_mono'],
                                             2580:['RluC_mono'],
                                             995 :[ 'RluC_mono'],
                                             1915:['RluD_mono_mod_1:mg2'],
                                             1911:['RluD_mono_mod_1:mg2'],
                                             1917:['RluD_mono_mod_1:mg2'],
                                             2457 :['YmfC_mono'],
                                             2604 :[ 'YjbC_mono'],
                                             13 :[ 'TruD_mono'],
                                             65 :[ 'YqcB_mono'],
                                            55 : ['TruB_mono'],
                                            38 : ['TruA_dim'],
                                             39 :[ 'TruA_dim'],
                                             40 : ['TruA_dim'],
                                             516 :['RsuA_mono']}
                                },
                     
                     'U_to_acp3U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {47:['enzyme_unknown']}},
                     
                     'U_to_cmnm5U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                     
                     'U_to_ho5U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {34:['enzyme_unknown2']}},
                     
                     'U_to_m3U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {1498:['YggJ_dim']}},
                     
                     'U_to_m5U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {747:['RumB_mono_mod_1:4fe4s'],
                                                 1939:['RumA_mono_mod_1:4fe4s'],
                                                 54 :['TrmA_mono']
                                                 }},
                     
                     'U_to_nm5U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                     
                     'U_to_s2U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {34:['TrmU_mono']}},
                     
                     'U_to_s4U' : {'upstream_rxns' : ['U'],
                                     'enzymes' : {8:['ThiI_mono']}},
                     
                     'ho5U_to_mo5U' : {'upstream_rxns' : ['U_to_ho5U'],
                                     'enzymes' : {34:['YecP_mono']}},
                     
                     's2U_to_nm5s2U' : {'upstream_rxns' : ['U_to_s2U'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                     
                     'cmnm5U_to_cmnm5s2U' : {'upstream_rxns' : ['U_to_cmnm5U'],
                                             'enzymes' : {34:['TrmU_mono']}},
                                             
                     's2U_to_ges2U' : {'upstream_rxns' : ['U_to_s2U'],
                                     'enzymes' : {34:['YbbB_dim']}},
                                             
                     's2U_to_se2U' : {'upstream_rxns' : ['U_to_s2U'],
                                     'enzymes' : {34:['YbbB_dim']}}, # this is a guess!
                                             
                     's2U_to_cmnm5s2U' : {'upstream_rxns' : ['U_to_s2U'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                                             
                     'cmnm5s2U_to_cmnm5se2U' : {'upstream_rxns' : ['s2U_to_cmnm5s2U','cmnm5U_to_cmnm5s2U'],
                                     'enzymes' : {34:['YbbB_dim']}},
                                             
                     'mnm5s2U_to_mnm5ges2U' : {'upstream_rxns' : ['nm5s2U_to_mnm5s2U','mnm5U_to_mnm5s2U'],
                                     'enzymes' : {34:['YbbB_dim']}},
                                             
                     'cmnm5se2U_to_nm5se2U' : {'upstream_rxns' : ['se2U_to_cmnm5se2U','cmnm5s2U_to_cmnm5se2U'],
                                     'enzymes' : {34:['MnmC_mono_mod_fad']}},
                                               
                     'Y_to_m3Y' : {'upstream_rxns' : ['U_to_Y'],
                                     'enzymes' : {1915:['RlmH_dim']}},
                                               
                     'se2U_to_cmnm5se2U' : {'upstream_rxns' : ['s2U_to_se2U'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                                               
                     'cmnm5s2U_to_nm5s2U' : {'upstream_rxns' : ['s2U_to_cmnm5s2U','cmnm5U_to_cmnm5s2U'],
                                     'enzymes' : {34:['MnmC_mono_mod_fad']}},
                                               
                     'nm5se2U_to_mnm5se2U' : {'upstream_rxns' : ['cmnm5se2U_to_nm5se2U',  'se2U_to_nm5se2U' ,'nm5s2U_to_nm5se2U'],
                                     'enzymes' : {34:['MnmC_mono_mod_fad']}},
                                               
                     'mnm5s2U_to_mnm5se2U' : {'upstream_rxns' : ['nm5s2U_to_mnm5s2U','mnm5U_to_mnm5s2U'],
                                     'enzymes' : {34:['YbbB_dim']}},
                                               
                     'mnm5U_to_mnm5s2U' : {'upstream_rxns' : ['nm5U_to_mnm5U'],
                                     'enzymes' : {34:['TrmU_mono']}},
                                               
                     'nm5s2U_to_nm5se2U' : {'upstream_rxns' : ['s2U_to_nm5s2U','cmnm5s2U_to_nm5s2U'],
                                     'enzymes' : {34:['YbbB_dim']}},
                                               
                     'nm5s2U_to_mnm5s2U' : {'upstream_rxns' : ['s2U_to_nm5s2U','cmnm5s2U_to_nm5s2U'],
                                     'enzymes' : {34:['MnmC_mono_mod_fad']}},
                                               
                     'se2U_to_nm5se2U' : {'upstream_rxns' : ['s2U_to_se2U'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                                               
                     'cmnm5U_to_nm5U' : {'upstream_rxns' : ['U_to_cmnm5U'],
                                     'enzymes' : {34:['MnmC_mono_mod_fad']}},
                                               
                     'cmnm5U_to_cmnm5Um' : {'upstream_rxns' : ['U_to_cmnm5U'],
                                     'enzymes' : {34:['trmL_dim']}},
                                               
                     'Um_to_cmnm5Um' : {'upstream_rxns' : ['U_to_Um'],
                                     'enzymes' : {34:['MnmEG_cplx_mod_fad_mod_2:k']}},
                                               
                     'nm5U_to_mnm5U' : {'upstream_rxns' : ['U_to_nm5U', 'cmnm5U_to_nm5U'],
                                     'enzymes' : {34:['MnmC_mono_mod_fad']}},
                                               
                     'ho5U_to_cmo5U' : {'upstream_rxns' : ['U_to_ho5U'],
                                     'enzymes' : {34:['YecP_mono']}
                                       }}

                                               
                                               
cytidine_mods_paths = {'C_to_s2C' : {'upstream_rxns' : ['C'],
                                     'enzymes' : {32:['YdaO_mono']}},
                     
                     'C_to_m5C' : {'upstream_rxns' : ['C'],
                                     'enzymes' : {1962:['RlmI_dim'],
                                                 967 : ['RsmB_mono'],
                                                 1407 : ['RsmF_mono']}},
                     
                     'C_to_Cm' : {'upstream_rxns' : ['C'],
                                     'enzymes' : {2498:['RlmM_mono'],
                                                 1402:['RsmI_mono'],
                                                 32:['TrmJ_dim'],
                                                 34 : ['trmL_dim']}},
                     
                     'C_to_ac4C' : {'upstream_rxns' : ['C'],
                                     'enzymes' : {34:['TmcA_mono']}},
                     
                     'Cm_to_m4Cm' : {'upstream_rxns' : ['C_to_Cm'],
                                     'enzymes' : {1402:['RsmH_mono']}},
                     
                     'm4Cm_to_m44Cm' : {'upstream_rxns' : ['Cm_to_m4Cm','m4C_to_m4Cm'],
                                     'enzymes' : {1402:['RsmH_mono']}},
                     
                     'C_to_m4C' : {'upstream_rxns' : ['C'],
                                     'enzymes' : {1402:['RsmH_mono']}},
                     
                     'm4C_to_m44C' : {'upstream_rxns' : ['C_to_m4C'],
                                     'enzymes' : {1402:['RsmI_mono']}},
                     
                     'm4C_to_m4Cm' : {'upstream_rxns' : ['C_to_m4C'],
                                     'enzymes' : {1402:['RsmH_mono']}},
                     
                     'C_to_k2C' : {'upstream_rxns' : ['C'],
                                     'enzymes' : {34:['TilS_mono']}}
    
}




adenine_mods_paths ={'A_to_m2A' : {'upstream_rxns' : ['A'],
                                     'enzymes' : {37:['RlmN_mono_mod_1:4fe4s'],
                                                 2503:['RlmN_mono_mod_1:4fe4s']}},
                    
                    'A_to_m6A' : {'upstream_rxns' : ['A'],
                                     'enzymes' : {2058:['enzyme_new_ErmBC'],
                                                 1618:['RlmF_mono'],
                                                 2030:['enzyme_new_RlmJ'],
                                                 1518:['KsgA_mono'],
                                                  1519:['KsgA_mono'],
                                                 37:['YfiC_mono']}},
                    
                    'm6A_to_m66A' : {'upstream_rxns' : ['A_to_m6A'],
                                     'enzymes' : { 1518:['KsgA_mono'],
                                                  1519:['KsgA_mono']}},
                    
                    'A_to_I' : {'upstream_rxns' : ['A'],
                                     'enzymes' : {34:['TadA_dim_mod_2:zn2']}},
                    
                    'A_to_m1A' : {'upstream_rxns' : ['A'],
                                     'enzymes' : {1408:['enzyme_new_NpmA']}},
                    
                    'A_to_i6A' : {'upstream_rxns' : ['A'],
                                     'enzymes' : {37:['MiaA_dim_mod_2:mg2']}},
                    
                    'i6A_to_ms2i6A' : {'upstream_rxns' : ['A_to_i6A'],
                                     'enzymes' : {37:['MiaB_mono_mod_1:4fe4s']}},
                    
                    'A_to_t6A' : {'upstream_rxns' : ['A'],
                                     'enzymes' : {37:['TsaBCDE']}},
                    
                    't6A_to_m6t6A' : {'upstream_rxns' : ['A_to_t6A'],
                                     'enzymes' : {37:['EG11503_MONOMER']}},
                    
                    't6A_to_ct6A' : {'upstream_rxns' : ['A_to_t6A'],
                                     'enzymes' : {37:['TcdA_dim']}}      
                  
}









guanine_mods_paths={'G_to_m7G' : {'upstream_rxns' : ['G'],
                                     'enzymes' : {2069:['RlmL_dim'],
                                                 1405:['enzyme_new_RmtB'],
                                                 527:['RsmG_mono'],
                                                 46:['YggH_mono']}},
                   
                    'G_to_m2G' : {'upstream_rxns' : ['G'],
                                     'enzymes' : {1835:['RlmG_mono'],
                                                 2445:['RlmL_dim'],
                                                 1207:['RsmC_mono'],
                                                 966:['RsmD_mono'],
                                                 1516:['enzyme_new_RsmJ']
                                                 }},
                   
                    'G_to_Gm' : {'upstream_rxns' : ['G'],
                                     'enzymes' : {2251:['RlmB_dim'],
                                                 18:['TrmH_dim']}},
                   
                    'G_to_m1G' : {'upstream_rxns' : ['G'],
                                     'enzymes' : {745:['RrmA_dim_mod_2:zn2'],
                                                 37:['TrmD_dim']}},
                   
                    'G_to_preq1tRNA' : {'upstream_rxns' : ['G'],
                                     'enzymes' : {34:['Tgt_hexa_mod_6:zn2']}},
                   
                    'preq1tRNA_to_oQtRNA' : {'upstream_rxns' : ['G_to_preq1tRNA'],
                                     'enzymes' : {34:['QueA_mono']}},
                   
                    'oQtRNA_to_QtRNA' : {'upstream_rxns' : ['preq1tRNA_to_oQtRNA'],
                                     'enzymes' : {34:['QueG_mono_mod_adocbl']}},
                   
                    'QtRNA_to_gluQtRNA' : {'upstream_rxns' : ['oQtRNA_to_QtRNA'],
                                     'enzymes' : {34:['YadB_mono']}}
                  
    
}