import subprocess

import typer

from utils.path_utils import get_project_root


def run_dbt_transformation():
    # Define the dbt CLI command to execute
    dbt_command = "dbt run --profile zoomcamp_project_dbt"

    # Execute the dbt CLI command using subprocess
    dbt_project_path = get_project_root() / "zoomcamp_project_dbt"
    result = subprocess.run(dbt_command, shell=True, capture_output=True, cwd=dbt_project_path)

    # Print the output of the dbt CLI command
    print(result.stdout.decode())


if __name__ == '__main__':
    typer.run(run_dbt_transformation)
