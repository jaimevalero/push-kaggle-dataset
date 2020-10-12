# Push Kaggle Dataset action

This action push data from a github repository to a dataset at [kaggle.](https://kaggle.com)   


Use this action to keep synchronized your datasets at kaggle with your repositories.

## Inputs

### `who-to-greet`

**Required** The name of the person to greet. Default `"World"`.

### `id`

Dataset identifier in format {username}/{dataset}). Default is `"{KAGGLE_USERNAME}/{GITHUB_REPO_NAME}"`

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
Must be between 20 and 80 characters.

### `description`

Description of the dataset, only if it has to be created.
Only if it is a new dataset. Otherwise it is not used.

### `is_public`

Visibility of the the new dataset. Boolean (True or False)
Default is `"*.False"`- private datasets are created by default.
Only if it is a new dataset. Otherwise it is not used.

## Secrets

You have to configure your secrets at Settings >> Secrets

- ` ${{ secrets.KAGGLE_USERNAME }}` - **Required** The dataset owner.
- ` ${{ secrets.KAGGLE_KEY }}` - **Required** The API key for your user. You can [create your api key here.](https://www.kaggle.com/account)   

## Examples usage


## Example

Deploy an application in the root directory to `production`:

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
        uses: jaimevalero/push-kaggle-dataset@develop # This is the action
        env:
          # Do not leak your credentials.
          KAGGLE_USERNAME: ${{ secrets.KAGGLE_USERNAME }}
          KAGGLE_KEY: ${{ secrets.KAGGLE_KEY }}

        with:
          id:  "jaimevalero/my-new-dataset"
          is_public: false

          title: "Testing github actions for upload datasets"

          subtitle: "We highly recommend entering a subtitle for your Dataset (20-80 characters)."

          description: "## Description in MD syntax <br/>Source https://github.com/jaimevalero/test-actions "
          files:  titanic.csv



```

```yaml

name: upload
jobs:
  # This workflow contains a single job called "build"
  upload:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest
    jobs:
      # This workflow contains a single job called "build"
      upload:
        # The type of runner that the job will run on
        runs-on: ubuntu-latest

        # Steps represent a sequence of tasks that will be executed as part of the job
        steps:
          # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
          - uses: actions/checkout@v2
          - name: Upload datasets
            uses: jaimevalero/push-kaggle-dataset@v1 # This is the action
            env:
              # Do not leak your credentials.
              KAGGLE_USERNAME: ${{ secrets.KAGGLE_USERNAME }}
              KAGGLE_KEY: ${{ secrets.KAGGLE_KEY }}
            with:
              # Data of the dataset to be created.
              id:  "jaimevalero/test202010111235"
              title: "Testing github actions for upload datasets"
              subtitle: "We highly recommend entering a subtitle for your Dataset (20-80 characters)."
              description: "## Description in MD syntax <br/>Source https://github.com/jaimevalero/test-actions "
              files: titanic.csv

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      - name: Upload datasets
        uses: jaimevalero/push-kaggle-dataset@v1 # This is the action
        env:
          # Do not leak your credentials.
          KAGGLE_USERNAME: ${{ secrets.KAGGLE_USERNAME }}
          KAGGLE_KEY: ${{ secrets.KAGGLE_KEY }}
        with:
          id:  "jaimevalero/test202010111235"
          title: "Testing github actions for upload datasets"
          subtitle: "We highly recommend entering a subtitle for your Dataset (20-80 characters)."
          description: "## Description in MD syntax <br/>Source https://github.com/jaimevalero/test-actions "
          files: |
            titanic.csv
            *.xlsx
            images



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
          is_public: false
          title: "Testing github actions for upload datasets"
          subtitle: "We highly recommend entering a subtitle for your Dataset (20-80 characters)."
          description: "## Description in MD syntax <br/>Source https://github.com/jaimevalero/test-actions "
          files: |
            titanic.csv
            *.xlsx
            images


```



uses: actions/hello-world-docker-action@v1
with:
  who-to-greet: 'Mona the Octocat'



  id:
    description: "Dataset identifier in format {username}/{dataset})."
    required: true

  files:
    description: "Files to upload."
    required: true
    default: "*.csv"

  title:
    description: "Title of the dataset, only if it has to be created."
    required: false
    default: "dataset id"

  subtitle:
    description: "Subtitle of the dataset. Must be between 20 and 80 characters"
    required: false
    default: ""

  description:
    description: "Description of the dataset, only if it has to be created."
    required: false
    default: ""

  is_public:
    description: "Create publicly (default is private)."
    required: false
    default: false

  version_notes:
    description: 'Message describing the new version'
    required: false
    default: commit message
