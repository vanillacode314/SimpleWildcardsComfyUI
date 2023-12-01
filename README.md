# SimpleWildcardsComfyUI

A simple wildcard node for ComfyUI. Can also be used a style prompt node.

## Where to place wildcard files

Place the wildcard files in the `wildcards` folder in the root of your comfyui directory.
The files should end in `.txt` and each value should be on it's own line.

## inputs

- `seed(INT)`: The seed to use to choose the wildcard.
- `control_after_generate`: What to do with the seed after queuing the prompt.
- `input_files(LIST)`: A glob for the input files to use.
- `input_text(LIST)`: Choose a line from the files yourself or select `*` to choose at random using seed.

## outputs

- `output_text(STRING)`: The generated string
