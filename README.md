# PokiDoki

This is an Python package to simulate the game of poker with large language. its a game with four players and each player can be given a different personality.

If you like this work, consider joining our [![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/Qy69gzmpt4).

## Installation

```sh
pip install pokidoki
```

## Usage 

The game exists of four players. Each player needs to get configured in a yaml file as follows:

```yaml
playerName: "Player One"

# Attributes of the player, these can be used to dictate the player's behavior if it's an AI player
attributes:
  aggressiveness: 7  # on a scale of 1-10
  riskTolerance: 5   # on a scale of 1-10
  strategy: "balanced" # could also be "aggressive", "defensive", "random" etc.

description: #short description of the personality

# The initial number of chips the player has at the start of the game
chips: 1000
```

To start the simulation we need also a yaml file for configuring the table config as following:

```yaml
Table limit min: 20
Table limit max: 
Small blind: 20
Big blind: 20
```

In this scenario we defining the minimum amount a player can play as 20 and the empty field for the maximum value means their is no maximum value. The respective values for small and big blind are also set.

To start the simulation call the agent as follows:

```python
from poki_doki import agent 

agent(
    path_to_player_config_files=[
        "player_one.yaml",
        "player_two.yaml",
        "player_three.yaml",
        "player_four.yaml"
    ],
    api_key="openai_key",
    model_name="model_name",
    table_config="table_config.yaml",
    logging="true",
)
```

The result is displayed as plot and if the logging is set to true all player actions are logged as well.

Result:

**some plot image**

### Gradio 

There is also a more interactive and entertaining Gradio demo for the poker simulation. See details [here](link to gradio)


## Todo 

- [ ] Create a Gradio demo
- [ ] Make experiments possible with dynamic inputs
- [ ] Improve error handling / code refactoring
- [ ] Add support for other models
 

## Citation 

```bibtex
@article{horton2023large,
  title={Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?},
  author={Horton, John J},
  journal={arXiv preprint arXiv:2301.07543},
  year={2023}
}
```
