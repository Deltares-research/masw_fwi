"""Command-line entry point for masw_fwi."""

from masw_fwi.pipeline import run_pipeline


def main() -> None:
    run_pipeline()


if __name__ == "__main__":
    main()
