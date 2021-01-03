#!/bin/bash
set -e

PACKAGE_NAME="python3-jookies-messaging"

# Get installed package version and install the related pypi package(s)
if [ "$(grep -Ei 'debian|buntu' /etc/*release)" ]; then
  PACKAGE_VERSION=$(dpkg -s "$PACKAGE_NAME"|grep ^Version:|awk '{print $2}')
  pip3 install python-messaging=="$PACKAGE_VERSION"
elif [ "$(grep -Ei 'centos|rhel|fedora' /etc/*release)" ]; then
  PACKAGE_VERSION=$(rpm -qi "$PACKAGE_NAME"|grep ^Version|awk {'print $3'})
  pip3 install python-messaging=="$PACKAGE_VERSION"
else
  echo "ERROR: Unsupported OS for this package."
  exit 1
fi

