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

Subtitle of the dataset.
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

- ` ${{ secrets.KAGGLE_USERNAME }}` - **Required** The dataset owner.
- ` ${{ secrets.KAGGLE_KEY }}` - **Required** The API key for your user. You can [create your api key here.](https://www.kaggle.com/account)   

## Example usage

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
