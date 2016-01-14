#!/usr/bin/env bash
BRANCH=master
TARGET_REPO=ultramar/ultramar.github.io.git
PELICAN_OUTPUT_FOLDER=output
#if [ "$CI_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$CIRCLECI" == "true" ]; then
        git config --global user.email "ci@circle-ci.org"
        git config --global user.name "Circle CI"
    fi
    #using token clone gh-pages branch
    git clone --quiet --branch=$CIRCLE_BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null
    #go into directory and copy data we're interested in to that directory
    cd built_website
    rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
    #add, commit and push files
    git add -f .
    git commit -m "Circle CI build $CIRCLE_BUILD_NUM pushed to Github Pages"
    git push -fq origin $CIRCLE_BRANCH > /dev/null
    echo -e "Deploy completed\n"
#fi
