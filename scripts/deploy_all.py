from aws_data_landing_zone import Scripts
from data_landing_zone_example_python.config_minimum import config

scripts = Scripts()
scripts.deploy_all(props=config)
