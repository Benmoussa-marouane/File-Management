import re

# sort a list of complex string name using a regex patterns
def grp(pat, txt): 
     r = re.search(pat, txt)
     return r.group(0)

    


if __name__ == "__main__":

        pattern = '_D_([0-9]*)'
        # sort list by direction
        quartier_id = [

    's_N_quartier_01_D_140_V_3_xmax_75.0_ymin_-75.0_ymax_75.0',
    's_N_quartier_01_D_080_V_3_xmax_75.0_ymin_-75.0_ymax_75.0', 
    's_N_quartier_01_D_080_V_1.5_xmax_75.0_ymin_-75.0_ymax_75.0',
    's_N_quartier_01_D_200_V_1.5_xmax_75.0_ymin_-75.0_ymax_75.0', 
    's_N_quartier_01_D_140_V_1.5_xmax_75.0_ymin_-75.0_ymax_75.0',
    's_N_quartier_01_D_080_V_5_xmax_75.0_ymin_-75.0_ymax_75.0', 
    's_N_quartier_01_D_020_V_1.5_xmax_75.0_ymin_-75.0_ymax_75.0',
    's_N_quartier_01_D_020_V_3_xmax_75.0_ymin_-75.0_ymax_75.0', 
    's_N_quartier_01_rotated_180_D_020_V_5_xmax_75.0_ymin_-75.0_ymax_75.0',
    's_N_quartier_09_rotated_270_D_240_V_4_xmax_75.0_ymin_-85.0_ymax_65.0',
    's_N_quartier_09_rotated_90_D_000_V_6_xmax_75.0_ymin_-65.0_ymax_85.0', 
    's_N_quartier_09_rotated_90_D_120_V_2_xmax_75.0_ymin_-65.0_ymax_85.0', 
    's_N_quartier_09_rotated_90_D_240_V_4_xmax_75.0_ymin_-65.0_ymax_85.0', 
    's_N_quartier_09_rotated_90_D_300_V_4_xmax_75.0_ymin_-65.0_ymax_85.0',
    's_N_quartier_09_rotated_90_D_300_V_6_xmax_75.0_ymin_-65.0_ymax_85.0', 
     's_N_quartier_09_rotated_90_D_240_V_6_xmax_75.0_ymin_-65.0_ymax_85.0', 
    's_N_quartier_09_rotated_90_D_300_V_2_xmax_75.0_ymin_-65.0_ymax_85.0'

    ]

        quartier_id.sort( key =  lambda  l: grp(pattern, l)) 

        print(quartier_id)