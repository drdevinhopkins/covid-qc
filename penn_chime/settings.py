#!/usr/bin/env python

from datetime import date

from .parameters import Parameters, Regions, Disposition


def get_defaults(qc_data_df):
    return Parameters(
        population=8537674,  # from wikipedia, default was 3600000
        current_hospitalized=qc_data_df.hospitalisations.dropna(
        ).iloc[-1],  # default was 69
        date_first_hospitalized=date(2020, 3, 19),  # defaul was 2020-03-7
        doubling_time=4.0,
        hospitalized=Disposition(0.025, 7),
        icu=Disposition(0.0075, 9),
        infectious_days=14,
        market_share=1.0,  # defaul was 0.15
        n_days=30,  # default was 100
        mitigation_date=date(2020, 3, 13),  # default was date.today()
        relative_contact_rate=0.3,  # default was 0.3
        ventilated=Disposition(0.005, 10),
    )
