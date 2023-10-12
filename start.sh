

#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/firefox ]]; then
  echo "...Downloading Firefox"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=ru
  tar xjf ./firefox-*.tar.bz2 $STORAGE_DIR/firefox
  rm firefox-*.tar.bz2
  cd $HOME/project/src # Make sure we return to where we were
else
  echo "...Using Firefox from cache"
fi

# be sure to add Chromes location to the PATH as part of your Start Command
# export PATH="${PATH}:/opt/render/project/.render/chrome/opt/google/chrome"

# add your own build commands...