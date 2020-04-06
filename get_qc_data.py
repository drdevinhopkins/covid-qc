import pandas as pd


def load_qc_data():
    qc_data_df = pd.read_csv(
        'https://raw.githubusercontent.com/pboardman/covid19-data-quebec/master/csv/total.csv')
    qc_data_df.date = pd.to_datetime(qc_data_df.date)
    qc_data_df.total_case = pd.to_numeric(
        qc_data_df.total_case, errors='coerce')
    qc_data_df.total_death = pd.to_numeric(
        qc_data_df.total_death, errors='coerce')
    qc_data_df.total_recovered = pd.to_numeric(
        qc_data_df.total_recovered, errors='coerce')
    qc_data_df.hospitalisations = pd.to_numeric(
        qc_data_df.hospitalisations, errors='coerce')
    qc_data_df.ICU = pd.to_numeric(qc_data_df.ICU, errors='coerce')
    # qc_data_df.total_case = qc_data_df.total_case.astype('Int64')
    # qc_data_df.total_death = qc_data_df.total_death.astype('Int64')
    # qc_data_df.total_recovered = qc_data_df.total_recovered.astype('Int64')
    # qc_data_df.hospitalisations = qc_data_df.hospitalisations.astype('Int64')
    # qc_data_df.ICU = qc_data_df.ICU.astype('Int64')
    return qc_data_df
