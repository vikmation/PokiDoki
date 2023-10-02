from pokidoki import agent


#each config file contains all the necessary data 
agent(path_to_player_one_config_file, path_to_player_two_config_file, path_to_player_three_config_file, path_to_player_four_config_file, api_key, model_name, logging=True, gradio=true, number_of_games, speed)

agent(
    path_to_player_config_files=[
        "player_one.yaml",
        "player_two.yaml",
        # ...
    ],
    api_key="your_api_key",
    model_name="model_name",
    table_config="table_config.yaml",
    game_rules="game_rules.yaml",
    simulation_config="simulation_config.yaml",
    logging_config="logging_config.yaml"
)