from masw_fwi.pipeline import run_pipeline


def test_run_pipeline_returns_status_message() -> None:
    assert run_pipeline() == "Pipeline scaffold is ready."
