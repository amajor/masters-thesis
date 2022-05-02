#For every modules, the script generates number of violations for each pylint message along with git bugs.
import csv
from datastore.pg_store import PgDataStore

MASTER_PREDICTROS_BUGS_FILE = '../data/master_predictors_n_bugs.csv'

if __name__ == '__main__':

    pg_store = PgDataStore()
    all_msgs = pg_store.retrieve_distinct_msgs()
    all_msgs = [x[0] for x in all_msgs]

    all_modules = pg_store.retrieve_distinct_module_names()
    all_modules = [x[0] for x in all_modules]

    with open(MASTER_PREDICTROS_BUGS_FILE, 'w') as predictors_file:
        fieldnames = ['module_name']
        fieldnames.extend(all_msgs)
        fieldnames.extend(['n_bugs'])

        csv_output = csv.DictWriter(predictors_file, fieldnames=fieldnames)
        csv_output.writeheader()

        for module_name in all_modules:
            output_row = {'module_name': module_name}
            data = pg_store.retrieve_v_by_msg_bugs(module_name=module_name)

            for r in data:
                msg_type = r[1]     # pylint message (e.g.: bad variable name)
                n = r[2]            # number of violations of msg_type in module_name
                n_bugs = r[3]       # number of bugs obtained via git commits
                output_row[msg_type] = n
                output_row['n_bugs'] = n_bugs

            csv_output.writerow(output_row)