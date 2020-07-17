#!/bin/bash


: '
Script to demonstrate the use of IF /ELSE
(1) Take input name from terminal
(2) Condition to determine if name is correct

Written by: Ufuoma Okoro
Department: Home Office

'

read -p "Enter your firstname: " inFirstName
echo
read -p "Now you lastname: " inLastName
echo

#check input against conditions
 if [[ "$inFirstName" -eq "Ufuoma" && "$inLastname" -eq "Okoro" ]]

 then
	 echo "You name is $inFirstName and your last name is $inLastName"

 else
	 echo "You are a differnt person"

 fi


