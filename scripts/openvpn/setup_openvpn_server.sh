#!/bin/bash
echo 'Install OpenVPN From Repo'
yum -y install openvpn easy-rsa
echo 'Copy Example Configurations To Folder'
cp /usr/share/doc/openvpn-*/sample/sample-config-files/server.conf /etc/openvpn/server.conf
echo 'Copy Easy-RSA'
sudo mkdir /etc/openvpn/easy-rsa/
cp -vR /usr/share/easy-rsa/2.0/* /etc/openvpn/easy-rsa/
read -p "KEY_COUNTRY: " _key_country
read -p "KEY_PROVINCE: " _key_province
read -p "KEY_CITY: " _key_city
read -p "KEY_ORG: " _key_org
read -p "KEY_EMAIL: " _key_email
read -p "KEY_OU: " _key_ou
sed -i "s|US|$_key_country|g;
  s|CA|$_key_province|g;
  s|SanFrancisco|$_key_city|g;
  s|Fort-Funston|$_key_org|g;
  s|me@myhost.mydomain|$_key_email|g;
  s|MyOrganizationalUnit|$_key_ou|g" /etc/openvpn/easy-rsa/vars
cd /etc/openvpn/easy-rsa
source /etc/openvpn/easy-rsa/vars
echo "Clear All"
/etc/openvpn/easy-rsa/clean-all
echo "Build CA: ca.crt"
/etc/openvpn/easy-rsa/build-ca
echo "Build Server Key: server.key, server.crt"
/etc/openvpn/easy-rsa/build-key-server server
echo "Build DH: dh2048.pem"
/etc/openvpn/easy-rsa/build-dh
echo "Copy Key Server"
mv /etc/openvpn/easy-rsa/keys/server.key /etc/openvpn/.
mv /etc/openvpn/easy-rsa/keys/server.crt /etc/openvpn/.
mv /etc/openvpn/easy-rsa/keys/ca.crt /etc/openvpn/.
mv /etc/openvpn/easy-rsa/keys/dh2048.pem /etc/openvpn/.
read -p "DNS Server 1: " dns1
read -p "DNS Server 2: " dns2
echo "push "dhcp-option DNS $dns1"" >> /etc/openvpn/server.conf
echo "push "dhcp-option DNS $dns2"" >> /etc/openvpn/server.conf
echo "Choose Type of Authentication"
echo "1. Linux User"
echo "2. Personal Key"
read -p "Choose" choose
case "$choose" in
	1)
		echo 'client-cert-not-required' >> /etc/openvpn/server.conf
    echo 'plugin /usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so login' >> /etc/openvpn/server.conf
    ;;
	2)
		echo "Personal Key"
		;;
	*)
		echo "Personal Key";;
esac
read -p 'Range IP VPN' ipvpn netmask
sed -i "s|server 10.8.0.0 255.255.255.0|server $ipvpn $netmask|g" /etc/openvpn/server.conf
echo 'Start OpenVPN service'
# Fix for Centos7
systemctl -f enable openvpn@server.service
systemctl start openvpn@server.service