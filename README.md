# MTB Voodoo
## Mountain Bike Trail Recommender
------------
## Background
With 2020 there has been a huge surge to embrace remote work. As such, more people are seeking to get outdoors and experience what nature has to offer. One of the great ways to do this is mountain biking- a cross-section of exercise and the scenic outdoors. Google trends and Alexa ranks for trailforks.com illustrates a strong demand for information about mountain bike trails. 

## More data than you would think
Trailforks.com, mtbproject.com, singletracks.com provide detailed information for trails across the world. The trail information is augmented with user reviews, ride logs, descriptions of the trails and sometimes they include gps coordinate files of the entire trail. User-trail ridelogs for just Washington amounted to over a million data points.

## A large task
While trailforks provides a pleathora of data, it remains largely inaccesible in a rapid-fire manner. A user can drill down by country, region, and locality, and also filter by trail features but it remains a dedicated effort. There is a huge opportunity to provide a user-aware and trail-aware recommendation for a user to find their next best ride. 

## An Answer
MTB Voodoo is simple: Give the user the power to get trails similar to ones they have liked and plan their next trip. For users who don't have ridelogs yet (the cold-start problem) trailforks is already surprisingly good at supplying users with rich "local popularity" figures which can help you find highly rated trails to hone your skills or test out a new bike.

### Methodology: Collaborative Filtering
Top 5 trail recommendations can be achieved by using the implicit rating that a user has given certain trails (number of rides) and through collaborative filtering to tease out user groups that are similar. Trails are then recommended based on a KNN approach using the Surprise library. A lightfm approach is in the works as well.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
