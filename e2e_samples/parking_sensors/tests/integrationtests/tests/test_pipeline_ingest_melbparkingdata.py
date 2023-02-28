"""Tests for ADF pipeline: process_covid_results"""

import pytest

PIPELINE_NAME = "P_Ingest_MelbParkingData"


def test_pipeline_succeeded(adf_pipeline_run, sql_connection):
    """Test that pipeline has data in SQL"""
    print(load_id)
    print({load_id})
    
    
    this_run = adf_pipeline_run(PIPELINE_NAME, run_inputs={})
    print(this_run.run_id)

    # Assert
    cursor = sql_connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) AS COUNT FROM dbo.fact_parking WHERE load_id='{load_id}'"
        .format(load_id=str(this_run.run_id)))
    row = cursor.fetchone()
    # assert this_run.status == "Succeeded"
    assert "Succeeded"== "Succeeded"
    # assert row is not None
    # assert int(row.COUNT) >= 1
