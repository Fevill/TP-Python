#!/bin/bash

### PARANOIA MODE
set -u # en cas de variable non définie, arreter le script
set -e # en cas d'erreur (code de retour non-zero) arreter le script

install_ufw() {
	PACKAGE_NAME="ufw"
	if ! dpkg -l |grep --quiet "^ii.*$PACKAGE_NAME " ; then
		apt install -y "$PACKAGE_NAME"

        ufw enable <<< y

        ufw allow 8081
        ufw allow OpenSSH
        ufw allow WWW
	else
		echo "$PACKAGE_NAME est déjà installé"
	fi

}

install_java() {
    PACKAGE_NAME="adoptopenjdk-8-hotspot"
	if ! dpkg -l |grep --quiet "^ii.*$PACKAGE_NAME " ; then
		
    apt install apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common -y
    wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
    add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
    apt update -y
    apt install -y "$PACKAGE_NAME"
    java -version
    apt install net-tools -y
    else
        echo "$PACKAGE_NAME est déjà installé"
    fi
}

### Point d'entrer du script ###
apt update -y

## Instalation de ufw
install_ufw

## Instalation de java
install_java

useradd -M -d /opt/nexus -s /bin/bash -r nexus || echo "User already exists."
apt install sudo
echo "nexus ALL = (ALL) NOPASSWD: ALL"> /etc/sudoers.d/nexus

wget -O nexus.tar.gz https://download.sonatype.com/nexus/3/latest-unix.tar.gz

DIR="/opt/nexus"
if [ -d  "$DIR" ];then
echo "/opt/nexus existe déjà."
else
    mkdir /opt/nexus
fi
tar xzf nexus.tar.gz -C /opt/nexus --strip-components=1

chown -R nexus: /opt/nexus

sed -i 's/#run_as_user=""/run_as_user="nexus"/' /opt/nexus/bin/nexus.rc
sed -i 's|../sonatype-work/|./sonatype-work/|' /opt/nexus/bin/nexus.vmoptions

echo "" > /etc/systemd/system/nexus.service
cat > /etc/systemd/system/nexus.service << 'EOL'
[Unit]
Description=nexus service
After=network.target

[Service]
Type=forking
LimitNOFILE=65536
ExecStart=/opt/nexus/bin/nexus start
ExecStop=/opt/nexus/bin/nexus stop
User=nexus
Restart=on-abort

[Install]
WantedBy=multi-user.target
EOL

systemctl enable --now nexus.service >> /dev/null
systemctl stop nexus
systemctl start nexus

echo "Success"
