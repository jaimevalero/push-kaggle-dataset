# Push Kaggle Dataset action

This action push data from a github repository to a dataset at kaggle.

Use this action to keep synchronized your datasets at kaggle.com with your repositories.

## Inputs

### `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

## Outputs

### `time`

The time we greeted you.

## Example usage

uses: actions/hello-world-docker-action@v1
with:
  who-to-greet: 'Mona the Octocat'
