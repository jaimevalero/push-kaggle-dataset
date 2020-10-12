# Push Kaggle Dataset action

This action push data from a github repository to a dataset at [kaggle.](https://kaggle.com)   

Use this action to keep synchronized your datasets at kaggle with your repositories.

Please bear in mind that this action do NOT work with kernels nor notebooks, so it is of not use on competitions.


## Inputs

### `id`

Dataset identifier in format {username}/{dataset}). Default is `"{KAGGLE_USERNAME}/{GITHUB_REPO_NAME}"`
Where KAGGLE_USERNAME is a secret - see sections [secret](#Secret)
You cannot upload data to other kaggle user.

### `files`

Files to upload. Default is `"*.csv"`

### `title`

Title of the dataset.

Only if it is a new dataset. Otherwise it is not used.
Default is the dataset id.

*Eg: if the dataset is mlg-ulb/creditcardfraud, the default title would be 'creditcardfraud'*

### `subtitle`

Subtitle of the dataset. We highly recommend entering a subtitle for your Dataset.
Only if it is a new dataset. Otherwise it is not used.
Must be between 20 and 80 characters. If the subtitle has fewer than 20 characters, trailing white spaces are added.

### `description`

Description of the dataset, only if it has to be created.
Only if it is a new dataset. Otherwise it is not used.

### `is_public`

Visibility of the the new dataset. Boolean (True or False)
Default is `"*.False"`- private datasets are created by default.
Only if it is a new dataset. Otherwise it is not used.

## Secrets

You have to configure your secrets at: Settings >> Secrets

- ` ${{ secrets.KAGGLE_USERNAME }}` - **Required** The dataset owner.
- ` ${{ secrets.KAGGLE_KEY }}` - **Required** The API key for your user. You can [create your api key here.](https://www.kaggle.com/account)   

## Examples usage

Create a main.yml file like this in the path your repo, in the path `.github/workflows/main.yml`

Change the fields in that yaml : id, files, title, subtitle and description.
Add the secrets.

Please consider that if you are NOT creating a new dataset, only updating it, title, subtitle, description and is_public are not used.

## Example

### Example1 : Create a new dataset, uploading a file, "titanic.csv"
```yaml

name: upload

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  upload:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      # Runs a single command using the runners shell
      - name: Upload datasets
        uses: jaimevalero/push-kaggle-dataset@v1 # This is the action
        env:
          # Do not leak your credentials.
          KAGGLE_USERNAME: ${{ secrets.KAGGLE_USERNAME }}
          KAGGLE_KEY: ${{ secrets.KAGGLE_KEY }}

        with:
          id:  "jaimevalero/my-new-dataset"
          title: "Testing github actions for upload datasets"
          subtitle: "Titanic data2"
          description: "## Example of dataset syncronized by github actions <br/>Source https://github.com/jaimevalero/test-actions and https://github.com/jaimevalero/push-kaggle-dataset <br/> "
          files:  titanic.csv
          is_public: true

```

### Example2 : Add more than one file

You can use
 - wildcards (eg: *.xlsx )
 - directory names (eg: images )

Please bear in mind that files in subdirectories are packaged in tar file.

In case you use more than one line, you should use the "|" operator.

```yaml


          files: |
            titanic.csv
            *.xlsx
            images

```
