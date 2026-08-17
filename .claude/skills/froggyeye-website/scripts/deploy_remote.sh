#!/bin/bash
# Runs ON the Hostinger shared-hosting account (fetched and executed by the
# temporary cron job that scripts/deploy.py creates via the Hostinger API).
# Pulls the latest main tarball from GitHub and syncs public_html/ into the
# live docroot. Idempotent — safe to run repeatedly.
set -e
cd /home/u384964577
rm -rf deploy_tmp
mkdir deploy_tmp
curl -sL https://codeload.github.com/FroggyEye-Ltd/froggyeye-ltd.github.io/tar.gz/main -o deploy_tmp/site.tgz
tar -xzf deploy_tmp/site.tgz -C deploy_tmp
# The .well-known / .htaccess excludes below are unanchored, so they match at
# EVERY level — which silently swallowed the ApexRoute app-association files and
# its /r/ rewrite. These includes come first (rsync takes the first match) and
# are anchored to the transfer root, so only that one subdomain folder is opted
# back in; the docroot's own server-managed .well-known and .htaccess stay
# untouched, as do every other subdomain's.
rsync -a --delete \
  --include='/apexroute/.well-known/***' --include='/apexroute/.htaccess' \
  --exclude=.well-known --exclude=.htaccess --exclude=error_log \
  --exclude=cgi-bin --exclude='*.log' \
  deploy_tmp/froggyeye-ltd.github.io-main/public_html/ \
  domains/froggyeye.com/public_html/
rm -rf deploy_tmp
echo "DEPLOYED $(cat domains/froggyeye.com/public_html/version.txt)"
