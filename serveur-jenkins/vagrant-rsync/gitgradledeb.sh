#!/bin/sh

apt -y update
apt -y install zip unzip
apt -y install git

wget https://services.gradle.org/distributions/gradle-7.0.2-bin.zip -P /tmp
unzip -d /opt/gradle /tmp/gradle-*.zip
ls /opt/gradle/gradle-*

export GRADLE_HOME=/opt/gradle/gradle-7.0.2 >> /etc/profile.d/gradle.sh
export PATH=${GRADLE_HOME}/bin:${PATH}>> /etc/profile.d/gradle.sh

chmod +x /etc/profile.d/gradle.sh

/etc/profile.d/gradle.sh

gradle -v