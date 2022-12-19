import visual as v
import input_data as ind
import data_processing as dp
import user_interfase as ui

import os

def click_button():
    os.system('cls')
    r = ui.select_mode()
    v.print_mode(r)
    match (r):
        case 1:
            v.res_operation(dp.new_contact(ind.input_data()),r)
        case 2:
            v.res_operation(dp.serch_cont(ind.serch_contact()), r)
        case 3:
            v.res_operation(v.print_phonebook(),r)
        case 4:
            v.res_operation(dp.del_cont(ind.serch_for_del()), r)
        case 5:
            v.res_operation(dp.file_del(), r)
        case 6:
            v.res_operation(dp.csv_to_json(), r)
        case 7:
            v.res_operation(dp.json_to_csv(), r)
 
    
    