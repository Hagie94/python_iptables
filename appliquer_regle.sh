 #!/bin/bash
chaine="$1"
protocole="$2"
int_entree="$3"
int_sortie="$4"
port_entre="$5"
port_sorti="$6"
cible="$7"

if [[ "$protocole" != "" ]] && [["$int_entree" != "" ]] && [[ "$int_sortie" != "" ]]
then
	sudo iptables -A "$chaine" -p "$protocole" -s "$int_entree" -d "$int_sortie" -j "$cible"
elif [[ "$protocole" != "" ]] && [["$int_entree" != "" ]] && [[ "$int_sortie" != "" ]] && [[ "$port_entre" != "" ]] && [[ "$port_sorti" != "" ]]
then
	sudo iptables -A "$chaine" -p "$protocole" -s "$int_entree" -d "$int_sortie" --sport "$port_entre" --dport "$port_sorti" -j "$cible"
elif [[ "$protocole" = "" ]] && [[ "$int_entree" != "" ]] && [[ "$int_sortie" != "" ]]
then
	sudo iptables -A "$chaine" -s "$int_entree" -d "$int_sortie" -j "$cible"
elif [[ "$protocole" = "" ]] && [[ "$int_sortie" = "" ]] && [[ "$int_entree" != "" ]]
then
	sudo iptables -A "$chaine" -s "$int_entree" -j "$cible"
elif [[ "$int_entree" = "" ]] && [[ "$protocole" = "" ]] && [[ "$int_sortie" != "" ]]
then
	sudo iptables -A "$chaine" -d "$int_sorti" -j "$cible"
elif [[ "$int_entree" != "" ]] && [[ "$protocole" != "" ]] && [[ "$int_sortie" = "" ]]
then
	sudo iptables -A "$chaine" -p "$protocole" -s "$int_entree" -j "$cible"
elif [[ "$protocole" != "" ]] && [[ "$int_sortie" != "" ]] && [[ "$int_entree" = "" ]]
then
	sudo iptables -A "$chaine" -p "$protocole" -d "$int_sorti" -j "$cible"
elif [[ "$protocole" != "" ]] && [["$int_entree" = "" ]] && [[ "$int_sortie" = "" ]]
then
	sudo iptables -A "$chaine" -p "$protocole" -j "$cible"
elif [[ "$protocole" = "" ]] && [["$int_entree" = "" ]] && [[ "$int_sortie" = "" ]]
then
	sudo iptables -A "$chaine" -j "$cible"
fi
#sauvegarde des regles
sudo iptables-save > /etc/iptables/rules.v4
