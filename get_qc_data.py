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

    region_data_df = pd.read_csv(
        'https://raw.githubusercontent.com/pboardman/covid19-data-quebec/master/csv/region.csv')
    region_data_df.date = pd.to_datetime(region_data_df.date)
    region_data_df.total_case = pd.to_numeric(
        region_data_df.total_case, errors='coerce')  # .astype('Int64')
    region_data_df.new_case = pd.to_numeric(
        region_data_df.new_case, errors='coerce')  # .astype('Int64')

    mtl_data_df = pd.read_csv(
        'https://raw.githubusercontent.com/pboardman/covid19-data-quebec/master/csv/montreal.csv')
    mtl_data_df.date = pd.to_datetime(mtl_data_df.date)
    mtl_data_df.total_case = pd.to_numeric(
        mtl_data_df.total_case, errors='coerce')  # .astype('Int64')

    mtl_ed_df = pd.read_csv(
        'https://www.dropbox.com/s/w7n297w7pnapezn/dailyMontrealEdStats.csv?dl=1')
    mtl_ed_df.date = pd.to_datetime(mtl_ed_df.date)

    # return qc_data_df
    return qc_data_df, region_data_df, mtl_data_df, mtl_ed_df
